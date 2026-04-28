#Ask user their name
name = input("Whats your name ? ").title().strip()

#split user names into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello, {name}")