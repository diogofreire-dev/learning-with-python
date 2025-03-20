class Student:
    def __init__(self, name, house): # constructor 
        if name == "": # or "if not name:" instead
            raise ValueError("Name cannot be empty") # raise an error if name is empty
        self.name = name 
        self.house = house
    
    def __str__(self): # __str__ method to return a string representation of the object
        return f"{self.name} from {self.house}"

    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()