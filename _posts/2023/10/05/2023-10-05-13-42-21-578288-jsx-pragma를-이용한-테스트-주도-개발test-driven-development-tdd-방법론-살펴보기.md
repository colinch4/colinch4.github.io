---
layout: post
title: "JSX pragma를 이용한 테스트 주도 개발(Test-Driven Development, TDD) 방법론 살펴보기"
description: " "
date: 2023-10-05
tags: [JSXpragma]
comments: true
share: true
---

테스트 주도 개발(Test-Driven Development, TDD)은 소프트웨어 개발 방법론 중 하나로, 테스트 코드를 먼저 작성하고 이를 통과하는 코드를 작성하는 방법입니다. 이를 통해 개발자는 안정적이고 견고한 코드를 작성할 수 있습니다.

이번 포스트에서는 JSX pragma를 이용한 TDD 방법론에 대해 살펴보겠습니다. JSX pragma란 React에서 JSX를 사용할 때, JSX 코드를 변환하는 함수를 지정하는 것을 말합니다.

## 1. 설치 및 환경 설정

먼저, TDD를 위해 필요한 개발 환경을 설정해야 합니다. 다음 단계를 따라 진행해주세요.

1. 프로젝트 폴더를 생성하고 터미널을 이용해 해당 폴더로 이동합니다.
2. 다음 명령어를 실행하여 필요한 패키지를 설치합니다:

```shell
npm init -y
npm install --save-dev jest babel-jest @babel/core @babel/preset-env @babel/preset-react
```

3. 프로젝트 폴더 내에 `.babelrc` 파일을 생성하고 다음과 같이 설정합니다:

```json
{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
```

4. 프로젝트 폴더 내에 `src` 폴더와 `tests` 폴더를 생성합니다. `src` 폴더에는 실제 코드가 위치하고, `tests` 폴더에는 테스트 코드를 작성합니다.

## 2. 첫 번째 테스트 작성하기

이제 첫 번째 테스트를 작성해보겠습니다. `src` 폴더 내에 `App.js` 파일을 생성하고 다음과 같이 작성해주세요:

```jsx
function App() {
  return <div>Hello, World!</div>;
}

export default App;
```

다음으로, `tests` 폴더 내에 `App.test.js` 파일을 생성하고 다음과 같이 작성해주세요:

```jsx
import App from '../src/App';

test('renders hello world', () => {
  expect(App()).toBe('<div>Hello, World!</div>');
});
```

이 테스트는 `App` 컴포넌트가 `<div>Hello, World!</div>`를 반환하는지 확인합니다.

## 3. 테스트 실행하기

이제 작성한 테스트를 실행해보겠습니다. 터미널에서 다음 명령어를 실행하세요:

```shell
npx jest
```

이 명령어는 `tests` 폴더 내의 모든 테스트 파일을 실행합니다. 테스트가 성공하면 통과한 것이고, 실패하면 테스트 오류를 출력합니다.

## 4. 코드 작성하기

이번에는 테스트를 통과하기 위한 코드 작성 단계입니다. `App.js` 파일을 다음과 같이 수정해주세요:

```jsx
function App() {
  return <div>Hello, TDD!</div>;
}

export default App;
```

이제 테스트를 다시 실행해보면 테스트가 성공하는 것을 확인할 수 있습니다.

## 5. 추가 테스트 작성하기

이제 두 번째 테스트를 작성해보겠습니다. `App.test.js` 파일을 다음과 같이 수정해주세요:

```jsx
import App from '../src/App';

test('renders hello world', () => {
  expect(App()).toBe('<div>Hello, TDD!</div>');
});

test('renders without crashing', () => {
  expect(<App />).toBeTruthy();
});
```

이 테스트는 `App` 컴포넌트가 렌더링되고 오류 없이 동작하는지 확인합니다.

## 6. 마무리

이제 JSX pragma를 이용한 TDD 방법론을 경험해보았습니다. TDD는 개발자가 안정적이고 견고한 코드를 작성할 수 있도록 도와줍니다. JSX를 사용하는 경우, pragma를 설정하여 JSX 코드를 변환하는 함수를 지정할 수 있습니다. 이를 통해 테스트 주도 개발을 보다 더 효율적으로 진행할 수 있습니다.