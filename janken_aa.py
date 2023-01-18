import numpy as np
hand = {0:'グー',1:'チョキ',2:'パー'}
data = [[0 for i in range(3)] for j in range(3)]
next_j = {0:2 ,1:0 ,2:1}
last = 0
count = 0
print('ジャンケンゲーム')
how_many = int(input('何回やりたい?'))

while(how_many != count):
    user = int(input('0:グー、1:チョキ、2:パー>'))
    com = np.argmax(data,last)
    print(com)
    if user in hand:
        print('あなたの手は{}ですね'.format(hand[user]))
        print('コンピューターの手は{}です'.format(hand[com]))
        if user == com:
            print('あいこです')
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com ==0):
            print('あなたの勝ちです')
        else:
            print('あなたの負けです')
        data[last][user] += 1
        last = user
    else:
        print('ずるいぞ')
        break
    count += 1
    
