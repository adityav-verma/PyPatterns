# Creational

## Builder
- Separate component when object construction gets too complicated
- Can create mutually cooperating sub-builders
- Often has a fluent interface

## Factories
- Factory method more expressive than initializer
- Factory can be an outside class or inner class

## Prototype
- Creation of object from an existing object
- Requires explicit deep copy

## Singleton
- When you need to ensure just a single instance exisits
- Easy to make with a decorator or metaclass
- Consider using dependency injection

# Structural

## Adapter
- Converts the interface you get to the interface you need

## Bridge
- Decouple abstraction from implementation

## Composite
- Allows clients to treat individual objects and compositions of objects uniformly

## Decorator
- Attach additional responsibilities to object
- Python has functional decorator

## Facade
- Provide a single unified interface over a set of interface
- Friendly and easy-to-use, but can provide access to low-level features

## Flyweight
- Efficiently support very large numbers of similar objects

## Proxy
- Provide a surrogate object that forwards calls to the real object while performing additional functions
- E.g., access control, communication, logging, etc.

# Behavioural
## Chain of Responsibility
- Allow components to process information/events in a chain
- Each element in the chain refers to next element; or
- Make a list and go through it

## Command
- Encapsulate a request into a separate object
- Good for audit, replay, undo/redo
- Part of CQS/CQRS

## Interpreter
- Transform textual input into object-oriented structures
- Used by interpreters, compilers, static analysis tools, etc.
- Compiler Theory is a separate branch of Computer Science

## Iterator
- Provide an interface for accessing elements of an aggregate object
- `__iter__/__next` are stateful, but `yield` is much more convenient

## Mediator
- Provides mediation services between two objects
- E.g., message passing, chat room

## Memento
- Yield tokens representing system states
- TOkens do not allow direct manipulation, but can be used in appropriate APIs


## Observer
- Allows notifications of changes/happenings in a component

## State
- We model system by having one of a possible states and transitions between these states
- Such a system is called a state machine
- Special frameworks exists to orchestrate state machines

## Strategy & Template Method
- Both define a skeleton algorithm with details filled in by implementor
- Strategy uses ordinary composition, template method uses inheritance

## Visitor
- Allows non-intrusive addition of functionality to hierarchies



