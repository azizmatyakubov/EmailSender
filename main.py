import smtplib

#Info
my_email = 'blabla@gmail.com'
password = 'password'

#program
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs='blablabla@gmail.com', msg='Subject:Hello \n\n My name is Aziz, this is a test')
