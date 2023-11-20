---
layout: post
title: "AngularJS의 ng-model 디렉티브를 이용한 Two-way Data Binding 이해하기"
description: " "
date: 2023-09-15
tags: [angularjs]
comments: true
share: true
---

AngularJS는 웹 개발에서 인기 있는 JavaScript 프레임워크 중 하나입니다. 이 프레임워크는 데이터와 사용자 인터페이스 간의 상호작용을 간소화하기 위해 다양한 디렉티브를 제공합니다. 그 중 ng-model 디렉티브는 Two-way Data Binding을 구현하는데 사용됩니다.

## Two-way Data Binding이란?

Two-way Data Binding은 데이터의 변경이 반영되는 동시에 사용자 인터페이스에 반영되고, 반대로 사용자 인터페이스의 변경이 데이터에도 반영되는 것을 의미합니다. 이는 개발자가 데이터와 UI를 동기화하는 작업을 간소화하고 생산성을 향상시킵니다.

## ng-model 디렉티브의 사용법

ng-model 디렉티브는 주로 폼 요소(input, select, textarea 등)와 함께 사용됩니다. 아래는 ng-model 디렉티브를 사용한 예시 코드입니다.

```html
{% raw %}
<!DOCTYPE html>
<html ng-app="myApp">
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
  </head>
  <body>
    <div ng-controller="myController">
      <input type="text" ng-model="message">
      <p>{{ message }}</p>
    </div>

    <script>
      var app = angular.module("myApp", []);
      app.controller("myController", function($scope) {
        $scope.message = "Hello, AngularJS!";
      });
    </script>
  </body>
</html>
{% endraw %}
```
{% raw %}
위 코드에서 input 요소에 ng-model 디렉티브를 사용하고, p 요소에서는 {{ message }}를 사용하여 데이터 바인딩을 수행합니다.
{% endraw %}
## 결과 확인하기

위 코드를 실행하면 사용자가 input 요소에 텍스트를 입력할 때마다 그 내용이 바로 아래의 p 태그에 표시됩니다. 이는 ng-model 디렉티브를 통해 입력한 값을 데이터에 반영하고, 데이터의 변경이 사용자 인터페이스에도 반영되기 때문입니다.

## 결론

AngularJS의 ng-model 디렉티브를 사용하면 Two-way Data Binding을 쉽게 구현할 수 있습니다. 이를 통해 개발자는 데이터와 UI를 동기화하는 작업에 신경 쓰지 않고 개발에 집중할 수 있습니다. #AngularJS #Two-wayDataBinding