# Écrivez votre code ici !


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def afficher_details(self):
        print(f"\nNom : {self.name}"
              f"\nAge : {self.age}")


class Employee(Person):
    def __init__(self, name, age, salaire):
        super().__init__(name, age)
        self.salaire = salaire

    def afficher_details(self):
        super().afficher_details()
        print(f"Salaire{self.salaire}")


person1 = Person("Jean", 20)
person1.afficher_details()

person2 = Person("Franck", 25)
person2.afficher_details()

employee1 = Employee("Franck", 25, 32000)
employee1.afficher_details()

employee2 = Employee("Alice", 38, 47000)
employee2.afficher_details()
