"""Geometry checks independent of browser rendering."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('placement_figures', ROOT / 'scripts/render-placement.py')
FIGURES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FIGURES)


class PlacementFigureTests(unittest.TestCase):
    def setUp(self):
        self.battles = json.loads((ROOT / 'docs/assets/placement/observations.json').read_text())['battles']

    def test_all_recorded_cells_and_both_armies_are_present(self):
        for battle in self.battles:
            with self.subTest(battle=battle['id']):
                document = ET.fromstring(FIGURES.render(battle))
                cells = [node.get('data-cell') for node in document.iter() if node.get('data-cell') is not None]
                width, height = battle['grid']
                self.assertEqual(len(cells), width * height)
                self.assertEqual(len(set(cells)), width * height)
                self.assertIn('0,0', cells)
                self.assertIn(f'{width - 1},{height - 1}', cells)
                text = ''.join(document.itertext())
                for unit in battle['units']:
                    self.assertIn(unit['label'], text)

    def test_large_footprint_collision_is_rejected_even_if_anchor_is_free(self):
        battle = copy.deepcopy(self.battles[0])
        battle['blocked'].append([2, 3])  # A1 anchor is (3,4); lower-left footprint cell.
        with self.assertRaisesRegex(ValueError, 'overlaps obstacle'):
            FIGURES.validate_battle(battle)

    def test_overlapping_armies_are_rejected(self):
        battle = copy.deepcopy(self.battles[0])
        battle['units'][1]['cell'] = battle['units'][0]['cell']
        with self.assertRaisesRegex(ValueError, 'overlaps obstacle or another'):
            FIGURES.validate_battle(battle)

    def test_missing_hero_army_is_rejected(self):
        battle = copy.deepcopy(self.battles[0])
        battle['units'] = [unit for unit in battle['units'] if unit['side'] == 'neutral']
        with self.assertRaisesRegex(ValueError, 'both armies'):
            FIGURES.validate_battle(battle)

    def test_footprint_cannot_extend_beyond_grid(self):
        battle = copy.deepcopy(self.battles[0])
        battle['units'][0]['cell'] = [0, 0]
        with self.assertRaisesRegex(ValueError, 'outside grid'):
            FIGURES.validate_battle(battle)

    def test_candidate_layer_requires_the_actual_recorded_obstacle(self):
        battle = copy.deepcopy(self.battles[0])
        battle['blocked'].remove([8, 6])
        with self.assertRaisesRegex(ValueError, 'recorded obstacle'):
            FIGURES.render(battle, 'footprint')


if __name__ == '__main__':
    unittest.main()
