import pandas as pd
import datetime as dt
import random as rd
import smtplib

password = 'qltd hgfn udtm ddhf'
user = 'rabadjiiskib@gmail.com'

def sendMail(message):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user, password)
    connection.sendmail(from_addr=user, to_addrs='stu2201681049@uni-plovdiv.bg', msg=message)
    connection.close()

open("birthdays.csv").close()
file = pd.read_csv('birthdays.csv')
print(file)
days = file["day"].tolist()
months = file["month"].tolist()
date = dt.date.today()
if date.day in days:
    if date.month in months:
        with open(f"letter_templates/letter_{rd.randint(1,3)}.txt") as m:
            message = m.read()
            message = message.replace("[NAME]", f"{file.iloc[file.index[file['month'] == date.month][0]]['name']}")
            print(message)
            sendMail(f"Subject: {date}, \n{message}")
        pass




