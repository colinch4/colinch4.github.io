---
layout: post
title: "[javascript] Marionette.js에서 데이터 검증(Validation)과 에러 처리(Error Handling)를 다루는 방법은 무엇인가?"
description: " "
date: 2023-11-29
tags: [javascript]
comments: true
share: true
---

## 데이터 검증(Validation)
Marionette.js는 모델(Model)과 컬렉션(Collection)에 내장된 검증기(Validator)를 활용하여 데이터의 유효성을 검사할 수 있습니다. 모델이나 컬렉션에 검증 규칙을 정의한 후, 데이터를 설정할 때마다 자동으로 검증이 수행됩니다.

아래는 Marionette.js에서 데이터 검증을 설정하는 예시입니다:

```javascript
const MyModel = Backbone.Model.extend({
  validation: {
    name: {
      required: true,
      minLength: 3,
      maxLength: 50
    },
    age: {
      range: [18, 65]
    }
  }
});
```

위 코드에서 `name` 필드는 필수(required)이고 최소길이(minLength)는 3, 최대길이(maxLength)는 50으로 설정되었습니다. `age` 필드는 범위(range)가 18부터 65까지로 설정되었습니다.

데이터를 설정할 때, Marionette.js는 내장된 검증기를 사용하여 데이터의 유효성을 검사합니다. 검증이 실패할 경우, `validate` 이벤트가 트리거되고 유효성 검증 함수가 실행됩니다. 유효성 검증 함수에서는 `validations` 객체를 이용하여 검증 결과를 확인할 수 있습니다.

```javascript
const myModel = new MyModel();

myModel.set({
  name: "John",
  age: 25
});

myModel.on("validate", function(model, error) {
  if (error) {
    console.log(error); // 유효성 검증 에러 메시지 출력
  }
});
```

위 코드에서 `myModel` 인스턴스를 생성한 후 `set` 메서드를 사용하여 데이터를 설정합니다. 데이터가 검증될 때 `validate` 이벤트가 트리거되어 유효성 검증 함수가 실행됩니다. 유효성 검증이 실패할 경우 에러 메시지가 출력됩니다.

## 에러 처리(Error Handling)
Marionette.js는 Ajax 요청, 이벤트 처리, 모델과 컬렉션의 상태 변화 등 다양한 상황에서 발생하는 에러를 처리할 수 있는 메커니즘을 제공합니다.

아래는 Ajax 요청에서 에러를 처리하는 예시입니다:

```javascript
const MyModel = Backbone.Model.extend({
  url: "api/my-model",
  error(model, xhr, options) {
    console.log("에러 발생:", xhr.status);
  }
});

const myModel = new MyModel();

myModel.save();
```

위 코드에서 `MyModel`은 `url`을 지정하여 서버로부터 데이터를 가져옵니다. 만약 Ajax 요청이 실패하면 `error` 메서드가 호출되어 에러를 처리합니다. 위 예시에서는 단순히 에러 상태 코드를 콘솔에 출력하도록 설정되었습니다.

Marionette.js는 이벤트 처리나 모델과 컬렉션의 상태 변화에 따라 발생하는 다양한 상황에서 에러를 처리할 수 있는 메커니즘을 제공합니다. 이를 활용하여 애플리케이션에서 발생하는 에러를 적절하게 처리할 수 있습니다.

Marionette.js 공식 문서에서 더 자세한 내용을 확인할 수 있습니다 [(링크)](https://marionettejs.com/docs/v4.1.0/)