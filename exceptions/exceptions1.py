"""
#ValueError
x = int(input("Whats x?"))
print(f"x is {x}") #if a initiliaze this anserw with a cat 

#1
try:
    x = int(input("Whats your x ?"))
    print(f"x is {x}")
except ValueError:
    print("x is not a integer")  
#2
try:
    x = int(input("Whats your x ?"))
except ValueError:
    print("x is not a integer")
else:
    print(f"x is {x}")    #NameError if defined a not intenger and use  else to change that.
#3 use break in loop just end when sucess input
while True: 
    try:
        x = int(input("Whats your x ?"))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")
#4
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            x = int(input("Whats your x ?"))
        except ValueError:
            print("x is not a integer")
        else:
            break
    return x        

main()
#5
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True: 
        try:
            return int(input("Whats your x ?"))
        except ValueError:
            pass        

main()
"""
#raise
def main():
    x = get_int("WHats x?")
    print(f"x is {x}")

def get_int(prompt):
    while True: 
        try:
            return int(input(prompt))
        except ValueError:
            pass  

main()