import tkinter
import sys
import random

#init
root = tkinter.Tk( )
hand = {0:'グー',1:'チョキ',2:'パー'}

#define
def janken(user):
    com = random.randint(0,2)
    label4.configure(text=hand[user])
    label5.configure(text=hand[com])
    if user == com:
        label6.configure(text='結果はあいこです。')
    elif (user == 0 and com == 1) or (user == 1 and com == 2) or (user == 2 and com ==0):
        label6.configure(text='結果はあなたの勝ちです。')
    else:
        label6.configure(text='結果はコンピュータの勝ちです。')
    
#ウィジェットの生成
label1 = tkinter.Label(root, text='じゃんけんゲーム　ボタンを押してね')
label2 = tkinter.Label(root, text='あなた')
label3 = tkinter.Label(root, text='コンピュータ')
label4 = tkinter.Label(root, text='じゃんけん')
label5 = tkinter.Label(root, text='ジャンケン')
label6 = tkinter.Label(root, text='対戦結果')
button1 = tkinter.Button(root, width=10, text='グー', command=lambda : janken(0))
button2 = tkinter.Button(root, width=10, text='チョキ', command=lambda : janken(1))
button3 = tkinter.Button(root, width=10, text='パー', command=lambda : janken(2))
button4 = tkinter.Button(root, text='ばいばい', command=sys.exit) #exit

#ウィジェットの配置
label1.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
label2.grid(row=1, column=0, padx=1, pady=1)
label3.grid(row=1, column=2, padx=1, pady=1)
label4.grid(row=2, column=0, padx=1, pady=1)
label5.grid(row=2, column=2, padx=1, pady=1)
label6.grid(row=3, column=0, columnspan=3, padx=1, pady=1)
button1.grid(row=4, column=0, padx=1, pady=1)
button2.grid(row=4, column=1, padx=1, pady=1)
button3.grid(row=4, column=2, padx=1, pady=1)
button4.grid(row=5, column=0, columnspan=3, sticky='ew' , padx=1, pady=1)

#mainloop
root.mainloop( )


    


