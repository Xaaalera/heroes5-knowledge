"""Compare an independent reconstruction with recorded game outcomes and attempts."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ASSETS = Path(__file__).resolve().parents[1] / 'docs/assets/placement'
SPEC = importlib.util.spec_from_file_location('walkthrough', ASSETS / 'placement_walkthrough.py')
WALKTHROUGH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WALKTHROUGH)


class PlacementWalkthroughTests(unittest.TestCase):
    def setUp(self):
        records = json.loads((ASSETS / 'observations.json').read_text())['battles']
        self.battles = {battle['id']: battle for battle in records}

    def test_equal_rows_follow_the_measured_native_tie_order(self):
        self.assertEqual([index + 1 for index in WALKTHROUGH.native_order([10] * 10)],
                         [8, 4, 6, 10, 2, 7, 3, 5, 9, 1])

    def test_two_recorded_fields_match_all_eight_final_cells(self):
        for name in ('pack_12', 'elementals_trace'):
            with self.subTest(name=name):
                result = WALKTHROUGH.verify(self.battles[name])
                self.assertEqual(len(result['placements']), 4)

    def test_seven_native_attempts_include_three_real_rejections(self):
        battle = self.battles['elementals_trace']
        result = WALKTHROUGH.verify(battle)
        self.assertEqual(result['attempts'], battle['native_attempts'])
        self.assertEqual(len(result['attempts']), 7)
        self.assertEqual(sum(not attempt['success'] for attempt in result['attempts']), 3)

    def test_calculated_scores_match_the_separate_native_arithmetic_control(self):
        scores = WALKTHROUGH.replay(self.battles['elementals_trace'])['scores']
        self.assertEqual(scores, {'CREATURE_EARTH_ELEMENTAL': 2034, 'CREATURE_WATER_ELEMENTAL': 1269,
                                  'CREATURE_FIRE_ELEMENTAL': 940, 'CREATURE_AIR_ELEMENTAL': 733})

    def test_target_positions_are_not_inputs_to_the_reconstruction(self):
        battle = copy.deepcopy(self.battles['elementals_trace'])
        before = WALKTHROUGH.replay(battle)
        for unit in battle['units']:
            if unit['side'] == 'neutral':
                unit['cell'] = [0, 0]
        self.assertEqual(WALKTHROUGH.replay(battle), before)
        with self.assertRaisesRegex(ValueError, 'recorded game positions'):
            WALKTHROUGH.verify(battle)

    def test_altered_game_attempt_record_is_not_silently_accepted(self):
        battle = copy.deepcopy(self.battles['elementals_trace'])
        battle['native_attempts'][2]['success'] = True
        with self.assertRaisesRegex(ValueError, 'native attempt sequence'):
            WALKTHROUGH.verify(battle)

    def test_unsupported_formation_is_rejected(self):
        for field, value in [('defensive', 1), ('spread', 1), ('depth', 3)]:
            with self.subTest(field=field):
                battle = copy.deepcopy(self.battles['elementals_trace'])
                battle['placement_context'][field] = value
                with self.assertRaisesRegex(ValueError, 'does not implement'):
                    WALKTHROUGH.replay(battle)


if __name__ == '__main__':
    unittest.main()
