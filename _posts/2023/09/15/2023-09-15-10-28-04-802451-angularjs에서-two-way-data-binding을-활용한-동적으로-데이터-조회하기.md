---
layout: post
title: "AngularJS에서 Two-way Data Binding을 활용한 동적으로 데이터 조회하기"
description: " "
date: 2023-09-15
tags: [AngularJS]
comments: true
share: true
---

AngularJS는 웹 애플리케이션 개발을 위한 JavaScript 프레임워크로, 특히 데이터 바인딩 관련 기능으로 유명합니다. Two-way Data Binding은 AngularJS에서 제공하는 강력한 기능 중 하나로, 데이터의 변경 사항을 자동으로 감지하여 화면의 데이터와 모델의 데이터를 동기화시킵니다. 이를 통해 동적으로 데이터를 조회하고 업데이트할 수 있습니다.

## 데이터 바인딩 개념 이해하기

먼저 AngularJS에서의 데이터 바인딩 개념을 이해해야 합니다. AngularJS에서는 디렉티브(Directive)를 사용하여 HTML 요소와 AngularJS의 모델을 연결합니다. 디렉티브는 ng-model, ng-bind 등이 있는데, ng-model 디렉티브를 사용하면 HTML 요소의 값과 모델의 값을 양방향으로 바인딩할 수 있습니다.

## Two-way Data Binding을 사용하여 데이터 조회하기

예를 들어, 사용자 이름을 동적으로 조회하고 업데이트하는 기능을 구현해보겠습니다.

HTML에서는 다음과 같이 ng-model 디렉티브를 사용하여 input 요소와 모델을 바인딩합니다.

```html
<input type="text" ng-model="username">
```

AngularJS에서는 데이터를 조회하고 업데이트하는 로직을 컨트롤러(Controller)에서 작성합니다. 컨트롤러에서는 $scope 객체를 사용하여 모델을 관리할 수 있습니다. 다음과 같이 컨트롤러를 정의하고 데이터를 초기화하고 업데이트하는 함수를 작성합니다.

```javascript
var app = angular.module("myApp", []);
app.controller("myController", function($scope) {
  $scope.username = ""; // 초기값 설정

  $scope.fetchUserData = function() {
    // 데이터 조회 로직
    // ...
    $scope.username = "John Doe"; // 조회한 데이터를 모델에 설정
  };
});
```

이제 HTML에서 ng-click 디렉티브를 사용하여 버튼 클릭 시 fetchUserData 함수를 호출하도록 설정합니다.

```html
<div ng-app="myApp" ng-controller="myController">
  <input type="text" ng-model="username">
  <button ng-click="fetchUserData()">조회</button>
</div>
```

위 코드에서 ng-click 디렉티브를 사용하여 버튼 클릭 시 fetchUserData 함수가 호출되고, 해당 함수에서 데이터를 조회하여 $scope.username에 설정합니다. 이로써 input 요소의 값과 모델의 값이 동기화되어 사용자 이름이 동적으로 업데이트됩니다.

## 결론

AngularJS에서 Two-way Data Binding을 활용하여 동적으로 데이터를 조회하고 업데이트하는 방법을 살펴보았습니다. Two-way Data Binding을 사용하면 사용자 인터페이스와 데이터 모델 간의 관계를 편리하게 관리할 수 있으며, 웹 애플리케이션의 사용성과 개발 생산성을 크게 향상시킬 수 있습니다.

#AngularJS #TwoWayDataBinding