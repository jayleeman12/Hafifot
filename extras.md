# Extras
If you're here, that means you finished everything else you had to do

The extra exercises assume knowledge in design & full-stack development
## Message Queue
The year is 2146.

Communication between services using RESTful API's directly is banned.

And in such dark times, the heroes of Hafifot-Land must rise to the occasion!

During a super secret convention by the rebel forces (#PyCon2146), a decision was made to write a new concept never thought of before, a **message queue!**, and it is your job, as the future of overly-paid full-stack developers, to create this new unheard-of concept.

First things first, read about what a message queue is.

Done? Great, so here's what you need to do (ordered by importance)
### #1 - In Memory MQ
Implement a simple MQ, that stores messages in-memory (no persistent storage required). The interactions are:
- Create/delete a queue
- Post a new message to a queue
- Pull messages from a queue
- Subscribe to a queue and get notified when a new message is pushed

**Notes**

When pulling/subscribing to messages, they are removed from the 
queue

The exposed API has to be over network (HTTP, Websockets, etc)
### #2 - Persistency
Everyone likes your MQ! But there's a major complaint coming from alot of people - when the service crashes, all the messages & queues disappear!

You've been tasked with making the MQ **persistent**. Meaning, every change in the MQ state must persist through crashes.

Feel free to use any type of persistent storage (file, DB etc)
### #3 - UI
So you've reached 5k stars on github, and everyone's happy - except product managers. Your clients' product managers found a missing part in your system, a UI! They want to:
- See what queues currently exist
- Delete, Create, Rename a queue
- Read the message currently unread in a queue
- See who is listening to a queue