
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage
 
 
mail_host="smtp.163.com"
mail_user="jetfang1990@163.com"
mail_pass="helloworld123"
sender = 'jetfang1990@163.com'
receivers = ['1284842285@qq.com']
body_content = """ For most applications the only preferencelist combinations that really make sense are ('plain',), ('html', 'plain'), and the default ('related', 'html', 'plain'). (2) Because matching starts with the object on which get_body is called, calling get_body on a multipart/related will return the object itself unless preferencelist has a non-default value. (3) Messages (or message parts) that do not specify a Content-Type or whose Content-Type header is invalid will be treated as if they are of type text/plain, which may occasionally cause get_body to return unexpected results  """
 
# message = MIMEText(body_content, 'plain', 'utf-8')
message = EmailMessage()
message.set_content(body_content)
message['From'] = "jetfang1990@163.com"
message['To'] = "1284842285@qq.com"
subject = 'hello world'
message['Subject'] = subject
print(message)
print(message.get_content_type())
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  
smtpObj.set_debuglevel(1)
smtpObj.login(mail_user,mail_pass)
smtpObj.send_message( message)
print("邮件发送成功")

smtpObj.quit()

