---
layout: post
title: "Vue.js의 v-model 디렉티브와 input 태그를 이용한 Two-way Data Binding 구현 방법"
description: " "
date: 2023-09-15
tags: [VueJS, vmodel, twowaydatabinding]
comments: true
share: true
---

Vue.js는 데이터 바인딩을 쉽게 구현할 수 있게 해주는 JavaScript 프레임워크입니다. v-model 디렉티브와 input 태그를 조합하여 Two-way Data Binding을 구현하는 방법에 대해 알아보겠습니다.

## 1. v-model 디렉티브란?

v-model 디렉티브는 Vue.js에서 제공하는 양방향 데이터 바인딩을 위한 디렉티브입니다. 이 디렉티브를 사용하면 HTML 요소와 Vue의 데이터 속성을 쉽게 연결할 수 있습니다.

## 2. input 태그와 Two-way Data Binding

input 태그는 웹 애플리케이션에서 사용자의 입력을 받을 수 있는 요소입니다. Vue.js의 v-model 디렉티브와 input 태그를 함께 사용하면 사용자의 입력과 Vue의 데이터 속성을 양방향으로 연결할 수 있습니다.

아래는 예시 코드입니다.

```javascript
{% raw %}
<template>
  <div>
    <input v-model="message" type="text">
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    };
  }
};
</script>
{% endraw %}
```
{% raw %}
위의 코드에서 `v-model="message"`는 input 태그의 값과 Vue의 데이터 속성인 `message`를 양방향으로 연결합니다. 사용자가 input 태그에 입력한 값은 `message` 변수에 저장되며, 그 값을 다시 `{{ message }}`를 통해 출력할 수 있습니다.
{% endraw %}
이제 사용자가 input 태그에 어떤 값을 입력하면, 그 값이 실시간으로 화면에 출력되는 것을 확인할 수 있습니다.

## 3. v-model 디렉티브와 다른 요소

v-model 디렉티브는 input 태그뿐만 아니라 다른 요소들과도 함께 사용할 수 있습니다. 예를 들어, checkbox, radio, select 등도 v-model을 이용하여 데이터 바인딩을 할 수 있습니다.

```javascript
{% raw %}
<template>
  <div>
    <input v-model="checked" type="checkbox">
    <p>체크 상태: {{ checked }}</p>
    
    <input v-model="selected" type="radio" value="A">
    <input v-model="selected" type="radio" value="B">
    <p>선택한 값: {{ selected }}</p>
    
    <select v-model="selectedOption">
      <option value="A">A</option>
      <option value="B">B</option>
    </select>
    <p>선택한 옵션: {{ selectedOption }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checked: false,
      selected: '',
      selectedOption: ''
    };
  }
};
</script>
{% endraw %}
```

위의 코드에서는 v-model 디렉티브를 이용하여 checkbox, radio, select 요소들의 상태를 Vue의 데이터 속성과 양방향으로 연결하고 있습니다. 사용자의 입력에 따라 데이터가 업데이트되어 실시간으로 화면에 반영됩니다.

## 마무리

Vue.js의 v-model 디렉티브와 input 태그를 이용하면 쉽게 Two-way Data Binding을 구현할 수 있습니다. 사용자의 입력과 화면의 상태를 동기화시키는 간편하고 효율적인 방법을 제공하여 웹 애플리케이션 개발을 보다 편리하게 할 수 있습니다.

#VueJS #vmodel #twowaydatabinding