---
layout: post
title: "[nodejs] Node.js 기반 마이크로서비스 아키텍처에서의 컨테이너화 기술 (Docker, Kubernetes 등)"
description: " "
date: 2023-12-20
tags: [nodejs]
comments: true
share: true
---

마이크로서비스 아키텍처에서는 **컨테이너 기술**이 중요한 역할을 수행하여 서비스의 확장성과 유지보수성을 향상시키는 데 기여합니다. **Node.js** 기반의 마이크로서비스 아키텍처에서 **Docker**와 **Kubernetes** 같은 컨테이너화 기술의 적용은 매우 중요합니다.

## Docker를 이용한 컨테이너화

**Docker**는 마이크로서비스를 컨테이너로 패키징하고 배포할 수 있는 오픈 플랫폼입니다. Node.js 애플리케이션을 Docker 이미지로 빌드하고 실행할 수 있으며, 각 마이크로서비스를 독립적으로 컨테이너화하여 관리할 수 있습니다.

예를 들어, 다음은 Node.js로 작성된 간단한 웹 서버를 Docker 컨테이너로 만드는 예제입니다.

```javascript
// server.js
const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

```dockerfile
# Dockerfile
FROM node:14

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm install

COPY . /app/

EXPOSE 3000

CMD ["node", "server.js"]
```

## Kubernetes를 통한 컨테이너 오케스트레이션

**Kubernetes**는 컨테이너 오케스트레이션 플랫폼으로, 여러 대상 환경에서 컨테이너화된 애플리케이션을 배포, 확장 및 관리할 수 있습니다. Node.js 기반의 마이크로서비스를 Kubernetes에서 실행하면, **자동 확장**과 **자가치유** 같은 장점을 누릴 수 있습니다.

다음은 Kubernetes에서 Node.js 애플리케이션을 배포하는 간단한 예제입니다.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nodejs-app
  labels:
    app: nodejs
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nodejs
  template:
    metadata:
      labels:
        app: nodejs
    spec:
      containers:
        - name: nodejs
          image: your-registry/nodejs-app
          ports:
            - containerPort: 3000
```

이러한 방식으로 Node.js 기반의 마이크로서비스를 컨테이너화하여 Docker와 Kubernetes를 통해 관리함으로써, 유연하고 안정적인 마이크로서비스 아키텍처를 구축할 수 있습니다.

마이크로서비스 아키텍처에서의 컨테이너화 기술에 대한 세부 사항은 [여기](https://kubernetes.io/docs/home/)에서 더 읽어볼 수 있습니다.