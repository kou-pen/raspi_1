kodukai = int(input('基本額は?>'))
grade = input('成績は?>')
print('今月のあなたの成績は{}ですね。'.format(grade))

if grade == 'A':
    kodukai = kodukai * 3
elif grade == 'B':
    kodukai = kodukai * 2
elif grade == 'C':
    pass
elif grade == 'F':
    kodukai = kodukai // 2
else:
    print('入力エラー')
    
print('したがってお小遣いは{}円です。'.format(kodukai))