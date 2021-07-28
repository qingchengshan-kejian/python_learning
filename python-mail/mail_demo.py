"""
author:zhangyue
version:python3
date:2018-9-13

"""
import smtplib
from email.mime.text import MIMEText
#set server info
#163 email address
mail_host = 'smtp.163.com'
#163 username
mail_user = 'y***dom'
#passwd
mail_pass = 'J?9+whereis'
#sender address
sender = 'y***dom@163.com'
#receivers' addresses
receivers = ['1**35@qq.com']

#set email info
#mail content
message = MIMEText('content', 'plain', 'utf-8')
#mail subject
message['Subject'] = 'title'
#sender info
message['From'] = sender
#receiver info
message['To'] = receivers[0]

#login and send email
try:
	smtpObj = smtplib.SMTP()
	#connect server
	smtpObj.connect(mail_host,25)
	#login server
	smtpObj.login(mail_user, mail_pass)
	#send email
	smtpObj.sendmail(
		sender,receivers,message.as_string())
	#exit
	smtpObj.quit()
	print('success')
except smtplib.SMTPException as e:
	print ('error',e)
	#print error info



