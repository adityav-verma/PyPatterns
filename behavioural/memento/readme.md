- An object or system goes through changes
    - Like bank account's deposits and withdrawals
- One way to record every change (Command) and teach a command to `undo` itself
- Another way is to simply have snapshots of the system (`Memento`).

**Memento is a token/handle representing the system state. Lets us roll back to the state when the
token was generated. May or may not directly expose state information.**

- Mementos are used to roll back states arbitrarily
- A memento is simply a token/handle of class with (typically) no functionality of it's own
- A memento is not required to expose directly the state(s) to which it reverts the system
- Can be used to implement undo/redo