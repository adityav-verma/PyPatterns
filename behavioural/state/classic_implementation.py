"""This is a classic pattern, but it's not very convenient and easy to use, hence we won't be using this much.
Infact we would use a State <-> Trigger approach.
"""


from abc import ABC


class State(ABC):
    def on(self, switch):
        print('Light switch is already on')

    def off(self, switch):
        print('Light switch is already off')


class OnState(State):
    def off(self, switch):
        print('Turing light bulb off')
        switch.state = OffState()


class OffState(State):
    def on(self, switch):
        print('Turing light bulb on')
        switch.state = OnState()


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


if __name__ == '__main__':
    s = Switch()
    s.on()
    s.off()
    s.off()