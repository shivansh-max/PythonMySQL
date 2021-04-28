import mysql.connector as mc
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mydb = mc.connect(host="localhost", user="root", passwd="Qwaszx@123", database="names",
                  auth_plugin='mysql_native_password')

m = mydb.cursor()

m.execute("select *from house;")
rez = m.fetchall()
print(rez)


def onWriteFile(data):
    file = open('contentsOfChange.csv', 'a')
    file.write(data)
    file.close()


m.execute("select *from house;")
rez = m.fetchall()

for i in range(len(rez)):
    # placeHolder = rez[i]
    for j in range(len(rez[i])):
        if i == (len(rez) - 1) and j == (len(rez[i]) - 1):
            onWriteFile(str(rez[i][j]))
        else:
            onWriteFile(f"{rez[i][j]},")

    if i != len(rez) - 1:
        onWriteFile("\n")

mail_content = f'''
HI Admins, 

Please find the last month's detail below. 
Number of users currently is : {len(rez)};
The detail report is attached below. 

Thanks & Regards
Prakash Upadhyay
'''
# The mail addresses and password
sender_address = 'prakash.upadhyay@gmail.com'
sender_pass = 'Qwas@123'
receiver_address = 'shivanshupadhyay22@gmail.com'
# shivanshupadhyay22@gmail.com
# Setup the MIME
# Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Report on users'
# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = ''
attach_file = open(r'C:\Users\shiva\Python\PapasChallenges\MYSQL\contentsOfChange.csv',
                   'rb')  # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment
# add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
