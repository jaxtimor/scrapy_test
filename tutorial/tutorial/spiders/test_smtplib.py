from smtplib import SMTP

with SMTP('smtp.163.com') as s:
    res = s.noop()
    print(res)