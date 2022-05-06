import random
#1 create list
new_var=[ ]

#print(type(new_var), new_var)

#2 list 1-100
numbers = list(range(1-100))

#print(numbers)

#3 reverse
#numbers.reverse()

#print (numbers)

#4 random shuffle
#random.shuffle(numbers)

#print(numbers)

#5 sort
#numbers.sort()

#print(numbers)

#5 index
index = numbers.index(7)

#print(numbers[index])

#6 iterate through list
for number in numbers:
    print(number)
    new_var.append(number**2)
    #print(number **2)
    print(new_var)   

#list comprehension
numbers_squared = [number **2 for number in numbers] 

print(numbers_squared)

numbers_squared_odd = [number ** 2 for number in numbers if number % 2 == 1]

print(numbers_squared_odd)
    
