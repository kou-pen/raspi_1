def kazu_kime():
    import random
    k = [0] *3
    k[0] = random.randint(0,9)
    while True:
        k[1] = random.randint(0,9)
        if k[0] != k[1]:
            break
    while True:
        k[2] = random.randint(0,9)
        if k[0] != k[2] and k[1] != k[2]:
            break
    return k

def bunkatu(n):
    g = [0] * 3
    nn = n
    for i in range(3):
        g[i] = nn % 10
        nn = nn // 10
    return g

def check(com,usr):
    h = 0
    b = 0
    for i in range(3):
        for j in range(3):
            if com[i] == usr[j]:
                if i == j:
                    h = h + 1
                else:
                    b = b + 1
    return h,b

#main
kotae = [0] * 3
kaitou = [0] * 3
kotae = kazu_kime()
while True:
    u = int(input('数を入れて'))
    kaitou = bunkatu(u)
    h,b = check(kaitou,kotae)
    print('%03dは%dヒット%dブローです'%(u,h,b))
    if h == 3:
        break
print('正解しました。おめでとうございます。')