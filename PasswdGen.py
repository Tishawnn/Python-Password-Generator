import random

#these are the some characters that I chose to be in the passwords you can add more.
characters = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEDFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"

#this is where you ask how much characters you want the password to be. 
length = input("How long do you want your password to be? ")
length = int(length)

#this is the piece of code that basically generates the password.
password = ''
for c in range(length):
  password +=  random.choice(characters)

print(password)
