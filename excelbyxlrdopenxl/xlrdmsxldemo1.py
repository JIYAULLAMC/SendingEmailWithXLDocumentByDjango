import xlrd
import datetime

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True



# how to read the data from the excel file


"""
path = "C:\\Users\\JiyaUlla\\Desktop\\pyfiles\\msbook1.xlsx" 
book = xlrd.open_workbook(path)

sheet = book.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols

for row in range(rows):
    for col in range(cols):
        if row!=0 and col == 2:
            row_value = sheet.cell_value(row, col)
            converted_obj = xlrd.xldate_as_tuple(row_value, book.datemode)
            str_date = datetime.datetime(*converted_obj).strftime("%d/%m/%y")
            print(str_date)

        else:
            value = sheet.cell_value(row, col)
            print(value)

"""

# how to create and write the data into the excel file

import xlsxwriter

path = "C:\\Users\\JiyaUlla\\Desktop\\pyfiles\\mswritebook1.xlsx" 

book = xlsxwriter.Workbook(path)

sheet1 = book.add_worksheet()
sheet2 = book.add_worksheet()


book.close()





