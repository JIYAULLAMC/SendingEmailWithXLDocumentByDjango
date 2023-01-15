import xlrd

print(xlrd)
print(2222222222222222)
book = xlrd.open_workbook(r"C:\Users\JiyaUlla\Desktop\pyfiles\Book1.xlsx")
print(1111111111111)
sheet =book.sheet_by_index(0)
print(sheet.cell_value(0,0))