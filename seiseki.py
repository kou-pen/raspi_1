eng = input('英語の成績を入れて>')
math = input('数学の成績を入れて>')
print('あなたの成績は、英語が{0}で数学が{1}だね'.format(eng,math))
if (eng == 'a' or eng == 'b')and(math == 'a' or math == 'b'):
    print('頑張ったね')