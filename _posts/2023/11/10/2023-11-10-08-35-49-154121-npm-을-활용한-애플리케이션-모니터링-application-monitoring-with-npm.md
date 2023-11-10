---
layout: post
title: "npm 을 활용한 애플리케이션 모니터링 (Application monitoring with npm)"
description: " "
date: 2023-11-10
tags: []
comments: true
share: true
---

모든 개발자들은 자신의 애플리케이션의 성능을 모니터링하고 최적화하는 것이 중요하다는 것을 알고 있습니다. 이러한 작업을 수행하기 위해 여러 도구와 서비스가 있지만, npm을 활용하여 간편하게 애플리케이션 모니터링을 할 수도 있습니다.

## npm 모듈 설치

먼저, 애플리케이션 모니터링을 위해 npm에서 제공하는 모듈을 설치해야 합니다. 여러 가지 선택지가 있지만, 아래의 모듈들을 설치하는 것을 추천합니다.

1. [**express-status-monitor**](https://www.npmjs.com/package/express-status-monitor): Express 애플리케이션의 상태를 모니터링하는 데 사용됩니다.
2. [**pm2**](https://www.npmjs.com/package/pm2): 프로세스 관리자로, 애플리케이션의 실행 및 모니터링을 쉽게 할 수 있습니다.

이제 `npm`을 사용하여 모듈들을 설치해보겠습니다. 아래의 커맨드를 터미널에 입력하세요.

```
npm install express-status-monitor pm2
```

## express-status-monitor 설정

1. Express 애플리케이션의 `app.js` 파일을 열고, 다음의 코드를 추가합니다.

```javascript
const express = require('express');
const statusMonitor = require('express-status-monitor');

const app = express();

app.use(statusMonitor());
```

2. 애플리케이션을 실행한 뒤 브라우저에서 `http://localhost:3000/status`로 접속해보세요. 여기서 애플리케이션의 상태와 성능을 확인할 수 있습니다.

## pm2 설정

1. `pm2`를 사용하여 애플리케이션을 실행 및 모니터링하기 위해, 아래의 커맨드를 터미널에 입력하세요.

```
pm2 start app.js
```

2. 애플리케이션을 실행한 후, `pm2`로 애플리케이션의 상태를 확인할 수 있습니다.

```
pm2 status
```

3. 추가적으로, 애플리케이션의 로그를 확인하거나 앱을 재시작하는 등의 작업도 `pm2`를 통해 실행할 수 있습니다.

## 결론

이제 애플리케이션 모니터링을 위해 npm을 활용하는 방법을 배웠습니다. `express-status-monitor`와 `pm2`를 사용하여 애플리케이션의 상태 및 성능을 쉽게 모니터링할 수 있습니다. 이러한 모듈들을 적절하게 활용하면 애플리케이션의 성능 최적화 및 문제 해결에 도움이 될 것입니다.

### 참고 자료

- [express-status-monitor npm 모듈](https://www.npmjs.com/package/express-status-monitor)
- [pm2 npm 모듈](https://www.npmjs.com/package/pm2)

#npm #모니터링