import smtplib
import datetime as dt
import pandas
import random
from pathlib import Path

now = dt.datetime.now()
current_month = now.month
current_day = now.day

email = "silverguardgithub@gmail.com"
password = "ASecurePassword"

birthdays = pandas.read_csv("birthdays.csv")

birthday_people = birthdays[(birthdays["Month"] == current_month) & (birthdays["Day"] == current_day)]

for _, person in birthday_people.iterrows():
    recipient_name = person["name"]
    recipient_email = person["email"]

    # Pick a random template
    template_path = random.choice(list(Path("letter_templates").glob("*.txt")))

    with open(template_path, "r") as file:
        letter_contents = file.read()

    # Replace placeholder with actual name
    personalized_letter = letter_contents.replace("[NAME]", recipient_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=recipient_email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )



