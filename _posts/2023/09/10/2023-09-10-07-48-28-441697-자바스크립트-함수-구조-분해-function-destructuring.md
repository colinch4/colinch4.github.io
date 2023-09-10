---
layout: post
title: "자바스크립트 함수 구조 분해 (Function Destructuring)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서는 함수 구조 분해(Destructuring)라는 기능을 제공하여, 함수의 파라미터를 쉽게 분해할 수 있습니다. 이를 통해 코드의 가독성을 개선하고, 코드 작성을 더욱 편리하게 할 수 있습니다.

## 1. 기본 사용법

함수 구조 분해는 객체나 배열과 유사한 문법을 사용하여 함수 파라미터를 분해할 수 있습니다. 다음은 함수 구조 분해의 기본적인 사용법입니다.

```javascript
function getUserInfo(user) {
  const { name, age, email } = user;
  console.log(name, age, email);
}

const user = {
  name: 'John Doe',
  age: 25,
  email: 'johndoe@example.com'
};

getUserInfo(user); // John Doe 25 johndoe@example.com
```

위 코드에서 `getUserInfo` 함수는 `user` 객체를 파라미터로 받습니다. 함수 내부에서 `{ name, age, email }` 구조 분해를 사용하여 `user` 객체의 속성들을 변수로 할당하였습니다. 이후 `console.log`를 사용하여 변수들을 출력하였습니다.

## 2. 기본값 설정

함수 구조 분해를 사용하면, 파라미터의 기본값을 설정할 수도 있습니다. 파라미터에 기본값을 설정하면 해당 파라미터가 주어지지 않았을 때 기본값으로 설정됩니다.

```javascript
function getUserInfo({ name, age, email = 'N/A' }) {
  console.log(name, age, email);
}

const user = {
  name: 'John Doe',
  age: 25
};

getUserInfo(user); // John Doe 25 N/A
```

위 코드에서 `email` 속성은 기본값으로 `'N/A'`가 설정되어 있습니다. 만약 `user` 객체에 `email` 속성이 없다면, `email` 변수는 기본값으로 `'N/A'`가 됩니다.

## 3. 중첩된 객체 구조 분해

함수 구조 분해를 사용할 때 객체의 속성이 중첩되어 있는 경우, 중첩된 구조 분해도 가능합니다.

```javascript
function getProductDetails({ name, price, details: { description, stock } }) {
  console.log(name, price, description, stock);
}

const product = {
  name: 'iPhone 13',
  price: 999,
  details: {
    description: 'The latest iPhone model',
    stock: 100
  }
};

getProductDetails(product); // iPhone 13 999 The latest iPhone model 100
```

위 코드에서 `getProductDetails` 함수는 `product` 객체를 파라미터로 받습니다. 중첩된 구조 분해를 통해 `details` 객체의 `description`과 `stock` 속성을 변수로 할당하였습니다.

## 4. 배열 구조 분해

함수 구조 분해는 객체 뿐만 아니라, 배열에서도 사용할 수 있습니다. 배열 구조 분해는 배열의 요소를 변수에 할당하는 것입니다.

```javascript
function getFirstAndLastNames([firstName, lastName]) {
  console.log(firstName, lastName);
}

const names = ['John', 'Doe'];

getFirstAndLastNames(names); // John Doe
```

위 코드에서 `getFirstAndLastNames` 함수는 배열 `names`를 파라미터로 받습니다. 구조 분해를 통해 배열의 첫 번째 요소를 `firstName` 변수에, 두 번째 요소를 `lastName` 변수에 할당하였습니다.

## 마무리

자바스크립트 함수 구조 분해를 사용하면 복잡한 객체나 배열의 요소들을 쉽게 분해하여 사용할 수 있습니다. 이를 통해 코드의 가독성을 높이고, 작성하는 코드의 양을 줄일 수 있습니다. 함수 구조 분해를 잘 활용하여 효율적인 코드를 작성해보세요!