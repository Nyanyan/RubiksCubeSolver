# coding:utf-8
'''
Corner
   B
  0 1 
L 2 3 R
   F

   F
  4 5
L 6 7 R
   B


Edge
top layer
    B
    0
L 3   1 R
    2
    F

middle layer
4 F 5 R 6 B 7

bottom layer
    F
    8
L 11  9 R
    10
    B
'''

def move_cp(cp, mov):
    surface = [[3, 1, 7, 5], [0, 2, 4, 6], [0, 1, 3, 2], [4, 5, 7, 6], [2, 3, 5, 4], [1, 0, 6, 7]]
    res = [i for i in cp]
    mov_type = mov // 3
    mov_amount = mov % 3
    for i in range(4):
        res[surface[mov_type][(i + mov_amount + 1) % 4]] = cp[surface[mov_type][i]]
    return res

def move_co(co, mov):
    surface = [[3, 1, 7, 5], [0, 2, 4, 6], [0, 1, 3, 2], [4, 5, 7, 6], [2, 3, 5, 4], [1, 0, 6, 7]]
    pls = [2, 1, 2, 1]
    res = [i for i in co]
    mov_type = face(mov)
    mov_amount = mov % 3
    for i in range(4):
        res[surface[mov_type][(i + mov_amount + 1) % 4]] = co[surface[mov_type][i]]
        if axis(mov) != 1 and mov_amount != 1:
            res[surface[mov_type][(i + mov_amount + 1) % 4]] += pls[(i + mov_amount + 1) % 4]
            res[surface[mov_type][(i + mov_amount + 1) % 4]] %= 3
    return res

def move_ep(ep, mov):
    surface = [[1, 6, 9, 5], [3, 4, 11, 7], [0, 1, 2, 3], [8, 9, 10, 11], [2, 5, 8, 4], [0, 7, 10, 6]]
    res = [i for i in ep]
    mov_type = face(mov)
    mov_amount = mov % 3
    for i in range(4):
        res[surface[mov_type][(i + mov_amount + 1) % 4]] = ep[surface[mov_type][i]]
    return res

def move_eo(eo, mov):
    surface = [[1, 6, 9, 5], [3, 4, 11, 7], [0, 1, 2, 3], [8, 9, 10, 11], [2, 5, 8, 4], [0, 7, 10, 6]]
    res = [i for i in eo]
    mov_type = face(mov)
    mov_amount = mov % 3
    for i in range(4):
        res[surface[mov_type][(i + mov_amount + 1) % 4]] = eo[surface[mov_type][i]]
    if axis(mov) == 2 and mov_amount != 1:
        for i in surface[mov_type]:
            res[i] += 1
            res[i] %= 2
    return res

# cp配列から固有の番号を作成
# Return the number of CP
def cp2idx(cp):
    res = 0
    for i in range(8):
        cnt = cp[i]
        for j in cp[:i]:
            if j < cp[i]:
                cnt -= 1
        res += fac[7 - i] * cnt
    return res

# co配列から固有の番号を作成
# Return the number of CO
def co2idx(co):
    res = 0
    for i in co[:7]:
        res *= 3
        res += i
    return res

def ep2idx(ep):
    ep_proc = []
    ep_e_slice = [True for _ in range(12)]
    for i in range(12):
        if 4 <= ep[i] <= 7:
            ep_e_slice[i] = False
        elif ep[i] < 4:
            ep_proc.append(ep[i])
        else:
            ep_proc.append(ep[i] - 4)
    res = 0
    for i in range(8):
        cnt = ep_proc[i]
        for j in ep_proc[:i]:
            if j < ep_proc[i]:
                cnt -= 1
        res += fac[7 - i] * cnt
    res *= 495
    remain = 4
    for i in reversed(range(12)):
        if ep_e_slice[i]:
            res += cmb(i, remain - 1)
        else:
            remain -= 1
    return res

def eo2idx(eo):
    res = 0
    for i in range(11):
        res *= 2
        res += eo[i]
    return res

def idx2cp(cp_idx):
    res = [-1 for _ in range(8)]
    for i in range(8):
        candidate = cp_idx // fac[7 - i]
        marked = [True for _ in range(i)]
        for _ in range(8):
            for j, k in enumerate(res[:i]):
                if k <= candidate and marked[j]:
                    candidate += 1
                    marked[j] = False
        res[i] = candidate
        cp_idx %= fac[7 - i]
    return res

def idx2co(co_idx):
    res = [0 for _ in range(8)]
    for i in range(7):
        res[6 - i] = co_idx % 3
        co_idx //= 3
    res[7] = (3 - sum(res) % 3) % 3
    return res

def idx2ep(ep_idx):
    

def cmb(n, r):
    if r == 0:
        return 0
    return fac[n] // fac[r] // fac[n - r]

fac = [1]
for i in range(1, 12):
    fac.append(fac[-1] * i)

