class Student:
    def __init__(self, name, house): # constructor 
        if name == "": # or "if not name:" instead
            raise ValueError("Name cannot be empty") # raise an error if name is empty
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") # raise an error if house is not valid
        self.name = name 
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()