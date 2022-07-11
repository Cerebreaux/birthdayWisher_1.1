######################################MUST UPDATE birthday data in csv##################################################
import smtplib
import random as r
import datetime as dt
import pandas as pd

# Constants variable set for login
MY_EMAIL = ""
PASSWORD = ""

# Get today's date and time and set it to a tuple variable to put in dict
today = dt.datetime.now()
today_tup = (today.month, today.day)
# Get csv data and set to pandas variable
birthdays = pd.read_csv("birthdays.csv")
# Create new dictionary with that pulls out a tuple for month and day for person in list
birthday_data = {(row.month, row.day): row for (index, row) in birthdays.iterrows()}
# Check if today's date is in the new dictionary
if today_tup in birthday_data:
    # Puts birthday person month and day into a variable
    birthday_person = birthday_data[today_tup]
    # Create a random path variable to select vary letter selection
    file_path = f"letter_templates/letter_{r.randint(1, 3)}.txt"
    # Open random letter in folder
    with open(file_path) as letter_file:
        # Read contents in letter and check for placeholder and replace name with name of birthday person
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])  # Must put back into same variable to be updated
    # Open connection to email server
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
        server.ehlo()  # preps server for requests
        server.starttls()  # encryption
        server.ehlo()
        server.login(MY_EMAIL, PASSWORD)  # login to email with constants
        # Prepares and sends email to birthday person email address with updated email contents
        server.sendmail(from_addr=MY_EMAIL,
                        to_addrs=birthday_person["email"],
                        msg=f"Subject: Happy Birthday!!!\n\n{contents}")
