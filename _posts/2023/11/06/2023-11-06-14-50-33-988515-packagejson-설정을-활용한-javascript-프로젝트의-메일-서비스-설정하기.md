---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 메일 서비스 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

이번 튜토리얼에서는 JavaScript 프로젝트에서 메일 서비스를 설정하는 방법을 알아보겠습니다. 우리는 `package.json` 파일을 사용하여 필요한 패키지를 설치하고, 메일 서비스 관련 설정을 추가할 것입니다.

## 단계 1: 패키지 설치하기

먼저, 프로젝트 디렉토리에서 터미널을 열고 다음 명령어를 실행하여 메일 서비스에 필요한 패키지를 설치합니다.

```bash
npm install nodemailer
```

이렇게 하면 [Nodemailer](https://nodemailer.com/about/) 패키지가 프로젝트에 설치됩니다. Nodemailer는 Node.js에서 메일을 보내는 데 도움이 되는 강력한 라이브러리입니다.

## 단계 2: package.json 파일 수정하기

이제 `package.json` 파일을 열고 다음과 같이 `scripts` 부분을 추가해 보겠습니다.

```json
"scripts": {
  "send-mail": "node send-mail.js"
}
```

위의 예시에서 `send-mail.js`는 우리가 작성한 메일 보내기 스크립트 파일의 이름입니다. 이제 나중에 `npm run send-mail` 명령어를 사용하여 이 스크립트를 실행할 수 있습니다.

## 단계 3: 메일 서비스 설정하기

이제 메일 서비스에 필요한 설정을 추가해 보겠습니다. 프로젝트 디렉토리에 `send-mail.js` 파일을 생성하고 다음 코드를 추가합니다.

```javascript
const nodemailer = require('nodemailer');

async function sendMail() {
  let transporter = nodemailer.createTransport({
    host: 'smtp.example.com',
    port: 587,
    secure: false, // true for 465, false for other ports
    auth: {
      user: 'your-email@example.com',
      pass: 'your-email-password'
    }
  });

  let mailOptions = {
    from: 'your-email@example.com',
    to: 'recipient@example.com',
    subject: 'Hello from Node.js',
    text: 'This is a test email.'
  };

  let info = await transporter.sendMail(mailOptions);
  console.log('Message sent: %s', info.messageId);
}

sendMail().catch(console.error);
```

위의 코드에서 `host`, `port`, `user`, `pass`, `from`, `to`, `subject`, `text` 등을 실제 메일 서비스에 맞게 설정해야 합니다. 예를 들어, `host`는 사용하고 있는 메일 서비스 제공자의 호스트 주소를 입력해야 합니다.

## 단계 4: 메일 보내기

이제 메일 보내기 스크립트를 실행해 보겠습니다. 터미널에서 다음 명령어를 실행합니다.

```bash
npm run send-mail
```

이렇게 하면 우리가 작성한 스크립트가 실행되고, 설정한 메일이 보내집니다.

## 결론

JavaScript 프로젝트에서 메일 서비스를 설정하는 방법에 대해 알아보았습니다. `package.json` 파일을 활용하여 필요한 패키지를 설치하고, 메일 서비스 관련 설정을 추가함으로써 간단하게 메일을 보낼 수 있습니다.