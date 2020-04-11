1. For some components, it only makes sense to have one in the system
    - Database repository
    - Object factory
2. Initializer call is expensive
    - We do it only once
    - We provide everyone with the same instance
3. Want to prevent anyone from creating additional copies
4. Need to take care of lazy initialization

**Singleton is a component which is initialized only once.**