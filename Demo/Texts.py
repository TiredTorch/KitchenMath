import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="sample.xlsx", data_only = True)

wb.active = 0
ws = wb.active

find = input()

for i in range(2, 11):
    if(str(find) == str(ws['A'+str(i)].value)):
        print("Успех")
        break