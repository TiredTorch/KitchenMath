from tkinter import *


def InsertMainMenu():
    window = Tk()
    window.title('Главная')
    w = (window.winfo_screenwidth())//2 - 300
    h = (window.winfo_screenheight())//2 - 200
    window.geometry('600x400+{}+{}'.format(w,h))
    window.configure(bg='#8fb5f2')
    window.minsize(600,400)
    window.maxsize(600,400)



    btnRep = Button(text='Составить Отчет', width=30, height=5, font=('Times New Roman', '20'), bg='#e0905e')
    btnRep.pack(side=TOP, padx=0, pady=30)

    btnRep = Button(text='Добавить Ингредиент', width=30, height=5, font=('Times New Roman', '12'), bg='#e0905e')
    btnRep.pack(side=LEFT, padx=30, pady=30)

    btnRep = Button(text='Добавить Блюдо', width=30, height=5, font=('Times New Roman', '12'), bg='#e0905e')
    btnRep.pack(side=RIGHT, padx=30, pady=30)

    window.mainloop()

def IngrMenu():
    window = Tk()
    window.title('Добавить Ингредиент')
    w = (window.winfo_screenwidth())//2 - 300
    h = (window.winfo_screenheight())//2 - 200
    window.geometry('600x400+{}+{}'.format(w,h))
    window.configure(bg='#8fb5f2')
    window.minsize(600,400)
    window.maxsize(600,400)

    btnExit = Button(window, text='Вернутся в меню', width=18, height=2, font=('Times New Roman', '10'), bg='#e0905e')
    btnExit.grid(row=4, column=3, pady=200, padx=50)

    lbl_Ingr = Label(master=None, text='Ингредиенты:', width=12, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    ent_Ingr = Entry(width=20, font=('Times New Roman', '14'))

    lbl_Ingr.grid(row=1, column=0, padx=50)
    ent_Ingr.grid(row=1, column=1)

    lbl_Price = Label(master=None, text='Цена:', width=12, height=2, font=('Times New Roman', '14'), bg='#8fb5f2')
    ent_Price = Entry(width=20, font=('Times New Roman', '14'))

    lbl_Price.grid(row=2, column=0)
    ent_Price.grid(row=2, column=1)

    btn_Done = Button(master=None, text='Добавить', width=12, height=2, font=('Times New Roman', '14'), bg='#e0905e')
    btn_Done.grid(row=3, column=1)

    window.mainloop()

InsertMainMenu()