---
layout: post
title: "AngularJS의 $watch를 이용한 Two-way Data Binding 구현 방법"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 강력한 기능을 제공하는 JavaScript 기반 프런트엔드 프레임워크입니다. 그 중에서도 Two-way Data Binding은 데이터의 양방향 흐름을 쉽게 관리할 수 있는 중요한 기능 중 하나입니다. 이 기능을 활용하여 사용자 입력의 변화를 실시간으로 반영하거나, 데이터의 변경을 자동으로 화면에 업데이트하는 등 다양한 기능을 구현할 수 있습니다.

아래는 AngularJS의 $watch 메서드를 사용하여 Two-way Data Binding을 구현하는 방법을 설명한 예제 코드입니다.

```javascript
// AngularJS 애플리케이션 정의
var app = angular.module("myApp", []);

// 컨트롤러 정의
app.controller("myCtrl", function($scope) {
  $scope.name = "John"; // 초기 값 설정
  
  // $watch 메서드를 사용하여 name 변수의 변경을 감지
  $scope.$watch("name", function(newValue, oldValue) {
    // name이 변경될 때마다 실행되는 로직
    console.log("변경된 값:", newValue);
  });
});
```

위의 예제 코드에서는 AngularJS 애플리케이션을 정의하고, myCtrl이라는 컨트롤러를 생성합니다. 컨트롤러 안에서는 $scope 객체를 사용하여 데이터 바인딩을 관리합니다. 여기서는 name이라는 변수를 초기값 "John"으로 설정하고, $watch 메서드를 사용하여 name 변수의 변경을 감지합니다. $watch 메서드는 첫 번째 인자로 감시할 변수의 이름을 받고, 두 번째 인자로 변수가 변경될 때마다 실행될 콜백 함수를 전달합니다. 콜백 함수는 변경된 값(새로운 값)과 이전 값(이전 값)을 인자로 받아 로직을 실행할 수 있습니다.

위의 예제 코드를 실행하면, 웹 브라우저의 개발자 콘솔에서 name 변수의 값이 변경될 때마다 "변경된 값: [새로운 값]"이라는 로그가 출력됩니다. 이를 통해 Two-way Data Binding이 정상적으로 동작하고 있음을 확인할 수 있습니다.

AngularJS의 $watch를 이용한 Two-way Data Binding은 복잡한 데이터 연동을 쉽게 구현할 수 있는 강력한 도구입니다. 이를 활용하여 사용자와의 상호작용을 높이는 멋진 웹 애플리케이션을 개발할 수 있습니다.

#AngularJS #TwoWayDataBinding