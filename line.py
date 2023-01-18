import tkinter
root = tkinter.Tk()
canvas = tkinter.Canvas(root,width = 640,height = 480)
canvas.configure(bg='#FFFFFF')
canvas.create_line(320,50,200,400,490,176,150,176,440,400,320,50,fill='red')
canvas.pack()
root.mainloop()