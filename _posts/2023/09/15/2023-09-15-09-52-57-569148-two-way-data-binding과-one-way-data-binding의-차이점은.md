---
layout: post
title: "Two-way Data Binding과 One-way Data Binding의 차이점은?"
description: " "
date: 2023-09-15
tags: [javascript]
comments: true
share: true
---

Two-way Data Binding은 데이터의 변경이 요소에 반영되는 것뿐만 아니라, 요소의 변경이 데이터에도 반영되는 방식입니다. 이는 데이터와 요소 간의 양방향 통신을 의미하며, 사용자가 입력한 내용이 바로 데이터에 반영되는 장점이 있습니다. 예를 들어, 사용자가 입력 필드에 값을 입력하면 해당 값이 바로 데이터에 저장되고, 이때 데이터의 변경이 다른 요소들에도 자동으로 반영됩니다. 주로 폼 입력과 관련된 기능에서 많이 사용됩니다.

```
{% raw %}
<input type="text" [(ngModel)]="name">
<p>Hello, {{name}}!</p>
{% endraw %}
```

One-way Data Binding은 데이터의 변경이 요소에만 반영되는 방식입니다. 요소의 변경이 데이터에 영향을 주지 않고, 단방향 통신을 하기 때문에 간단하고 효율적입니다. 데이터의 변경을 요소에 반영하기 위해서는 수동으로 업데이트를 해주어야 합니다. 이는 데이터의 상태를 요소에 표시하는 용도로 사용됩니다. 예를 들어, 데이터를 요소에 출력하는 경우에 사용됩니다.

```
{% raw %}
<p>{{message}}</p>
<button (click)="updateMessage()">Update</button>
{% endraw %}
```

따라서, Two-way Data Binding은 양방향으로 데이터를 동기화하므로 사용자의 입력을 실시간으로 반영하고 업데이트하는 데 유용합니다. 반면에 One-way Data Binding은 데이터의 단방향으로 요소에 표시하는 용도로 사용되며, 간단하고 효율적인 방식입니다.

#TwoWayDataBinding #OneWayDataBinding