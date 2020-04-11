from typing import List


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room: ChatRoom = None

    def receive(self, sender, message):
        s = f'{sender}: {message}'
        self.chat_log.append(s)
        print(f'[{self.name} chat session]: {s}')

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, to, message):
        pass


# Chat room here is acting aa the mediator
class ChatRoom:
    def __init__(self):
        self.people: List[Person] = []

    def broadcast(self, sender, message):
        for person in self.people:
            if sender != person.name:
                person.receive(sender, message)

    def join(self, person: Person):
        join_message = f'{person.name} joins the room!'
        self.broadcast('room', join_message)
        self.people.append(person)
        person.room = self

    def message(self, sender, receiver, message):
        for person in self.people:
            if person == receiver:
                person.receive(sender.name, message)


if __name__ == '__main__':
    p1 = Person('John')
    p2 = Person('Jessi')

    room = ChatRoom()
    room.join(p1)
    room.join(p2)

    p1.say('Hello everyone')

    p3 = Person('Walter')
    room.join(p3)

    room.message(p1, p3, 'Hello')