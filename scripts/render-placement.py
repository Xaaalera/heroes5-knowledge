"""Generate full-field SVG illustrations from recorded battle geometry."""
import argparse
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'docs/assets/placement'


def validate_battle(battle):
    width, height = battle['grid']
    if not all(type(value) is int and 4 <= value <= 32 for value in (width, height)):
        raise ValueError('Grid dimensions must be integers in 4..32')
    blocked = set()
    for cell in battle['blocked']:
        x, y = cell
        if not all(type(value) is int for value in cell) or not (0 <= x < width and 0 <= y < height):
            raise ValueError('Blocked cell outside grid')
        blocked.add((x, y))
    occupied = set()
    labels = set()
    sides = set()
    for unit in battle['units']:
        x, y = unit['cell']
        size = unit['size']
        if type(size) is not int or size not in (1, 2) or not all(type(value) is int for value in (x, y)):
            raise ValueError('Invalid creature footprint')
        if unit['side'] not in ('hero', 'neutral') or not re.fullmatch(r'[AN][1-9][0-9]*', unit['label']):
            raise ValueError('Invalid army or label')
        if not unit['label'].startswith('A' if unit['side'] == 'hero' else 'N'):
            raise ValueError('Label must identify the correct army')
        if unit['label'] in labels:
            raise ValueError('Duplicate unit label')
        labels.add(unit['label'])
        sides.add(unit['side'])
        for column in range(x - size + 1, x + 1):
            for row in range(y - size + 1, y + 1):
                if not (0 <= column < width and 0 <= row < height):
                    raise ValueError('Creature extends outside grid')
                if (column, row) in blocked or (column, row) in occupied:
                    raise ValueError('Creature overlaps obstacle or another creature')
                occupied.add((column, row))
    if sides != {'hero', 'neutral'}:
        raise ValueError('An illustration must include both armies')


def render(battle, layer='positions'):
    validate_battle(battle)
    width, height = battle['grid']
    cell_size, left, top = 48, 60, 68
    canvas_width = left + width * cell_size + 82
    canvas_height = top + height * cell_size + 58
    blocked = {tuple(cell) for cell in battle['blocked']}
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas_width} {canvas_height}">',
             f'<title>{escape(battle["id"])} · {escape(layer)}</title>',
             '<defs><pattern id="blocked" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#374047"/><path d="M0 8L8 0" stroke="#78818a"/></pattern></defs>',
             f'<rect width="{canvas_width}" height="{canvas_height}" fill="#101c22"/>',
             '<g font-family="sans-serif" font-size="18" text-anchor="middle" fill="#e6e8de">',
             f'<text x="{left + width * cell_size / 2}" y="28">X →</text>',
             '<text x="23" y="43">Y ↑</text>']
    # Every grid cell and coordinate label is emitted by these loops.
    for x in range(width):
        parts.append(f'<text x="{left + (x + .5) * cell_size}" y="54">{x}</text>')
        for y in range(height):
            fill = 'url(#blocked)' if (x, y) in blocked else '#1a3038'
            parts.append(f'<rect data-cell="{x},{y}" x="{left + x * cell_size}" y="{top + (height - 1 - y) * cell_size}" width="{cell_size}" height="{cell_size}" fill="{fill}" stroke="#58696f"/>')
    for y in range(height):
        parts.append(f'<text x="35" y="{top + (height - y - .5) * cell_size + 6}">{y}</text>')
    if layer == 'approach':
        parts.append(f'<text x="{canvas_width - 37}" y="54">L</text>')
        for y in range(1, height - 1):
            cells = []
            for x in range(width - 5, 1, -1):
                if (x, y) in blocked:
                    break
                cells.append(x)
            row_center = top + (height - y - .5) * cell_size
            if cells:
                parts.append(f'<path d="M{left + (min(cells) + .5) * cell_size} {row_center}H{left + (max(cells) + .5) * cell_size}" stroke="#c8e095" stroke-width="4" stroke-dasharray="7 5"/>')
            parts.append(f'<text x="{canvas_width - 37}" y="{row_center + 6}">{len(cells)}</text>')
    for unit in battle['units']:
        x, y = unit['cell']
        size = unit['size']
        position_x = left + (x - size + 1) * cell_size
        position_y = top + (height - 1 - y) * cell_size
        color = '#5ed2e4' if unit['side'] == 'hero' else '#ffb971'
        parts.append(f'<rect x="{position_x + 3}" y="{position_y + 3}" width="{size * cell_size - 6}" height="{size * cell_size - 6}" fill="{color}" fill-opacity=".24" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{position_x + size * cell_size / 2}" y="{position_y + size * cell_size / 2 + 7}" font-size="22" font-weight="bold">{unit["label"]}</text>')
        # Dot marks the actual native anchor, not the footprint's top-left corner.
        parts.append(f'<circle cx="{left + (x + 1) * cell_size - 9}" cy="{top + (height - 1 - y) * cell_size + 9}" r="4" fill="{color}"/>')
    if layer == 'footprint':
        # Explicit hypothetical candidate anchored on a measured obstacle.
        x, y = 8, 6
        if (x, y) not in blocked:
            raise ValueError('Footprint example must intersect its recorded obstacle')
        position_x, position_y = left + (x - 1) * cell_size, top + (height - 1 - y) * cell_size
        parts.append(f'<rect x="{position_x + 2}" y="{position_y + 2}" width="{2 * cell_size - 4}" height="{2 * cell_size - 4}" fill="none" stroke="#ff737b" stroke-width="4" stroke-dasharray="8 4"/>')
        parts.append(f'<text x="{position_x + cell_size}" y="{position_y + cell_size + 9}" font-size="34" fill="#ff737b">×</text>')
    parts.append('</g></svg>')
    return '\n'.join(parts) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    options = parser.parse_args()
    data = json.loads((ASSETS / 'observations.json').read_text(encoding='utf-8'))
    for battle in data['battles']:
        if not re.fullmatch(r'pack_[0-9]+', battle['id']):
            raise ValueError('Invalid battle identifier')
        layers = ('positions', 'footprint', 'approach') if battle['id'] == 'pack_8' else ('positions',)
        for layer in layers:
            path = ASSETS / f'{battle["id"]}-{layer}.svg'
            expected = render(battle, layer)
            if options.check:
                if not path.is_file() or path.read_text(encoding='utf-8') != expected:
                    raise ValueError(f'Stale diagram: {path.name}; run npm run figures')
            else:
                path.write_text(expected, encoding='utf-8')
    print('Full-field diagrams: both armies, obstacle masks, axes and footprints validated.')


if __name__ == '__main__':
    main()
