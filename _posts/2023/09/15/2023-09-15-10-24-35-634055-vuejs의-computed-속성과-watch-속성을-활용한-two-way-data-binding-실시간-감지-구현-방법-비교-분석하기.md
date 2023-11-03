---
layout: post
title: "Vue.js의 computed 속성과 watch 속성을 활용한 Two-way Data Binding 실시간 감지 구현 방법 비교 분석하기"
description: " "
date: 2023-09-15
tags: [VueJS, computed, watch, TwoWayDataBinding]
comments: true
share: true
---

Vue.js는 데이터 바인딩을 처리하는 강력한 기능을 제공합니다. computed 속성과 watch 속성은 특히 데이터의 변경을 실시간으로 감지하고 반응할 수 있는 기능을 제공합니다. 이번 글에서는 computed 속성과 watch 속성을 활용한 Two-way Data Binding의 구현 방법을 비교 분석해보겠습니다.

## computed 속성을 활용한 Two-way Data Binding

computed 속성은 자동으로 캐싱되는 특징을 갖고 있으며, 응답형(getter) 속성으로 선언됩니다. computed 속성을 사용하여 계산된 값을 바인딩해주면, 데이터의 변경이 감지될 때마다 해당 속성이 업데이트됩니다.

```vue
{% raw %}
<template>
  <div>
    <input v-model="inputValue">
    <p>{{ computedValue }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputValue: ''
    }
  },
  computed: {
    computedValue() {
      return this.inputValue.toUpperCase()
    }
  }
}
</script>
{% endraw %}
```

위의 코드는 사용자의 입력값을 받는 input 요소와 입력값을 대문자로 변환하여 보여주는 p 요소를 가진 Vue 컴포넌트입니다. `v-model` 디렉티브를 통해 input 요소와 `inputValue` 데이터를 양방향으로 바인딩하고, computed 속성 `computedValue`를 활용하여 변환된 값이 실시간으로 업데이트되도록 구현하였습니다.

## watch 속성을 활용한 Two-way Data Binding

watch 속성은 데이터 변화를 감지하기 위해 설정된 감시자(Watcher) 함수를 실행합니다. watch 속성은 데이터의 변경 여부를 감시하고, 변경되었을 때 특정 동작을 수행하기 위해 사용됩니다.

```vue
{% raw %}
<template>
  <div>
    <input v-model="inputValue">
    <p>{{ watchedValue }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputValue: '',
      watchedValue: ''
    }
  },
  watch: {
    inputValue(value) {
      this.watchedValue = value.toUpperCase()
    }
  }
}
</script>
{% endraw %}
```

위의 코드는 computed 속성을 사용한 예제와 동일한 기능을 watch 속성을 사용하여 구현한 Vue 컴포넌트입니다. `inputValue` 데이터를 감시하고 변경될 때마다 `watchedValue`를 업데이트하여 변환된 값을 보여주도록 구현하였습니다.

## 비교 및 분석

computed 속성과 watch 속성은 둘 다 데이터의 변경을 감지하여 반응하는 기능을 제공하지만, 사용하는 방법과 동작 방식이 다릅니다.

computed 속성을 사용하면 자동으로 캐싱되는 특징을 갖고 있으며, 응답형(getter) 속성으로 선언됩니다. 데이터의 변경이 감지될 때마다 computed 속성이 업데이트되므로, 효율적인 리렌더링을 할 수 있습니다. 하지만 computed 속성은 읽기 전용이기 때문에 데이터를 변경할 수 없습니다.

반면에 watch 속성은 데이터의 변경을 감시하고, 변경되었을 때 특정 동작을 수행하기 위해 사용됩니다. watch 속성은 데이터의 변경 여부를 감시하는데, computed 속성과 달리 getter와 setter 둘 다를 사용할 수 있습니다. 따라서 데이터의 변경에 따른 다양한 동작을 수행할 수 있습니다.

결론적으로, computed 속성은 읽기 전용의 데이터 연산을 효율적으로 처리하기 위해 사용되고, watch 속성은 데이터의 변경에 따른 동작을 처리하기 위해 사용됩니다. 프로젝트의 요구사항에 맞게 적절한 방식을 선택하여 구현할 필요가 있습니다.

#Vue #VueJS #computed속성 #watch속성 #TwoWayDataBinding