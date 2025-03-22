class Student:
    def __init__(self, name, house): # constructor 
        self.name = name 
        self.house = house
    
    def __str__(self): # __str__ method to return a string representation of the object
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
    

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()