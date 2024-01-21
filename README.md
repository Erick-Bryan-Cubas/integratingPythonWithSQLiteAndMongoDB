# Integrating Python with SQLite and MongoDB

### Part 1 - Implementing a Relational Database with SQLAlchemy

Objective:

In this challenge, you will implement an integration application with SQLite based on a provided relational schema. Therefore, use the schema within the context of client and account to create classes for your API. These classes will represent the tables of the relational database within the application.

<img src="GitHub\tables.png" alt="Client x Account Table">
Deliverables:

- Application with schema definition through classes using SQLAlchemy
- Insertion of a minimal dataset for information manipulation
- Execution of data retrieval methods via SQLAlchemy

### Part 2 - Implementing a NoSQL Database with Pymongo

You will implement a NoSQL database with MongoDB to provide an aggregated view of the relational model. Therefore, existing client and account information is contained within documents according to the client.

Perform the following operations:

- Connect to MongoDB Atlas and create a database
- Define a collection 'bank' to create client documents
- Insert documents with the mentioned structure
- Write retrieval instructions based on key-value pairs as demonstrated in class