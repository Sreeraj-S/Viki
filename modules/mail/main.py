import smtplib

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ai.assistant101@gmail.com', 'vikiIstheBEst')
    server.sendmail('ai.assistant101@gmail.com', to , content)
    server.close()

