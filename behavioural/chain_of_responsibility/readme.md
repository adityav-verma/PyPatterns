A chain of components will all get a chance to process a command or a query, optionally having default processing
implementation and *an ability to terminate the processing chain*

- Chain of responsibility can be implemented as a chain of references or a centralised construct
- Enlist objects in the chain, possibly controlling their order
- Object removal from chain on `__exit__`, if we need only for a specific duration