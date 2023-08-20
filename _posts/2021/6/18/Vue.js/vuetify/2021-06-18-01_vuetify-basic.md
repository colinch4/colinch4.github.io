---
layout: post
title: "[Vuetify] Vuetify basic"
description: " "
date: 2021-06-18
tags: [Vuetify]
comments: true
share: true
---


## Vuetify

> Vue.js 에서 사용하는 `Bootstrap4` 같은 `UI 프레임워크` 라고 생각하면 편하다..
>
> [참고 블로그](http://blog.weirdx.io/post/60376)
>
> [Vuetify Component 참고](https://code-machina.github.io/2019/02/17/Vuetify-Layout-Part-1.html)
>
> [참고3](https://osc131.tistory.com/122)





## 설치 ( 코드 컨벤션 AirBnB )

```shell
$ npm i -g @vue/cli
$ vue create frontend ( + router, vuex, ESLint+AirBnB )
$ cd frontend
$ vue add vuetify
```

설정 한 뒤에, `App.vue` 파일의 import 부분 끝에 `.vue` 확장자 추가 ( AirBnB 컨벤션 때문에.. )





## 그리드 시스템

Vuetify는 12개를 컬럼을 사용한 그리드 시스템을 사용한다. 5가지 화면 크기에 따른 유형을 적용할 수 있다.

`v-container`는 전체 너비를 기준으로 화면에 출력될 컨테이너를 중앙에 배치한다. `v-layout`은 섹션을 구분하는데 사용하고 `v-flex`를 포함한다. 대부분의 경우 `v-layout`의 `row`와 `column`을 주로 사용한다. `v-flex`의 내부에는 `div` 태그를 사용해서 필요한 내용을 추가한다.

### 기본적인 vuetify 예제

아래 예제는 vuetify에서 소개한 예제이다. 레이아웃 요소를 배치 할 땐 `v-app` 속성을 최상위에 사용해야 한다. `v-content`를 사용하면 구성 요소가 동적으로 조정된다.

```html
<v-app>
  <v-navigation-drawer app></v-navigation-drawer>
  <v-toolbar app></v-toolbar>
  <v-content>
    <v-container fluid>
      <router-view></router-view>
    </v-container>
  </v-content>
  <v-footer app></v-footer>
</v-app>
```





