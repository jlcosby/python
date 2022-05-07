#Enter a message: This Is My Message

message = input("Enter a message: ")

#Lowercase: this is my message

print("Lowercase:", message.lower())

#Uppercase: THIS IS MY MESSAGE

print("Uppercase:", message.upper())

#Capitalized: This is my message

print("Capitalized:", message.capitalize())

#Title Case: This Is My Message

print("Title Case:", message.title())

#Words: ['This', 'is', 'a','test','Message!']

words = message.split()

print("Words:", words)

#Alphabetic First Word: This
#Alphabetic Last Word: test

sorted_words = sorted(words)
print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])