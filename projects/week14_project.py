#week 14 project: name generator for a specified number of ec2 instances

#"random" and "string" libraries added to generate names at random with a defined string type
import random
import string

#verify users select the appropriate department for use with the Name Generator

while True:
    try:
        dept = input("Identify the department that will utilize this Name Generator - Accounting, Marketing, or FinOps ").lower()
        list = ["accounting", "marketing", "finops"]
        if dept not in list:
            raise ValueError
        break
    except ValueError:
        print("The department you entered is not approved to utilize this application. ")
        exit ()
    else:
        break
    
#allow user input userid to be used in unique name

while True:
    try: 
        user = input("Enter the first 4 characters of the user id. ")
        if len(user) != 4:
            raise ValueError
        break
    except ValueError:
        print("Invalid response. Enter the first 4 characters of the user id. ")
        continue
    else:
        break

#request user input for the number of unique names needed

while True:
    try:
        names_needed = int(input("Please specify the number of unique names needed. "))
        break
    except ValueError:
        print("Invalid response. Please enter a numerical value. ")
        continue
    else:
        break
    
#create unique name - generate 4 random characters to add to department code and the first 4 characters of the user id

unique_name = ''.join([random.choice(string.ascii_letters + string.digits) for names_needed in range(4)])

x = names_needed

for _ in range(x):
    unique_name = str(''.join([random.choice(string.ascii_letters + string.digits) for names_needed in range(4)]))
    print('{}-{}-{}'.format(dept, user, unique_name))
