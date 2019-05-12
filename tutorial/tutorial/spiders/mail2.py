
#coding:utf-8
import smtplib
from email.mime.text import MIMEText  # 引入smtplib和MIMEText
 
host = 'smtp.163.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
sender = 'jetfang1990@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
# pwd = 'qhpr huek kjgx cfih'
pwd = 'helloworld123'  # 设置发件邮箱的密码，等会登陆会用到
receiver = 'skyflyingpig@163.com' # 设置邮件接收人，可以是扣扣邮箱
body = '手机降价了' # 设置邮件正文，这里是支持HTML的
 
msg = MIMEText(body, 'plain','utf-8') # 设置正文为符合邮件格式的HTML内容
msg['Subject'] = '今天有活动' # 设置邮件标题
msg['From'] = 'jetfang1990@163.com'  # 设置发送人
msg['To'] = receiver  # 设置接收人
 
try:
    s = smtplib.SMTP()  # 注意！如果是使用SSL端口，这里就要改为SMTP_SSL
    s.set_debuglevel(1)
    s.connect(host)
    s.login(sender, pwd)  # 登陆邮箱
    s.sendmail(sender, [receiver], msg.as_string())  # 发送邮件！
    print('Done')
except smtplib.SMTPException as e:
    print(e)