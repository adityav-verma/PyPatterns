- Need to define a new operation on an entire class hierarchy
    - Eg. make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in our hierarchy
- Need to access non-common aspects of classes in the hierarchy


**Visitor is a component that knows how to traverse a data structure composed of (possibly related) types.**

- OOP double dispatch approach is not necessary in Python (we have to get around using a decorator)
- Make a visitor, decorating each `overload` with @visitor
- call `visit()` and the entire structure gets traversed