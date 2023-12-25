---
layout: post
title: "[nodejs] 데이터베이스 연동을 위한 ORM(Object-Relational Mapping) 사용법"
description: " "
date: 2023-12-26
tags: [nodejs]
comments: true
share: true
---

ORM은 개발자가 데이터베이스와 상호 작용하기 위한 객체 지향적인 방법을 제공하는 프로그래밍 기술이다. JavaScript 개발자들은 주로 Node.js를 사용하여 백엔드와 데이터베이스를 연동하는데, 이때 ORM을 사용하면 데이터베이스와 상호 작용하는 코드를 좀 더 간결하고 유지보수하기 쉽게 작성할 수 있다.

## ORM 라이브러리 선택

가장 대중적인 ORM 라이브러리 중 하나인 Sequelize를 선택하여 사용해보자. 

```javascript
const Sequelize = require('sequelize');

// 데이터베이스 연결 설정
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql'
});
```

## 데이터 모델 정의

ORM을 사용하면 데이터베이스 테이블의 구조를 JavaScript 클래스 형태로 정의할 수 있다. 

```javascript
const { DataTypes } = require('sequelize');

const User = sequelize.define('User', {
  // 속성 정의
  firstName: {
    type: DataTypes.STRING,
    allowNull: false
  },
  lastName: {
    type: DataTypes.STRING
  },
  email: {
    type: DataTypes.STRING
  }
});
```

## 데이터베이스 쿼리

ORM을 사용하면 JavaScript로 데이터베이스 쿼리를 작성할 수 있다.

```javascript
// 사용자 생성
await User.create({
  firstName: 'John',
  lastName: 'Doe',
  email: 'john.doe@example.com'
});

// 사용자 조회
const users = await User.findAll();
```

## 결론

ORM은 데이터베이스 연동을 좀 더 쉽게 만들어주며, 데이터 모델을 명확히 정의하고 데이터베이스 쿼리를 관리하기 용이하게 해준다. Sequelize와 같은 ORM 라이브러리를 사용하면 Node.js 애플리케이션을 보다 효율적으로 개발할 수 있다.

---
참조: [Sequelize 공식 문서](https://sequelize.org/master)