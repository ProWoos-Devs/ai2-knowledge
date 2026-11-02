#!/usr/bin/env python3
"""Check every card in cards/ and write them to cards-for-reading.txt.

A card fails if it lacks a required field, if any of the four resource-limit
sections lacks a valid state, if a "supported" section is empty, or if an
instruction has no source. Passing says the card is complete, not that it is
correct: that is what the independent check is for.
"""
import glob
import os
import shutil
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
STATES = {"supported", "none-known", "not-applicable", "pending"}
EMPTY = {"none-known": "None known in the sources used for this card.", "not-applicable": "Does not apply to this card.",
         "pending": "Not written yet.", "supported": ""}
LIMIT_SECTIONS = {
    "without_medical_supplies": "With no medical supplies",
    "supported_alternatives": "Alternatives using what is available",
    "if_help_is_delayed_or_unreachable": "If help is delayed or cannot be reached",
    "no_effective_substitute_for": "What has no effective substitute",
}
REQUIRED = ("id", "title", "population", "age_definition", "age_groups", "jurisdiction", "protocol_family",
            "emergency_number_profile", "source_editions", "applicability", "untrained_scope",
            "source_differences", "review")
LABEL = "Written from IFRC 2025. Not reviewed by a clinician."


def check(card, name):
    problems = [f"{name}: missing {key}" for key in REQUIRED if key not in card]
    display = card.get("display", {})
    if card.get("review", {}).get("label") != LABEL:
        problems.append(f"{name}: wrong or missing label")
    if not display.get("urgent_help"):
        problems.append(f"{name}: no urgent_help")
    if not display.get("immediate_actions"):
        problems.append(f"{name}: no immediate_actions")
    for key in LIMIT_SECTIONS:
        section = display.get(key)
        if not isinstance(section, dict) or section.get("state") not in STATES:
            problems.append(f"{name}: {key} has no valid state")
        elif section["state"] == "supported" and not section.get("items"):
            problems.append(f"{name}: {key} says supported but is empty")
    lists = [display.get("immediate_actions", []), display.get("do_not", []),
             display.get("reassess_and_change_actions", [])]
    lists += [display.get(key, {}).get("items", []) for key in LIMIT_SECTIONS]
    for items in lists:
        for item in items:
            if not item.get("text") or not item.get("src"):
                problems.append(f"{name}: an instruction has no text or no source: {item}")
            stray = set(item) - {"text", "src", "warn", "limits"}
            if stray:
                problems.append(f"{name}: stray keys {stray}, usually an unquoted comma that cut off the text")
    return problems


def bullets(items, numbered=False):
    lines = []
    for n, item in enumerate(items, 1):
        lead = f"{n}. " if numbered else "- "
        line = lead + item["text"]
        if item.get("warn"):
            line += " WARNING: " + item["warn"]
        if item.get("limits") and item["limits"] != "None stated.":
            line += " Limits: " + item["limits"]
        lines.append(f"{line} [{item['src']}]")
    return lines


def render(card):
    d = card["display"]
    out = [card["title"], "", "DRAFT, NOT FOR EMERGENCY USE", "", LABEL, "", "For: " + card["population"],
           "Age: " + card["age_definition"]]
    if card.get("exclusions"):
        out.append("Not for: " + " ".join(card["exclusions"]))
    out += ["", "USE THIS CARD WHEN"] + ["- " + a for a in card["applicability"]]
    out += ["", "GET HELP", d["urgent_help"], "", "WHAT TO DO"] + bullets(d["immediate_actions"], numbered=True)
    if d.get("do_not"):
        out += ["", "DO NOT"] + bullets(d["do_not"])
    if d.get("reassess_and_change_actions"):
        out += ["", "IF THINGS CHANGE"] + bullets(d["reassess_and_change_actions"])
    for key, heading in LIMIT_SECTIONS.items():
        out += ["", heading.upper()] + (bullets(d[key]["items"]) or [EMPTY[d[key]["state"]]])
    if card["source_differences"]:
        out += ["", "WHERE SOURCES DIFFER OR ARE SILENT"] + ["- " + s for s in card["source_differences"]]
    left_out = card["untrained_scope"].get("left_out", [])
    if left_out:
        out += ["", "LEFT OFF THIS CARD"] + [f"- {x['what']}. {x['why']}" for x in left_out]
    review = card["review"]
    out += ["", "Source: " + "; ".join(card["source_editions"]) + ". Page numbers in square brackets are pages of that source.",
            "Checked on: " + str(review.get("checked_on") or "no date yet") + ".",
            "Next review due: " + str(review.get("next_review_due") or "no date yet") + ".", ""]
    return "\n".join(out)


def document(card):
    """The card as the Knowledge Pack holds it. Every line is its own paragraph, because
    indexing joins lines that have no blank line between them, and the short search terms
    follow the title, so the first part of a card says in plain words what it is for."""
    text = render(card)
    title, rest = text.split("\n", 1)
    terms = [a for a in card["query_aliases"] if len(a.split()) <= 4]
    lines = [title, "Search terms: " + ", ".join(terms) + "."] + [x for x in rest.split("\n") if x.strip()]
    return "\n\n".join(lines) + "\n"


def main():
    files = sorted(glob.glob(os.path.join(HERE, "cards", "*.yml")))
    cards, problems = [], []
    for path in files:
        with open(path, encoding="utf-8") as fh:
            card = yaml.safe_load(fh)
        problems += check(card, os.path.basename(path))
        cards.append(card)
    if problems:
        print("\n".join(problems))
        return 1
    order = ["start-here"]
    cards.sort(key=lambda c: (c["id"] not in order, c["id"]))
    with open(os.path.join(HERE, "cards-for-reading.txt"), "w", encoding="utf-8") as fh:
        fh.write("DRAFT, NOT FOR EMERGENCY USE\n\n\n" + "\n\n".join(render(c) for c in cards))
    # one document per card: what ai-2 doc index reads to make the Knowledge Pack
    folder = os.path.join(HERE, "documents")
    os.makedirs(folder, exist_ok=True)
    for old in glob.glob(os.path.join(folder, "*.txt")):
        os.remove(old)
    for card in cards:
        with open(os.path.join(folder, card["id"] + ".txt"), "w", encoding="utf-8") as fh:
            fh.write(document(card))
    shutil.copy(os.path.join(HERE, "about-this-pack.txt"), folder)
    print(f"{len(cards)} cards checked, 0 problems, cards-for-reading.txt and documents/ written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
