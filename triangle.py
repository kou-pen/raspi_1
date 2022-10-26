#面積を求める
p = [[0,0],[0,0],[0,0]]
p[0][0] = int(input('X1>>>')) 
p[0][1] = int(input('Y1>>>'))
p[1][0] = int(input('X2>>>'))
p[1][1] = int(input('Y2>>>'))
p[2][0] = int(input('X3>>>'))
p[2][1] = int(input('Y3>>>'))

print('p=',p)
print('A=',p[0])
print('B=',p[1])
print('C=',p[2])

s = (1/2)*abs((p[1][0] - p[0][0])*(p[2][1] - p[0][1]) - (p[1][1] - p[0][1])*(p[2][0] - p[0][0]))
print('面積は',s)