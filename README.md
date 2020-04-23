# Birthday-Notification-System
This program has two separate functions: to record and search birthdays of loved ones, and then to notify you when it is their birthday. 

The search program prompts the user to enter a name, if there is an identified match, it returns their birthday. If not, it asks the user if they would like to add that person's information to the system. The user then can append the data easily to the text file and it will be there next time the user wants to search. 

The notification program operates in a similar way. It first converts todays date into a string, but in the exact format in which we stored our data (Month, Day). It is important that it is in that order, the month is not abbreviated, and that we store our data as a two digit numer (01,02,03...). Then the program runs a function that returns the key for any value that it is given. Accordingly, we give it todays date in the format that we want, and it sends an email alert to the user of whose birthday is it. If there is no birthday, the program quits. 

It utilizes a text document stored in your home file path to store birthday data. Data is intially converted from .txt to dictionary data (Key = Name, Value = birthday). 
