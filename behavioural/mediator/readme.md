- Components may go in and out of the system at any time
    - Chat room participants
    - Multi-player online game

- It makes no sense for them to have direct references to one another
    - Those references may go dead
- Solution: Have them all refer to some central component that facilitates communication

**Mediator is a component that facilitates communication between other components without thme
necessarily being aware of each other or having direct (reference) access to each other**

- Create a mediator and have each object refer to it
- Mediator engages in bi-directional communication with it's connected components
- Mediator has function which the components can call
- Components have functions that the mediator can call
- Event processing libraries make communication easier to implement
    