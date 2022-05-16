class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

name = input("Enter your pets name: ")
animal_type = input("Enter what type on animal it is: ")
age = input("Enter your pets age: ")

userPet = Pet(name, animal_type, age)

print('Name:', userPet.get_name())
print('Animal:', userPet.get_animal_type())
print('Age:', userPet.get_age())
