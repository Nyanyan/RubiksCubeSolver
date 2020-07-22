from cube_class import Cube, face, axis
from time import time

def distance(puzzle_arr, phase):
    if phase == 0:
        idxes = [puzzle_arr[0], puzzle_arr[1] + puzzle_arr[2] * 495]
    else:
        idxes = [puzzle_arr[0], puzzle_arr[1] * 24 + puzzle_arr[2]]
    return max(prunning[phase][i][idxes[i]] for i in range(2))

def twist_arr(phase, puzzle_arr, twist):
    if phase == 0:
        return [move_co[puzzle_arr[0]][twist], move_ep_phase0[puzzle_arr[1]][twist], move_eo_phase0[puzzle_arr[2]][twist]]
    else:
        return [move_cp[puzzle_arr[0]][twist], move_ep_ud_phase1[puzzle_arr[1]][twist], move_ep_fbrl_phase1[puzzle_arr[2]][twist]]

def phase_search(phase, puzzle_arr, depth):
    global path
    if depth == 0:
        if distance(puzzle_arr, phase) == 0:
            return True
    else:
        if distance(puzzle_arr, phase) <= depth:
            l_twist = path[-1] if len(path) >= 1 else -10
            ll_twist = path[-2] if len(path) >= 2 else -10
            for twist in successor[phase]:
                if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
                    continue
                n_puzzle_arr = twist_arr(phase, puzzle_arr, twist)
                path.append(twist)
                if phase_search(phase, n_puzzle_arr, depth - 1):
                    return True
                path.pop()

def solver(puzzle):
    global solution, path
    solution = []
    for phase in range(2):
        print('phase', phase, 'depth', end=' ',flush=True)
        strt = time()
        if phase == 0:
            puzzle_arr = [puzzle.idx_co(), puzzle.idx_phase0_ep(), puzzle.idx_phase0_eo()]
        else:
            puzzle_arr = [puzzle.idx_cp(), puzzle.idx_phase1_ep_ud(), puzzle.idx_phase1_ep_fbrl()]
        for depth in range(20):
            print(depth, end=' ', flush=True)
            path = []
            if phase_search(phase, puzzle_arr, depth):
                for twist in path:
                    puzzle = puzzle.move(twist)
                solution.extend(path)
                print('')
                for i in path:
                    print(move_candidate[i], end=' ')
                print('')
                print(time() - strt, 'sec')
                break

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

prunning = [[[] for _ in range(2)] for _ in range(2)]
for phase in range(2):
    for i in range(2):
        with open('prunning_phase' + str(phase) + '_' + str(i) + '.csv', mode='r') as f:
            prunning[phase][i] = [int(i) for i in f.readline().replace('\n', '').split(',')]


successor = [
    [0,    2, 3,    5, 6, 7, 8, 9, 10, 11, 12,     14, 15,     17],
    [   1,       4,    6, 7, 8, 9, 10, 11,     13,         16    ]
]
move_candidate = ["R", "R2", "R'", "L", "L2", "L'", "U", "U2", "U'", "D", "D2", "D'", "F", "F2", "F'", "B", "B2", "B'"]
solution = []
path = []
scarmble = [move_candidate.index(i) for i in input('scramble: ').split()]
puzzle = Cube()
for i in scarmble:
    puzzle = puzzle.move(i)
strt = time()
solver(puzzle)
print('solution:', end=' ')
for i in solution:
    print(move_candidate[i], end=' ')
print('')
print(len(solution), 'moves')
print('time:', time() - strt, 'sec')
