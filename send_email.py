import smtplib
from email.message import EmailMessage

def send_email(reciever_email, message):
    sender_email = "rebelbean@seznam.cz"
    receiver_email = [reciever_email] #recipients
    password = "passwordtest" #fill your password
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Rebelbean Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP_SSL('smtp.seznam.cz', 465) #choose your provider server
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    return "Email sent!"

print(send_email("petrsevcik93@gmail.com", "hallo, test here"))