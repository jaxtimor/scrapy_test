from scrapy.mail import MailSender
mailer = MailSender(smtphost='smtp.163.com',mailfrom = 'jetfang1990@163.com', smtpuser='jetfang1990@163.com',smtppass='helloworld123',smtpport=25)
mailer.send(to=["1284842285@qq.com"], subject="Some subject", body="Some body")