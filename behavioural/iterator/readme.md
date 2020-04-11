- Iteration is a core functionality of various data structures
- An iterator is a class which facilitates the traversal
    - Keep reference to the current element
    - Knows how to move to a different element
- The iterator protocol requires
    - `__iter__()` to expose the iterator which uses
    - `__next__()` to return each of the iterated elements or
    - raise `StopIteration` when it's done

**An iterator is an object that facilitates the traversal of a data structure**

- Stateful iterators cannot be recursive and are complex to implement
- `yield` allows for much more succinct iteration