import DB as db
import os

def Menu():
    act = 0
    while(act != 9):  
        print('-------------------------------------------------------')
        print('(1) Для добавления ингредиента')
        print('(2) Для добавления блюда')
        print('(3) Для формирования отчета')
        print('(4) Для просмотра ID инградиентов')
        print('(5) Для просмотра ID блюд')
        print('(9) Для выхода из программы')
        act = int(input("Выберете действие: "))
        print('-------------------------------------------------------')

        if(act == 1):
            db.AddIngredient()  
            os.system('CLS')
            print('Ингредиент успешно добавлен')
        elif(act == 2):
            db.AddDish()  
            os.system('CLS')
            print('Блюдо успешно добавлено')
        elif(act == 3):
            db.FillReport()
            os.system('CLS')
            print('Отчет успешно составлен')
        elif(act == 4):
            print('-------------------------------------------------------')
            db.ShowIngredientID()
        elif(act == 5):
            print('-------------------------------------------------------')
            db.ShowDishesID()
        elif(act == 9):  
            os.system('CLS')
            print('Завершение программы...')
        else:  
            os.system('CLS')
            print('Неопознаный ключ, введите ключ заново.')
            
Menu()