import logging

print(dir(logging))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("will talk")

    def dumb(self):
        print("cant talk")


person = Person("sridhar", 42)
print(person.name)
print(person.age)
person.talk()
person.dumb()


