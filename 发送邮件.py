import smtplib
from email.mime.multipart import MIMEMultipart

mailserver="mail.163.com"
user=""
pw=""
sender=""
reciver=""
subject=""

file=""
with open(file,"rb") as f:
    mailbody=f.read()
msg=MIMEMultipart("mixed")
msg_html=msg(mailbody,"html","utf-8")
msg.attach(msg_html)

msg_html1=msg(mailbody,"html","utf-8")
msg["Content-Disposition"]='attachment;filename="1.txt"'
msg.attach(msg_html1)

msg["From"]=sender
msg["To"]=reciver
msg["Subject"]=subject

smtp= smtplib.SMTP
smtp.connect(mailserver,25)
smtp.login(user,pw)
smtp.send(sender,reciver,subject)
smtp.close()
