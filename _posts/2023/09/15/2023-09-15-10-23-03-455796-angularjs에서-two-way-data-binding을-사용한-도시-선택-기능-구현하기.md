---
layout: post
title: "AngularJS에서 Two-way Data Binding을 사용한 도시 선택 기능 구현하기"
description: " "
date: 2023-09-15
tags: [angularjs]
comments: true
share: true
---

AngularJS는 동적 웹 애플리케이션을 구축하는 데 사용되는 JavaScript 프레임워크로, Two-way Data Binding 기능을 제공합니다. Two-way Data Binding은 데이터를 모델과 뷰 간에 자동으로 동기화시키는 기능으로, 모델의 값이 변경될 경우 뷰가 자동으로 업데이트되고, 뷰에서 입력된 값이 변경될 경우 모델이 자동으로 업데이트됩니다. 이를 활용하여 도시 선택 기능을 구현할 수 있습니다.

## 단계 1: AngularJS 라이브러리 추가하기

우선 AngularJS 라이브러리를 HTML 파일에 추가해야 합니다. 아래와 같이 `<script>` 태그를 이용하여 AngularJS 라이브러리를 가져옵니다. 또한, AngularJS 어플리케이션을 정의할 `<script>` 태그도 추가해야 합니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>도시 선택 기능</title>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
</head>
<body>
  <div ng-app="myApp" ng-controller="myCtrl">
    <!-- TODO: 도시 선택 기능 구현 -->
  </div>

  <script>
    var app = angular.module("myApp", []);
    app.controller("myCtrl", function($scope) {
      // TODO: 도시 데이터와 선택된 도시 변수 선언
    });
  </script>
</body>
</html>
```

## 단계 2: 도시 데이터와 선택된 도시 변수 선언하기

AngularJS 컨트롤러에서 도시 데이터와 선택된 도시를 저장할 변수를 선언해야 합니다. 아래와 같이 `$scope` 객체를 사용하여 도시 데이터와 선택된 도시를 선언합니다.

```javascript
app.controller("myCtrl", function($scope) {
  // 도시 데이터
  $scope.cities = [
    { name: "서울", id: 1 },
    { name: "부산", id: 2 },
    { name: "대구", id: 3 },
    { name: "인천", id: 4 },
    { name: "광주", id: 5 },
    { name: "대전", id: 6 }
  ];

  // 선택된 도시
  $scope.selectedCity = null;
});
```

## 단계 3: 도시 선택 기능 구현하기

이제 도시 선택 기능을 구현할 차례입니다. 아래와 같이 `<select>`와 `<option>` 태그를 사용하여 도시 목록을 표시하고 선택된 도시를 바인딩합니다.

```html
{% raw %}
<div ng-app="myApp" ng-controller="myCtrl">
  <select ng-model="selectedCity">
    <option ng-repeat="city in cities" value="{{city.id}}">{{city.name}}</option>
  </select>
  <p>선택된 도시: {{selectedCity}}</p>
</div>
{% endraw %}
```

위 코드에서 `ng-model` 디렉티브를 사용하면 선택된 도시를 `$scope.selectedCity` 변수에 양방향으로 바인딩할 수 있습니다. `ng-repeat` 디렉티브는 `cities` 배열을 순회하면서 도시 목록을 생성합니다.

## 단계 4: 실행해보기
{% raw %}
이제 HTML 파일을 브라우저에서 실행하면 도시 목록이 표시되고 선택된 도시를 확인할 수 있습니다. 선택된 도시가 변경되면 자동으로 `{{selectedCity}}` 부분이 업데이트됩니다.
{% endraw %}
위의 예시 코드를 웹 서버에 업로드하거나, 로컬에서 서버를 실행하여 도시 선택 기능을 확인해보세요.

## 결론

AngularJS에서 Two-way Data Binding을 활용하여 도시 선택 기능을 구현하는 방법에 대해 알아보았습니다. Two-way Data Binding은 데이터의 동기화를 자동으로 처리해주기 때문에 간편하고 효율적인 개발을 가능하게 합니다. AngularJS를 사용하여 다양한 동적 웹 애플리케이션을 구축할 수 있으며, Two-way Data Binding은 그 중에서도 가장 핵심적인 기능 중 하나입니다.

#AngularJS #TwoWayDataBinding