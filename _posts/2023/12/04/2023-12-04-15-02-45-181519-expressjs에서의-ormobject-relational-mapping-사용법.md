---
layout: post
title: "[javascript] Express.js에서의 ORM(Object-Relational Mapping) 사용법"
description: " "
date: 2023-12-04
tags: [javascript]
comments: true
share: true
---

ORM(Object-Relational Mapping)은 관계형 데이터베이스와 객체 지향 프로그래밍 간의 데이터 변환을 자동화해주는 도구입니다. 이번 포스트에서는 Express.js에서 ORM을 사용하는 방법을 알아보겠습니다.

## 1. ORM 라이브러리 선택

Express.js에서 ORM을 사용하기 위해서는 먼저 적절한 ORM 라이브러리를 선택해야 합니다. 대표적인 ORM 라이브러리로는 Sequelize, TypeORM, Prisma 등이 있습니다. 각 라이브러리마다 특징과 사용법이 다르므로, 프로젝트의 요구사항과 개인적인 취향에 맞게 선택해야 합니다.

## 2. ORM 설치

선택한 ORM 라이브러리를 설치해야 합니다. npm을 이용하면 간단하게 설치할 수 있습니다. 예를 들어 Sequelize를 사용한다면 다음 명령을 사용하여 설치할 수 있습니다:

```
npm install sequelize
```

## 3. 모델 정의

ORM을 사용하기 위해서는 데이터베이스와의 연결 설정과 모델 정의가 필요합니다. 모델은 데이터베이스의 테이블과 매핑되는 객체입니다. 모델의 정의는 ORM 라이브러리마다 조금씩 다를 수 있으므로, 해당 라이브러리의 문서를 참고하여 작성해야 합니다.

Sequelize를 사용한다면, 다음과 같이 모델을 정의할 수 있습니다:

```javascript
const { Sequelize, Model, DataTypes } = require('sequelize');
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql'
});

class User extends Model {}
User.init({
  username: DataTypes.STRING,
  email: DataTypes.STRING,
  password: DataTypes.STRING
}, { sequelize, modelName: 'user' });
```

## 4. 라우터에서 ORM 사용

정의한 모델을 Express.js의 라우터에서 사용하여 데이터베이스 조작을 할 수 있습니다. 데이터베이스에 데이터를 조회, 생성, 수정, 삭제하는 등의 작업은 모델의 메서드를 이용하면 됩니다.

Sequelize를 사용한다면, 다음과 같이 라우터에서 ORM을 사용할 수 있습니다:

```javascript
const express = require('express');
const router = express.Router();
const User = require('../models/user');

router.get('/users', async (req, res) => {
  const users = await User.findAll();
  res.json(users);
});

router.post('/users', async (req, res) => {
  const newUser = await User.create(req.body);
  res.json(newUser);
});

// 이 외에도 필요한 라우터를 추가할 수 있습니다.

module.exports = router;
```

## 5. 데이터베이스 마이그레이션

ORM을 사용하면 데이터베이스 스키마를 코드로 관리할 수 있는 장점이 있습니다. 데이터베이스의 테이블을 생성, 수정, 삭제하기 위해서는 마이그레이션 작업을 수행해야 합니다. ORM 라이브러리마다 마이그레이션 도구가 포함되어 있으므로, 해당 도구를 사용하여 마이그레이션 작업을 수행할 수 있습니다.

Sequelize를 사용한다면, 다음과 같이 마이그레이션 파일을 작성하고 실행할 수 있습니다:

```javascript
'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('users', {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      username: {
        type: Sequelize.STRING,
        allowNull: false
      },
      email: {
        type: Sequelize.STRING,
        allowNull: false
      },
      password: {
        type: Sequelize.STRING,
        allowNull: false
      },
      createdAt: {
        type: Sequelize.DATE,
        allowNull: false
      },
      updatedAt: {
        type: Sequelize.DATE,
        allowNull: false
      }
    });
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('users');
  }
};
```

```
npx sequelize-cli db:migrate
```

## 마무리

이제 Express.js에서 ORM을 사용하는 기본적인 방법을 알아보았습니다. ORM을 사용하면 객체 지향적으로 데이터베이스를 다룰 수 있으며, 데이터베이스 스키마 관리를 쉽게 할 수 있습니다. 다양한 ORM 라이브러리를 비교해보고, 프로젝트에 알맞은 ORM을 선택하여 사용해보세요.

## 참고 자료

- Sequelize 공식 문서: [https://sequelize.org/](https://sequelize.org/)
- TypeORM 공식 문서: [https://typeorm.io/](https://typeorm.io/)
- Prisma 공식 문서: [https://www.prisma.io/](https://www.prisma.io/)