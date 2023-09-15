---
layout: post
title: "AngularJS의 ng-change 디렉티브와 컨트롤러 함수를 이용한 Two-way Data Binding 변경 이벤트 처리 방법"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 클라이언트 측 웹 애플리케이션을 개발하는 데 사용되는 JavaScript 프레임워크입니다. 이 프레임워크는 UI와 데이터 간의 동적인 관계를 구축하기 위해 Two-way Data Binding 기능을 제공합니다. 이 기능을 사용하면 데이터의 변경이 UI에 자동으로 반영되고, UI에서의 변경도 데이터에 반영됩니다.

그 중에서도 `ng-change` 디렉티브는 사용자 입력 요소 (input, select, checkbox 등)의 값이 변경될 때 호출되는 이벤트 핸들러를 정의하는 데 사용됩니다. 이 디렉티브를 사용하여 Two-way Data Binding에서 데이터 변경이 발생했을 때 원하는 작업을 수행할 수 있습니다.

```html
<input type="text" ng-model="name" ng-change="handleChange()">
```

위의 예제 코드에서는 `ng-model` 디렉티브를 사용하여 `name` 변수와 입력 요소를 바인딩하고, `ng-change` 디렉티브를 사용하여 `handleChange()` 함수를 호출하도록 설정했습니다.

```javascript
app.controller('MyCtrl', function($scope) {
  $scope.name = '';

  $scope.handleChange = function() {
    console.log('Name changed: ' + $scope.name);
    // 데이터 변경 이벤트 처리 로직 추가
  };
});
```

위의 예제 코드에서는 AngularJS 컨트롤러를 사용하여 `$scope` 객체를 생성하고, `name` 변수를 초기화합니다. 그리고 `handleChange()` 함수를 정의하여 데이터 변경 이벤트가 발생할 때 수행할 작업을 구현했습니다. 예제에서는 단순히 콘솔에 변경된 이름을 출력하는 로직을 추가했습니다.

위의 예제 코드를 실행하면 입력 요소의 값이 변경될 때마다 `handleChange()` 함수가 호출되고, 변경된 이름이 콘솔에 출력됩니다. 이제 `handleChange()` 함수 내부에서 필요한 작업을 수행하면 됩니다.

이와 같이 AngularJS의 `ng-change` 디렉티브와 컨트롤러 함수를 이용하면 Two-way Data Binding에서 데이터의 변경을 감지하고, 필요한 작업을 처리할 수 있습니다. 이를 통해 사용자 인터페이스와 데이터 간의 실시간 동기화를 간편하게 구현할 수 있습니다.

#AngularJS #TwoWayDataBinding