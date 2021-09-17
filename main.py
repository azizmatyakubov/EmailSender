import smtplib

my_email = 'blabla@gmail.com'
password = 'password'

connnection = smtplib.SMTP("smtp.gmail.com")
connnection.starttls()
connnection.login(user=my_email, password=password)
connnection.sendmail(from_addr=my_email, to_addrs='blablabla@gmail.com', msg='Hello')
connnection.close()