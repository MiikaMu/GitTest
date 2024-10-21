class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def age(self):
        return self._age

    def age(self, value):
            self._age = value

    def __str__(self):
        return f"Persons name: {self._name}, age: {self._age})"