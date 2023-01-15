from openpyxl import Workbook, load_workbook


wb = Workbook()

ws = wb.active

ws.append(['Name', 'Age', 'Phone', 'Address'])

wb.save('student.xlsx')