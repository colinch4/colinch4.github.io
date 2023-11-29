---
layout: post
title: "[javascript] Marionette.js로 개발된 웹 애플리케이션의 디버깅(Debugging) 및 로깅(Logging) 방법은 어떤 것인가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

## 디버깅(Debugging)
Marionette.js는 기본적으로 Backbone.js의 기능을 확장하므로, Backbone.js 디버깅 도구를 사용해 Marionette.js 애플리케이션을 디버깅할 수 있습니다. 일반적인 웹 브라우저 개발자 도구인 Chrome 개발자 도구(Console 탭)를 사용하여 디버깅할 수 있습니다.

```javascript
// Marionette.js 애플리케이션의 모듈 로깅 활성화
Marionette.setLogger(console);

// 디버깅 용도로 로그 출력
MyApp.on('start', () => {
  MyApp.logger.debug('Application started');
});

// 특정 모듈의 로깅 활성화
MyApp.module('MyModule', (MyModule, MyApp, Backbone, Marionette, $, _) => {
  MyModule.logger = Marionette.getLogger('MyModule');
  
  MyModule.on('before:start', () => {
    MyModule.logger.debug('MyModule is about to start');
  });
});
```

디버깅 목적으로 로깅을 사용하는 경우, 개발자 도구의 콘솔을 통해 해당 로그를 확인할 수 있습니다.

## 로깅(Logging)
Marionette.js는 [Marionette.Application](https://marionettejs.com/docs/v4.1.0/marionette.application.html) 객체 내장 로깅 기능을 제공합니다. 이를 사용하여 애플리케이션 이벤트 및 모듈 동작에 대한 로그를 작성할 수 있습니다.

```javascript
const MyApp = new Marionette.Application();

MyApp.on('start', () => {
  MyApp.logger.log('Application started');
});

MyApp.module('MyModule', (MyModule, MyApp, Backbone, Marionette, $, _) => {
  MyModule.on('before:start', () => {
    MyApp.logger.log('MyModule is about to start');
  });
});
```

위 코드에서 `logger.log()`를 사용하여 로그를 작성하고, 필요에 따라 `logger.debug()`, `logger.info()`, `logger.warn()`, `logger.error()` 등을 사용할 수 있습니다. 로그는 디버깅 목적으로 사용될 수 있으며, 실시간으로 확인할 수 있는 개발자 도구의 콘솔을 통해 확인할 수 있습니다.

Marionette.js는 또한 [loglevel](https://github.com/pimterry/loglevel) 라이브러리를 이용한 로깅 시스템을 쉽게 통합할 수 있습니다. 자세한 내용은 [Marionette.js의 로깅 가이드](https://marionettejs.com/docs/v4.1.0/logger.html)를 참조하시기 바랍니다.

---

**참고 문서**
- [Marionette.js 공식 문서](https://marionettejs.com/docs/v4.1.0/)
- [Backbone.js 디버깅 가이드](https://backbonejs.org/#Events-debug)