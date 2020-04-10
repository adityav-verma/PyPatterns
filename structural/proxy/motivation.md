1. Same interface, entirely different behaviour.
2. Proxy intercepts an interface adds a different behaviour
3. Authenticate requests, logging, etc

**Proxy is a class which functions as an interface to a particular resource. That resource may be remote
, expensive to construct, or may require logging or some other added functionality**

### Proxy vs Decorator
- Proxy provides an identical interface, decorator provides an enhanced interface
- Decorator typically aggregates (has reference to) what it is decorating; proxy doesn't have to
- Proxy might not even be working with a materialised object (lazy loading)