---
layout: post
title: "npm 을 활용한 리팩토링 (Refactoring with npm)"
description: " "
date: 2023-11-10
tags: [npm]
comments: true
share: true
---

리팩토링은 소프트웨어의 기능을 변경하지 않고 코드의 구조를 개선하는 작업입니다. 이는 코드의 가독성을 향상시키고 유지보수를 용이하게 만들어줍니다. npm은 JavaScript 패키지 매니저로, 다양한 패키지를 설치하고 관리할 수 있는 도구입니다. npm을 활용하여 리팩토링을 더욱 효율적으로 수행할 수 있습니다.

## 패키지 설치

리팩토링을 시작하기 전에, npm을 사용하여 필요한 패키지를 설치해야 합니다. 예를 들어, 코드의 중복을 제거하기 위해 `lodash` 패키지를 사용하려고 한다면, 다음 명령어를 실행하여 해당 패키지를 설치할 수 있습니다:

```shell
npm install lodash
```

설치된 패키지는 `node_modules` 폴더에 저장되며, 프로젝트에서 사용할 수 있게 됩니다.

## 코드 리팩토링

이제 패키지가 설치되었으므로, 코드를 리팩토링할 준비가 되었습니다. 예를 들어, 배열 요소의 합을 계산하는 함수를 작성한다고 가정해봅시다:

```javascript
function sumArray(array) {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
}
```

위 코드는 동작은 잘하지만, 조금 더 간결하게 작성할 수 있습니다. `lodash` 패키지의 `sum` 함수를 사용하여 코드를 리팩토링해보겠습니다:

```javascript
const _ = require('lodash');

function sumArray(array) {
  return _.sum(array);
}
```

리팩토링 된 코드는 더욱 간단하고 가독성이 좋아졌습니다. 이렇게 `lodash` 패키지를 활용하여 리팩토링을 수행하면, 더욱 효율적으로 코드를 개선할 수 있습니다.

## 참고 자료

- [npm 공식 웹사이트](https://www.npmjs.com/)
- [lodash 패키지](https://lodash.com/)

#리팩토링 #npm