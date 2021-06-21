from tkinter import *

isGarten = False

def Clear(frame):
    frame.destroy()

def InsertMainFrame():
    frame = Frame(bg='#8fb5f2')
    frame.grid()

    btnRep = Button(frame, text='Составить Отчет', width=18, height=4, font=('Times New Roman', '18'), bg='#e0905e', command=lambda:[Clear(frame), InsertReportFrame()])
    btnRep.grid(row=1, column=1, padx=0, pady=30)

    btnRep = Button(frame, text='Добавить Ингредиент', width=18, height=4, font=('Times New Roman', '18'), bg='#e0905e', command=lambda:[Clear(frame), InsertIngrFrame()])
    btnRep.grid(row=2, column=0, padx=30, pady=30)

    btnRep = Button(frame, text='Добавить Блюдо', width=18, height=4, font=('Times New Roman', '18'), bg='#e0905e', command=lambda:[Clear(frame), InsertDishFrame()])
    btnRep.grid(row=2, column=1, padx=30, pady=30)

def InsertIngrFrame():
    frame = Frame(bg='#8fb5f2')
    frame.grid()

    btnExit = Button(frame, text='Вернутся в меню', width=18, height=2, font=('Times New Roman', '10'), bg='#e0905e', command=lambda:[Clear(frame), InsertMainFrame()])
    btnExit.grid(row=4, column=3, pady=200, padx=50)

    lbl_Ingr = Label(frame, text='Ингредиент:', width=12, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    ent_Ingr = Entry(frame, width=20, font=('Times New Roman', '14'))

    lbl_Ingr.grid(row=1, column=0, padx=50)
    ent_Ingr.grid(row=1, column=1)

    lbl_Price = Label(frame, text='Цена:', width=12, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    ent_Price = Entry(frame, width=20, font=('Times New Roman', '14'))

    lbl_Price.grid(row=2, column=0)
    ent_Price.grid(row=2, column=1)

    btn_Done = Button(frame, text='Добавить', width=12, height=2, font=('Times New Roman', '14'), bg='#e0905e')
    btn_Done.grid(row=3, column=1)

def InsertDishFrame():
    frame = Frame(bg='#8fb5f2')
    frame.grid()

    lblDish = Label(frame, text='Название Блюда:', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    entDish = Entry(frame, width=20, font=('Times New Roman', '14'))

    lblDish.grid(row=0, column=0)
    entDish.grid(row=1, column=0, padx=20)

    lblID = Label(frame, text='ID:', width=4, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    entID = Entry(frame, width=10, font=('Times New Roman', '14'))

    lblID.grid(row=0, column=1, padx=1, columnspan=1)
    entID.grid(row=1, column=1)

    lblDish = Label(frame, text='Кол-во для Сада:', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    entDish = Entry(frame, width=18, font=('Times New Roman', '14'))

    lblDish.grid(row=2, column=1, padx=200)
    entDish.grid(row=3, column=1)

    lblDish = Label(frame, text='Кол-во для Яслей:', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    entDish = Entry(frame, width=18, font=('Times New Roman', '14'))

    lblDish.grid(row=4, column=1, padx=10)
    entDish.grid(row=5, column=1)

    btn_Done = Button(frame, text='Добавить\nингредиент\nв блюдо', width=12, height=3, font=('Times New Roman', '14'), bg='#e0905e')
    btn_Done.grid(row=6, column=1, pady=20)

    btn_Done = Button(frame, text='Добавить\nблюдо', width=12, height=3, font=('Times New Roman', '14'), bg='#e0905e')
    btn_Done.grid(row=6, column=0)

    btnExit = Button(frame, text='Вернутся в меню', width=18, height=2, font=('Times New Roman', '10'), bg='#e0905e', command=lambda:[Clear(frame), InsertMainFrame()])
    btnExit.grid(row=7, column=1, pady=12, padx=50)

def InsertReportFrame():
    frame = Frame(bg='#8fb5f2')
    frame.grid()


    def GartenText():
        if isGarten == True:
            return 'САД'
        else:
            return 'ЯСЛИ'
    def Swap(isGartenTry):
        global isGarten
        if isGartenTry == True:
            isGarten = False
        else:
            isGarten = True
        lbl0 = Label(frame, text=GartenText(), width=5, height=2, font=('Times New Roman', '14', 'bold'), bg='#8fb5f2', fg='#872d00')
        lbl0.grid(row=1, column=0)


    lbl0 = Label(frame, text=GartenText(), width=5, height=2, font=('Times New Roman', '14', 'bold'), bg='#8fb5f2', fg='#872d00')
    lbl1 = Label(frame, text='Завтрак', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    lbl2 = Label(frame, text='Обед', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    lbl3 = Label(frame, text='Ужин', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')

    lbl0.grid(row=1, column=0)
    lbl1.grid(row=1, column=1, padx=10)
    lbl2.grid(row=1, column=2, padx=10)
    lbl3.grid(row=1, column=3, padx=10)
    
    lbl4 = Label(frame, text='Блюдо', width=8, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    lbl5 = Label(frame, text='Кол-во', width=8, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')

    lbl4.grid(row=2, column=0, padx=1)
    lbl5.grid(row=3, column=0, padx=1)

    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=2, column=1)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=2, column=2)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=2, column=3)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=3, column=1)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=3, column=2)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=3, column=3)
    
    btn_Done = Button(frame, text='Добавить\nблюдо на\nзавтрак', width=15, height=3, font=('Times New Roman', '13'), bg='#e0905e')
    btn_Done.grid(row=4, column=1)
    btn_Done = Button(frame, text='Добавить\nблюдо на\nобед', width=15, height=3, font=('Times New Roman', '13'), bg='#e0905e')
    btn_Done.grid(row=4, column=2)
    btn_Done = Button(frame, text='Добавить\nблюдо на\nужин', width=15, height=3, font=('Times New Roman', '13'), bg='#e0905e')
    btn_Done.grid(row=4, column=3)
    btn_Done = Button(frame, text='САД/ЯСЛИ', width=11, height=3, font=('Times New Roman', '10'), bg='#e0905e', command=lambda:[Swap(isGarten)])
    btn_Done.grid(row=4, column=0)

    
    lblName = Label(frame, text='Название файла:', width=14, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    lblName.grid(row=5, column=2, padx=10, pady=20)
    entDish = Entry(frame, width=17, font=('Times New Roman', '14'))
    entDish.grid(row=5, column=3)

    btn_Done = Button(frame, text='Создать отчет', width=16, height=2, font=('Times New Roman', '14'), bg='#e0905e', command=lambda:[Clear(frame), InsertMainFrame()])
    btn_Done.grid(row=6, column=3)

window = Tk()
window.title('KitchenMath')
w = (window.winfo_screenwidth())//2 - 300
h = (window.winfo_screenheight())//2 - 200
window.geometry('600x400+{}+{}'.format(w,h))
window.configure(bg='#8fb5f2')
window.minsize(600,400)
window.maxsize(600,400)

InsertMainFrame()



window.mainloop()