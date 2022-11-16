import math
n = int(input('1からnまでの平方根を求めます.n>'))
for i in range(1,n+1):
    sq = math.sqrt(i)
    print('%3d:%8.4f'%(i,sq))
