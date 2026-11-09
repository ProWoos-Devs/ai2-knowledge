# basic-physics

The fundamental principles of physics—forces, motion, gravity, friction, drag, energy, simple machines, states of matter, heat, light, sound, electricity, magnetism, and buoyancy—for children ages 6 to 12 (`school-age` and `preteen`), written for offline study and reference on an AI-2 machine.

There are no telephone numbers here, or in any Knowledge Pack.

## Rebuilding

```
ai-2 doc index --in basic-physics --embedder nomic-embed-text-v1.5 topics/*.txt
ai-2 knowledge export basic-physics --manifest manifest.yml -o basic-physics.ai2pack
```

## House style

- One topic per file, first line the title, then the search terms people would type.
- Written for children exploring physics, or parents and teachers guiding them, with everyday analogies and safe tabletop experiments.
- Explanations state the concept first in clear words before demonstrating with worked examples.
- Self-contained passages of about 110 words so answers retrieved by search provide clear understanding without needing preceding headings.
- Metric units only (meters, kilograms, Newtons, Joules, degrees Celsius) aligned with international curricula and UNESCO standards.

## Topics included

1. `start-here.txt`: Welcome, what physics is, and how to search this pack.
2. `forces-pushes-and-pulls.txt`: Newtons, balanced and unbalanced forces, and changes in motion.
3. `gravity-and-falling.txt`: Earth's downward pull, mass vs weight, and falling objects.
4. `friction-and-grip.txt`: Surface resistance, useful grip (shoes, brakes), and lubrication (oil).
5. `air-and-water-resistance.txt`: Drag, surface area, parachutes, and streamlined aerodynamic shapes.
6. `energy-movement-and-storage.txt`: Kinetic and potential energy, forms of energy, and conservation.
7. `simple-machines-making-work-easier.txt`: Trading force for distance: levers, ramps, pulleys, and wheels.
8. `states-of-matter.txt`: Particle behavior in solids, liquids, and gases; melting and boiling.
9. `heat-temperature-and-conduction.txt`: Moving particles, degrees Celsius, conduction, convection, and insulators.
10. `light-shadows-and-reflection.txt`: Straight rays, transparent/opaque materials, shadows, and mirrors.
11. `color-and-rainbows.txt`: White light spectrum (ROYGBIV), prism refraction, rainbows, and color absorption.
12. `sound-and-vibrations.txt`: Vibrating waves, speed in air/water/steel, pitch, volume, and echoes.
13. `electricity-and-circuits.txt`: Flow of electrons, complete circuit loops, conductors, insulators, and safety.
14. `magnets-and-magnetism.txt`: Magnetic fields, north and south poles (attract/repel), and compasses.
15. `floating-sinking-and-buoyancy.txt`: Upthrust, density, Archimedes' displacement, and why steel ships float.
