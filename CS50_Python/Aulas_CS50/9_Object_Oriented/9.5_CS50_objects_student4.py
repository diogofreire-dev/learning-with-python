class Student:
    def __init__(self, name, house, patronus): # constructor 
        if name == "": # or "if not name:" instead
            raise ValueError("Name cannot be empty") # raise an error if name is empty
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house") # raise an error if house is not valid
        self.name = name 
        self.house = house
        self.patronus = patronus
    
    def __str__(self): # __str__ method to return a string representation of the object
        return f"{self.name} from {self.house}"
    
    

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()