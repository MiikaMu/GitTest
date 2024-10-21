class Person:
<<<<<<< HEAD
    def __init__(self, city, address, phone_number):
        self._city = city
        self._address = address
        self._phone_number = phone_number

    @property
    def city(self, _default = None):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self, _default=None):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    def __str__(self):
        return f'Address: {self._address}\nCity: {self._city}\nPhone: {self._phone_number}'
=======
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
>>>>>>> dev2
