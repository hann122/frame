#!/usr/bin/env python3
"""Post-process vr_db_update output for 31/10 per Chow's verdicts (script cannot represent these):
 1. Convert placeholder R350-0277 (kira is sleepy, D2 row 194) back to R350-0217 kira21.
 2. Add 4 supplementary members present per Chow but NOT in the video, with Chow's stats.
 3. Re-sort by Power, recompute ranks, fix aliases + snapshot note, validate everything.
Input: B_3110/new/ (pristine script output). Output: B_3110/final/ (pushable DB).
"""
import json, sys
sys.path.insert(0, 'scripts')
from vr_common import load_json, dump_json, GAP_IDS, id_num

BASE = 'B_3110'
db = load_json(f'{BASE}/new/member_db.json')
al = load_json(f'{BASE}/new/aliases.json')
snaps = sorted(db['snapshots'], key=lambda s: s['date'])
d1 = next(s for s in snaps if s['date'] == '2026-10-27')
snap = next(s for s in snaps if s['date'] == '2026-10-31')
canon = {m['id']: m['name'] for m in d1['members']}
members = {m['id']: m for m in snap['members']}

# --- 1. kira21 conversion (assert the placeholder really is row 194) ---
ph = members.pop('R350-0277')
assert (ph['power'], ph['kill_points'], ph['activity_points']) == (94094747, 470155550, 1433100), ph
assert 'R350-0217' not in members
members['R350-0217'] = {'id': 'R350-0217', 'name': canon['R350-0217'],
                        'power': ph['power'], 'kill_points': ph['kill_points'],
                        'activity_points': ph['activity_points']}
assert canon['R350-0217'] == 'kira21', canon['R350-0217']

# --- 2. supplementary members (Chow's stats; canonical names from D1) ---
supp = {
    'R350-0003': (570884806, 11675253185, 15000, '133tz'),        # screen == canonical
    'R350-0142': (158733482, 6931115332, 0, 'llllllllllll'),       # screen != canonical (screenshot)
    'R350-0079': (183889375, 2432413110, 0, 'Phong Anh Kiet'),    # screen == canonical
    'R350-0193': (115342329, 1302918192, 0, 'Leader392837282'),    # screen != canonical
}
for i, (p, k, a_, scr) in supp.items():
    assert i not in members, f'{i} already in snapshot'
    assert canon[i] in ('133tz', 'Simona', 'Phong Anh Kiet', 'leader362717362'), (i, canon[i])
    members[i] = {'id': i, 'name': canon[i], 'power': p, 'kill_points': k, 'activity_points': a_}

# --- 3. re-sort + ranks ---
ordered = sorted(members.values(), key=lambda m: -m['power'])
assert len(ordered) == 199, len(ordered)
assert all(a_['power'] > b['power'] for a_, b in zip(ordered, ordered[1:])), 'power not strictly descending'
snap['members'] = [{'rank': r, 'name': m['name'], 'power': m['power'],
                    'kill_points': m['kill_points'], 'activity_points': m['activity_points'], 'id': m['id']}
                   for r, m in enumerate(ordered, 1)]

# --- 4. snapshot note addendum (auto note stays intact; this corrects the record) ---
add = (" MANUAL POST-PROCESSING (same session, per Chow's verdicts, because the script cannot represent "
       "these cases): placeholder R350-0277 (kira is sleepy) converted back to R350-0217 kira21 with D2 row-194 "
       "stats (P 94,094,747 / KP 470,155,550 / Act 1,433,100), so NO new ID was issued in the final snapshot. "
       "4 supplementary members added with Chow-provided stats (NOT from video): R350-0003 133tz, R350-0142 Simona, "
       "R350-0079 Phong Anh Kiet, R350-0193 leader362717362. Final snapshot: 199 members = 195 video rows + 4 "
       "supplementary. Only true departure: R350-0189 Deoniss. Game-UI count 196 vs final 199 differs by 3 (unresolved; "
       "upload authorized by Chow).")
snap['note'] = snap['note'] + add

# --- 5. aliases: drop nothing (no R350-0277 entry existed); add 3 where screen != canonical ---
al_list = {e['id']: e for e in al['aliases']}
assert 'R350-0277' not in al_list and 'R350-0217' not in al_list
assert 'R350-0142' not in al_list and 'R350-0193' not in al_list
new_aliases = [
    {'id': 'R350-0217', 'db_name': 'kira21', 'as_of': '2026-10-31', 'screen_name': 'kira is sleepy'},
    {'id': 'R350-0142', 'db_name': 'Simona', 'as_of': '2026-10-31', 'screen_name': 'llllllllllll'},
    {'id': 'R350-0193', 'db_name': 'leader362717362', 'as_of': '2026-10-31', 'screen_name': 'Leader392837282'},
]
for e in new_aliases:
    al_list[e['id']] = e
al['aliases'] = sorted(al_list.values(), key=lambda e: e['id'])
al['note'] = al['note'] + add
assert len(al['aliases']) == 20, len(al['aliases'])

# --- 6. full validation (mirrors vr_db_update section 7, on the FINAL snapshot) ---
errs = []
hist = {}
for s in snaps:
    ids = [x['id'] for x in s['members']]
    if len(ids) != len(set(ids)):
        errs.append(f"duplicate id in {s['date']}")
    for x in s['members']:
        hist.setdefault(x['id'], []).append((s['date'], x['kill_points']))
for i, h in hist.items():
    for (d1_, k1), (d2_, k2) in zip(h, h[1:]):
        if k2 < k1:
            errs.append(f'KP decrease {i} {d1_} {k1:,} -> {d2_} {k2:,}')
if [x['rank'] for x in snap['members']] != list(range(1, 200)):
    errs.append('rank is not 1..199')
if any(id_num(m['id']) in GAP_IDS for m in snap['members'] if m['id'] not in canon and m['id'] != 'R350-0217'):
    errs.append('gap id present')
if errs:
    print('VALIDATION FAILED:'); [print(' -', e) for e in errs]; sys.exit(3)

import os
os.makedirs(f'{BASE}/final', exist_ok=True)
dump_json(db, f'{BASE}/final/member_db.json')
dump_json(al, f'{BASE}/final/aliases.json')
print(f'OK final snapshot 2026-10-31: 199 members, aliases {len(al["aliases"])}, '
      f'0 KP decreases over {len(snaps)} snapshots')
for i in ('R350-0217', 'R350-0003', 'R350-0142', 'R350-0079', 'R350-0193'):
    m = next(x for x in snap['members'] if x['id'] == i)
    print(f"  {i} rank {m['rank']} {m['name']} P {m['power']:,} KP {m['kill_points']:,} A {m['activity_points']:,}")
print('  Deoniss present:', any(x['id'] == 'R350-0189' for x in snap['members']),
      '| R350-0277 present:', any(x['id'] == 'R350-0277' for x in snap['members']))
