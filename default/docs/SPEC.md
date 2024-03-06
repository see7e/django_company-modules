# SPECIFICATION

## Overview

### High-Level Overview:

1. **Functional Requirements**:
   - These describe the specific functions or features that the system must provide to satisfy user needs.

2. **Non-Functional Requirements**:
   - These describe the qualities or attributes of the system, such as performance, reliability, and scalability.

### Detailed Components:

#### Functional Requirements:
1. **User Authentication & Authorization**:
   - Allows users to log in and access the system based on their roles and permissions.

2. **Inventory Management**:
   - Enables users to manage inventory, including adding, updating, and removing items.

3. **Order Management**:
   - Facilitates the processing of orders, including creation, fulfillment, and tracking.

4. **Reporting**:
   - Provides reporting functionality to generate various types of reports, such as sales reports, inventory reports, and performance metrics.

5. **Notification System**:
   - Sends notifications to users for important events, such as order status updates or low inventory alerts.

#### Non-Functional Requirements:
1. **Performance**:
   - The system should respond to user requests within a specified time frame, even under heavy load.

2. **Scalability**:
   - The system should be able to handle increasing numbers of users, transactions, and data volume without significant degradation in performance.

3. **Reliability**:
   - The system should be available and reliable, with minimal downtime and data integrity maintained.

4. **Security**:
   - The system should implement appropriate security measures to protect sensitive data and prevent unauthorized access.

5. **Usability**:
   - The system should be user-friendly and intuitive, with clear navigation and informative error messages.

### UML Diagram:

Here's a simplified UML diagram illustrating the main components and their relationships:

```
+-------------------+
|    Functional    |
+-------------------+
| - UserAuth       |
| - InventoryMgmt  |
| - OrderMgmt      |
| - Reporting      |
| - Notification   |
+-------------------+

+-------------------+
| Non-Functional   |
+-------------------+
| - Performance    |
| - Scalability    |
| - Reliability    |
| - Security       |
| - Usability      |
+-------------------+
```

This UML model provides a structured overview of both the functional and non-functional requirements of the system. Each component can be further expanded to include more detailed requirements, use cases, and interactions as needed. Additionally, you may consider using other UML diagrams such as use case diagrams, sequence diagrams, and activity diagrams to further elaborate on the system's behavior and architecture.


## Appications

### Core

Will handle the event driven architecture each business logic will be handled by a separate application.

I'm in doubt from what to use, I've noticed that I could create a simple event driven architecture using a built program such as RabbitMQ or Kafka, but this will take from me the possibility to understand how everything goes in the background, so I'm thinking about three options:

- using **model classes** (sql tables) to create a history of events, and then create a service that will handle the events and send them to the right application.
   > In this approach, events are persisted in a database table (Event table) when they occur.
   > You can have separate processes or background jobs that periodically read from this event log table and process the events.
   > This approach is suitable for simpler systems or when real-time event processing is not a strict requirement.
   > It provides a simple and straightforward way to handle events without introducing additional infrastructure complexities.
- using a **controller along with a middleware** to handle the events and send them to the right application.
   > In this approach, you can implement a custom middleware that acts as a pub/sub controller.
   > The middleware can subscribe to specific events and publish events when certain conditions are met.
   > This approach allows for more real-time event processing compared to reading from a log table.
   > It provides flexibility and can be tailored to your specific application requirements.
   > However, implementing custom middleware for event handling adds complexity to your application and may require careful design and testing.
- using a **event-bus** (don't make sense create one from the ground up, when there are already the two options above, RabbitMQ and Kafka).
   > An event bus is a centralized component that facilitates the exchange of events between different parts of your application.
   > Components can publish events to the event bus, and other components can subscribe to specific types of events.
   > Event buses offer a scalable and decoupled architecture for event-driven systems.
   > Popular event bus implementations include Apache Kafka, RabbitMQ, and AWS EventBridge.
   > Using an event bus adds some overhead in terms of setup and maintenance but provides a robust solution for handling events in complex applications.
