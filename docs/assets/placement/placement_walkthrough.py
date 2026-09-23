"""Executable reconstruction of the ordinary four-elemental example, not a universal predictor.

Input: the published observations.json. Output: row lengths, candidate order and
placement attempts, compared with independently recorded game positions/attempts.
Only equal stacks of the four size-1 elementals and the unspread general pass are covered.
"""
import json
from pathlib import Path
import struct


def stack_score(creature, quantity):
    """The checked single-stack score control: reference attack=1, reference defence slot=0.

    Both coefficients are float32 0.05; no hero modifiers, extras or damage cap.
    This is placement scoring, not the formula for damage dealt in combat.
    """
    coefficient = struct.unpack('<f', struct.pack('<f', 0.05))[0]

    def adjustment(attack, defence):
        difference = attack - defence
        return 1 + coefficient * difference if difference > 0 else 1 / (1 - coefficient * difference)

    damage = ((creature['min_damage'] + creature['max_damage']) * quantity) // 2
    health = creature['health'] * quantity
    return int(health * max(0.1, 1 / adjustment(1, creature['defence']))
               + damage * max(1, adjustment(creature['attack'], 0)))


def native_order(scores):
    """Descending merge passes; ties take the right lane, as in the inspected game sort."""
    order = list(range(len(scores)))
    if len(order) < 2:
        return order
    stride = 1
    while stride * 2 < len(order):
        stride *= 2
    while stride:
        result = order.copy()
        for lane in range(min(stride, len(order) - stride)):
            left, right, destination = lane, lane + stride, lane
            while left < len(order) or right < len(order):
                if right >= len(order) or (left < len(order) and scores[order[left]] > scores[order[right]]):
                    result[destination] = order[left]
                    left += 2 * stride
                else:
                    result[destination] = order[right]
                    right += 2 * stride
                destination += stride
        order = result
        stride //= 2
    return order


def row_lengths(width, height, blocked):
    lengths = []
    for y in range(1, height - 1):
        length = 0
        for x in range(width - 5, 1, -1):
            if (x, y) in blocked:
                break
            length += 1
        lengths.append(length)
    return lengths


def replay(battle):
    """Reconstruct this documented fixture without reading its recorded target cells."""
    width, height = battle['grid']
    blocked = {tuple(cell) for cell in battle['blocked']}
    neutrals = {unit['creature']: unit for unit in battle['units'] if unit['side'] == 'neutral'}
    # Fields from Universe_mod.pak/GameMechanics/Creature/Creatures/Neutrals/*_Elemental.xdb.
    # Scores are calculated below, not supplied as the expected placement order.
    traits = {
        'CREATURE_EARTH_ELEMENTAL': dict(shooter=False, flying=False, speed=4, attack=8, defence=14, min_damage=10, max_damage=14, health=72),
        'CREATURE_WATER_ELEMENTAL': dict(shooter=False, flying=False, speed=5, attack=10, defence=10, min_damage=8, max_damage=12, health=48),
        'CREATURE_FIRE_ELEMENTAL': dict(shooter=True, flying=False, speed=5, attack=12, defence=4, min_damage=11, max_damage=20, health=33),
        'CREATURE_AIR_ELEMENTAL': dict(shooter=False, flying=True, speed=8, attack=8, defence=4, min_damage=6, max_damage=8, health=34),
    }
    if set(neutrals) != set(traits) or any(unit['size'] != 1 for unit in neutrals.values()):
        raise ValueError('This walkthrough covers only the four size-1 elementals')
    context = battle.get('placement_context')
    if context and (context['defensive'] or context['spread'] or context['depth'] != 2):
        raise ValueError('This example does not implement defensive, spread or deeper deployment')
    if width != 16 or height != 12:
        raise ValueError('This worked example uses the recorded 16x12 grid and two-column depth')
    shooters = [creature for creature in neutrals if traits[creature]['shooter']]
    melee = [creature for creature in neutrals if not traits[creature]['shooter']]
    # Distance = 16 - 2 - 6 = 8. Earth/Water speeds 4/5 do not reach it;
    # the speed comparison between these two is inactive. Flight splits Air out first.
    scores = {creature: stack_score(properties, 15) for creature, properties in traits.items()}
    keys = [(not traits[creature]['flying'], scores[creature]) for creature in melee]
    types = shooters + [melee[index] for index in native_order(keys)]
    lengths = row_lengths(width, height, blocked)
    # One shooter: the cyclic minimum window has length one; equal minima retain the first.
    shooter_row = min(range(len(lengths)), key=lambda index: lengths[index])
    shooter_priority = [int(index == shooter_row) for index in range(len(lengths))]
    melee_rows = [index + 1 for index in native_order(lengths)]
    shooter_rows = [index + 1 for index in native_order(shooter_priority)]
    occupied = set()
    for unit in battle['units']:
        if unit['side'] == 'hero':
            x, y = unit['cell']
            occupied.update((column, row) for column in range(x - unit['size'] + 1, x + 1)
                            for row in range(y - unit['size'] + 1, y + 1))
    attempts, placements = [], {}
    for creature in types:
        shooter = creature == 'CREATURE_FIRE_ELEMENTAL'
        x = width - (3 if shooter else 4)
        for y in shooter_rows if shooter else melee_rows:
            success = (x, y) not in blocked and (x, y) not in occupied
            attempts.append({'creature': creature, 'candidate': [x, y], 'success': success})
            if success:
                placements[creature] = [x, y]
                occupied.add((x, y))
                break
        else:
            raise ValueError('No cell in the illustrated pass; fallback is outside this example')
    return {'scores': scores, 'lengths': lengths, 'melee_rows': melee_rows,
            'shooter_row': shooter_row + 1, 'attempts': attempts, 'placements': placements}


def verify(battle):
    result = replay(battle)
    observed = {unit['creature']: unit['cell'] for unit in battle['units'] if unit['side'] == 'neutral'}
    if result['placements'] != observed:
        raise ValueError('Reconstruction does not match recorded game positions')
    if 'native_attempts' in battle and result['attempts'] != battle['native_attempts']:
        raise ValueError('Reconstruction does not match the recorded native attempt sequence')
    return result


if __name__ == '__main__':
    data = json.loads(Path(__file__).with_name('observations.json').read_text(encoding='utf-8'))
    for battle in data['battles']:
        if battle['id'] in ('pack_12', 'elementals_trace'):
            print(battle['id'], json.dumps(verify(battle), ensure_ascii=False))
