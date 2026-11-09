# basic-maths

The core building blocks of arithmetic, fractions, decimals, negative numbers, shapes and measurements for children ages 6 to 12 (`school-age` and `preteen`), written for offline study and reference on an AI-2 machine.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in basic-maths --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export basic-maths --manifest manifest.yml -o basic-maths.ai2pack
```

## House style

- One topic per file, first line the title, then the search terms people would type.
- Written for children learning mathematics or parents and teachers helping them, with everyday analogies (sharing fruit, folding paper, walking along lines, measuring rooms).
- Explanations state the concept first in clear words before demonstrating with worked examples.
- Self-contained passages of about 110 words so answers retrieved by search provide clear understanding without needing preceding headings.
- Metric units only (mm, cm, m, km; g, kg; ml, l) aligned with international curricula and UNESCO standards.

## Topics included

1. `start-here.txt`: Welcome, what maths is, and how to search this pack.
2. `counting-and-place-value.txt`: Digits, ones, tens, hundreds, thousands, and zero as a placeholder.
3. `addition-and-combining.txt`: What addition means, order rules, making ten, and column carrying over.
4. `subtraction-and-difference.txt`: Taking away, finding differences, and column borrowing.
5. `multiplication-and-groups.txt`: Equal groups, arrays, and times table tricks (2x, 4x, 5x, 9x, 10x).
6. `division-and-sharing.txt`: Fair sharing, inverse multiplication, and handling remainders.
7. `fractions-parts-of-a-whole.txt`: Halves, quarters, numerators, denominators, and equivalent fractions.
8. `decimals-and-tenths.txt`: Place value past the decimal point, tenths, hundredths, and money.
9. `percentages-out-of-one-hundred.txt`: What percent means, benchmarks (50%, 25%, 10%), and mental math.
10. `negative-numbers-below-zero.txt`: Numbers less than zero, thermometers, and number line movement.
11. `shapes-and-basic-geometry.txt`: 2D polygons and circles; 3D solids (faces, edges, vertices).
12. `perimeter-and-area.txt`: Distance around outer edges vs flat square surface inside.
13. `measuring-length-weight-volume.txt`: Metric prefixes, length, mass, and liquid capacity.
14. `telling-time-and-calendar.txt`: Analog clock hands, digital 12/24-hour time, and calendar cycles.
