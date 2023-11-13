---
layout: post
title: "npm 을 활용한 데이터베이스 연동 (Database integration with npm)"
description: " "
date: 2023-11-10
tags: [npm]
comments: true
share: true
---

데이터베이스는 현대 소프트웨어 개발에서 필수적인 요소입니다. 데이터베이스를 손쉽게 연동하기 위해 npm을 사용할 수 있습니다. npm은 노드 패키지 매니저로서 수많은 라이브러리와 모듈을 제공합니다. 따라서 데이터베이스와의 연동에 필요한 패키지를 쉽게 설치하고 사용할 수 있습니다.

이번 포스트에서는 가장 많이 사용되는 몇 가지 데이터베이스와 npm을 사용하여 어떻게 연동할 수 있는지 알아보겠습니다.

## 1. MongoDB

MongoDB는 NoSQL 데이터베이스로서, JSON 형식을 사용하는데요. JavaScript와의 호환성이 높아 Node.js와의 연동이 매우 간편합니다. MongoDB와의 연동을 위해 `mongodb` 패키지를 설치해야 합니다. 아래 명령어를 사용하여 패키지를 설치할 수 있습니다.

```shell
$ npm install mongodb
```

설치가 완료되면 다음과 같은 코드를 사용하여 MongoDB에 연결할 수 있습니다.

```javascript
const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017'; // MongoDB 서버 주소
const dbName = 'mydb'; // 사용할 데이터베이스 이름

(async () => {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    console.log('Connected to MongoDB');

    const db = client.db(dbName);
    // 데이터베이스 조작 코드 작성

  } catch (err) {
    console.error(err);
  } finally {
    await client.close();
  }
})();
```

위의 코드에서는 `MongoClient`를 사용하여 MongoDB에 연결하고, 연결된 데이터베이스를 사용하여 조작할 수 있습니다.

## 2. MySQL

MySQL은 관계형 데이터베이스로 가장 많이 사용하는 데이터베이스 중 하나입니다. MySQL과의 연동을 위해 `mysql` 패키지를 설치해야 합니다. 아래 명령어를 사용하여 패키지를 설치할 수 있습니다.

```shell
$ npm install mysql
```

설치가 완료되면 다음과 같은 코드를 사용하여 MySQL에 연결할 수 있습니다.

```javascript
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydb'
});

connection.connect((err) => {
  if (err) {
    console.error('Failed to connect to MySQL:', err);
  } else {
    console.log('Connected to MySQL');

    // 데이터베이스 조작 코드 작성

    connection.end();
  }
});
```

위의 코드에서는 `connection` 객체를 생성하여 MySQL에 연결하고, 연결된 데이터베이스를 사용하여 조작할 수 있습니다.

## 마무리

위에서는 npm을 사용하여 MongoDB와 MySQL과의 데이터베이스 연동 방법을 알아보았습니다. npm의 다양한 패키지를 활용하면 다른 데이터베이스들과의 연동도 쉽게 구현할 수 있습니다. 데이터베이스 연동을 통해 더욱 강력하고 유연한 애플리케이션을 개발해보세요!

_참고문서:_
- MongoDB: https://docs.mongodb.com/
- MySQL: https://dev.mysql.com/doc/