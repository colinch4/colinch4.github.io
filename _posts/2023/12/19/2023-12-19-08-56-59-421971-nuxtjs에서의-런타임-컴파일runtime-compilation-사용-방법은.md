---
layout: post
title: "[javascript] Nuxt.js에서의 런타임 컴파일(Runtime compilation) 사용 방법은?"
description: " "
date: 2023-12-19
tags: [javascript]
comments: true
share: true
---

## 런타임 컴파일(Runtime compilation)이란?

런타임 컴파일은 애플리케이션이 실행 중에 템플릿을 컴파일하는 방식입니다. 이것은 템플릿을 런타임에 JavaScript 렌더링 함수로 변환하기 때문에 서버 렌더링 시 컴파일된 코드를 클라이언트로 보낼 필요가 없어집니다.

### Nuxt.js에서 런타임 컴파일 사용 방법

Nuxt.js에서 런타임 컴파일을 사용하려면 `nuxt.config.js` 파일에 `build` 속성을 추가하고 `build` 속성 내부에 `runtimeCompiler`를 `true`로 설정합니다.

```javascript
// nuxt.config.js

export default {
  build: {
    runtimeCompiler: true
  }
}
```

위와 같이 설정하면 Nuxt.js는 런타임 컴파일을 사용하여 뷰 컴포넌트를 렌더링합니다.

이제 런타임 컴파일을 사용하여 Nuxt.js 애플리케이션을 구축할 수 있을 것입니다.

이상입니다. 도움이 되었기를 바랍니다. weitere Hilfe가 필요하시면 언제든지 물어보십시오!