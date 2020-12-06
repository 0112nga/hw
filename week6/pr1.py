
class Pet:
    def __init__(self, name, animal_type, age ):
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
    def  get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    def displayInfo(self):
        print('Your Pet name is {}, \nYour Pet type is {}, \nYour Pet age is {}'.format(
            self.get_name(),self.get_animal_type(),self.get_animal_type()
        ))

def main():
    name = input('Enter the Pet name: ')
    type = input('Enter the Pet type: ')
    age = input('Enter the Pet age: ')
    p = Pet(name,type,age)
    p.displayInfo()

if __name__ == '__main__':
        main()