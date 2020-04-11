"""
A centralised construct for chain of responsibility

1) event broker
2) command-query separation (cqs)
3) observer
"""

from enum import Enum, auto


class Event(list):
    """This behaves like a event broker"""
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = auto()
    DEFENCE = auto()


# Any command in the system is being fired via this Query
class Query:
    def __init__(self, creature, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature = creature


# This is the mediator between event and query
class Game:
    def __init__(self):
        self.queries = Event()

    # On a query invocation, all handlers attached to the message broker are called
    def perform_query(self, sender, query: Query):
        self.queries(sender, query)


class Creature:
    def __init__(self, game: Game, name: str, attack: int, defence: int):
        self.initial_attack = attack
        self.initial_defence = defence
        self.game = game
        self.name = name

    @property
    def attack(self):
        # Creates a query, then performs it, basically all handlers receive this query via the broker
        # then they update the value of the query, which is then finally returned
        query = Query(self, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defence(self):
        # Creates a query, then performs it, basically all handlers receive this query via the broker
        # then they update the value of the query, which is then finally returned
        query = Query(self, WhatToQuery.DEFENCE, self.initial_defence)
        self.game.perform_query(self, query)
        return query.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defence})'


class CreatureModifier:
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        # Handler is appended to the games, event broker
        # When a query is fired, the game object passes that query to all the handlers associated with a broker
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This works when we use a scope (like with), on completion of the scope, the handler is removed from the broker
        self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name:
            if query.what_to_query == WhatToQuery.ATTACK:
                query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name:
            if query.what_to_query == WhatToQuery.DEFENCE:
                query.value += 3


if __name__ == '__main__':
    game = Game()
    goblin = Creature(game, 'Strong Goblin', 2, 2)
    print(goblin)
    with DoubleAttackModifier(game, goblin):
        print(goblin)
        with IncreaseDefenseModifier(game, goblin):
            print(goblin)

    print(goblin)
