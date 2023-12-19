---
layout: post
title: "[design] ag-grid 디자인을 원하는대로 수정하기"
description: " "
date: 2021-09-09
tags: [개발]
comments: true
share: true
---


## ag-grid 디자인을 원하는대로 수정하기


## 테마 수정하는 방법
1. [제공된 테마](https://www.ag-grid.com/javascript-grid-themes-provided/) 중 하나를 사용. CSS 수정으로 간단하게 원하는 부분을 수정한다
2. 테마 매개변수 및 CSS를 사용하여 [제공된 테마를 재정의](https://www.ag-grid.com/javascript-grid-themes-customising/). 이를 위해서는 Sass 파일을 빌드하도록 프로젝트를 구성해야한다. 모양, 느낌, 색상, 패딩 및 테두리와 같은 요소를 변경할 수 있다
3. 기본 테마를 확장하여 처음부터 자신만의 테마를 만든다. 제공된 테마와 크게 다르게 보이는 경우에 적합한 옵션

3번 방법을 활용해 제공된 테마를 확장한 다음, 완전히 다른 디자인을 만들기 위해 광범위하게 수정하면 몇가지 문제가 발생할 수 있다.

1. 제공된 테마에 원하지 않는 디자인 요소가 표함된 경우 CSS 규칙을 추가하여 제거해야한다
2. 릴리즈 버전간, 세부사항 중 일부가 변경되어 재선언한 스타일이 적용되지 않을 수 있다. 제공된 테마와 완전히 다른 륵엔필을 원하는 앱의 경우 기본 테마를 확장하는것이 좋다. 기본 테마에는 가장 기본 구성 가능한 테두리와 적절한 기본 패딩이 포함되어있다.

## Customizing Themes

제공되고 있는 테마는 theme 파라미터(매개변수)와 CSS 규칙으로 커스터마이징 할 수 있다. 엘리먼트의 색상, 여백, 테두리와 같은 룩앤필을 수정하기 위해  프로젝트에 Sass 파일을 빌드할 수 있는 환경이 요구된다.

### Theme Parameters

테마의 외형을 바꾸기 위한 인수. 몇몇 파라미터(매개변수)는 CSS 재정의로 달성하기 어려운 효과를 가져온다. Sass API를 통해 매개 변수를 설정하고 CSS 변수를 사용해 색상 매개변수를 추가로 설정할 수 있다.

주요한 테마 매개 변수리스트는 아래와 같다.

- `grid-size`: 데이터와 UI 요소가 얼마나 밀접하게 묶여 있는지에 영향을 주는 요소이다. 그리드의 모든 패딩 및 간격은 gfrid-size의 배수로 정의 되므로, 텍스트와 아이콘의 크기는 변경하지 않고 내부 공백을 늘려 대부분의 구성 요소를 더 크게 만들 수 있다.
- `borders`  그리드 주위에 테두리를 그릴 지 여부를 제어한다. 더 많은 `border-*` 매개 변수가 있어 어떤 테두리가 그려지는지와 색상을 세밀하게 제어할 수 있다
- `row-height` 행의 높이를 정의한다
- `header-height` 헤더 행의 높이를 정의한다
- `foreground-color`, `background-color` 그리드의 텍스트 컬러와 배경 컬러를 설정한다 - 컬러 스킴을 보다 세밀하게 제어하기 위한 더 많은 매개변수가 있다
- 제공된 테마에는 여러 요소의 색상을 한번에 설정하기 위한 테마별 매개변수가 있다.
    - `alpine-active-color` (Alpine 테마 전용) 체크된 상태의 체크박스, 범위 선택, 행 선택, 선택된 탭의 밑줄과 input 선택시 outline의 색상을 설정
    - `balham-active-color` (Balham 테마 전용) 체크된 상태의 체크박스, 범위 선택, 행 선택, 선택된 탭의 밑줄 색상을 설정
    - `material-primary-color` , `material-accent-color` (Material 테마 전용) 기본과 액센트 컬러 역할을 설정할 수 있다. 기본 색상은 버튼, 범위 선택, 선택된 탭의 밑줄과 input 이 포커스상태일 때 밑줄이고, 액센트 컬러는 체크된 상태의 체크박스 색상이다.

### Sass를 사용해 매개변수 셋팅하기

Sass로 매개변수를 정의하기 위해, 프로젝트가 Sass파일을 컴파일하도록 셋팅되어야한다. 추천되는 방식은 웹팩을 통하는것이다. 테마 수정을 위해 테마 믹스인 파일을 포함시키고 믹스인 매개변수를 호출해 커스터미이징한다. 

또는 테마 매개변수가 없다면 선택자에 스타일을 재선언 해주는 방식도 가능하다.

```scss
@import "~ag-grid-community/src/styles/ag-grid.scss";
@import "~ag-grid-community/src/styles/ag-theme-alpine/sass/ag-theme-alpine-mixin";

.ag-theme-alpine {
    @include ag-theme-alpine((
        // use theme parameters where possible
        alpine-active-color: deeppink
    ));

    .ag-header {
        // or write CSS selectors to make customisations beyond what the parameters support
        text-style: italic;
    }
}
```

테마의 믹스인 파일을 불러오기 전 구조 스타일 (`ag-grid.scss`) 을 포함시킨다. 이는 즉 구조와 테마의 스타일이 컴파일된 CSS에 포함된다는 의미이다. 또는, 첫번째 `@import` 를 제외하고 구조 스타일 시트를 HTML페이지에 별도로 추가하는것도 가능하다.

## 참고자료
- [https://www.ag-grid.com/javascript-grid-styling/](https://www.ag-grid.com/javascript-grid-styling/)
- [ag-grid: Customising Themes](https://www.ag-grid.com/javascript-grid-themes-customising/)
- [Full list of theme parameters](https://www.ag-grid.com/javascript-grid-themes-customising/#base-theme-parameters)