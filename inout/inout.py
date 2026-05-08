"""
#append method

names = []

for _ in range(3):
    name = input("Whats your name?")
    names.append(name)
    #or
    #names.append(input("Whats your name ?"))

#sorted method
    for name in sorted(names):
        print(f"hello {name}")
#open function 
name = input("Whats your name ?")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()    


#with method - writing in a doc
name = input("What's your name? ")
with open("names.txt", "a") as file:
    lines = file.write(f"{name}\n")

for line in lines:
    print("hello", line)    

"""
#with method print that 
name = input("What's your name? ")
with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
    print("hello", line)     
