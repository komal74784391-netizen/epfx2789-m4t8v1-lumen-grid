# Lumen Grid

**Status:** Released · v1.0.4 · 2025-12-02

Responsive masonry layout primitives for the Lumen design system.  The
package ships a packing engine, a CSS-variable theme bridge and a small set of
accessibility helpers.

## Install

```bash
pip install lumen-grid
```

## What is in this repository

- `src/lumen_grid/layout.py` — column packing engine
- `src/lumen_grid/theme.py` — CSS variable bridge
- `src/lumen_grid/a11y.py` — focus and reading-order helpers
- `tests/test_layout.py` — packing regression tests
- `CHANGELOG.md` — release history

## Usage

```python
from lumen_grid import pack

columns = pack(cards, columns=3, gap=16)
```
