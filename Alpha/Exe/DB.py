import openpyxl
import os

wb = openpyxl.reader.excel.load_workbook(filename="DB.xlsx", data_only = True)
wbT = openpyxl.reader.excel.load_workbook(filename="template.xlsx", data_only = True)
wb.active = 0  #база данных ингредиентов
ws0 = wb.active
wb.active = 1  #база данных блюд
ws1 = wb.active
wbT.active = 0  #переменные шаблона Сада
wsT1 = wbT.active
wbT.active = 1  #переменные шаблона Яслей
wsT2 = wbT.active

def AddIngredient(): 
    os.system('CLS')

    i = 1
    while(ws0['A'+str(i)].value != '*'):
        i+=1
    
    ws0['B'+str(i)].value = input('Название ингредиента: ')
    ws0['C'+str(i)].value = float(input('Его цена: '))
    ws0['A'+str(i)].value = int(ws0['A'+str(i-1)].value) + 1
    ws0['A'+str(i+1)].value = '*'
    wb.save("DB.xlsx")

def AddDish():    
    os.system('CLS')
    
    i = 1
    while(ws1['H'+str(i)].value != '*'):
        i+=1

    ws1['A'+str(i)].value = input('Введите название блюда: ')
    ws1['B'+str(i)].value = int(input('Введите количество ингредиентов: '))
    ws1['C'+str(i)].value = ''

    ws1['A'+str(i+1)].value = 'Продукты'
    ws1['B'+str(i+1)].value = 'Цена за кг'
    ws1['C'+str(i+1)].value = 'Кол-во (сад)'
    ws1['D'+str(i+1)].value = 'Кол-во (ясли)'
    ws1['E'+str(i+1)].value = 'СумСт (сад)'
    ws1['F'+str(i+1)].value = 'СумСт (ясли)'
    ws1['G'+str(i)].value = 'ID:'

    for j in range(ws1['B'+str(i)].value):
        a = int(input('Укажите ID ингредиента '+str(j+1)+': '))
        
        ws1['A'+str(i+2+j)].value = ws0['B'+str(a+2)].value
        ws1['B'+str(i+2+j)].value = ws0['C'+str(a+2)].value

        ws1['C'+str(i+2+j)].value = float(input('Введите кол-во для сада: '))
        ws1['D'+str(i+2+j)].value = float(input('Введите кол-во для яслей: '))

        ws1['E'+str(i+2+j)].value = '=B'+str(i+2+j)+'*C'+str(i+2+j)+'/1000'
        ws1['F'+str(i+2+j)].value = '=B'+str(i+2+j)+'*D'+str(i+2+j)+'/1000'

        os.system('CLS')

        ws1['E'+str(i+3+int(ws1['B'+str(i)].value))].value = 'Сумма: '
        ws1['E'+str(i+4+int(ws1['B'+str(i)].value))].value = '=SUM(E'+str(i+2)+':E'+str(i+2+j)+')'
        ws1['F'+str(i+4+int(ws1['B'+str(i)].value))].value = '=SUM(F'+str(i+2)+':F'+str(i+2+j)+')'


    ws1['H'+str(i+6+int(ws1['B'+str(i)].value))].value = '*'

    temp = 1
    while(ws1['H'+str(i-temp)].value == None):
        temp+=1

    ws1['H'+str(i)].value = ws1['H'+str(i-temp)].value + 1

    wb.save("DB.xlsx")

def ShowIngredientID():
    os.system('CLS')

    i = 1
    while(ws0['A'+str(i)].value != '*'):
        print(ws0['B'+str(i)].value + ' :: ' + str(ws0['A'+str(i)].value))
        i+=1

def ShowDishesID():
    os.system('CLS')

    print('Блюдо :: ID')
    i = 2
    while(ws1['H'+str(i)].value != '*'):
        print(ws1['A'+str(i)].value + ' :: ' + str(ws1['H'+str(i)].value))
        i+=(ws1['B'+str(i)].value + 6)

def FillReport():


    letters = ['D','F','H','J','L','N']
    PrepareTable(letters, wsT1)
    PrepareTable(letters, wsT2)

    for FT in range (3):
        os.system('CLS')
        dishesAmount = int(input('Сколько блюд в ' + str(FT + 1) + ' приеме пищи: '))
        for DT in range (dishesAmount):
            os.system('CLS')
            print('Для '+str((DT+1))+' блюда: ')
            print('Сад:')
            DishPars(str(letters[FT * 2]), str(letters[(FT * 2) + 1]), wsT1, 'E')
            print('Ясли:')
            DishPars(str(letters[FT * 2]), str(letters[(FT * 2) + 1]), wsT2, 'F')

    
    wbT.save(str(input('Введите название документа: '))+'.xlsx')

def DishPars(firCell, secCell, wsT, ForE):

    tempDishID = int(input('Введите ID блюда: '))

    wsT[str(firCell)+'17'].value += (input('Введите его количество: ') + '\n')

    pointDB = 1
    while(tempDishID != ws1['H'+str(pointDB)].value): #ищет блюдо парсом по айди
        pointDB+=1
    
    wsT[firCell+'11'].value += (ws1['A'+str(pointDB)].value + '\n')
    IngrPars(pointDB, firCell, secCell, wsT, ForE)

def IngrPars(pointDB, firCell, secCell, wsT, ForE):
    for k in range(ws1['B'+str(pointDB)].value): #для каждого ингр
        pointRep = 19
        while(wsT['A'+str(pointRep)].value != ws1['A'+str(pointDB + 2 + k)].value): #ищет ингр в отчете
            pointRep+=1
        if(wsT[str(firCell)+str(pointRep)].value): #заполнение сумст
            wsT[str(secCell)+str(pointRep)].value += float(ws1[ForE+str(pointDB + 2 + k)].value)
        else:
            wsT[str(firCell)+str(pointRep)].value = ws1[ForE+str(pointDB + 2 + k)].value 
        
        wsT['R'+str(pointRep)].value = '=P'+str(pointRep)+'*'+str(ws1['B'+str(pointDB+2+k)].value)

def PrepareTable(letters, wsT):
    wsT['D17'].value = str('')
    wsT['D11'].value = str('')
    wsT['H17'].value = str('')
    wsT['H11'].value = str('')
    wsT['L17'].value = str('')
    wsT['L11'].value = str('')
    for letter in letters:
        for num in range (19, 81):
            wsT[letter+str(num)].value = float()

    wsT['S84'].value = '=SUM(R19:S81)'

    for i in range(19, 81):
        wsT['P'+str(i)].value = '=SUM(D'+str(i)+':O'+str(i)+')/1000'
        wsT['V'+str(i)].value = '=P'+str(i)+'*B5'

