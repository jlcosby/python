grade = int(input("What numerical grade did you get? "))

if grade >= 90 and grade <= 100:
    print("You have an A!")
elif grade <= 89 and grade >= 80:
    print("You have a B!")
elif grade <= 79 and grade >= 70:
    print("You have a C!")
elif grade <= 69 and grade >= 65:
    print("You have a D!")
elif grade <= 64 and grade > 0:
    print("You have an F! Better study!")
else:
    print(grade)