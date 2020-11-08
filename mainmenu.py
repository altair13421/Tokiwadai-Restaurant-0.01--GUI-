from tkinter import *
import sys


menu = Tk()
#defining main window
menu.geometry("500x500")
menu.title('TOKIWADAI Restaurant')
menu.config(background="black")
menu.resizable(width=FALSE, height=FALSE)

# cunt-sumer count
c = 0

#start of main gui window, this is were the fun begins
c1 = Canvas(menu, width = 500, height = 120, bg='black', bd=0, highlightthickness=0, relief='ridge')
c1.create_text(250, 20, fill='white', text="MENU", font=('helvetica', 20))
c1.create_text(100, 70, fill='white', text="Foods", font=('helvetica', 15))
c1.pack()
#og foods
var = IntVar()
R1 = Radiobutton(menu, text="Option 1: Omolette and Bread", variable=var, value=1, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
R1.pack()

R2 = Radiobutton(menu, text="Option 2: Chicken Soup", variable=var, value=2, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
R2.pack()

R3 = Radiobutton(menu, text="Option 3: Shwarma(large)", variable=var, value=3, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
R3.pack()
c1 = Canvas(menu, width = 500, height = 100, bg='black', bd=0, highlightthickness=0, relief='ridge')
c1.create_text(100, 50, fill='white', text="Drinks", font=('helvetica', 15))
c1.pack()
#drink
var2 = IntVar()
r1 = Radiobutton(menu, text="Option 1: Sprite", variable=var2, value=1, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
r1.pack()
r2 = Radiobutton(menu, text="Option 1: Coke", variable=var2, value=2, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
r2.pack()
r3 = Radiobutton(menu, text="Option 1: Dew", variable=var2, value=3, fg='white', bg='black'
                 ,activebackground='black', activeforeground='gray', selectcolor='black', justify=LEFT)
r3.pack()
#just jank
def disable_event():
    pass

#reset function
def r():
    var.set(0)
    var2.set(0)

#total function
def compute():
    global c
    c=c+1
    #new windows
    to = Tk()
    to.protocol("WM_DELETE_WINDOW", disable_event)
    to.geometry("500x300")
    to.title('TOTAL')
    to.config(background="black")
    to.resizable(width=FALSE, height=FALSE)

    total = 0
    foo = 0
    dri = 0.99
    v=var.get()
    v1 = var2.get()
    if (v==1):
        total = 4.99
        foo = 4.99
        sor = "Omolette and Bread"
    elif (v==2):
        total = 3.99
        foo = 3.99
        sor = "Chicken Soup"
    elif (v==3):
        total = 5.99
        foo = 5.99
        sor = "Shwarma(large)"
    else:
        sor = "you didn't select any food items"
    if (v1==1):
        total = total+0.99
        sor1 = "Sprite"
    elif (v1==2):
        total = total+0.99
        sor1 = "Coke"
    elif (v1==3):
        total = total+0.99
        sor1 = "Dew"
    else:
        dri = 0
        sor1 = "you didn't select any drink"
    c1 = Canvas(to, width=500, height=260, bg='black', bd=0, highlightthickness=0, relief='ridge')
    c1.create_text(250, 20, fill='white', text="Total", font=('helvetica', 20))
    c1.create_text(50, 50, fill='white', text="Food", font=('helvetica', 15))
    c1.create_text(70, 90, fill='white', text=sor, font=('helvetica', 10))
    c1.create_text(450, 90, fill='white', text=foo, font=('helvetica', 10))
    c1.create_text(50, 130, fill='white', text="Drink", font=('helvetica', 15))
    c1.create_text(80, 170, fill='white', text=sor1, font=('helvetica', 10))
    c1.create_text(450, 170, fill='white', text=dri, font=('helvetica', 10))
    temtol = "Total:" + str(total)
    c1.create_text(250, 210, fill='white', text=temtol, font=('helvetica', 17))
    c1.pack()
    b = Button(to, text='close', command=to.destroy, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    b.pack()
    selection = "Customer:" + str(c)
    label.config(text=selection)
    r()

#exit function window for toolbar / menu
def des():
    to1 = Tk()
    to1.geometry("100x70")
    to1.title('EXIT')
    to1.config(background="black")
    to1.resizable(width=FALSE, height=FALSE)
    c = Canvas(to1, width='100', height='20',bg='black', bd=0, highlightthickness=0, relief='ridge')
    c.pack()
    b = Button(to1, text='exit',command=sys.exit, bg='green',fg='white',font=('helvetica',12,'bold'))
    b.pack()
def hel():
    he="Exit the program:\n if you want to exit the program \n just click on \"exit\" in the taskbar\n then click the \"exit\" button\n then click the \"exit\" button in the new dialog box"
    to2 = Tk()
    to2.geometry("300x110")
    to2.title('HELP')
    to2.config(background="black")
    to2.resizable(width=FALSE, height=FALSE)
    c = Canvas(to2, width='200', height='20',bg='black', bd=0, highlightthickness=0, relief='ridge')
    c.pack()
    l = Label(to2, text=he,bg='black',fg='white',font=('helvetica',10))
    l.pack(anchor = W)
#diableing the 'x' button
menu.protocol("WM_DELETE_WINDOW", disable_event)

#toolbar / menu
m = Menu(menu)
e = Menu(m ,tearoff=0)
e.add_command(label='exit', command=des)
m.add_cascade(label="exit", menu=e)

h = Menu(m ,tearoff=0)
h.add_command(label='help', command=hel)
m.add_cascade(label='help', menu=h)

#totalbutton
c1 = Canvas(menu, width = 500, height = 100, bg='black', bd=0, highlightthickness=0, relief='ridge')
button1 = Button(text='total_it!',width=10, command=compute, bg='green', fg='white', font=('helvetica', 12, 'bold'))
button2 = Button(text='reset', command=r, bg='green', fg='white', font=('helvetica', 12, 'bold'))
c1.create_window(250, 50, window=button1)
c1.create_window(450, 50, window=button2)
c1.pack()
label = Label(menu,fg='white',bg='black',justify=LEFT)
label.pack(anchor = W)

menu.config(menu=m)

menu.iconphoto(False, PhotoImage(file='Restaurant-icon.png'))

menu.mainloop()
#this is where the fun ends