ride = {'m':'メリーゴーランド','j':'ジェットコースター'}
age = int(input('何歳ですか?>'))
n = input('乗りたいものはなんですか?(m/j)>')
print('あなたの年齢は{0}歳で希望の乗り物は{1}ですね'.format(age,ride[n]))
if (age >= 5 and n == 'm')or(age >= 8 and n == 'j'):
    print('どうぞお乗りください')
else:
    print('大きくなってからね')