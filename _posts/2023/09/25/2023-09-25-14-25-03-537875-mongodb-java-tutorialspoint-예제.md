---
layout: post
title: "mongodb java tutorialspoint 예제"
description: " "
date: 2023-09-25
tags: [mongodb]
comments: true
share: true
---

MongoDB is a popular NoSQL database that allows developers to store and analyze large amounts of unstructured data. In this tutorial, we will cover the basics of working with MongoDB using the Java programming language. 

Before diving into the tutorial, make sure you have MongoDB installed and running on your machine. You can download MongoDB from the official website and follow the installation instructions.

## Step 1: Setting up the Java Development Environment

To work with MongoDB using Java, we need to set up our development environment. Follow these steps to get started:

1. Install Java Development Kit (JDK) on your machine if you haven't already.

2. Set up your favorite Integrated Development Environment (IDE) for Java development. IntelliJ IDEA, Eclipse, and NetBeans are popular choices.

3. Create a new Java project in your chosen IDE.

4. Add the MongoDB Java driver as a dependency to your project. You can do this by adding the following Maven dependency to your `pom.xml` file:

```xml
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongodb-driver-sync</artifactId>
    <version>4.3.1</version>
</dependency>
```

Alternatively, if you are not using Maven, you can manually download the MongoDB Java driver from the official MongoDB website and add it to your project's classpath.

## Step 2: Connecting to MongoDB

Now that our development environment is ready, let's start by connecting to a MongoDB database. Here's an example code snippet:

```java
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;

public class MongoDBDemo {
    public static void main(String[] args) {
        // Connect to MongoDB server
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            // Connect to a specific database
            MongoDatabase database = mongoClient.getDatabase("mydb");
            System.out.println("Connected to MongoDB successfully!");
        } catch (Exception e) {
            System.err.println("MongoDB connection error: " + e.getMessage());
        }
    }
}
```

In this example, we use the `MongoClients` class from the MongoDB Java driver to create a connection to the MongoDB server running on `localhost` at the default port `27017`. We then get a reference to a specific database using the `getDatabase()` method and print a success message if the connection is established.

## Step 3: Performing CRUD Operations

Once we have established a connection to MongoDB, we can perform CRUD (Create, Read, Update, Delete) operations. Here are some examples to get you started:

### Inserting a Document

```java
import org.bson.Document;
import com.mongodb.client.MongoCollection;

// ...

// Get a reference to a collection
MongoCollection<Document> collection = database.getCollection("mycollection");

// Create a new document
Document document = new Document("name", "John Doe")
    .append("age", 30)
    .append("email", "johndoe@example.com");

// Insert the document into the collection
collection.insertOne(document);
```

### Querying Documents

```java
import com.mongodb.client.MongoCursor;

// ...

// Find documents that match a specific condition
MongoCursor<Document> cursor = collection.find(new Document("age", new Document("$gt", 25))).iterator();

// Iterate over the cursor and print the documents
while (cursor.hasNext()) {
    Document doc = cursor.next();
    System.out.println(doc.toJson());
}
```

### Updating Documents

```java
import static com.mongodb.client.model.Filters.*;
import static com.mongodb.client.model.Updates.*;

// ...

// Update a document that matches a specific condition
collection.updateOne(eq("name", "John Doe"), set("age", 35));
```

### Deleting Documents

```java
import static com.mongodb.client.model.Filters.*;

// ...

// Delete documents that match a specific condition
collection.deleteMany(eq("name", "John Doe"));
```

These examples demonstrate some basic CRUD operations using the MongoDB Java driver. However, MongoDB offers many more features and functionalities that you can explore in the official documentation.

## Conclusion

In this tutorial, we covered the basics of working with MongoDB using the Java programming language. We set up the development environment, connected to a MongoDB database, and performed CRUD operations using the MongoDB Java driver. Now it's time to dive deeper and explore the various capabilities of MongoDB in your Java applications. Happy coding!

## #MongoDB #Java