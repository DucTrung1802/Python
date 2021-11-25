# Create a Python class Person with attributes: name and age of type string.
# Create a display() method that displays the name and age of an object created via the Person class.
# Create a child class Student  which inherits from the Person class and which also has a section attribute.
# Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# Create a student object via an instantiation on the Student class and then test the displayStudent method.

class Person(object):
    def __init__(self, name, age):
        self._name = str(name)
        self._age = str(age)

    def display(self):
        print("Name: " + self._name)
        print("Age: " + self._age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self._section = str(section)


    def displayStudent(self):
        super().display()
        print("Section: " + self._section)




def main():
    a = Person("Trung", 21)
    a.display()

    print()
    
    b = Student("Kien", 16, "Math")
    b.displayStudent()

if __name__ == '__main__':
    main()
