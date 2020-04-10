"""Add some protection before an operation"""

class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} of age {self.age}'


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f'Car is being driven by {self.driver}')


# To add some more validations on who can drive a car, we can add a car proxy

class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self.car = Car(self.driver)

    def drive(self):
        if self.driver.age < 18:
            raise Exception(f'Driver {self.driver} not allowed to drive')
        self.car.drive()


if __name__ == '__main__':
    driver = Driver('John', 17)
    # car = Car(driver)
    car = CarProxy(driver)
    car.drive()