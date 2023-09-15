---
layout: post
title: "AngularJS에서 Two-way Data Binding을 구현하는 방법"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 데이터 바인딩을 통해 데이터 모델과 화면 간의 동기화를 쉽게 구현할 수 있는 프런트엔드 프레임워크입니다. Two-way Data Binding은 데이터 모델과 화면 간의 양방향 연결을 제공하여 변경된 데이터가 화면에 자동으로 반영되고, 화면에서의 입력이 데이터 모델에 자동으로 반영되는 기능입니다. 

Two-way Data Binding을 구현하기 위해 다음 단계를 따라 간단한 예제를 작성해보겠습니다.

## 1. HTML 템플릿 작성
```html
<div ng-app="myApp" ng-controller="myController">
  <label for="name">이름:</label>
  <input type="text" id="name" ng-model="name">
  <p>안녕하세요, {{name}}님!</p>
</div>
```
위의 코드는 AngularJS 앱의 루트 엘리먼트를 정의하고, 컨트롤러와 템플릿을 연결하는 역할을 합니다. `ng-app` 디렉티브는 앱의 이름을 정의하고, `ng-controller` 디렉티브는 컨트롤러를 설정합니다. `<input>` 요소는 `ng-model` 디렉티브를 사용하여 `name` 변수와 양방향 바인딩되도록 설정하는 역할을 합니다. `<p>` 요소는 `{{name}}`을 출력하여 변경된 데이터를 반영하는 역할을 합니다.

## 2. AngularJS 모듈 및 컨트롤러 정의
```javascript
var app = angular.module('myApp', []);

app.controller('myController', function($scope) {
  $scope.name = 'John Doe';
});
```
위의 코드는 AngularJS 모듈을 생성하고 `myApp`이라는 이름을 설정합니다. `controller` 메서드를 사용하여 `myController`라는 이름을 가진 컨트롤러를 정의합니다. 컨트롤러 함수는 `$scope` 객체를 매개변수로 받아 데이터 모델을 정의합니다. 위의 예제에서는 `name` 변수를 생성하여 초기값을 'John Doe'로 설정합니다.

## 3. 결과 확인하기
위의 코드를 작성하고 웹 브라우저에서 실행하면, '이름:' 레이블과 입력 필드가 나타나고, 입력한 값이 '안녕하세요, 입력한_값_님!' 메시지에 반영됩니다. 입력 필드에 새로운 값을 입력하면 메시지도 자동으로 업데이트됩니다.

AngularJS에서 Two-way Data Binding을 구현하는 방법에 대해 간단한 예제를 통해 알아보았습니다. 이 기능을 활용하면 화면과 데이터 모델 간의 동기화를 쉽게 처리할 수 있으며, 개발 생산성을 향상시킬 수 있습니다.

#AngularJS #TwoWayDataBinding