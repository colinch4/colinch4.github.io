---
layout: post
title: "AngularJS에서 Two-way Data Binding을 활용한 동적 폼 필드 추가 방법"
description: " "
date: 2023-09-15
tags: [AngularJS, TwoWayDataBinding]
comments: true
share: true
---

AngularJS는 데이터 바인딩 및 폼 처리와 같은 기능을 제공하는 강력한 프론트엔드 프레임워크입니다. 이 글에서는 AngularJS의 Two-way Data Binding을 사용하여 동적 폼 필드를 추가하는 방법에 대해 알아보겠습니다.

## Step 1: 폼 필드 모델 생성하기

먼저, 폼에 동적으로 추가할 필드들을 가지고 있는 모델을 생성해야 합니다. 이 모델은 컨트롤러에서 관리될 것이며, 필드의 이름, 값을 포함하는 속성을 가지고 있어야 합니다.

```javascript
$scope.formFields = [
  { name: 'field1', value: '' },
  { name: 'field2', value: '' },
  { name: 'field3', value: '' }
];
```

## Step 2: 폼 필드 추가 기능 구현하기

AngularJS의 Two-way Data Binding을 이용하여 폼 필드를 동적으로 추가하려면, 컨트롤러에서 폼 필드 추가 및 삭제 기능을 구현해야 합니다.

```javascript
$scope.addFormField = function() {
  $scope.formFields.push({ name: '', value: '' });
};

$scope.removeFormField = function(index) {
  $scope.formFields.splice(index, 1);
};
```

위의 코드에서 `addFormField` 함수는 새로운 폼 필드를 모델에 추가하고, `removeFormField` 함수는 특정 인덱스의 폼 필드를 모델에서 제거하는 역할을 합니다.

## Step 3: HTML 템플릿에 폼 필드를 반복해서 출력하기

마지막으로, HTML 템플릿에서 모델의 필드들을 반복해서 출력하는 작업을 수행해야 합니다. 이 과정에서 AngularJS의 `ng-repeat` 지시자를 사용할 수 있습니다.

```html
<div ng-repeat="field in formFields">
  <input type="text" ng-model="field.value" placeholder="Enter {{ field.name }}" />
  <button ng-click="removeFormField($index)">Remove</button>
</div>

<button ng-click="addFormField()">Add Field</button>
```

위의 코드에서 `ng-repeat` 지시자는 `formFields` 배열의 각 요소에 대해 반복하며, 각 필드에 대한 폼 입력 필드와 제거 버튼을 출력합니다. 추가 버튼을 클릭하면 새로운 폼 필드가 추가되며, 제거 버튼을 클릭하면 해당 필드가 제거됩니다.

## 결론

AngularJS의 Two-way Data Binding을 사용하여 동적 폼 필드를 추가하는 방법에 대해 알아보았습니다. 이를 활용하면 사용자가 필요에 따라 폼 필드를 추가하거나 제거할 수 있는 유연한 폼을 구현할 수 있습니다.

#AngularJS #TwoWayDataBinding