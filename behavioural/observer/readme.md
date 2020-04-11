- We need to be informed when certain things happen
    - Object's property changes
    - Object does something
    - Some external event happened
- We want to listen to events and get notified when when they occur
    - Notification should contain useful data
- Want to unsubscribe from events if we are no longer interested

**An Observer is an object that wishes to be informed about events happening in the system.
The entity generating the events is an Observable**

- Observer is an intrusive approach: an observable must provide an event to subscribe
- Subscription/unsubscription is handled by addition or removal of items in the list
- Property notifications are easy, dependent notification are a little tricky