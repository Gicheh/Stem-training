class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"My name is {self.name} and I am {self.age} years old")
person1=person("Titus Gicheha",19)
print(person1.name,person1.age)
person1.details()

class Employee(person):
    def __init__(self, name, age, ID):
        super().__init__(name, age)
        self.ID=ID
    def details(self):
        print(f"My name is {self.name},I am {self.age} years old and my ID number is {self.ID}")
person2=Employee("Joe",22,36841154)
person2.details()