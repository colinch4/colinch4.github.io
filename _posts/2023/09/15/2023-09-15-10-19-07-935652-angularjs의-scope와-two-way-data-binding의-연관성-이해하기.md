---
layout: post
title: "AngularJS의 $scope와 Two-way Data Binding의 연관성 이해하기"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 개발자들에게 데이터 바인딩을 통한 빠른 개발을 제공하기 위해 설계된 JavaScript 프레임워크입니다. 이 프레임워크는 컨트롤러와 뷰 간의 소통을 단순화하기 위해 $scope 객체와 Two-way Data Binding을 제공합니다.

## $scope 객체

AngularJS의 $scope는 컨트롤러와 뷰 간의 중간 매개체로 작용합니다. **$scope 객체**는 이벤트, 값, 함수 등 컨트롤러와 뷰에서 공유할 수 있는 데이터를 담고 있습니다. 컨트롤러에서 작성된 정보는 $scope 객체에 저장되며, 뷰에서는 이 $scope 객체를 참조하여 데이터를 읽고 수정할 수 있습니다.

다음은 $scope 객체를 사용하여 데이터를 공유하는 간단한 예시입니다.

```javascript
app.controller('MyController', function($scope) {
  $scope.message = 'Hello World!';
});
```

위 코드에서 `$scope.message`는 컨트롤러와 뷰에서 공유할 수 있는 'Hello World!'라는 문자열을 나타냅니다.

## Two-way Data Binding

AngularJS의 가장 강력한 기능 중 하나인 **Two-way Data Binding**은 $scope 객체를 통해 데이터의 양방향 전송을 실현합니다. 즉, 데이터의 변경이 한 곳에서 발생하면 다른 곳에 자동으로 업데이트됩니다. 이러한 방식으로 개발자는 직접 데이터 변경을 처리할 필요없이 프로젝트의 생산성을 높일 수 있습니다.

다음은 Two-way Data Binding의 예시입니다.

```html
{% raw %}
<div ng-controller="MyController">
  <input type="text" ng-model="message">
  <p>{{ message }}</p>
</div>
{% endraw %}
```

위 코드에서 `<input>` 요소의 `ng-model` 디렉티브는 $scope 객체의 `message` 변수와 바인딩됩니다. 즉, `<input>` 요소의 값이 변경되면 뷰에 있는 `<p>` 요소에 자동으로 반영됩니다.

## $scope와 Two-way Data Binding의 관계

AngularJS의 $scope는 Two-way Data Binding을 구현하기 위한 핵심입니다. $scope 객체를 통해 컨트롤러와 뷰 간의 데이터를 공유하고 변경사항을 실시간으로 반영할 수 있습니다. 이를 통해 개발자는 데이터의 동기화에 대해 걱정할 필요 없이 더욱 집중할 수 있습니다.

AngularJS의 $scope와 Two-way Data Binding은 개발자들에게 강력하고 효율적인 개발 경험을 제공합니다.

#AngularJS #$scope #TwoWayDataBinding