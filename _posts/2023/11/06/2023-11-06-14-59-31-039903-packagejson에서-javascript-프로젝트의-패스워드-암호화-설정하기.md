---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 패스워드 암호화 설정하기"
description: " "
date: 2023-11-06
tags: [Package]
comments: true
share: true
---

JavaScript 프로젝트에서 패스워드를 암호화하는 것은 보안을 강화하는 중요한 단계입니다. 패스워드를 암호화하면 사용자의 개인 정보를 보호하고, 데이터 무결성을 유지할 수 있습니다. 이 기사에서는 package.json 파일을 사용하여 JavaScript 프로젝트에서 패스워드를 암호화하는 방법을 알아보겠습니다.

## 패스워드 암호화 패키지 설치

패스워드를 암호화하기 위해서는 먼저 암호화 패키지를 프로젝트에 설치해야 합니다. 많은 암호화 패키지 중에서 bcrypt.js를 사용해 보겠습니다. bcrypt.js는 강력한 해시 함수를 제공하여 패스워드를 안전하게 저장할 수 있습니다. 

프로젝트 폴더에서 아래 명령어를 사용하여 bcrypt.js 패키지를 설치합니다:

```shell
npm install bcryptjs
```

## 패스워드 암호화 처리

이제 패스워드 암호화 로직을 구현해보겠습니다. package.json 파일을 열고, "scripts" 섹션에 "hash:password" 스크립트를 추가합니다:

```json
"scripts": {
  "hash:password": "node -e 'const bcrypt = require(\"bcryptjs\"); const password = \"mypassword\"; bcrypt.genSalt(10, (err, salt) => { bcrypt.hash(password, salt, (err, hash) => { console.log(hash); }); });'"
}
```

위의 예제에서 "mypassword"를 암호화하고 싶은 패스워드로 변경해야 합니다.

이제 아래 명령어를 사용하여 패스워드를 암호화합니다:

```shell
npm run hash:password
```

실행 결과로 암호화된 패스워드가 콘솔에 출력됩니다.

## 패스워드 암호화 설정

패스워드를 암호화하고 나면, 프로젝트의 설정 파일에서 패스워드를 저장할 수 있습니다. 보안을 위해 패스워드는 환경 변수로 설정되어야 합니다. package.json 파일의 "scripts" 섹션에서 "start" 스크립트에 패스워드를 전달하는 로직을 추가합니다:

```json
"scripts": {
  "start": "node -e 'const bcrypt = require(\"bcryptjs\"); const password = process.env.PASSWORD; bcrypt.genSalt(10, (err, salt) => { bcrypt.hash(password, salt, (err, hash) => { console.log(hash); }); });'"
}
```

위의 예제에서 process.env.PASSWORD는 패스워드 값을 환경 변수로부터 읽어옵니다.

이제 패스워드를 설정하려면, 아래와 같이 명령어를 실행합니다:

```shell
export PASSWORD=mypassword
```

위의 예제에서 "mypassword"는 실제 패스워드로 변경해야 합니다.

이제 아래 명령어를 사용하여 패스워드를 암호화합니다:

```shell
npm start
```

실행 결과로 암호화된 패스워드가 콘솔에 출력됩니다.

## 결론

package.json 파일을 사용하여 JavaScript 프로젝트에서 패스워드를 암호화하는 방법을 배웠습니다. 패스워드를 암호화하면 보안을 강화하고 사용자의 개인 정보를 보호할 수 있습니다. bcrypt.js와 같은 암호화 패키지를 사용하여 안전한 암호화 로직을 구현하는 것이 중요합니다.