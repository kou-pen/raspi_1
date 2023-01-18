def mma(a,b,c):
    maxdata = max(a,b,c)
    mindata = min(a,b,c)
    average = (a + b + c) / 3
    return maxdata,mindata,average
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
maxdata ,mindata ,average = mma(a,b,c)

print('最大値=',maxdata)
print('最小値=',mindata)
print('平均値=',average)