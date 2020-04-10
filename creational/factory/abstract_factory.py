"""We can even have interface for factories, for some common type of objects
That factory interface can then be used by some controller
"""

from abc import ABC, abstractmethod


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Coffee(HotDrink):
    def __init__(self):
        pass

    def consume(self):
        print('This coffee is smooth')


class Tea(HotDrink):
    def __init__(self):
        pass

    def consume(self):
        print('This tea is sweet')


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount: int) -> HotDrink:
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f'This is how you prepare tea, amount: {amount}')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f'This is how you prepare coffee, amount: {amount}')
        return Coffee()


# This will use a factory to create drinks
class HotDrinkMachine:
    def __init__(self):
        self.factories = {
            'tea': TeaFactory(),
            'coffee': CoffeeFactory()
        }

    def make_drink(self, drink, amount):
        factory = self.factories.get(drink)
        if factory:
            factory.prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    hdm.make_drink('tea', 10)
    hdm.make_drink('coffee', 5)
