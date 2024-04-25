#PYTHON PROGRAMMING INTERNSHIP
#PROJECT 3 - SIMPLE PASSWORD GENERATOR
#NAME: SEJAL DAROLIYA

#Importing the required modules
import random

#Setting up the required parameters
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!',"@",'$','%','^','&','*','(',')']


print("WELCOME TO THE PASSWORD GENERATOR!!!")
n_letters = int(input("How many letters you want in your password?\n"))
n_symbols = int(input("How many symbols you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
password = []

for i in range (1, n_letters+1):
    char = random.choice(letters)
    password += char
for i in range (1, n_numbers+1):
    char = random.choice(numbers)
    password += char
for i in range (1, n_symbols+1):
    char = random.choice(symbols)
    password += char

random.shuffle(password)
pswd = ""
for i in password:
    pswd += i

print(pswd)

