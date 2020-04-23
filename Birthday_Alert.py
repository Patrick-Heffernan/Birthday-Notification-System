import time
import datetime
import ezgmail

file = open("C:\\Users\\UserName\\Birthdays.txt","r")

today = datetime.date.today()
todays_date = today.strftime("%B %d") #converts timestamp to string value

#makes .txt into dictionary
birthdays = {}
for line in file:
    x = line.split(",")
    a = x[0]
    b = x[1]
    c = len(b)-1 #gets rid of the newline character
    b = b[0:c]
    birthdays[a] = b

#converts dictionary into two separate lists
key_list = list(birthdays.keys())
value_list = list(birthdays.values())

email_address = "Your Email"
subject = "Birthday Alert"

def get_key(val):
    for key, value in birthdays.items():
        if val == value:
            return key
    return "None"

if get_key(todays_date) == "None":
    exit()

else:
    content = "Today is " + get_key(todays_date) + "'s Birthday!"
    ezgmail.send(email_address, subject, content)

