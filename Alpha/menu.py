import DB as db

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
            print(chr(27) + "[2J")
            print('Ингредиент успешно добавлен')
        elif(act == 2):
            db.AddDish()  
            print(chr(27) + "[2J")
            print('Блюдо успешно добавлено')
        elif(act == 3):
            print('Coming soon')
        elif(act == 4):
            print('-------------------------------------------------------')
            db.ShowIngredientID()
        elif(act == 5):
            print('-------------------------------------------------------')
            db.ShowDishesID()
        elif(act == 9):  
            print(chr(27) + "[2J")
            print('Завершение программы...')
        else:  
            print(chr(27) + "[2J")
            print('Неопознаный ключ, введите ключ заного.')
            
Menu()