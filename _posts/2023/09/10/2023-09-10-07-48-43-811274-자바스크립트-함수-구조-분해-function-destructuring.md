---
layout: post
title: "자바스크립트 함수 구조 분해 (Function Destructuring)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

함수 구조 분해(Function Destructuring)는 자바스크립트에서 매우 유용한 기능 중 하나입니다. 이 기능은 함수의 파라미터로 전달된 객체나 배열의 속성을 간편하게 추출하는 데 사용됩니다. 이번 기사에서는 함수 구조 분해의 개념과 사용법에 대해 알아보겠습니다. 

## 함수 구조 분해를 사용하는 이유

함수 호출 시 전달되는 인자들은 종종 객체나 배열로 전달됩니다. 이때 객체나 배열의 특정 속성에 접근하기 위해서는 일반적으로 dot notation이나 array indexing을 사용해야 합니다. 이는 코드를 길고 복잡하게 만들 수 있습니다. 

함수 구조 분해를 사용하면 객체나 배열의 속성을 선언하는 것과 동일한 방법으로 추출할 수 있습니다. 이를 통해 코드의 가독성을 향상시키고 보다 간결하게 작성할 수 있습니다. 

## 객체 분해 (Object Destructuring)

아래의 예시 코드를 통해 객체 분해를 이해해 보겠습니다.

```javascript
function getUserInfo(user) {
  const { name, age, email } = user;
  console.log(`Name: ${name}`);
  console.log(`Age: ${age}`);
  console.log(`Email: ${email}`);
}

const user = {
  name: 'John Doe',
  age: 30,
  email: 'johndoe@example.com'
};

getUserInfo(user);
```

위의 코드에서는 `getUserInfo` 함수의 파라미터로 `user` 객체를 전달받습니다. 함수 내부에서는 `user` 객체의 `name`, `age`, `email` 속성을 추출하여 변수로 선언합니다. 

`const { name, age, email } = user;`와 같이 중괄호를 사용하여 추출할 속성을 선언하고, `user` 객체를 할당합니다. 이후 선언된 변수를 사용하여 각 속성의 값을 출력합니다.

## 배열 분해 (Array Destructuring)

배열의 경우도 객체와 비슷한 방식으로 분해할 수 있습니다. 다음의 예시 코드를 통해 배열 분해를 살펴보겠습니다.

```javascript
function getFirstAndLastNames(names) {
  const [firstName, , lastName] = names;
  console.log(`First Name: ${firstName}`);
  console.log(`Last Name: ${lastName}`);
}

const names = ['John', 'Doe', 'Smith'];

getFirstAndLastNames(names);
```

위의 코드에서는 `getFirstAndLastNames` 함수의 파라미터로 `names` 배열을 전달받습니다. 함수 내부에서는 `names` 배열의 첫 번째 요소와 세 번째 요소를 추출하여 변수로 선언합니다.

`const [firstName, , lastName] = names;`와 같이 대괄호 안에 추출할 요소의 위치를 비워두고 변수를 선언하면, 해당 위치의 요소를 할당받고, 무시하고자 하는 요소의 경우에는 비워둡니다.

## 기본값 설정 (Default Values)

함수 구조 분해의 또 다른 유용한 기능은 기본값 설정입니다. 만약 분해한 객체나 배열에서 값을 찾지 못한 경우, 기본값을 사용할 수 있습니다. 아래의 예시 코드를 통해 기본값 설정을 확인해 보세요.

```javascript
function getUserInfo(user) {
  const { name, age, email, gender = 'unknown' } = user;
  console.log(`Name: ${name}`);
  console.log(`Age: ${age}`);
  console.log(`Email: ${email}`);
  console.log(`Gender: ${gender}`);
}

const user = {
  name: 'Jane Doe',
  age: 25,
  email: 'janedoe@example.com'
};

getUserInfo(user);
```

위의 코드에서는 `gender` 속성의 기본값을 'unknown'으로 설정했습니다. 따라서 `user` 객체에 `gender` 속성이 없는 경우에는 'unknown'이 출력됩니다.

## 결론

자바스크립트의 함수 구조 분해는 코드를 더욱 간결하고 가독성 좋게 작성할 수 있는 유용한 기능입니다. 객체나 배열에서 원하는 속성을 쉽게 추출하고 기본값을 설정하는 등 다양한 상황에서 활용할 수 있습니다. 함수 구조 분해를 잘 활용하여 더 효율적인 코드 작성에 도전해 보세요.