---
layout: post
title: "[javascript] Nuxt.js에서의 실시간 커뮤니케이션(Socket.io, WebSockets) 구현 방법은?"
description: " "
date: 2023-12-19
tags: [javascript]
comments: true
share: true
---

Nuxt.js는 Vue.js 기반의 프레임워크로, 클라이언트 측에서 실시간 커뮤니케이션을 구현할 때 **Socket.io**나 **WebSockets**를 사용할 수 있습니다. 이 블로그 포스트에서는 Nuxt.js에서의 각각의 방법을 설명하고 있습니다.

## Socket.io를 이용한 실시간 커뮤니케이션 구현

Socket.io는 실시간 양방향 이벤트 기반 통신을 가능하게 하는 라이브러리로, Nuxt.js에서 사용하기 위해서는 다음 단계를 따르면 됩니다.

1. Nuxt.js 프로젝트에 Socket.io를 설치합니다.
```bash
npm install socket.io-client
```

2. 컴포넌트에서 Socket.io를 import하여 사용합니다.
```javascript
import io from 'socket.io-client'

export default {
  created() {
    const socket = io('http://localhost:3000')
    socket.on('connect', () => {
      console.log('Socket.io 연결됨')
    })
  }
}
```

## WebSockets를 이용한 실시간 커뮤니케이션 구현

WebSockets은 TCP 기반의 네트워크 프로토콜로, Nuxt.js에서 사용하기 위해서는 다음 단계를 따르면 됩니다.

1. Nuxt.js 프로젝트에 웹 소켓 라이브러리를 설치합니다.
```bash
npm install ws
```

2. 컴포넌트에서 웹 소켓을 import하여 사용합니다.
```javascript
import WebSocket from 'ws'

export default {
  created() {
    const ws = new WebSocket('ws://localhost:3000')
    ws.onopen = () => {
      console.log('웹 소켓 연결됨')
    }
  }
}
```

## 마치며

위의 방법들을 통해 Nuxt.js에서도 간단하게 실시간 커뮤니케이션을 구현할 수 있습니다. 다만, **보안상의 이유**로 반드시 안전한 연결(SSL)을 고려해야 하며, **서버 측 구현**에도 유의해야 합니다.

이상으로 Nuxt.js에서의 실시간 커뮤니케이션(Socket.io, WebSockets) 구현 방법에 대해 살펴보았습니다.

참고: [Nuxt.js 공식 문서](https://nuxtjs.org/)