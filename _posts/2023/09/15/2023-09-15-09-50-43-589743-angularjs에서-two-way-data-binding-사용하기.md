---
layout: post
title: "AngularJS에서 Two-way Data Binding 사용하기"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 데이터의 양방향 바인딩(Two-way Data Binding) 기능을 제공하여 자동으로 모델과 뷰를 동기화할 수 있습니다. 이 기능을 사용하면 모델의 변경 사항이 자동으로 뷰에 반영되고, 사용자가 입력한 값이 모델에 바로 반영되는 편리함을 누릴 수 있습니다.

먼저, AngularJS 앱을 초기화하고 모듈을 정의해야 합니다. 다음 예제에서는 "myApp"이라는 모듈을 정의합니다.

```javascript
angular.module('myApp', []);
```

그리고 컨트롤러를 정의하고 해당 모듈에 연결해야 합니다. 컨트롤러는 데이터와 로직을 관리하는 역할을 합니다. 다음 예제에서는 "MainController"라는 컨트롤러를 정의하고 "myApp" 모듈에 연결합니다.

```javascript
angular.module('myApp').controller('MainController', function($scope) {
  $scope.message = "안녕하세요!";
});
```

이제 HTML에서 AngularJS의 템플릿 문법을 사용하여 Two-way Data Binding을 구현할 수 있습니다. `ng-model` 디렉티브를 사용하여 입력 요소에 모델을 바인딩하고, {{}} 중괄호를 사용하여 모델 값을 표시할 수 있습니다.

```html
<div ng-app="myApp" ng-controller="MainController">
  <input type="text" ng-model="message">
  <p>{{message}}</p>
</div>
```

위의 코드에서 `ng-model="message"` 부분은 입력 요소와 모델을 바인딩하는 부분입니다. 사용자가 입력한 값은 자동으로 "message" 변수에 할당됩니다. `{{message}}` 부분은 모델 값을 표시하는 부분입니다. 모델이 변경될 때마다 해당 부분이 자동으로 업데이트됩니다.

이제 웹 페이지를 열어보면 입력한 값이 실시간으로 반영되는 것을 확인할 수 있습니다. AngularJS의 Two-way Data Binding을 사용하면 모델과 뷰 간의 동기화를 간단하게 처리할 수 있습니다.

#AngularJS #TwoWayDataBinding