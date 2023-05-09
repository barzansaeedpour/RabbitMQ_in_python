# RabbitMQ, What is that?

RabbitMQ is one part of Message Broker that implemented Advance Message Queue Protocol (AMQP), that help your application to communicate each other, when you extends your application scale.

![alt text](/images/1.webp)

There are 2 ways to communicate between micro-services. They are Point to Point (P2P)/Synchronous Communication, and Publish-Subscribe (Pub-Sub)/Asynchronous Communication. What is the differences between those two?
P2P as it’s called Synchronous Communication, we know that one app will directly communicate to other app, using HTTP protocol, which is the app does require immediate get response directly from the server.
Pub-Sub as it’s called asynchronous communication, we know that it does not required immediate response from the server, and the message that sent will be placed to a message queue (or known as Event Queue in Enterprise Messaging System).

RabbitMQ also called as middleware build using Erlang, due it can be both micro-services and an app. RabbitMQ support multiple protocols, here is the protocol that RabbitMQ support:
- AMQP
- HTTP
- STOMP
- MQTT

## How RabbitMQ works?
Exchange is an algorithm that decide which queue that will store the message (get message from producer, include in queue of consumer). Each consumer get it’s own Queue based on logic that you use, there are 4 type of logic that you can use in Exchange:
- Direct Exchange: Will be direct to queue based on a message routing key
- Fanout Exchange: Will publish to all queues that have same routing key
- Topic Exchange: Will publish to all queue that have same routing key and routing pattern specified in the binding
- Headers Exchange: Header means header in sending a file http, like when you send Image the header is ‘image/*’

## Why do we need to use RabbitMQ?
Decouple: What means by decoupling is separate the core components of the application. This is what any application that implement micro-services wanted. Because their application will be maintainable and improve it’s quality of Single Responsibility Principle.

Flexibility: flexibility is a key advantage of our decoupled application architecture. By separating the various components, we've created a system that is easily adaptable to future development needs. But our flexibility extends beyond just the application itself. Thanks to our use of RabbitMQ, we can seamlessly connect different apps and services, even if they were developed using different technologies. The Message Oriented Middleware (MOM) acts as a translator, enabling these applications to communicate with each other effectively.

Another benefit of using RabbitMQ:
- Highly Available Queue
- Multi-Protocol
- Many Client
- Clustering
- Management UI
- Tracing (Using dashboard can trace support)
- Plugin System (Extend core broker functionality in a variety of ways)
