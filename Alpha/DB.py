import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="DB.xlsx", data_only = True)

def AddIngredient(): 
    wb.active = 0
    ws = wb.active

    i = 1
    while(ws['A'+str(i)].value != '*'):
        i+=1
    
    ws['B'+str(i)].value = input('Название ингредиента: ')
    ws['C'+str(i)].value = float(input('Его цена: '))
    ws['A'+str(i)].value = int(ws['A'+str(i-1)].value) + 1
    ws['A'+str(i+1)].value = '*'
    wb.save("DB.xlsx")




def AddDish():    
    wb.active = 0
    wsh = wb.active
    
    wb.active = 1
    ws = wb.active

    i = 1
    while(ws['H'+str(i)].value != '*'):
        i+=1

    ws['A'+str(i)].value = input('Введите название блюда: ')
    ws['B'+str(i)].value = int(input('Введите количество ингредиентов: '))
    ws['C'+str(i)].value = ''

    ws['A'+str(i+1)].value = 'Продукты'
    ws['B'+str(i+1)].value = 'Цена за кг'
    ws['C'+str(i+1)].value = 'Кол-во (сад)'
    ws['D'+str(i+1)].value = 'Кол-во (ясли)'
    ws['E'+str(i+1)].value = 'СумСт (сад)'
    ws['F'+str(i+1)].value = 'СумСт (ясли)'
    ws['G'+str(i)].value = 'ID:'

    for j in range(ws['B'+str(i)].value):
        a = int(input('Укажите ID ингредиента '+str(j+1)+': '))
        
        ws['A'+str(i+2+j)].value = wsh['B'+str(a+2)].value
        ws['B'+str(i+2+j)].value = wsh['C'+str(a+2)].value

        ws['C'+str(i+2+j)].value = int(input('Введите кол-во для сада: '))
        ws['D'+str(i+2+j)].value = int(input('Введите кол-во для яслей: '))

        ws['E'+str(i+2+j)].value = '=B'+str(i+2+j)+'*C'+str(i+2+j)+'/1000'
        ws['F'+str(i+2+j)].value = '=B'+str(i+2+j)+'*D'+str(i+2+j)+'/1000'

        

    #ws['H'+str(i)].value =

    wb.save("DB.xlsx")
        
AddDish()