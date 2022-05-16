y = 5

def set_x(z):
#if 1 < 2:
   # print("Inner y:", y)
    x = z
    global y
    global a 
    y = x
    a = 7

print("y before set_x:", y)

set_x(10)
print("y after set_x:", y)
print("a after set_x:", y)

#while x < 6: 
    #print(x)
    #x += 1
    
print("Outer y:", y)
