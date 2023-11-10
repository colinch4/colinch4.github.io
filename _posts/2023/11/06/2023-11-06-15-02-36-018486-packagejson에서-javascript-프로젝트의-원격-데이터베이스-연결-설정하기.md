---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 원격 데이터베이스 연결 설정하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

이 기술 블로그에서는 JavaScript 프로젝트에서 원격 데이터베이스에 연결하는 방법을 배우게 될 것입니다. Node.js 환경에서 작업하는 경우 프로젝트의 Package.json 파일을 활용하여 데이터베이스 연결을 구성할 수 있습니다.

## 1. 필요한 패키지 설치하기

먼저, 프로젝트 디렉토리에서 터미널을 열고 아래 명령어를 사용하여 필요한 패키지를 설치해야 합니다.

```javascript
npm install mysql
```

이 명령어를 실행하여 MySQL 데이터베이스에 연결하기 위한 'mysql' 패키지를 설치합니다.

## 2. Package.json 파일 수정하기

프로젝트의 루트 디렉토리에 있는 Package.json 파일을 엽니다. 'scripts' 섹션 아래에서 'start' 명령어 부분을 수정하여 데이터베이스 연결 정보를 설정할 수 있습니다.

```javascript
"scripts": {
  "start": "DB_HOST=your_host DB_USER=your_user DB_PASSWORD=your_password DB_NAME=your_database node app.js"
},
```

위 코드에서 'your_host', 'your_user', 'your_password', 'your_database' 부분을 본인의 데이터베이스 연결 정보로 대체해야 합니다. 각각의 필드를 본인의 데이터베이스 호스트, 사용자 이름, 비밀번호, 데이터베이스 이름으로 수정해 주세요.

## 3. 데이터베이스 연결 코드 작성하기

이제 원격 데이터베이스에 연결하기 위한 JavaScript 코드를 작성해야 합니다. app.js 파일을 열고 아래 코드를 추가합니다.

```javascript
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME
});

connection.connect((error) => {
  if (error) {
    console.error('Error connecting to database:', error);
  } else {
    console.log('Connected to database successfully!');
  }
});
```

위 코드에서 `mysql` 패키지를 `require`하여 사용하고 있으며, `process.env` 객체를 통해 Package.json 파일에서 설정한 환경 변수를 가져와 데이터베이스에 연결합니다.

## 4. 프로젝트 실행하기

이제 터미널에서 아래 명령어를 실행하여 프로젝트를 실행할 수 있습니다.

```javascript
npm start
```

위 명령어를 실행하면 Package.json에 설정된 데이터베이스 연결 정보를 사용하여 프로젝트가 시작됩니다. 만약 연결에 실패하면 오류 메시지가 출력됩니다.

이렇게 하면 JavaScript 프로젝트에서 원격 데이터베이스에 연결하는 것이 가능합니다. 이를 통해 프로젝트에서 데이터베이스와의 상호작용을 수행할 수 있습니다.

## 5. 참고 자료

- [Node.js MySQL - Packagist](https://www.npmjs.com/package/mysql)
- [dotenv - Packagist](https://www.npmjs.com/package/dotenv)

잘못된 설정으로 인한 문제가 발생하지 않도록 주의해 주시고, 위 정보를 참고하여 원격 데이터베이스 연결을 구성해 주세요.