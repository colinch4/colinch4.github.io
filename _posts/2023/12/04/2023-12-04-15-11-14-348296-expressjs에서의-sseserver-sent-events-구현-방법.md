---
layout: post
title: "[javascript] Express.js에서의 SSE(Server-Sent Events) 구현 방법"
description: " "
date: 2023-12-04
tags: [javascript]
comments: true
share: true
---

Express.js는 Node.js를 위한 빠르고 유연한 웹 애플리케이션 프레임워크입니다. 이 프레임워크를 사용하여 SSE(Server-Sent Events)를 구현하는 방법에 대해 알아보겠습니다.

## SSE란?
SSE는 웹 브라우저와 서버 간에 지속적인, 단방향으로 이루어지는 통신 방식입니다. 이를 통해 서버에서 클라이언트로 데이터 스트림을 보낼 수 있습니다. 웹 소켓과는 다르게 SSE는 HTTP를 사용하며, 자동으로 재연결 기능을 제공합니다.

## Express.js에서 SSE 구현하기
1. Express.js 및 필요한 종속성 설치하기:
```bash
npm install express
```

2. Express.js 애플리케이션 생성하기:
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

3. SSE 엔드포인트 설정하기:
```javascript
app.get('/sse', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');
  res.setHeader('Access-Control-Allow-Origin', '*');

  // SSE 데이터 전송
  setInterval(() => {
    const data = `data: ${new Date()}\n\n`;
    res.write(data);
  }, 1000);

  // 클라이언트 연결 종료 시 SSE 연결 해제
  req.on('close', () => {
    console.log('Client disconnected');
    res.end();
  });
});
```

위 코드에서 `/sse` 경로에 접속하면 SSE 데이터가 전송됩니다. `setInterval` 함수를 사용하여 1초마다 현재 시간을 클라이언트로 전송합니다.

4. SSE 클라이언트 구현하기:
```javascript
const eventSource = new EventSource('/sse');

eventSource.onmessage = (event) => {
  const data = event.data;
  console.log(data);
};
```

위 코드에서 `/sse` 경로로부터 SSE 데이터를 받아와 출력합니다.

## 결론
Express.js를 사용하여 SSE를 구현하는 방법에 대해 알아보았습니다. SSE는 실시간 업데이트가 필요한 애플리케이션에서 유용하게 사용될 수 있으며, Express.js는 이를 구현하기에 적합한 프레임워크입니다.

더 자세한 내용은 [MDN SSE 문서](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)를 참조하십시오.