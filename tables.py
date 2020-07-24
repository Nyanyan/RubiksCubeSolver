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

'''
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


ep_move = [[[-1 for _ in range(18)] for _ in range(11880)] for _ in range(3)]
que = deque([solved])
cnt = 0
print('EP move index')
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle = que.popleft()
    idxes = puzzle.idx_ep()
    if ep_move[0][idxes[0]][0] == -1:
        for twist in range(18):
            n_puzzle = puzzle.move(twist)
            n_idxes = n_puzzle.idx_ep()
            for mse in range(3):
                ep_move[mse][idxes[mse]][twist] = n_idxes[mse]
            que.append(n_puzzle)
with open('move_ep.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in ep_move:
        for arr2 in arr:
            writer.writerow(arr2)
'''


''' ボツ
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
'''


move_cp = [[] for _ in range(40320)]
with open('move_cp.csv', mode='r') as f:
    for idx in range(40320):
        move_cp[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_co = [[] for _ in range(2187)]
with open('move_co.csv', mode='r') as f:
    for idx in range(2187):
        move_co[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
'''
move_ep_phase0 = [[] for _ in range(495)]
with open('move_ep_phase0.csv', mode='r') as f:
    for idx in range(495):
        move_ep_phase0[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
'''
move_eo = [[] for _ in range(2048)]
with open('move_eo.csv', mode='r') as f:
    for idx in range(2048):
        move_eo[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
'''
move_ep_ud_phase1 = [[] for _ in range(40320)]
with open('move_ep_ud_phase1.csv', mode='r') as f:
    for idx in range(40320):
        move_ep_ud_phase1[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
move_ep_fbrl_phase1 = [[] for _ in range(24)]
with open('move_ep_fbrl_phase1.csv', mode='r') as f:
    for idx in range(24):
        move_ep_fbrl_phase1[idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]
'''

move_ep = [[[] for _ in range(11880)] for _ in range(3)]
with open('move_ep.csv', mode='r') as f:
    for mse in range(3):
        for idx in range(11880):
            move_ep[mse][idx] = [int(i) for i in f.readline().replace('\n', '').split(',')]

'''
# EO
print('EO')
prunning = [99 for _ in range(2048)]
solved_idx = solved.idx_eo()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in range(18):
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_eo[puzzle][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)


# EP
print('EP')
prunning = [[99 for _ in range(11880)] for _ in range(3)]
solved_idx = solved.idx_ep()
que = deque([[solved_idx, 0, -10, -10]])
for mse in range(3):
    prunning[mse][solved_idx[mse]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in range(18):
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = [move_ep[mse][puzzle[mse]][twist] for mse in range(3)]
        flag = False
        for mse in range(3):
            if prunning[mse][n_puzzle[mse]] > num + 1:
                prunning[mse][n_puzzle[mse]] = num + 1
                flag = True
        if flag:
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase1.csv', mode='a') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in prunning:
        writer.writerow(arr)
'''

'''
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
'''
'''
print('phase0 EP')
prunning = [[99 for _ in range(11880)] for _ in range(3)]
solved_idx = solved.idx_ep()
que = deque([[solved, 0, -10, -10]])
for mse in range(3):
    prunning[mse][solved_idx[mse]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in range(18):
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = puzzle.move(twist)
        n_idxes = n_puzzle.idx_ep()
        flag = False
        if n_puzzle.solved_ep_phase0():
            for mse in range(3):
                if prunning[mse][n_idxes[mse]] != 0:
                    prunning[mse][n_idxes[mse]] = 0
                    flag = True
        else:
            for mse in range(3):
                if prunning[mse][n_idxes[mse]] > num + 1:
                    prunning[mse][n_idxes[mse]] = num + 1
                    flag = True
        if flag:
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0.csv', mode='a') as f:
    writer = csv.writer(f, lineterminator='\n')
    for arr in prunning:
        writer.writerow(arr)


print('phase0 EO')
prunning = [99 for _ in range(2048)]
solved_idx = solved.idx_eo()
que = deque([[solved_idx, 0, -10, -10]])
prunning[solved_idx] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in range(18):
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = move_eo[puzzle][twist]
        if prunning[n_puzzle] > num + 1:
            prunning[n_puzzle] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0.csv', mode='a') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)
'''


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

'''
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
'''