---
layout: post
title: "AngularJS의 ngModelController를 이용한 Two-way Data Binding 커스텀 디렉티브 구현 방법"
description: " "
date: 2023-09-15
tags: [javascript]
comments: true
share: true
---

## 개요
AngularJS는 두 개의 컴포넌트 간에 데이터 바인딩을 쉽게 구현할 수 있는 기능을 제공합니다. 이를 Two-way Data Binding이라고 부르며, 데이터의 변경이 자동으로 반영되는 효과를 얻을 수 있습니다. 이번 포스트에서는 AngularJS의 ngModelController를 이용하여 Two-way Data Binding을 구현하는 방법에 대해 알아보겠습니다.

## ngModelController란?
ngModelController는 AngularJS에서 폼 요소의 값을 추적하고 변경하는 컨트롤러입니다. AngularJS의 ngModel 디렉티브가 요소에 적용되면, 해당 요소에 대한 ngModelController 인스턴스가 생성됩니다. 이 컨트롤러를 이용하여 Two-way Data Binding을 구현할 수 있습니다.

## 커스텀 디렉티브 생성
먼저 AngularJS 애플리케이션에 커스텀 디렉티브를 생성해야 합니다. 커스텀 디렉티브는 일반적으로 AngularJS 모듈의 하위 모듈로 정의됩니다. 다음은 간단한 커스텀 디렉티브의 예입니다.

```javascript
angular.module('myApp', [])
  .directive('myInput', function() {
    return {
      restrict: 'E',
      require: 'ngModel',
      template: '<input type="text">',
      link: function(scope, element, attrs, ngModelCtrl) {
        // ngModelController를 이용한 Two-way Data Binding 구현
        ngModelCtrl.$render = function() {
          element.val(ngModelCtrl.$viewValue || '');
        };

        element.on('input', function() {
          scope.$apply(function() {
            ngModelCtrl.$setViewValue(element.val());
          });
        });

        ngModelCtrl.$parsers.push(function(value) {
          // 데이터의 유효성 검사 로직 작성
          return value;
        });

        ngModelCtrl.$formatters.push(function(value) {
          // 데이터의 포맷팅 로직 작성
          return value;
        });
      }
    };
  });
```

위 코드에서는 `myInput`이라는 커스텀 디렉티브를 정의하고 있습니다. `require` 속성을 사용하여 ngModelController를 요구하고, `link` 함수에서 Two-way Data Binding을 구현합니다.

`ngModelCtrl.$render` 함수는 모델의 변경이 일어날 때마다 호출되며, 입력 요소의 값을 업데이트합니다. `element.on('input')` 이벤트 처리기에서는 입력 요소의 값이 변경될 때마다 `$setViewValue` 함수를 호출하여 모델의 값을 업데이트합니다.

`$parsers` 배열은 입력 값을 모델 값으로 변환하는 함수의 배열입니다. 유효성 검사나 포맷팅 로직을 작성할 수 있습니다. 마찬가지로 `$formatters` 배열은 모델 값을 화면에 보여줄 때 포맷팅을 적용하는 함수의 배열입니다.

## 커스텀 디렉티브 사용
이제 위에서 생성한 커스텀 디렉티브를 사용해보겠습니다. 다음은 컨트롤러와 뷰의 예입니다.

```html
{% raw %}
<body ng-app="myApp" ng-controller="myController">
  <my-input ng-model="myData"></my-input>
  <p>입력된 값: {{ myData }}</p>
</body>
{% endraw %}
```

```javascript
angular.module('myApp', [])
  .controller('myController', function($scope) {
    // 초기값 설정
    $scope.myData = 'Hello, AngularJS!';
  });
```
{% raw %}
위 예제에서는 `<my-input>` 요소를 통해 커스텀 디렉티브를 사용하고 있습니다. `ng-model` 속성을 통해 Two-way Data Binding을 설정할 수 있으며, 입력된 값은 `myData`라는 변수에 자동으로 반영됩니다. `{{ myData }}`를 통해 현재 값을 표시할 수 있습니다.
{% endraw %}
## 결론
AngularJS의 ngModelController를 이용한 Two-way Data Binding 커스텀 디렉티브 구현 방법에 대해 알아보았습니다. 이를 통해 AngularJS 애플리케이션에서 간편하게 데이터 바인딩을 구현할 수 있으며, 사용자 입력에 따라 모델의 값을 유동적으로 업데이트할 수 있습니다.

#AngularJS #Two-WayDataBinding #CustomDirective