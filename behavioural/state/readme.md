A pattern in which an objects behaviour is determined by it's state.
A object transitions from one state to another (something needs to trigger a transition).

**A formalised construct which manages state and transitions is called a state machine**

The classic implement is too complex, hence we use a Trigger <-> State combination
- State entry/exit behaviour
- Guard conditions enabling/disabling a transition
- Default action when no transitions are found for an event