---
layout: post
title: "Vue.js의 v-on 디렉티브와 커스텀 이벤트를 이용한 Two-way Data Binding 실시간 감지 구현하기"
description: " "
date: 2023-09-15
tags: []
comments: true
share: true
---

Vue.js는 재사용 가능한 UI 컴포넌트를 만들기 위해 사용되는 프레임워크입니다. 이 프레임워크는 데이터 바인딩을 통해 데이터와 UI를 동기화하는 기능을 제공합니다. 그 중에서도 v-on 디렉티브를 이용한 이벤트 핸들링을 통해 실시간으로 데이터를 감지 및 업데이트하는 기능을 구현하는 방법을 알아보겠습니다.

## v-on 디렉티브란?

v-on 디렉티브는 Vue.js에서 이벤트를 처리하기 위해 사용됩니다. 이 디렉티브를 사용하여 원하는 이벤트를 감지하고, 해당 이벤트가 발생했을 때 호출할 메소드를 정의할 수 있습니다. 예를 들어, 버튼 클릭, 입력값 변화 등의 이벤트를 감지하여 원하는 동작을 수행할 수 있습니다.

## 커스텀 이벤트란?

Vue.js에서는 컴포넌트 간의 통신을 위해 커스텀 이벤트를 사용할 수 있습니다. 이벤트를 발생시키는 컴포넌트에서 `$emit` 메소드를 이용하여 커스텀 이벤트를 발생시키고, 해당 이벤트를 수신할 컴포넌트에서는 v-on 디렉티브를 이용하여 이벤트를 처리할 수 있습니다. 이를 통해 부모 컴포넌트와 자식 컴포넌트 사이의 데이터 통신을 구현할 수 있습니다.

## Two-way Data Binding 구현하기

Two-way Data Binding은 입력 항목과 데이터 모델 사이의 양방향 데이터 흐름을 의미합니다. Vue.js에서는 v-model 디렉티브를 사용하여 입력 항목과 데이터 모델을 바인딩할 수 있습니다. 이를 통해 사용자의 입력에 따라 데이터가 자동으로 업데이트되고, 데이터의 변경에 따라 입력 항목이 실시간으로 갱신됩니다.

```html
<template>
  <div>
    <input type="text" v-model="message">
    <button v-on:click="sendMessage">Send</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage() {
      // 메세지를 처리하는 로직
      // ...
      this.$emit('message-sent', this.message);
      this.message = '';
    }
  }
};
</script>
```

위의 코드에서는 입력 항목인 `input` 요소와 버튼이 있습니다. `v-model` 디렉티브를 이용하여 `input` 요소와 `message` 데이터를 양방향으로 바인딩합니다. 즉, `message` 데이터에 변경이 발생하면 `input` 요소의 값이 자동으로 갱신되며, `input` 요소의 값이 변경되면 `message` 데이터도 자동으로 갱신됩니다.

또한, `v-on:click` 디렉티브를 이용하여 버튼 클릭 이벤트를 처리하는 메소드를 호출할 수 있습니다. 이때, `this.$emit` 메소드를 이용하여 `message-sent`라는 커스텀 이벤트를 발생시키고, `this.message` 값을 이벤트의 데이터로 함께 전달합니다.

이제 이벤트를 수신할 부모 컴포넌트에서는 해당 커스텀 이벤트를 처리하는 메소드를 정의하여 데이터를 업데이트할 수 있습니다.

```html
<template>
  <div>
    <custom-input v-on:message-sent="handleMessage"></custom-input>
    <p>Message: {{ message }}</p>
  </div>
</template>

<script>
import CustomInput from './CustomInput.vue';

export default {
  components: {
    CustomInput
  },
  data() {
    return {
      message: ''
    }
  },
  methods: {
    handleMessage(message) {
      this.message = message;
    }
  }
};
</script>
```

위의 코드에서는 `custom-input` 컴포넌트를 사용하여 `message-sent` 이벤트를 수신하고, `handleMessage` 메소드를 호출하여 자식 컴포넌트로부터 전달된 데이터를 업데이트합니다. 이후 `message` 데이터를 출력하여 컴포넌트 내에서 실시간으로 데이터가 갱신되는 것을 확인할 수 있습니다.

## 결론

Vue.js의 v-on 디렉티브와 커스텀 이벤트를 활용하면 Two-way Data Binding을 구현하여 데이터의 실시간 감지와 업데이트를 손쉽게 처리할 수 있습니다. 이를 통해 사용자와의 원활한 상호작용을 구현하고 재사용 가능한 컴포넌트를 개발할 수 있습니다.

#vue #v-on #two-way-data-binding