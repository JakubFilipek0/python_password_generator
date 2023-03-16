import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
letters_nr = int(input("How many letter do you want: "))
numbers_nr = int(input("How many numbers do you want: "))
symbols_nr = int(input("How many symbols do you want: "))

password_list = []

for char in range(letters_nr):
    password_list.append(random.choice(letters))

for char in range(numbers_nr):
    password_list.append(random.choice(numbers))

for char in range(symbols_nr):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password: {password}")
