from cube_class import Cube, face, axis
from time import time

def distance(cube, phase):
    if phase == 0:
        idxes = cube.idx_phase0()
    else:
        idxes = cube.idx_phase1()
    return max(prunning[phase][i][idxes[i]] for i in range(prunning_num[phase]))

def phase_search(phase, puzzle, depth):
    global path
    if depth == 0:
        if distance(puzzle, phase) == 0:
            return True
    else:
        if distance(puzzle, phase) <= depth:
            l_twist = path[-1] if len(path) >= 1 else -10
            ll_twist = path[-2] if len(path) >= 2 else -10
            for twist in successor[phase]:
                if face(twist) == face(l_twist) or axis(twist) == axis(l_twist) == axis(ll_twist):
                    continue
                n_puzzle = puzzle.move(twist)
                path.append(twist)
                if phase_search(phase, n_puzzle, depth - 1):
                    return True
                path.pop()

def solver(puzzle):
    global solution, path
    solution = []
    for phase in range(2):
        print('phase', phase, 'depth', end=' ',flush=True)
        strt = time()
        for depth in range(20):
            print(depth, end=' ', flush=True)
            path = []
            if phase_search(phase, puzzle, depth):
                for twist in path:
                    puzzle = puzzle.move(twist)
                solution.extend(path)
                print('')
                for i in path:
                    print(move_candidate[i], end=' ')
                print('')
                print(time() - strt, 'sec')
                break

prunning_num = [2, 2]
prunning = [[[] for _ in range(prunning_num[i])] for i in range(2)]
for phase in range(2):
    for i in range(prunning_num[phase]):
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
