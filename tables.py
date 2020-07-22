from cube_class import Cube, face, axis
from collections import deque
import csv

#                  0    1     2     3    4     5     6     7    8     9    10    11    12   13    14    15   16    17
move_candidate = ["R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'"]

successor = [
    [0,    2, 3,    5, 6, 7, 8, 9, 10, 11, 12,     14, 15,     17],
    [   1,       4,    6, 7, 8, 9, 10, 11,     13,         16    ]
]

solved = Cube()


cp_move = [[-1 for _ in range(18)] for _ in range(40320)]
que = deque([solved])
cnt = 0
print('CP move index')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_cp()
    if cp_move[idx][0] == -1:
        for twist in range(18):
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_cp()
            cp_move[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_cp.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in cp_move:
        writer.writerow(arr)


co_move = [[-1 for _ in range(18)] for _ in range(2187)]
que = deque([solved])
cnt = 0
print('CO move index')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_co()
    if co_move[idx][0] == -1:
        for twist in range(18):
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_co()
            co_move[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_co.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in co_move:
        writer.writerow(arr)


ep_phase0 = [[-1 for _ in range(18)] for _ in range(495)]
que = deque([solved])
cnt = 0
print('EP move index for phase 0')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_phase0_ep()
    if ep_phase0[idx][0] == -1:
        for twist in range(18):
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_phase0_ep()
            ep_phase0[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_ep_phase0.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in ep_phase0:
        writer.writerow(arr)


eo_phase0 = [[-1 for _ in range(18)] for _ in range(2048)]
que = deque([solved])
cnt = 0
print('EO move index for phase 0')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_phase0_eo()
    if eo_phase0[idx][0] == -1:
        for twist in range(18):
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_phase0_eo()
            eo_phase0[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_eo_phase0.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in eo_phase0:
        writer.writerow(arr)


ep_ud_phase1 = [[-1 for _ in range(18)] for _ in range(40320)]
que = deque([solved])
cnt = 0
print('EP UD move index for phase 1')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_phase1_ep_ud()
    if ep_ud_phase1[idx][1] == -1:
        for twist in successor[1]:
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_phase1_ep_ud()
            ep_ud_phase1[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_ep_ud_phase1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in ep_ud_phase1:
        writer.writerow(arr)


ep_fbrl_phase1 = [[-1 for _ in range(18)] for _ in range(24)]
que = deque([solved])
cnt = 0
print('EP FBRL move index for phase 1')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idx = puzzle.idx_phase1_ep_fbrl()
    if ep_fbrl_phase1[idx][1] == -1:
        for twist in successor[1]:
            n_puzzle = puzzle.move(twist)
            n_idx = n_puzzle.idx_phase1_ep_fbrl()
            ep_fbrl_phase1[idx][twist] = n_idx
            que.append(n_puzzle)
with open('move_ep_fbrl_phase1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in ep_fbrl_phase1:
        writer.writerow(arr)


move_cp = [[] for _ in range(40320)]
with open('move_cp.csv', mode='r') as f:
    for idx in range(40320):
        move_cp[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_co = [[] for _ in range(2187)]
with open('move_co.csv', mode='r') as f:
    for idx in range(2187):
        move_co[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_ep_phase0 = [[] for _ in range(495)]
with open('move_ep_phase0.csv', mode='r') as f:
    for idx in range(495):
        move_ep_phase0[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_eo_phase0 = [[] for _ in range(2048)]
with open('move_eo_phase0.csv', mode='r') as f:
    for idx in range(2048):
        move_eo_phase0[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_ep_ud_phase1 = [[] for _ in range(40320)]
with open('move_ep_ud_phase1.csv', mode='r') as f:
    for idx in range(40320):
        move_ep_ud_phase1[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_ep_fbrl_phase1 = [[] for _ in range(24)]
with open('move_ep_fbrl_phase1.csv', mode='r') as f:
    for idx in range(24):
        move_ep_fbrl_phase1[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]


print('phase0 CO')
prunning = [99 for _ in range(2187)]
solved_idx = solved.idx_cp()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_co[puzzle][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_0.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)


print('phase0 EPEO')
prunning = [99 for _ in range(1013760)]
solved_idx = solved.idx_phase0_eo() * 495 + solved.idx_phase0_ep()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    eo = puzzle // 495
    ep = puzzle % 495
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_eo_phase0[eo][twist] * 495 + move_ep_phase0[ep][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)




print('phase1 CP')
prunning = [99 for _ in range(40320)]
solved_idx = solved.idx_cp()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[1]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_cp[puzzle][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase1_0.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)


print('phase1 EP')
prunning = [99 for _ in range(967680)]
solved_idx = solved.idx_phase1_ep_ud() * 24 + solved.idx_phase1_ep_fbrl()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    ep_ud = puzzle // 24
    ep_fbrl = puzzle % 24
    for twist in successor[1]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_ep_ud_phase1[ep_ud][twist] * 24 + move_ep_fbrl_phase1[ep_fbrl][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase1_1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)
