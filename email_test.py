#test email setup---Works!
import smtplib
import os
import dotenv

dotenv.load_dotenv()
sender_email = os.getenv('SENDER_EMAIL')
e_pw = os.getenv('PW_SMT')
rec_email = os.getenv('REC_EMAIL')
msg = "hey, this was sent using python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() #start server
server.login(sender_email, e_pw)
print('login success')
#send email
server.sendmail(sender_email, rec_email, msg)
print("email sent")