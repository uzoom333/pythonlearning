"""
#1
for i in [0,1,2]:
    print("meow")

#2    
for i in range(3):
    print("meow")
    
print("meow\n" * 3, end ="")   

#3
while True:
    n = int(input("Whats n ?"))
    if n > 0:
        break

for n in range(n):
    print("meow")

#4   
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("Whats n ?"))
        if n > 0:
    return n        
    
    
def meow(n):
    for _ in range(n):
        print("meow")
        
#5
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)    
    
#6
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):      #think use range after relearning and remember for len
    print(i + 1, students[i])

#7 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#8 
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=" ")
    
#9
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
    
#10
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()
"""
def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()
