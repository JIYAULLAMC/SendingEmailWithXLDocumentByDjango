from django.shortcuts import render
import openpyxl
from myapp.models import Student
# Create your views here.



def send_email():
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    import smtplib
    import os.path

    message = MIMEMultipart()
    message['from'] = 'jiyaulla@zktecodev.com'
    message['to'] = 'jiyachindadi@gmail.com'
    message['subject'] = 'This is test'
    body = "My Body Budy"
    message.attach(MIMEText(body, 'html'))


    with open(r'C:\Users\JiyaUlla\Desktop\django\readxlproj\xlfiles\tempstudent.xlsx', 'rb') as a_file:
        basename = os.path.basename('student.xlsx')
        part = MIMEApplication(a_file.read(), Name=basename)
        part['Content-Disposition'] =    'attachment; filename="%s"' % basename 
        message.attach(part)

    with smtplib.SMTP(host= "smtp-mail.outlook.com"   , port='587', ) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('jiyaulla@zktecodev.com', 'Jiya@z20')
        smtp.send_message(message)
        print('sent')


import xlrd
import xlsxwriter


def home(request):
    print("--------------")
    path = r"C:\Users\JiyaUlla\Desktop\django\readxlproj\xlfiles\tempstudent.xlsx"
    book = xlsxwriter.Workbook(path)
    sheet = book.add_worksheet()    

    students = Student.objects.values()
    headings =  students[0].keys()
    sheet.write_row(0,0,headings)
    students = Student.objects.values_list()

    for student in  range(len(students)):
        sheet.write_row(1+student,0, list(students[student]))

    print(students)
    book.close()

    send_email()

    return render(request, "myapp/home.html")