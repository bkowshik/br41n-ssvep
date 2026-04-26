# br41n.io SSVEP Data Analysis

A code-first walkthrough of the [br41n.io](https://www.br41n.io/) SSVEP dataset, structured around the canonical EEG analysis pipeline: data → preprocessing → feature engineering → modelling → evaluation. Published as a Quarto book.

## Prerequisites

- **Python 3.10+** (developed against 3.13)
- **[Quarto](https://quarto.org/docs/get-started/) 1.4+** (developed against 1.9)

## Setup

```bash
# Clone the repo, then from the project root:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The data files (`subject_*_fvep_led_training_*.mat`, `montage.png`, `data_description.txt`) are already in `data/`.

## Render the book

```bash
# Full render to HTML (output in _book/)
quarto render

# Render a single chapter
quarto render 03-filtering.qmd --to html

# Live preview — watches files, rebuilds incrementally, opens browser
quarto preview
```

The first full render takes a few minutes (filter design, CCA fits, sweeps). Subsequent renders are fast: `execute.freeze: auto` in `_quarto.yml` caches each chapter's executed code under `_freeze/`, so a chapter only re-runs when its `.qmd` source actually changes. Pure prose edits don't trigger Python execution.

## Project layout

```
.
├── _quarto.yml              # Book config (chapters, format, theme)
├── index.qmd                # Front matter / about
├── 01-recordings.qmd        # Ch 1 — what's in the .mat files
├── 02-ssvep-signature.qmd   # Ch 2 — where the SSVEP lives in the spectrum
├── 03-filtering.qmd         # Ch 3 — bandpass + notch
├── 04-epoching.qmd          # Ch 4 — trials from CH10 transitions
├── 05-spectral-features.qmd # Ch 5 — PSD-sampled SNR features
├── 06-template-features.qmd # Ch 6 — CCA and FBCCA
├── 07-classification.qmd    # Ch 7 — three-way classifier comparison
├── 08-time-accuracy-itr.qmd # Ch 8 — epoch-length sweep, Wolpaw ITR
├── 09-subjects.qmd          # Ch 9 — both subjects, all four sessions
├── summary.qmd              # Summary + what's next
├── acronyms.qmd             # Appendix — glossary
├── references.qmd           # Appendix — bibliography
├── references.bib
├── custom.css               # Image overflow + responsive layout
├── data/                    # .mat files, montage, description
├── images/                  # Generated chapter figures
└── requirements.txt
```

## Continuous deployment

`.github/workflows/publish.yml` renders the book on every push to `main` and publishes it to the `gh-pages` branch via [`quarto-actions/publish`](https://github.com/quarto-dev/quarto-actions). To enable serving:

1. Push the workflow to `main`. The first run creates the `gh-pages` branch automatically.
2. In **Settings → Pages** of the GitHub repository, set **Source: Deploy from a branch**, branch `gh-pages`, folder `/ (root)`.
3. The book becomes available at `https://<user>.github.io/<repo>/` after the next push (typically 1–2 minutes after the workflow finishes).

The workflow can also be triggered manually from the **Actions** tab via *Run workflow*.

## Notes

- `_book/`, `_freeze/`, and `.quarto/` are gitignored — render artifacts only.
- The book renders HTML only by default (PDF is off in `_quarto.yml`). Re-add `pdf:` under `format:` if you want LaTeX output.
- `images/` holds the rendered figures; the `.qmd` source code regenerates them on render.
