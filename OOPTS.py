# Object Oriented Programming // Trening // TS


class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Invalid name")
        if not age:
            raise ValueError("Invalid age")
        self.name = name
        self.age = age
        self.patronus = "stag"

    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def charm(self):
        match self.patronus:
            case "stag":
                return "Expecto Patronum!"
            case "phoenix":
                return "Dumbledore's Army!"
            case "otter":
                return "Lumos"
            
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be a positive number")
        self._age = value

def main():
    student = get_student()
    print(f"{student.name} is {student.age} years old.")
    print(student.charm())

def get_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    try:
        student = Student(name, age)
    except ValueError as e:
        print(e)
        return get_student()
    return student
    

if __name__ == "__main__":
    main()
    student = get_student()
    print(student.name, student.age)

