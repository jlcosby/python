#import libraries

import random

#define functions

def classify_number(number):
    #expect all numbers
    if(number < 33):
       return("small number", number)
    elif(number < 66 and number >= 33):
        return("medium number", number)
    elif(number >= 66):
        return("large number", number)
    return("didn't catch", number)
#the code
random_list = [random.randint(0,100) for i in range(10)]

#print(random_list)

#response = classify_number(0)

#print(classify_number(0).lower() == "small number".lower())
#print(classify_number(100).lower() == "large number".lower())
#print(classify_number(52).lower() == "medium number".lower())
#print(classify_number(66).lower() == "small number".lower())
#print(classify_number(obj))

#for obj in random_list:
#    if(obj < 33):
#        print("small obj", obj)
#    elif(obj < 66 and obj >= 33):
#        print("medium obj", obj)
#    elif(obj > 66):
 #       print("large obj", obj)
#token = 2
#while token < 1024:
   # print(token)
  #  token = token **2
  #  break
  
 token = 2
 runs = 0
while token < 1024:
    print(token)
    token = token / 2
    runs = runs + 1
    if (runs > 10):
    break
