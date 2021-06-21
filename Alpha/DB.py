import openpyxl

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

def AddIngredient(name, price): 
    i = 1
    while(ws0['A'+str(i)].value != '*'):
        i+=1
    
    ws0['B'+str(i)].value = str(name)
    ws0['C'+str(i)].value = float(price)
    ws0['A'+str(i)].value = int(ws0['A'+str(i-1)].value) + 1
    ws0['A'+str(i+1)].value = '*'
    wb.save("DB.xlsx")


def StartDishPars():
    i = 1
    while(ws1['H'+str(i)].value != '*'):
        i+=1

    ws1['A'+str(i+1)].value = 'Продукты'
    ws1['B'+str(i+1)].value = 'Цена за кг'
    ws1['C'+str(i+1)].value = 'Кол-во (сад)'
    ws1['D'+str(i+1)].value = 'Кол-во (ясли)'
    ws1['E'+str(i+1)].value = 'СумСт (сад)'
    ws1['F'+str(i+1)].value = 'СумСт (ясли)'
    ws1['G'+str(i)].value = 'ID:'
    return i

def AddIngrToDish(ID, amount1, amount2):

    a = int(ID)
        
    ws1['A'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = ws0['B'+str(a+2)].value
    ws1['B'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = ws0['C'+str(a+2)].value

    ws1['C'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = float(amount1)
    ws1['D'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = float(amount2)

    ws1['E'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = float(float(ws0['C'+str(a+2)].value) * float(amount1) / 1000)
    ws1['F'+str(StartDishPars()+2+int(ws1['B'+str(StartDishPars())].value))].value = float(float(ws0['C'+str(a+2)].value) * float(amount2) / 1000)


    ws1['B'+str(StartDishPars())].value = ws1['B'+str(StartDishPars())].value + 1

def EndDishPars(dishName):
    ws1['E'+str(StartDishPars()+3+int(ws1['B'+str(StartDishPars())].value))].value = 'Сумма: '
    
    ws1['E'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value = 0
    for k in range (int(ws1['B'+str(StartDishPars())].value) - 1):
        ws1['E'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value = (ws1['E'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value) + float(ws1['E'+str(StartDishPars()+2+k)].value)
    
    ws1['F'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value = 0
    for k in range (int(ws1['B'+str(StartDishPars())].value) - 1):
        ws1['F'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value = (ws1['F'+str(StartDishPars()+4+int(ws1['B'+str(StartDishPars())].value))].value) + float(ws1['F'+str(StartDishPars()+2+k)].value)

    ws1['H'+str(StartDishPars()+6+int(ws1['B'+str(StartDishPars())].value))].value = '*'
    ws1['B'+str(StartDishPars()+6+int(ws1['B'+str(StartDishPars())].value))].value = 0

    temp = 1
    while(ws1['H'+str(StartDishPars()-temp)].value == None):
        temp+=1

    ws1['H'+str(StartDishPars())].value = ws1['H'+str(StartDishPars()-temp)].value + 1

    ws1['A'+str(StartDishPars())].value = dishName
    wb.save("DB.xlsx")

def ShowIngredientID():
    print(chr(27) + "[2J")

    i = 1
    while(ws0['A'+str(i)].value != '*'):
        print(ws0['B'+str(i)].value + ' :: ' + str(ws0['A'+str(i)].value))
        i+=1

def ShowDishesID():
    print(chr(27) + "[2J")

    print('Блюдо :: ID')
    i = 2
    while(ws1['H'+str(i)].value != '*'):
        print(ws1['A'+str(i)].value + ' :: ' + str(ws1['H'+str(i)].value))
        i+=(ws1['B'+str(i)].value + 6)


def StartReport():
    letters = ['D','F','H','J','L','N']
    PrepareTable(letters, wsT1)
    PrepareTable(letters, wsT2)

def FillReport(name):
    
    wbT.save(str(name)+'.xlsx')

def ReportDishesFill(bool, tryFood, ID, amount):

    letters = ['D','F','H','J','L','N']
    if bool == True:
        DishPars(str(letters[tryFood*2]), str(letters[(tryFood*2)+1]), wsT1, 'E', ID, amount)
    else:
        DishPars(str(letters[tryFood*2]), str(letters[(tryFood*2)+1]), wsT2, 'F', ID, amount)

def DishPars(firCell, secCell, wsT, ForE, ID, amount):

    tempDishID = int(ID)

    wsT[str(firCell)+'17'].value += (str(amount) + '\n')

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

