---
layout: post
title: "AngularJS에서의 ng-model을 사용한 Two-way Data Binding 활용 방법"
description: " "
date: 2023-09-15
tags: [AngularJS]
comments: true
share: true
---

AngularJS는 데이터와 화면의 동기화를 쉽게 도와주는 Two-way Data Binding 기능을 제공합니다. 이 기능을 사용하면 데이터의 변경이 화면에 자동으로 반영되고, 화면에서의 사용자 입력이 데이터에 바로 반영됩니다. 이를 통해 사용자 경험을 향상시킬 수 있습니다.

## ng-model 속성

ng-model은 AngularJS에서 데이터 바인딩을 위해 사용하는 속성입니다. 이 속성을 사용하여 HTML 요소의 값을 변수에 연결할 수 있습니다. 값을 가져오거나 변경할 때, AngularJS는 이를 감지하고 연결된 변수의 값을 업데이트합니다.

## 사용 예제

다음은 ng-model을 사용하여 Two-way Data Binding을 구현하는 예제입니다. 

```html
{% raw %}
<!DOCTYPE html>
<html ng-app="myApp">

<head>
    <title>AngularJS Two-way Data Binding</title>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.8.2/angular.min.js"></script>
</head>

<body>
    <div ng-controller="myController">
        <h2>Two-way Data Binding</h2>
        
        <input type="text" ng-model="message" placeholder="Type something">
        <p>{{ message }}</p>
    </div>

    <script>
        var app = angular.module('myApp', []);
        
        app.controller('myController', function ($scope) {
            $scope.message = "Hello AngularJS!";
        });
    </script>
</body>

</html>
{% endraw %}
```

위의 코드에서 \<input> 요소에 ng-model 속성을 사용하여 변수 message와 바인딩했습니다. 이는 사용자가 입력한 값이 message 변수에 자동으로 반영되고, 변수의 값이 변경되면 화면에 자동으로 업데이트됩니다. 
{% raw %}
\<p> 요소에서는 중괄호({{ }}) 안에 변수를 넣어 값을 표시하는 AngularJS 표현식을 사용했습니다. 이를 통해 변수의 값이 실시간으로 화면에 표시됩니다.
{% endraw %}
## 결론

AngularJS의 ng-model을 사용한 Two-way Data Binding은 데이터와 화면의 동기화를 쉽게 구현할 수 있는 강력한 기능입니다. 이를 활용하여 사용자 입력에 따라 동적으로 데이터를 업데이트하고, 화면에 반영하는 웹 애플리케이션을 개발할 수 있습니다.

#AngularJS #TwoWayDataBinding