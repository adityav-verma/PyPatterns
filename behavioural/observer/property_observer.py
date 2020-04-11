class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


# Define a Base class for observable, we might want to use an interface to keep this more generic and robust
class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age):
        super(Person, self).__init__()
        self._age = age

    @property
    def can_vote(self):
        return self._age >= 16

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value == self._age:
            return
        temp = self.can_vote
        self._age = value
        self.property_changed('age', value)
        if temp != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        self.person.property_changed.append(self.handle_age_change)
        self.person.property_changed.append(self.handle_can_vote)

    def handle_age_change(self, event_type, value):
        if event_type != 'age':
            return
        if value < 18:
            print(f'Your age is {value}, Not eligible to drive')
        else:
            print(f'Your age is {value}, Can drive now, we won\'t monitor you anymore')
            self.person.property_changed.remove(self.handle_age_change)

    def handle_can_vote(self, event_type, value):
        if event_type != 'can_vote':
            return
        if value:
            print(f'You can vote now!')
            self.person.property_changed.remove(self.handle_can_vote)
        else:
            print('You cannot vote')


if __name__ == '__main__':
    p1 = Person(10)
    ta = TrafficAuthority(p1)
    for i in range(10, 21):
        p1.age = i