---
layout: post
title: "자바스크립트 함수의 독립성과 결합도 (Independence and Coupling of Functions)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

자바스크립트에서 함수는 코드를 구조화하고 재사용 가능한 블록으로 만들어주는 중요한 역할을 합니다. 함수의 독립성과 결합도는 코드의 유지 보수성, 가독성 및 확장성에 큰 영향을 미치는 중요한 개념입니다. 이 블로그 포스트에서는 자바스크립트 함수의 독립성과 결합도에 대해 자세히 알아보겠습니다.

## 함수의 독립성 (Independence of Functions)

함수의 독립성은 함수가 다른 코드와 독립적으로 작동할 수 있는 정도를 나타냅니다. 독립적인 함수는 함수를 다른 곳에서 호출하거나 재사용하기 쉽게 만들어줍니다. 이는 코드의 유지 보수성과 재사용성을 높여줍니다. 

독립적인 함수를 작성하는 것은 몇 가지 원칙을 따라야 합니다.

1. **단일 책임 원칙 (Single Responsibility Principle)**: 각 함수는 한 가지 기능만을 수행해야 합니다. 이렇게 하면 함수가 더 작고 읽기 쉽게 만들어집니다.

```javascript
// 잘못된 예시
function calculatePriceAndSendEmail(product) {
  // 상품 가격 계산 로직...
  // 이메일 전송 로직...
}

// 올바른 예시
function calculatePrice(product) {
  // 상품 가격 계산 로직...
}

function sendEmail(product) {
  // 이메일 전송 로직...
}
```

2. **의존성 주입 (Dependency Injection)**: 함수가 다른 함수나 객체에 의존하지 않도록 만들어야 합니다. 이렇게 하면 함수를 다른 환경에서 테스트하거나 재사용하기 쉽게 만들어집니다.

```javascript
// 잘못된 예시
function calculateDiscountedPrice(product) {
  // 상품 가격 계산 로직...
  const discount = getDiscount(); // 다른 함수에 의존
  // 할인 가격 계산 로직...
}

// 올바른 예시
function calculateDiscountedPrice(product, discount) {
  // 상품 가격 계산 로직...
  // 할인 가격 계산 로직...
}
```

3. **부작용 최소화 (Minimizing Side Effects)**: 함수는 외부 상태를 변경하지 않거나 최소한으로 변경해야 합니다. 이렇게 하면 함수의 동작을 예측하기 쉽고 디버깅이 용이해집니다.

```javascript
// 잘못된 예시
function updateProductPrice(product) {
  // 상품 가격 변경 로직...
  product.price = calculatePrice(product); // 외부 상태 변경
}

// 올바른 예시
function calculateUpdatedPrice(product) {
  // 상품 가격 계산 로직...
  return updatedPrice;
}

function updateProductPrice(product) {
  const updatedPrice = calculateUpdatedPrice(product);
  // 상품 가격 업데이트 로직...
}
```

## 함수의 결합도 (Coupling of Functions)

결합도는 함수 간의 의존성 정도를 나타내며, 함수 간의 결합도가 높을수록 코드 유지 보수성이 저하될 수 있습니다. 따라서 결합도를 최소화하는 것이 중요합니다. 

결합도를 최소화하는 방법은 다음과 같습니다.

1. **인터페이스 정의 (Defining Interfaces)**: 함수 간의 인터페이스를 정의하여 의존성을 명확하게 만듭니다. 이렇게 하면 함수의 변경이 다른 함수에 영향을 덜 줄 수 있습니다.

```javascript
// 상품 가격을 계산하는 함수
function calculatePrice(product) {
  // 상품 가격 계산 로직...
}

// 인터페이스 정의
function calculatePrice(product) {
  // 상품 가격 계산 로직...
}

// 상품 가격을 사용하는 함수
function processProductPrice(product) {
  // 상품 가격 사용 로직...
}
```

2. **의존성 역전 (Dependency Inversion)**: 함수 간의 의존성을 역전시켜 결합도를 낮춥니다. 의존성 역전은 인터페이스를 사용하여 함수가 직접적으로 다른 함수에 의존하지 않도록 만듭니다.

```javascript
// 상품 가격을 계산하는 함수
function calculatePrice(product) {
  // 상품 가격 계산 로직...
}

// 의존성 역전을 이용한 호출
function processProductPrice(product, calculator) {
  const price = calculator.calculatePrice(product);
  // 상품 가격 사용 로직...
}

// 의존성 주입
processProductPrice(product, { calculatePrice });
```

3. **이벤트 중심 아키텍처 (Event-driven Architecture)**: 함수 간의 직접적인 호출을 피하고 이벤트를 통해 통신하도록 만듭니다. 이렇게 하면 결합도를 낮출 수 있습니다.

```javascript
// 이벤트 리스너 등록
eventEmitter.on('productPriceCalculated', function(price) {
  // 상품 가격을 사용하는 로직...
});

// 상품 가격 계산
function calculatePrice(product) {
  // 상품 가격 계산 로직...
  // 가격 계산 결과를 이벤트로 발송
  eventEmitter.emit('productPriceCalculated', price);
}
```