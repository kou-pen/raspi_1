import random as rand
hand = {0:'グー',1:'チョキ',2:'パー'}

print('ジャンケンゲーム')
while(True):
    user = int(input('0:グー、1:チョキ、2:パー>'))
    com = rand.randint(0,2)

    if user in hand:
        print('あなたの手は{}ですね'.format(hand[user]))
        print('コンピューターの手は{}です'.format(hand[com]))
        if user == com:
            print('あいこです')
        elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com ==0):
            print('あなたの勝ちです')
        else:
            print('あなたの負けです')
    else:
        print('ずるいぞ')
        break