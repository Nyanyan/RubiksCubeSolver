from cube_class import Cube, face, axis
from collections import deque
import csv

#                  0    1     2     3    4     5     6     7    8     9    10    11    12   13    14    15   16    17
move_candidate = ["R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'"]

successor = [
    [0,    2, 3,    5, 6, 7, 8, 9, 10, 11, 12,     14, 15,     17],
]

solved = Cube()
'''
print('phase0 CO')
prunning = [99 for _ in range(2187)]
que = deque([[solved, 0, -10, -10]])
prunning[solved.idx_phase0()[0]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = puzzle.move(twist)
        idx = n_puzzle.idx_phase0()[0]
        if prunning[idx] > num + 1:
            prunning[idx] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_0.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)

print('phase0 EPEO')
prunning = [99 for _ in range(1013760)]
que = deque([[solved, 0, -10, -10]])
prunning[solved.idx_phase0()[1]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = puzzle.move(twist)
        idx = n_puzzle.idx_phase0()[1]
        if prunning[idx] > num + 1:
            prunning[idx] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)
'''




''' ボツ
print('phase0 EP')
prunning = [99 for _ in range(495)]
que = deque([[solved, 0, -10, -10]])
prunning[solved.idx_phase0()[1]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = puzzle.move(twist)
        idx = n_puzzle.idx_phase0()[1]
        if prunning[idx] > num + 1:
            prunning[idx] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_1.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)

print('phase0 EO')
prunning = [99 for _ in range(2048)]
que = deque([[solved, 0, -10, -10]])
prunning[solved.idx_phase0()[2]] = 0
cnt = 0
while que:
    cnt += 1
    if cnt % 1000 == 0:
        print(cnt, len(que))
    puzzle, num, l_twist, ll_twist = que.popleft()
    for twist in successor[0]:
        if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
            continue
        n_puzzle = puzzle.move(twist)
        idx = n_puzzle.idx_phase0()[2]
        if prunning[idx] > num + 1:
            prunning[idx] = num + 1
            que.append([n_puzzle, num + 1, twist, l_twist])
with open('prunning_phase0_2.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(prunning)
'''