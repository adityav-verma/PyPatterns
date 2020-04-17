class Creature:
    def __init__(self):
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    # Here we can see addition of any new attribute will require changes in all these properties and is error prone
    @property
    def sum_of_stats(self):
        return self.agility + self.intelligence + self.strength

    @property
    def max_stat(self):
        return max(self.strength, self.intelligence, self.agility)

    @property
    def average_stat(self):
        return self.sum_of_stats/3


# Now lets use list to store the values
class BetterCreature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    # Here we can see addition of any new attribute will require no changes
    @property
    def sum_of_stats(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return self.sum_of_stats/len(self.stats)
