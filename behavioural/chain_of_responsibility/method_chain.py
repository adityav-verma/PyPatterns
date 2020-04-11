"""A chain of references construct for chain of responsibility pattern"""


class Creature:
    def __init__(self, name, attack, defence):
        self.name = name
        self.attack = attack
        self.defence = defence

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defence})'


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier: CreatureModifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    # chaining the request to the next handler
    # logic can be added to stop this chaining at a particular case
    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print('Doubling attack')
        self.creature.attack *= 2
        super(DoubleAttackModifier, self).handle()


class IncreaseDefenceModifier(CreatureModifier):
    def handle(self):
        if self.creature.defence <= 3:
            print('Increasing Defence')
            self.creature.defence += 1
        super(IncreaseDefenceModifier, self).handle()


class NoBonusModifier(CreatureModifier):
    def handle(self):
        print('No bonus')


if __name__ == '__main__':
    goblin = Creature('Goblin', 1, 1)
    print(goblin)
    cm = CreatureModifier(goblin)
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(IncreaseDefenceModifier(goblin))
    cm.add_modifier(IncreaseDefenceModifier(goblin))

    cm.handle()
    print(goblin)

    cm.add_modifier(NoBonusModifier(goblin))    # this will stop the chain
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))
    cm.add_modifier(DoubleAttackModifier(goblin))

    cm.handle()
    print(goblin)