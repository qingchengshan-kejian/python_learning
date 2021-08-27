import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#set login and server info
mail_host = 'smtp.163.com'
mail_user = 'y***dom'
mail_pass = 'J***s'
sender = 'y***dom@163.com'
receivers = ['1***35@qq.com']

#set email info
#create a MIMEMultipart class(instance), process content and appendix file
message = MIMEMultipart()
message['From'] = sender
message['To'] = receivers[0]
message['Subject'] = 'title'
#recommand use html type 
with open('abc.html', 'r') as f:
	content = f.read()
#set html type conferences
part1 = MIMEText(content, 'html', 'utf-8')
#add a txt file
with open('abc.txt', 'r') as h:
	conten2 = h.read()
#set txt conferences
part2 = MIMEText(conten2,'plain', 'utf-8')
#set appendix's type
part2['Conten-Type'] = 'application/octet-stream'
#set appendix's header and file name
part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
#add picture appendix
with open('1.png','rb') as fp:
	picture = MIMEImage(fp.read())
	#set pic conferences
	picture['Conten-Type'] = 'application/octet-stream'
	picture['Content-Disposition'] = 'attachment;filename="1.png"'
#add content to mail
message.attach(part1)
message.attach(part2)
message.attach(picture)

#login and send
try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(
		sender, receivers, message.as_string())
	print('success')
	smtpObj.quit()
except smtplib.SMTPExecption as e:
	print('error', e)
