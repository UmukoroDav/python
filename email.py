import smtplib

my_email = 'davidogheneothuke42@gmail.com'
my_password = 'Umukoros1@'


connect = smtplib.SMTP('smtp.gmail.com', 587)
connect.starttls()
connect.login(user=my_email, password=my_password)

connect.sendmail(from_addr=my_email, to_addrs='receipentemail.com', msg='HELLO WORLD')
connect.close()