s = input('いらっしゃいませ。性別は?(男/女)>')
r = int(input('ご飯の量は何g?>'))
print('あなたは{0}性で、ご飯の量は{1}gですね。'.format(s,r))
if s == '男':
    if r >= 900:
        print('やめたほうがいいんじゃない')
    else:
        print('ごゆっくり')
else:
    if r >= 600:
        print('無理しないほうがいいよ')
    else:
        print('ごゆっくり')