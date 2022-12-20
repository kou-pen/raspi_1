def syahen(x,y):
    import math
    z = math.sqrt(x*x + y*y)
    return z

print('直角を挟む2辺の長さは?')
x = float(input('x='))
y = float(input('y='))
z = syahen(x,y)
print('斜辺の長さは%6.2f'%z)