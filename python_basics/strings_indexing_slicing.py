message = input("Enter a message: ")

#first character in a string
print("First character:", message[0])

#second  character in a string
print("Last character:", message[-1])

#middle character in a string
print("Middle character:", message[int(len(message) / 2)])

#even characters in a string
print("Even index characters:", message[0::2])

#odd characters in a string
print("Odd index characters:", message[1::2])

#reverse a string
print("Reversed message:", message[::-1])
