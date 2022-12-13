import random
r = random.randint(1,100)
i = 0
while True:
    a = int(input('数を当ててみて>'))
    i += 1
    if a > r:
        print('もっと小さい')
    elif a < r:
        print('もっと大きい')
    else:
        break
print('%d手で正解!おめでとう!'%i)