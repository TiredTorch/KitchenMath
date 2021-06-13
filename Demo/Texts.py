import openpyxl
from openpyxl.styles import Alignment

wb = openpyxl.reader.excel.load_workbook(filename="sample.xlsx", data_only = True)

wb.active = 0
ws = wb.active

def Test():

    #ws['F2'].value = "ff\nff"
    #ws['F2'].value += "aaaa"

    #ws['F2'].alignment = Alignment(text_rotation=90, horizontal='center')


    if(ws['F2'].value):
        print(1)
    else:
        print(0)

    wb.save('sample.xlsx')

Test()