from tkinter import *
def ayush(event):

     text= event.widget.cget("text")
     print(text)

     if text=="=":
          if uservalue.get().isdigit():
               value=int(uservalue.get())
          else:
               value=eval(display.get())

          uservalue.set(value)
          display.update()

     elif text=="CC":
          uservalue.set("")
          display.update()
     else:
          uservalue.set(uservalue.get() + text)
          display.update()



ayush_root=Tk()
ayush_root.geometry("300x300")
ayush_root.title("Calculator by Ayush")

f=Frame(ayush_root,bg="grey")
f.pack()

uservalue=StringVar()
uservalue.set("")
display=Entry(f,textvariable=uservalue,font=5)
display.pack(fill=X,ipadx=10,ipady=10,padx=5,pady=5)

b1=Button(f,text="7",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="8",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="9",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="/",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="CC",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)


f=Frame(ayush_root,bg="grey")
f.pack()

b1=Button(f,text="4",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="5",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="6",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="*",padx=5,pady=5,font="bold")
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

f=Frame(ayush_root,bg="grey")
f.pack()

b1=Button(f,text="1",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="2",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="3",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="-",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)


f=Frame(ayush_root,bg="grey")
f.pack()


b1=Button(f,text="0",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text=".",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="=",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

b1=Button(f,text="+",padx=5,pady=5)
b1.pack(side=LEFT,padx=10,pady=10)
b1.bind('<Button-1>',ayush)

ayush_root.mainloop()