import statistics as stat

num = [0,0,0]

num[0] = int(input('a>'))
num[1] = int(input('b>'))
num[2] = int(input('c>'))

med = stat.median(num)
print(med)
