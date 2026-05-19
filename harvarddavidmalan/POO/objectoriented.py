"""
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

#1
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()

#2 tuple
def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()

#3 improvements 
def main():
    student = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()    
   
#4 tuples if [0],[1]
def main():
    student = get_student()
    if student[0] == "Corvinal":
        student[1] = "Lufa-Lufa"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house 

if __name__ == "__main__":
    main()

#5 using list 
def main():
    student = get_student()
    if student[0] == "Corvinal":
        student[1] = "Lufa-Lufa"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] 

if __name__ == "__main__":
    main()            
"""
#6
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")    

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "main":
    main() 
