import tkinter
from tkinter import *
x = 123
def button_clicked():
    print (x)
def caption():
    x = text1.get(0.0, END)
    print (x)
root=Tk()
# кнопка по умолчанию
root.title(u'MyProgram')
var=IntVar()
rbutton1=Radiobutton(root,text='1',variable=var,value=1)
rbutton2=Radiobutton(root,text='2',variable=var,value=2)
rbutton3=Radiobutton(root,text='3',variable=var,value=3)
rbutton1.grid(row=5, column='1')
rbutton2.grid(row=5, column='2')
rbutton3.grid(row=5, column='3')
label = Label(text=u'Значение')
label.grid(row=0, column='2')
text1 = Text(root, bg='black', fg="white", height=1, width=60,)
text1.grid(row=2, column='2')
button1 = Button(root, command=caption)
button1.grid(row=3, column='2',)
# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(root, bg="black", fg="white", text=u"Кликни меня!", command=button_clicked)
button2.grid(row=4, column='2')
root.mainloop()
