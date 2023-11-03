---
layout: post
title: "AngularJS의 ngModelOptions를 활용한 Two-way Data Binding 커스텀 디렉티브 구현 방법"
description: " "
date: 2023-09-15
tags: [AngularJS, ngModelOptions]
comments: true
share: true
---

AngularJS는 데이터 바인딩을 위해 ngModel 디렉티브를 제공합니다. 이 디렉티브를 사용하면 양방향 데이터 바인딩을 손쉽게 구현할 수 있습니다.
하지만 ngModel 디렉티브 자체로는 데이터 바인딩에 대한 세부 설정을 제공하지 않습니다. 이때 ngModelOptions를 활용하면 더 많은 컨트롤을 할 수 있습니다.

## ngModelOptions란?

ngModelOptions는 ngModel 디렉티브의 세부 설정을 제어하는 데 사용되는 옵션입니다. 이를 통해 데이터 변화를 감지하는 debounce, validation 처리, updateOn 옵션 등을 설정할 수 있습니다.

## 커스텀 디렉티브 구현 방법

커스텀 디렉티브를 사용하여 ngModelOptions를 활용한 양방향 데이터 바인딩을 구현해보겠습니다. 예시로 사용자가 입력한 값을 반전시켜서 표시하는 커스텀 디렉티브를 만들어보겠습니다.

```html
{% raw %}
<div ng-app="myApp" ng-controller="myController">
  <input type="text" ng-model="inputValue" my-directive ng-model-options="{ updateOn: 'blur' }">
  <p>The reversed value is: {{ reversedValue }}</p>
</div>
{% endraw %}
```

위 예제에서는 ng-model-options를 통해 데이터 갱신을 blur 이벤트에서만 수행하도록 설정했습니다. 그리고 `my-directive`라는 커스텀 디렉티브를 적용했습니다.

```javascript
var app = angular.module('myApp', []);

app.controller('myController', function($scope) {
  $scope.inputValue = 'Hello World';
});

app.directive('myDirective', function() {
  return {
    require: 'ngModel',
    link: function(scope, element, attrs, ngModelCtrl) {
      ngModelCtrl.$parsers.push(function(value) {
        return value.split('').reverse().join('');
      });
    }
  };
});
```

위 JavaScript 코드에서는 `my-directive`를 정의합니다. 이 디렉티브는 ngModel 디렉티브를 요구하며, `link` 함수를 통해 데이터 변환 작업을 수행합니다.
입력값을 받아서 문자열을 반전시켜주는 역할을 합니다.

이제 화면을 실행해보면 input 요소에 값을 입력할 때마다 역순으로 표시되는 것을 확인할 수 있습니다. 또한, 탭 이동으로 다른 요소로 포커스를 이동할 때에만 데이터가 갱신되는 것도 확인할 수 있습니다.

## 마무리

AngularJS의 ngModelOptions를 활용하면 편리한 데이터 바인딩을 구현할 수 있습니다. 커스텀 디렉티브를 사용하면 ngModelOptions를 더욱 유연하게 활용할 수 있습니다. 데이터 갱신의 타이밍을 설정하거나, 유효성 검사를 수행하는 등의 작업을 세밀하게 조정할 수 있습니다.

#AngularJS #ngModelOptions #데이터바인딩