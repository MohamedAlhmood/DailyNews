import smtplib ,ssl
import os

def sendMail(message):
    host = 'smtp.gmail.com'
    port = 465
    password = os.getenv('PASSWORD')

    reciever = 'moealhmood21@gmail.com'
    username= 'moealhmoodcs@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)


#mmnkrnnrjuyjjdel
#password = os.getenv('PASSWORD')
#print(password)