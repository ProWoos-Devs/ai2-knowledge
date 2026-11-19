# looking-after-a-laptop

Keeping old laptops working where there is no technician and often no Internet: where to use and keep them, heat, dust and cleaning, spills, charging safely, the battery and when to stop using it, getting rid of old batteries, a laptop that will not start, and checking its health with `ai-2 doctor`. For the teacher, volunteer or parent who looks after the laptops (audience `general`).

Written rather than extracted. The safety advice follows United States Government sources, in our own words, named in each topic where it is used:

- U.S. Fire Administration, "Lithium-Ion Battery Safety for Electronic Devices", https://www.usfa.fema.gov/downloads/pdf/publications/lithium-ion-battery-safety-handout.pdf
- U.S. Fire Administration, "Lithium-Ion Batteries: Everyday Convenience, Hidden Fire Risks", 13 October 2026, https://www.usfa.fema.gov/blog/lithium-ion-batteries/
- U.S. Fire Administration, "Appliance and Electrical Fire Safety", https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/appliance-and-electrical/
- U.S. Fire Administration, "Lithium-Ion Battery Safety After Flooding", https://www.usfa.fema.gov/downloads/pdf/publications/lithium-ion-battery-after-flooding-handout.pdf
- U.S. Fire Administration, "Risks and response strategies for lithium-ion battery fires", https://www.usfa.fema.gov/a-z/lithium-ion-batteries/risks-and-response-strategies/
- U.S. Fire Administration, "Battery Fire Safety", https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/batteries/
- U.S. Fire Administration, "Home Fire Escape Plans", https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/
- U.S. Environmental Protection Agency, "Used Lithium-Ion Batteries", https://www.epa.gov/recycle/used-lithium-ion-batteries
- U.S. Centers for Disease Control and Prevention, "What to Do to Protect Yourself From Electrical Hazards", https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-from-electrical-hazards.html

The AI-2 parts (`ai-2 doctor`, the processor temperature guard, the boot menu) come from the AI-2 manual and program and were checked on a computer running AI-2 0.29.3. Advice not taken from these sources, such as cleaning the outside of a laptop, carrying one and organizing a set of laptops, is labeled as ordinary care in the topics. No repair technician or electrician has reviewed it.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in looking-after-a-laptop --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export looking-after-a-laptop --manifest manifest.yml -o looking-after-a-laptop.ai2pack
```

## House style

- One subject per file, first line the title, then the search terms people would type.
- Every topic says "Written for AI-2, for the person who looks after the laptops. Not reviewed by a repair technician."
- Search shows passages of about 110 words, so each section is written to be understood without the ones before it.
- Every safety instruction names its source in the text. Where no source says something (how full to keep a battery, what to do where no collection point exists), the topic says that instead of guessing.
- No brand names, models or program versions. Laptops whose battery comes out and laptops whose battery is inside are both covered, and no topic asks anyone to open a laptop or a battery.
- Software trouble is left to Linux Essentials and named there by topic.

## Reviewing

Anyone who knows the subject is welcome to check these topics. [REVIEWING.md](../../REVIEWING.md) says what to look for and how to report it. Check especially the battery, charging and disposal advice against its sources, anything that is true of one kind of laptop and not another, and the AI-2 parts against a computer running it.

No repair technician or electrician has reviewed this Knowledge Pack.
