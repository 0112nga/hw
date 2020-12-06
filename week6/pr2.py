
class Car:
    def __init__(self,year_model, make ):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed

def main():
    c = Car('2000', 'abc')
    c.accelerate()
    c.accelerate()
    c.accelerate()
    c.accelerate()
    c.accelerate()
    print('the current speed {}'.format(c.get_speed()))
    c.brake()
    c.brake()
    c.brake()
    c.brake()
    c.brake()
    print('the current speed {}'.format(c.get_speed()))

if __name__ == '__main__':
        main()