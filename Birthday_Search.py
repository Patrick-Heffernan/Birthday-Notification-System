
#Open the text document
file = open('C:\\Users\\Username\\Birthdays.txt','r') #Must be in the same path as python code

#Convert text document into dictionary
birthdays = {} 
for line in file:
    x = line.split(",")
    a = x[0]
    b = x[1]
    c = len(b)-1 #gets rid of the newline character
    b = b[0:c]
    birthdays[a] = b


while True:
    print('Enter a name (blank to quit):')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + "'s Birthday is " + birthdays[name])

    else:
        print('I do not have birthday information for ' + name)
        print('Would you like to add their information to the list?')
        answer = input()
        if answer == "Yes" or "yes":
            print('Please type their birthday below:')
            bfile = open('C:\\Users\\Username\\Birthdays.txt','a')
            given_name = str(name)
            bfile.write(given_name + ",")
            bfile.write(input() + "\n") #option to write some data validation if someone enters a non-date format
            bfile.close()
            print('Birthday database updated.')

            
