---
layout: post
title: "[javascript] Jest에서의 의존성 모듈 주입(Dependency Injection) 테스트 방법은 어떻게 되는가?"
description: " "
date: 2023-11-24
tags: [javascript]
comments: true
share: true
---

# Jest에서의 의존성 모듈 주입(Dependency Injection) 테스트 방법

Jest는 JavaScript 애플리케이션 및 라이브러리를 테스트하기 위한 강력한 도구입니다. 의존성 모듈 주입(Dependency Injection)은 애플리케이션의 구성 요소들 사이에서 의존성을 주입하는 방식으로, 코드의 테스트 용이성과 재사용성을 향상시키는 데 도움이 됩니다. Jest에서도 의존성 모듈 주입을 테스트할 수 있는 방법을 제공하고 있습니다. 

## 모듈 모의(Mocking) 사용하기

의존성 모듈을 모킹(Mocking)하여 테스트를 수행할 수 있습니다. 예를 들어, 다음과 같이 모듈이 의존하는 모듈을 모의로 대체하여 테스트할 수 있습니다.

```javascript
// dependencies.js
export function getUser(id) {
  // ...
}

// user.js
import { getUser } from './dependencies';

export function getUserData(userId) {
  const user = getUser(userId);
  // ...
}
```

위의 예시에서 `getUser` 함수는 외부 모듈인 `dependencies.js` 에서 가져오는 함수입니다. 이 함수를 모의(Mock)해서 실제로 외부 서비스에 연결하지 않고도 테스트할 수 있습니다.

Jest에서는 `jest.mock` 함수를 사용하여 의존성 모듈을 모의할 수 있습니다.

```javascript
// user.test.js
import { getUserData } from './user';
import { getUser } from './dependencies';

jest.mock('./dependencies');

test('getUserData 함수가 getUser 함수를 호출하는지 확인', () => {
  getUserData(123);
  expect(getUser).toHaveBeenCalledWith(123);
});
```

위의 예시에서 `getUserData` 함수에서 `getUser` 함수를 호출하는지를 테스트하는 코드입니다. `jest.mock` 함수를 사용하여 `getUser` 함수를 모의(Mock)한 후, `getUserData` 함수를 호출하고 `getUser` 함수가 `123`과 함께 호출되었는지를 확인하고 있습니다.

## 실제 의존성 모듈 대신 모의 모듈 사용하기

의존성 모듈이 실제로 복잡한 로직을 포함하거나 외부 서비스에 의존할 경우, 모의(Mock) 모듈을 사용하여 모듈의 동작을 테스트하는 것이 좋습니다. Jest에서는 `jest.fn()` 함수를 사용하여 모의 모듈을 생성할 수 있습니다.

```javascript
// dependencies.js
export async function fetchData(url) {
  // ...
}

// data.js
import { fetchData } from './dependencies';

export async function getData() {
  const data = await fetchData('http://example.com');
  // ...
}
```

위의 예시에서 `fetchData` 함수는 외부 API에서 데이터를 가져오는 비동기 함수입니다. 이 함수의 동작을 테스트하기 위해 모의(Mock) 모듈을 사용할 수 있습니다.

```javascript
// data.test.js
import { getData } from './data';
import { fetchData } from './dependencies';

jest.mock('./dependencies');

describe('getData 함수', () => {
  test('fetchData 함수가 호출되는지 확인', async () => {
    fetchData.mockResolvedValue('mocked data');
    await getData();
    expect(fetchData).toHaveBeenCalledWith('http://example.com');
  });

  test('fetchData 함수의 반환값을 올바르게 처리하는지 확인', async () => {
    fetchData.mockResolvedValue('mocked data');
    const result = await getData();
    expect(result).toEqual('processed data');
  });
});
```

위의 예시에서 `getData` 함수를 테스트하는 코드입니다. `fetchData` 함수를 모의(Mock) 모듈로 대체하고, `fetchData` 함수가 호출되었는지와 반환값을 올바르게 처리하는지를 확인하고 있습니다.

## 마무리

Jest에서는 의존성 모듈 주입(Dependency Injection)을 테스트하기 위한 다양한 방법을 제공합니다. 의존성 모듈을 모킹(Mocking)하여 테스트할 수도 있고, 실제 의존성 모듈 대신 모의(Mock) 모듈을 사용하여 테스트할 수도 있습니다. 이러한 기능들을 활용하여 효과적이고 견고한 테스트 코드를 작성할 수 있습니다.

> 참고: 
> - [Jest 공식 문서](https://jestjs.io/)
> - [Jest Github 레포지토리](https://github.com/facebook/jest)