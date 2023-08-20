---
layout: post
title: "[Sass] Sass로 타이포그래피 규칙 관리하기"
description: " "
date: 2021-09-09
tags: [Sass]
comments: true
share: true
---


## Sass로 타이포그래피 규칙 관리하기

디자인 시스템에서 정의한 타이포그라피 규칙을 코드화해 편리하게 사용하고 싶었다.
타이포그래피 규칙은 `font-size`, `font-weight`, `line-height`, `letter-spacing` 등 복합적인 속성으로 구성되어 있어 변수만으로는 원하는 구조를 구현하기 힘들어 보였다.
위 타이포 규칙을 하나의 묶음으로 만들어 **타이포그라피 규칙 중 이 유형** 이라는 의미를 갖는 것이 원하는 형태였다.

방안 1. mixin으로 만들어 @include 로 사용하는 방법
방안 2. function으로 만들기?

### 1. `map`과 `@function` 을 사용하는 방법

1. map 정의

   ```scss
   $typography-size-map: (
     "heading-01": 72px,
     "heading-02": 48px,
     "heading-03": 32px,
     "heading-04": 24px,
     "heading-05": 20px,
     "heading-06": 18px,
     "heading-07": 16px,
     "p": 14px,
     "desc": 12px,
     "label": 12px
   );
   ```

2. @function 생성

   ```scss
   @function typography-size($name) {
     @return map-get($typography-size-map, $name);
   }
   ```

3. 특정 속성의 값으로 사용

   ```scss
   .test {
     font-size: typography-size("heading-01");
   }
   
   // 컴파일 결과 - typography-size-map에 정의된 값을 반환
   .test {
     font-size: 72px;
   }
   ```

   함수로 1개 속성을 반환하는 건 가능하다. 여러 속성을 묶음으로 반환시키려면 어찌 해야 하는가...

### 2. `mixin` 에 `@if`, `@else` 엮어 사용하는 방법

1. mixin 정의

   ```scss
   @mixin typo-scale($el) {
     @if $el == "heading-1" {
       font-size: 72px;
       line-height: 119%;
     } @else if $el == "heading-2" {
       font-size: 52px;
       line-height: 119%;
     } @else if $el == "heading-3" {
       font-size: 46px;
       line-height: 119%;
     }
   }
   ```

2. 원하는 부분에 `@include` 사용

```scss
.typo-scale-test-2 {
  @include typo-scale('heading-1');
}

// 컴파일 결과
.test {
  font-size: 72px;
  line-height: 119%;
}
```

mixin 코드가 불필요하게 길어지고 지저분해진다. 오버엔지니어링이라는 평가를 받았다.

### 3. `map`을 여러개 만들어서 믹스인에 엮기

1. size map 생성

   ```scss
   $typography-size-map: (
     "heading-01": 72px,
     "heading-02": 48px,
     "heading-03": 32px,
     "heading-04": 24px,
     "heading-05": 20px,
     "heading-06": 18px,
     "heading-07": 16px,
     "p": 14px,
     "desc": 12px,
     "label": 12px
   );
   
   @function typography-size($name) {
     @return map-get($typography-size-map, $name);
   }
   
   @mixin typography-size($name) {
     font-size: typography-size($name);
   }
   ```

2. line height map 생성

   ```scss
   $typography-line-height-map: (
     "heading-01": 1.2,
     "heading-02": 1.28,
     "heading-03": 1.36,
     "heading-04": 1.4,
     "heading-05": 1.44,
     "heading-06": 1.48,
     "heading-07": 1.5,
     "p": 1.54,
     "desc": 1.36,
     "label": 1.5
   );
   
   @function typography-line-height($name) {
     @return map-get($typography-line-height-map, $name);
   }
   
   @mixin typography-line-height($name) {
     line-height: typography-line-height($name);
   }
   ```

3. 위의 map을 참조하는 mixin 생성

   ```scss
   @mixin heading-01 {
     @include typography-size('heading-01');
     @include typography-line-height('heading-01');
   }
   ```

4. 클래스에 적용

   ```scss
   .heading-01 {
     @include heading-01;
   } 
   // 컴파일 결과
   .heading-01 {
     font-size: 72px;
     line-height: 1.2;
   }
   ```

   이건 거의 그냥 `@mixin` 만들어서 사용하는 수준인 것 같다. 3번에서 생기는 코드가 길어진다.

### 4. map을 만든 부분에 매개변수를 활용한 믹스인 만들기

1. 맵 만들고 함수와 믹스인 만드는 과정은 위의 1~2 과정과 동일하다

2. mixin을 만들 때 매개변수로 대입될 수 있도록 작성한다

   ```scss
   @mixin typography($size) {
     width: $size;
     height: $size;
   }
   ```

3. 클래스에 적용

   ```scss
   .typography-test {
     @include typography('heading-02');
   }
   // 컴파일 결과
   .typography-test {
     font-size: 48px;
     line-height: 1.28;
   }
   ```

드디어 내가 원하는 구조를 만들어냈다!
단순하게 믹스인을 만드는것 보다 키와 밸류가 한눈에 들어와 데이터 관리가 용이하고, 정의된 타이포그라피 스타일이 아닌 매개변수가 들어올 경우 오류 메시지가 뜨도록 개선도 가능할 것이다.
또한 _3. `map`을 여러개 만들어서 믹스인에 엮기_ 에서 결국 믹스인을 타이포그래피 유형별로 찍어내던 코드도 개선해준다.active

현재 내가 알고 있는 Sass 기술로는 이 정도 구현이 최선인 것 같다. 더 정진해서 멋진걸 만들어내고싶다!

### 📖Reference

- [Sass - @function](https://sass-lang.com/documentation/at-rules/function)
- [Sass - sass:map](https://sass-lang.com/documentation/modules/map)