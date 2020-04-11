- Algorithms can be decomposed into common parts + specifics
- `Strategy pattern` does this through composition
    - High level algorithms expects the strategies to conform to an interface
    - Concrete implementations implement the interface

- Template methods does the same thing through inheritance
    - Overall algorithm defined in the base calls; uses abstract functions/member
    - Inheritors override the abstract methods
    - Template methods invoked to get work done

**Template method allows us to define the skeleton of the algorithm, with concrete implementations defined in subclass**