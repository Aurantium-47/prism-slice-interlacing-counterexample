# Certificate-driven exhibit

`prism-interlacing.svg` and `prism-interlacing.png` show only the two leftmost certified open intervals, not numerical approximations of roots or all roots. Both were visually reviewed for clipping, overlap, and mathematical labels.

Optional regeneration: `python3 assets/render.py`, with Matplotlib installed (tested with 3.10.8). This is a presentation-only dependency; all mathematical checks in `python3 reproduce.py` use the standard library. The renderer reads `review/certificate.json` and asserts displayed dimensions, degrees, interval counts, and endpoints before plotting. Floating point is used only for drawing coordinates, never for the proof.

The artwork is locally generated from the exact audit certificate. SVG glyph paths are embedded; there are no external image or font links. Licensing remains subject to the package's pending license choice.
