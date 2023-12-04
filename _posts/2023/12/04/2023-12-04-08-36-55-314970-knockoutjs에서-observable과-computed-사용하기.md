---
layout: post
title: "[javascript] Knockout.js에서 Observable과 Computed 사용하기"
description: " "
date: 2023-12-04
tags: [javascript]
comments: true
share: true
---

Knockout.js는 JavaScript 기반의 MVVM(Model-View-ViewModel) 프레임워크로, UI와 데이터를 바인딩하기 위해 사용됩니다. 이 프레임워크에서는 observable과 computed라는 두 가지 핵심 기능을 제공합니다. 이 블로그 포스트에서는 Knockout.js의 observable과 computed를 사용하는 방법에 대해 알아보겠습니다.

## Observable

Observable은 데이터의 변경을 감지하고 자동으로 UI에 반영해주는 기능입니다. JavaScript 객체에 observable을 적용하면 해당 데이터가 변경될 때마다 알림을 받을 수 있습니다.

예를 들어, 다음과 같이 Person 객체를 생성하고 observable을 적용해보겠습니다.

```javascript
function Person(name, age) {
    this.name = ko.observable(name);
    this.age = ko.observable(age);
}

var person = new Person("John Doe", 25);

person.name(); // "John Doe"
person.name("Jane Doe");
person.name(); // "Jane Doe"
```

위의 예제에서 `Person` 객체의 `name` 속성과 `age` 속성을 observable로 선언하였습니다. `name` 속성의 값이 변경될 때마다 해당 값을 받을 수 있습니다.

## Computed

Computed는 observable을 기반으로 계산된 값을 반환하는 기능입니다. Computed는 의존하는 observable이 변경될 때마다 자동으로 새로운 값을 계산하고 반환합니다.

다음은 `Person` 객체에 `fullName`이라는 computed를 추가한 예제입니다.

```javascript
function Person(name, lastname) {
    this.name = ko.observable(name);
    this.lastname = ko.observable(lastname);
    
    this.fullName = ko.computed(function() {
        return this.name() + " " + this.lastname();
    }, this);
}

var person = new Person("John", "Doe");

person.fullName(); // "John Doe"
person.name("Jane");

person.fullName(); // "Jane Doe"
```

위의 예제에서 `fullName`은 `name`과 `lastname` observable에 의존하고 있으며, 이 값들이 변경될 때마다 새로운 fullName 값을 계산하여 반환합니다.

## 결론

Knockout.js의 observable과 computed는 UI와 데이터를 간단하고 효율적으로 바인딩하는데에 큰 도움을 줍니다. Observable은 데이터의 변경을 감지하고 자동으로 UI에 반영해주며, computed는 의존하는 데이터가 변경될 때마다 값을 계산하여 반환합니다. 이러한 기능을 적절히 활용하면 더 나은 사용자 경험을 제공할 수 있습니다.

더 자세한 내용은 Knockout.js 공식 문서를 참조해주세요.

- [Knockout.js 공식 문서](https://knockoutjs.com/documentation/introduction.html)