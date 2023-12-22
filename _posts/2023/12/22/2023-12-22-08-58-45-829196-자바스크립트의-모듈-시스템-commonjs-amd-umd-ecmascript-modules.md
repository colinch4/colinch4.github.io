---
layout: post
title: "[javascript] 자바스크립트의 모듈 시스템: CommonJS, AMD, UMD, ECMAScript Modules"
description: " "
date: 2023-12-22
tags: [javascript]
comments: true
share: true
---

자바스크립트는 모듈을 사용하여 코드를 구성하고 관리하는 데 사용되는 다양한 시스템을 가지고 있습니다. 이러한 다양한 모듈 시스템들은 개발자들이 코드를 구조화하고 재사용 가능한 모듈로 나누는 데 도움을 줍니다. 이 글에서는 CommonJS, AMD, UMD, 그리고 최신 ECMAScript Modules에 대해 알아보겠습니다.

## CommonJS
CommonJS는 노드.js(Node.js)에서 사용되는 모듈 시스템으로, 동기적인 방식으로 모듈을 로딩하고 가져옵니다. CommonJS 스타일 모듈은 `module.exports`를 사용하여 모듈을 정의하고 내보내며, `require` 함수를 사용하여 다른 모듈을 가져옵니다. 이 스펙은 브라우저 환경에서는 바로 동작하지 않을 수 있지만, 번들러(bundler)를 사용하여 사용 가능하게 할 수 있습니다.

```javascript
// 모듈 정의
// math.js
function add(a, b) {
  return a + b;
}
module.exports = { add };

// 모듈 가져오기
// app.js
const { add } = require('./math');
console.log(add(2, 3)); // 5
```

## AMD
Asynchronous Module Definition(Asynchronous 모듈 정의)은 브라우저 환경의 모듈 로딩을 비동기적으로 하기 위한 표준입니다. 주로 RequireJS와 함께 사용되며, `define` 함수로 모듈을 정의하고 `require` 함수로 모듈을 가져옵니다. 이 방식은 외부 종속성이 있는 웹 애플리케이션에서 유용합니다.

```javascript
// 모듈 정의
// math.js
define(function() {
  return {
    add: function(a, b) {
      return a + b;
    }
  };
});

// 모듈 가져오기
// app.js
require(['math'], function(math) {
  console.log(math.add(2, 3)); // 5
});
```

## UMD
Universal Module Definition(유니버설 모듈 정의)은 CommonJS와 AMD를 함께 지원하는 중립적인 모듈 시스템입니다. UMD는 먼저 CommonJS 방식으로 모듈을 로딩하고, 그 후에 AMD 방식으로 모듈을 로딩합니다. 이 모듈 시스템은 모든 환경에서 사용 가능하며, 브라우저, 노드, AMD, CommonJS 등에서 모두 동작합니다.

```javascript
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD 환경
        define(['exports'], factory);
    } else if (typeof exports === 'object') {
        // CommonJS/Node.js 환경
        module.exports = factory();
    } else {
        // 브라우저 환경
        root.returnExports = factory();
    }
}(this, function () {
    return {
        add: function(a, b) {
            return a + b;
        }
    };
}));
```

## ECMAScript Modules
ECMAScript 6부터 지원되는 ECMAScript Modules은 자바스크립트의 내장 모듈 시스템입니다. `import`와 `export` 문을 사용하여 모듈을 정의하고 내보내며, 파일 확장자를 통해 모듈을 가져옵니다. 이 모듈 시스템은 브라우저 및 모던 런타임 환경에서 기본적으로 지원됩니다.

```javascript
// 모듈 정의
// math.mjs
export function add(a, b) {
  return a + b;
}

// 모듈 가져오기
// app.mjs
import { add } from './math';
console.log(add(2, 3)); // 5
```

자바스크립트의 모듈 시스템에는 CommonJS, AMD, UMD, 그리고 ECMAScript Modules이 있으며, 각각의 모듈 시스템은 다른 환경에서 사용되는데 유용합니다.

참고 자료: 
- [MDN 웹 문서 - ECMAScript Modules](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Modules)
- [Modules | Node.js Documentation](https://nodejs.org/api/modules.html)
- [Asynchronous Module Definition - RequireJS](https://requirejs.org/docs/whyamd.html)
- [npm - UMD(Universal Module Definition)](https://www.npmjs.com/package/umd)