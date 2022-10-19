APY = 0.0025
a = int(input('預金額>>>'))
b = a * APY
c = int((b-int(b))*100)
print('{0}円の切り捨てられた利息は{1}銭です'.format(a,c))