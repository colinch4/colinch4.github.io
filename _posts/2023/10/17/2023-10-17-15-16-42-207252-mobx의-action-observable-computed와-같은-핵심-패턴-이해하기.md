---
layout: post
title: "MobX의 action, observable, computed와 같은 핵심 패턴 이해하기"
description: " "
date: 2023-10-17
tags: []
comments: true
share: true
---

MobX는 반응형 상태 관리 라이브러리로, JavaScript 애플리케이션에서 상태 변화를 관찰하고 자동으로 업데이트하는데 사용됩니다. MobX를 이해하는 핵심 패턴인 action, observable, computed에 대해 알아보겠습니다.

## 1. Action
Action은 상태를 변경하는 함수를 의미합니다. 일반적으로 애플리케이션 내에서 사용자 인터랙션, API 호출 또는 타이머와 같은 외부 이벤트에 의해 호출됩니다. MobX는 action 내에서 상태 변화를 추적하고, 이에 따른 업데이트를 자동으로 처리합니다.

```javascript
import { observable, action } from 'mobx';

class TodoStore {
  @observable todos = [];

  @action addTodo = (todo) => {
    this.todos.push(todo);
  }
}
```

위의 코드에서 `addTodo` 함수는 `@action` 데코레이터로 표시되어 있으며, 상태를 변경하는 기능을 수행합니다. MobX는 이 함수가 실행될 때 상태의 변경 사항을 추적하고 관련된 컴포넌트를 업데이트합니다.

## 2. Observable
Observable은 MobX에서 관찰 가능한 상태를 의미합니다. `observable` 데코레이터를 사용하여 일반 JavaScript 객체나 배열을 관찰 가능한 상태로 변환할 수 있습니다. 이렇게 변환된 상태는 MobX에 의해 자동으로 추적되며, 이에 따라 상태에 대한 의존성이 있는 컴포넌트가 업데이트됩니다.

```javascript
import { observable } from 'mobx';

class AppState {
  @observable count = 0;
}
```

위의 코드에서 `count` 변수는 `@observable` 데코레이터로 표시되어 있어 MobX에서 상태를 추적할 수 있게 됩니다. 상태가 변경될 때마다 MobX는 이를 관련된 컴포넌트에게 알려주고, 업데이트가 필요한 컴포넌트만 다시 렌더링됩니다.

## 3. Computed
Computed는 MobX에서 파생된 상태를 의미합니다. Computed 값을 사용하면 다른 상태의 값에 기반하여 자동으로 계산된 값을 얻을 수 있습니다. Computed 값을 사용하면 코드의 가독성과 성능을 향상시킬 수 있습니다.

```javascript
import { observable, computed } from 'mobx';

class Order {
  @observable price = 10;
  @observable quantity = 3;

  @computed get totalPrice() {
    return this.price * this.quantity;
  }
}
```

위의 코드에서 `totalPrice`는 `@computed`로 표시된 getter 함수입니다. MobX는 해당 함수에 의존적인 상태가 변경될 때마다 자동으로 다시 계산하고, 이 값을 사용하는 컴포넌트를 업데이트합니다.

## 결론
MobX의 action, observable, computed은 상태 관리를 효율적으로 처리하는 핵심 패턴입니다. 이러한 패턴을 적절히 사용하면 복잡한 상태 변화를 간단하게 관리할 수 있으며, 애플리케이션의 유지 보수성과 성능을 개선할 수 있습니다.

더 자세한 정보는 MobX 공식 문서 (https://mobx.js.org/)를 참조하시기 바랍니다.  

\#MobX #자바스크립트