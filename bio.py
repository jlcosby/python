name = input("What is your name? ")
color = input("What is your favorite color? ") 
age = int(input("How old are you today ")) 

#NAME is AGE years old and loves the color COLOR

#can do three separate strings with built-in newline
#print(name)
#print("is " + str(age) + " years old")
#print("and loves the color " + color + ".")

#'end' to specify what to print at the end - is defaulted to \n
#print(name, end=" ")
#print("is " + str(age) + " years old", end=" ")
#print("and loves the color " + color + ".", end=" ")

#use seperator
print(name, 'is', age, 'years old and loves the color',  color +'.', sep=" ")