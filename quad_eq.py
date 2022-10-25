#二次方程式の解を解の公式を使って求める
import math

print('二次方程式の係数を入力してください')
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))

ans1 = (-b + math.sqrt((b**2)+(-4 * a * c)))/ (2 * a)
ans2 = (-b - math.sqrt((b**2)+(-4 * a * c)))/ (2 * a)

print('解は%6.2fと%6.2fです'%(ans1,ans2))