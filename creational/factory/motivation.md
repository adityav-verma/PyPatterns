1. Object creation logic becomes too convoluted
2. Initializer is not descriptive enough
   - `__init__` , this does not tell much
   - Can turn into an optional parameter hell
4. Wholesale object creation (non-piecewise unlike Builder pattern) can be outsourced to
   - A separate method ie factory method
   - A separate class called Factory
   - A hierarchy of factories with Abstract Factory

So a factory is a component which is concerned with wholesale creation of an object as opposed to piece wise (Builder).