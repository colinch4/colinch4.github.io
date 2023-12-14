---
layout: post
title: "AngularJS의 ng-checked 디렉티브와 컨트롤러 함수를 활용한 Two-way Data Binding 구현 방법"
description: " "
date: 2023-09-15
tags: [javascript]
comments: true
share: true
---

AngularJS는 자바스크립트 기반의 프론트엔드 프레임워크로, Two-way Data Binding 기능을 통해 모델과 뷰 간에 자동으로 데이터를 동기화할 수 있습니다. 이를 통해 사용자 입력이나 모델의 변경에 따라 뷰가 자동으로 업데이트되며, 반대로 뷰에서의 변경도 모델에 반영됩니다.

AngularJS에서 Two-way Data Binding을 구현하기 위해 ng-model 디렉티브를 주로 사용하지만, 특정 경우에는 ng-checked 디렉티브와 컨트롤러 함수를 함께 활용할 수도 있습니다. 이 방법을 사용하면 체크박스 등의 요소의 상태를 모델과 양방향으로 바인딩할 수 있습니다. 

아래는 ng-checked 디렉티브와 컨트롤러 함수를 활용하여 Two-way Data Binding을 구현하는 방법의 예시입니다.

## HTML

```html
{% raw %}
<div ng-app="myApp" ng-controller="myController">
    <label>
        <input type="checkbox" ng-checked="isChecked()" ng-click="toggleCheck()"> 체크박스
    </label>
    <p>체크 상태: {{checkboxChecked}}</p>
</div>
{% endraw %}
```

## JavaScript (AngularJS)

```javascript
angular.module('myApp', [])
  .controller('myController', function($scope) {
    $scope.checkboxChecked = false;
    
    $scope.isChecked = function() {
        return $scope.checkboxChecked;
    }
    
    $scope.toggleCheck = function() {
        $scope.checkboxChecked = !$scope.checkboxChecked;
    }
});
```

위 예시에서는 ng-checked 디렉티브를 사용하여 체크박스 요소의 상태를 isChecked() 함수에 의해 결정합니다. isChecked() 함수는 현재의 checkboxChecked 모델 값을 반환합니다. 또한 ng-click 디렉티브를 사용하여 toggleCheck() 함수를 트리거하여 checkboxChecked 값을 토글합니다. 이렇게 함으로써 체크박스의 선택 상태는 모델과 양방향으로 바인딩되어 업데이트됩니다.

이처럼 ng-checked 디렉티브와 컨트롤러 함수를 활용하여 AngularJS에서 Two-way Data Binding을 구현할 수 있습니다. 이러한 기능을 사용하면 사용자와의 상호작용에 따라 자동으로 모델과 뷰가 동기화되는 웹 애플리케이션을 개발할 수 있습니다.

#AngularJS #Two-wayDataBinding