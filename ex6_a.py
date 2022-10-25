#sからrを求める
import math

PI = math.pi

s = float(input('面積>>>'))
r = math.sqrt(s / PI)
print('半径は%6.3f'%r)