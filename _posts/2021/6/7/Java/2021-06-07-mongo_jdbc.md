---
layout: post
title: "[java] MongoDB로 JDBC 사용하기"
description: " "
date: 2021-06-07
tags: [java]
comments: true
share: true
---

# 🦦 MongoDB로 JDBC 사용하기

### 1. 의존성 설정하기

> - MongoDB java Driver 다운받고 의존성 설정해주기
> - [MongoDB Java Driver API doc <--Click](https://mongodb.github.io/mongo-java-driver/3.12/javadoc/)

[Maven]

```java
<dependency>
    <groupId>org.mongodb</groupId>
    <artifactId>mongo-java-driver</artifactId>
    <version>3.12.7</version>
</dependency>
```

<br >

### 2. 데이터베이스 연결하기 : getDatabase()

> - 데이터베이스 연결을 위해서는 사용할 데이터베이스 이름을 명시해줘야 함
> - **getDatabase(db명)** : 명시된 db가 존재하면 가져오고, 없으면 자동으로 만들어줌

[MongoDB 연결 코드]

```java
import com.mongodb.client.MongoDatabase;
import com.mongodb.MongoClient;

public class ConnectToDB {
   public static void main( String args[] ) {
     // Creating a Mongo client
    MongoClient mongo = new MongoClient( "localhost" , 27017 );
     // Accessing the database
    MongoDatabase database = mongo.getDatabase("myDb"); // myDB에 연결
    System.out.println("Connected to the DB successfully"); }
}
```

<br >

### 3. Collection 생성하기 : createCollection()

> - com.mongodb.client.MongoDatabase class를 import해서 createCollection() 사용

```java
import com.mongodb.client.MongoDatabase;
import com.mongodb.MongoClient;

public class CreatingCollection {
   public static void main( String args[] ) {
     // Creating a Mongo client
MongoClient mongo = new MongoClient( "localhost" , 27017 );
     //Accessing the database
MongoDatabase database = mongo.getDatabase("myDb");
System.out.println("Connected to the DB successfully");

     //Creating a collection
database.createCollection("sampleCollection");
System.out.println("Collection created successfully"); }
}
```

<br>

### 4. Getting/Selecting a Collection

> - getColletcion()를 사용해서 MongoDB의 collection 받아오기

```java
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import com.mongodb.MongoClient;

public class selectingCollection {
   public static void main( String args[] ) {
     // Creating a Mongo client
MongoClient mongo = new MongoClient( "localhost" , 27017 ); // Accessing the database
MongoDatabase database = mongo.getDatabase("myDb");
     // Retrieving a collection
MongoCollection<Document> collection = database.getCollection("myCollection");

System.out.println("myCollection selected successfully"); }
}

```

<br>

### 5. Document 삽입하기 : new Document() & insertOne()

> - Document 타입을 생성해서 속성들을 넣기
> - => Document("key", "value") **ex>** Document("id", 1)
> - insertOne(Document)로 생성된 Document instance를 삽입하기

```java

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import com.mongodb.MongoClient;

public class InsertingDocument {
  public static void main( String args[] ) {
     // Creating a Mongo client
MongoClient mongo = new MongoClient( "localhost" , 27017 ); // Accessing the database
MongoDatabase database = mongo.getDatabase("myDb");
     // Retrieving a collection
MongoCollection<Document> collection = database.getCollection("sampleCollection");

System.out.println("sampleCollection selectedsuccessfully");

Document document =
new Document("title", "MongoDB")
.append("description", "database")
.append("likes", 100)
.append("url", "http://www.tutorialspoint.com/mongodb/")
.append("by", "tutorials point");

     //Collection에 생성한 document 넣어주기
collection.insertOne(document);
System.out.println("Document inserted successfully");
} }
```

<br>

### 5-1. insertMany()로 여러개의 document 넣기

> - 여러개의 document를 넣어주려면 List에 생성된 document를 넣어주고
> - 이 List를 insertMany()매소드를 통해 Collection에 삽입

```java
//Document 여러개 생성
Document document1 = new Document("title", "MongoDB")
.append("description", "database")
.append("likes", 100)
.append("url", "http://www.tutorialspoint.com/mongodb/")
.append("by", "tutorials point");


Document document2 = new Document("title", "RethinkDB")
.append("description", "database")
.append("likes", 200)
.append("url", "http://www.tutorialspoint.com/rethinkdb/") .append("by", "tutorials point");


//리스트 생성 후 하나씩 넣어주기
List<Document> list = new ArrayList<Document>();

list.add(document1);
list.add(document2);

//리스트 전체를 Collection에 넣어주기
collection.insertMany(list);


```

<br>

### 6. Document 찾기 : collection.find()

> - collection 내부의 모든 column을 받아오려면 collection.find() 메소드
> - 혹은 query를 통해 특정 값만 find 가능

```java

// select * from databaseName

collection.find();

//resultList 내부의 값들 받아오기 getString()으로 특정 row지정 가능

collection.find().into(resultList);
for (Document document : resultList) {
	System.out.println(document.getString("userid") + " is " + document.getString("name"));
    }

//userid가 mongo인 값 resultLust에서 받아오기

Document query = new Document("userid", "mongo");
collection.find(query).into(resultList);


```

<br>

### 7. Document 업데이트 : updateOne()

> - collection 내부의 특정 row를 업데이트 할 때 사용
> - 매소드 사용법 : updateOne(Filters.eq(key,value), Updates.set(update_key, update_value))

```java

// userid가 mongo인 row의 addr = Budapest로 업데이트 하기

collection.updateOne(Filters.eq("userid", "mongo"), Updates.set("addr", "Budapest"));
```

<br>

### 8. Document 삭제하기: deleteOne()

>

```java

//addr = SF인 document 삭제하기

Document query2 = new Document("addr", "SF");
collection.deleteOne(query2);

```

<br>

### 8. Collection 드롭하기 : drop()


```java

MongoCollection<Document> collection = database.getCollection("sampleCollection");

// Dropping a Collection
collection.drop();
System.out.println("Collection dropped successfully");
```

<br>
