"""A neuron and neuron layer, both the be connected to each other, via an implementation of connectable
Using Iterable abstract base class. The connectable class treats all objects as iterators. For a scalar object,
we yield self when iterated over
"""


from abc import ABC
from collections.abc import Iterable


class Connectable(ABC, Iterable):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self):
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super(NeuronLayer, self).__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f'{self.name} - {x}'))

    def __str__(self):
        return f'{self.name} with {len(self)} neurons'


if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)
    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)