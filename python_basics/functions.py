#functions definted with "def" <function_name>(0 or more parameters)
#def print_something(something):
    #pass

#def print_name(name):
    #print(f"Name is {name}")
    
#print_name("Jennelle")

# = print_name("Jennelle")

#def contact_card(name, age, car_model):
#    return f"{name} is {age} and drives a {car_model}"
    
#ways to call function
    #1. All-positional - knowing order
#contact_card("Jennelle", 35, "Jeep Grand Cherokee")

    #2. Knowing parameter names, but not the order (using keyword arguments)
#contact_card(age=35, car_model="Jeep Grand Cherokee", name="Jennelle")

    #3.Use some positional arguments and some arguments are unnecessary. (mixing positional and keyword arguments)
    #syntax error
#contact_card(age=35, "Jennelle", car_model="Jeep Grand Cherokee")

#def can_drive(age, driving_age=16):
    #return age >= driving_age
    
#can_drive(29)
#True

#can_drive(16, driving_age=18)
#False

#can_drive(16, 18)
#False

#recursion - calling a function from within itself

#1. Calculating Fibonacci sequence 1,1,2,3,5,8,13,
#f(n) = f(n - 2) + f(n - 1)

#f(5) = f(3) + f(4)
#f(5) = f(1) + f(2) + f(2) + f(3)
#f(5) = 1 + 0 + 1 + 0 + 1 + 1 + f(0) + f(1) f(1) + f(2)
#f(5) = 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1
#f(5) = 5

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("What Fibonaci item would you like to calculate? "))
print(fib(item_to_calculate))
