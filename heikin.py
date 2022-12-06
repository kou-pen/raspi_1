n = int(input('学生の人数は?>'))
sump = 0
student = [0] * n
for i in range(n):
    point = int(input('%d人目の点数は?>'%(i+1)))
    student[i] = point
    sump = sump + point
avg = sump / n
print('')
for i in range(n):
    print('%d人目の点数は%d点'%((i+1),student[i]))
print('平均点は%5.1f点です'%avg)

    