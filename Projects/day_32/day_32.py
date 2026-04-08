# import smtplib
#
# email = "silverguardgithub@gmail.com"
#
# connection = smtplib.SMTP('smtp.gmail.com', 587)
# connection.starttls()
# connection.login(user=email, password="ASecurePassword")
# connection.sendmail(from_addr=email, to_addrs="microsoft@contoso.com", msg=f"Subject: Hello World!\n\n"
#                                                                       f"This email was sent from {email}")
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year             #Can also call month, day, hour, minute, second, weekday
# print(now)
# print(year)
# print(now.weekday())
#
# birthday = dt.date(year=2000, month=7, day=18)
# print(birthday)

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
email = "silverguardgithub@gmail.com"
password = "ASecurePassword"

if weekday == 0:
    with open("../day_32/quotes.txt") as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=email,
                            msg=f"Subject: Monday Motivation\n\n{random_quote}")






