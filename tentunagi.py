import tkinter

#init
root = tkinter.Tk()
canvas = tkinter.Canvas(root,width = 620,height = 620)
canvas.configure(bg='#FFFFFF')

#define
try:
    f = open('g.txt','r')
    lines = f.readlines()
except IOError:
    print('ファイルが開けません。')
except EOFError:
    print('ファイルが壊れています。')
    f.close()
else:
    f.close()
    for line in lines:
        x1,y1,x2,y2 = line.split(',')
        canvas.create_line(x1,y1,x2,y2,fill='red')
    canvas.pack()
    root.mainloop()
    
        