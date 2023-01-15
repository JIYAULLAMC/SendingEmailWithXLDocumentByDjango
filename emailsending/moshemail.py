from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import os.path

message = MIMEMultipart()
message['from'] = 'jiyaulla@zktecodev.com'
message['to'] = 'jiyachindadi@gmail.com'
message['subject'] = 'This is test'
body = "Body of the email either html or normal "
message.attach(MIMEText(body, 'html'))


with open('student.xlsx', 'rb') as a_file:
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