- Ordinary statements are perishable
    - Cannot undo an operation like member assignment, etc
    - Cannot directly serialise a sequence of calls
- We want an object than represents an operations
    - This will allow features like rollback to the operation
- Uses: GUI commands, multi-level undo/redo operations, audit logs, etc


**Command is an object which represents an instruction to perform a particular action. Contains all information necessary
for that action to be taken.**

- Encapsulate all details of an operation in a separate object
- Define instructions for applying the command (either in the command itself, or elsewhere)
- Optionally define instructions for undoing a command
- Can create composite commands AKA Macros