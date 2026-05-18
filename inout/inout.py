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

<<<<<<< HEAD

=======
"""
>>>>>>> 1ee2e7b22df86f48061aec139bada4f63b31e898
#with method print that 
name = input("What's your name? ")
with open("names.txt", "a") as file:
    lines = file.readlines()

for line in lines:
<<<<<<< HEAD
    print("hello", line)  #use print("hello", line.rstrip())   
"""
names = []
with open("namex.txt", "a") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
=======
    print("hello", line)     
>>>>>>> 1ee2e7b22df86f48061aec139bada4f63b31e898
