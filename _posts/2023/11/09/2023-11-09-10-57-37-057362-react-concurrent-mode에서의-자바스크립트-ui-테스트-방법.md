---
layout: post
title: "React Concurrent Mode에서의 자바스크립트 UI 테스트 방법"
description: " "
date: 2023-11-09
tags: [React]
comments: true
share: true
---

React Concurrent Mode는 React 애플리케이션의 성능을 향상시키는 새로운 기능입니다. 이러한 모드에서 UI를 테스트하는 방법에 대해 알아보겠습니다.

## 1. Jest와 React Testing Library 사용하기

Jest와 React Testing Library는 React 애플리케이션의 테스트에 널리 사용되는 도구입니다. 이들 도구를 사용하여 React Concurrent Mode에서 UI 테스트를 작성할 수 있습니다. 다음은 사용 예시입니다.

```javascript
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders app component', async () => {
  render(<App />);
  
  const appElement = await screen.findByText(/Welcome to my app/i);
  expect(appElement).toBeInTheDocument();
});
```

위의 코드에서는 `render` 함수를 사용하여 `App` 컴포넌트를 렌더링하고, `screen.findByText` 함수를 사용하여 특정 텍스트를 가진 엘리먼트를 찾습니다. 그리고 `expect` 함수를 사용하여 해당 엘리먼트가 문서에 존재하는지를 검증합니다.

## 2. React Testing Library의 waitFor 함수 사용하기

React Concurrent Mode에서는 코드가 비동기적이므로, 테스트를 작성할 때 일부 UI 변경 작업이 완료되기를 기다려야 할 수 있습니다. 이 경우, React Testing Library의 `waitFor` 함수를 사용할 수 있습니다. 다음은 사용 예시입니다.

```javascript
import { render, screen, waitFor } from '@testing-library/react';
import App from './App';

test('renders data after fetching', async () => {
  render(<App />);
  
  const loadingElement = screen.getByText(/Loading.../i);
  expect(loadingElement).toBeInTheDocument();
  
  await waitFor(() => {
    const dataElement = screen.getByText(/Data: Hello World/i);
    expect(dataElement).toBeInTheDocument();
  });
});
```

위의 코드에서는 `waitFor` 함수를 사용하여 특정 조건이 충족될 때까지 기다립니다. 이 예시에서는 "Data: Hello World" 텍스트가 화면에 나타날 때까지 기다리도록 설정되어 있습니다.

## 3. act 함수 사용하기

React Concurrent Mode에서는 UI 업데이트가 비동기적으로 처리됩니다. 따라서, 테스트 중에 UI 상태 변경에 대한 액션을 수행하고자 할 때는 React Testing Library의 `act` 함수를 사용해야 합니다. 다음은 사용 예시입니다.

```javascript
import { render, screen, act } from '@testing-library/react';
import App from './App';

test('renders updated text after clicking button', async () => {
  render(<App />);

  const buttonElement = screen.getByRole('button');
  act(() => {
    buttonElement.click();
  });

  const updatedTextElement = await screen.findByText(/Updated Text/i);
  expect(updatedTextElement).toBeInTheDocument();
});
```

위의 코드에서는 `act` 함수를 사용하여 버튼 클릭과 같은 액션을 수행합니다. 이를 통해 테스트할 때 발생하는 비동기적인 UI 업데이트를 동기적으로 처리할 수 있습니다.

## 4. React Testing Library의 async 함수 사용하기

React Testing Library는 테스트할 때 자동으로 async 및 await를 처리할 수 있는 `async` 함수를 제공합니다. 이를 사용하면 비동기적으로 동작하는 테스트를 간편하게 작성할 수 있습니다. 다음은 사용 예시입니다.

```javascript
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import App from './App';

test('renders updated text after fetching data', async () => {
  render(<App />);

  const loadingElement = screen.getByText(/Loading.../i);
  expect(loadingElement).toBeInTheDocument();

  await waitForElementToBeRemoved(() => screen.getByText(/Loading.../i));

  const dataElement = screen.getByText(/Data: Hello World/i);
  expect(dataElement).toBeInTheDocument();
});
```

위의 코드에서는 `waitForElementToBeRemoved` 함수를 사용하여 "Loading..." 텍스트가 화면에서 사라질 때까지 기다립니다. 그리고 "Data: Hello World" 텍스트가 나타나는지 검증합니다.

React Concurrent Mode에서의 자바스크립트 UI 테스트 방법에 대해 알아보았습니다. Jest와 React Testing Library를 활용하여 효율적으로 테스트를 작성할 수 있습니다. #React #테스트