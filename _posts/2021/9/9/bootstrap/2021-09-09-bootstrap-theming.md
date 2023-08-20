---
layout: post
title: "[bootstrap] Bootstrap 테마 설정"
description: " "
date: 2021-09-09
tags: [bootstrap]
comments: true
share: true
---

## Bootstrap 테마 설정

테마와 구성 요소의 변경을 쉽게 하기 위한 글로벌 스타일 설정이 가능합니다. 새로운 빌트인 Sass 변수를 사용하여 Bootstrap 4를 정의하세요.

## Introduction

Bootstrap 3에서 테마는 LESS, custom CSS의 변수 오버라이드, 그리고 `dist` 파일에 포함된 별도의 테마 스타일 시트를 오버라이드하는 방법으로 크게 좌우되었습니다. 약간의 노력으로, 코어 파일을 건드리지 않고 Bootstrap 3의 외관을 완전이 재설계할 수 있습니다. Bootstrap 4는 친숙하지만 약간 다른 접근법을 제공합니다.

이제, 테마는 Sass 변수, Sass 맵 및 사용자 정의 CSS에 의해 수행됩니다. 더이상 전용 테마 스타일 시트는 존재하지 않습니다. 대신, 내장된 테마를 사용하여 그래디언트, 그림자등을 추가할 수 있습니다.

## Sass

Sass 파일의 variables, maps, mixins 등 장점을 활용하세요. 빌드시 브라우저 라운딩 문제를 방지하기 위해 Sass 반올림 정밀도를 6 (기본값은 5)으로 늘 렸습니다.

### File structure

가능한 경우 Bootstrap의 코어 파일을 수정하지 마십시오. Sass의 경우 부트스트랩을 가져와서 스타일 시트를 수정하고 확장할 수 있다는 것을 의미합니다. npm과 같은 패키지 관리자를 사용한다고 가정하면 다음과 같은 파일 구조가됩니다.

```
your-project/
├── scss
│   └── custom.scss
└── node_modules/
    └── bootstrap
        ├── js
        └── scss
```

만약 파일을 다운로드 했지만 패키지 매니저를 사용하지 않는 경우, 부트스트랩의 소스 파일을 사용자 자신의 것과 별도로 유지하며 해당 구조와 비슷한 구조를 수동으로 설정해야 합니다.

```
your-project/
├── scss
│   └── custom.scss
└── bootstrap/
    ├── js
    └── scss
```

### importing

`custom.scss`에서 부트스트랩의 소스파일을 가져옵니다. 두가지 옵션이 있습니다: 모든 부트스트랩을 포함 시키거나, 필요한 부분을 선택하는 것입니다. 후자를 권장하지만 부트스트랩 구성요소 전반에 몇 가지 요구사항과 종속성이 있음을 알고 있어야 합니다. 또한 플러그인용 JavaScript를 일부 포함시켜야 합니다.

```scss
// Custom.scss
// Option A: Include all of Bootstrap

@import "../node_modules/bootstrap/scss/bootstrap";
```

```scss
// Custom.scss
// Option B: Include parts of Bootstrap

// Required
@import "../node_modules/bootstrap/scss/functions";
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/mixins";

// Optional
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/type";
@import "../node_modules/bootstrap/scss/images";
@import "../node_modules/bootstrap/scss/code";
@import "../node_modules/bootstrap/scss/grid";
```

위 설정을 사용하면 `custom.scss` 의 Sass 변수 및 맵을 수정할 수 있습니다. 필요헤 따라 `// Optional` 섹션 아래에 Bootstrap의 일부를 추가할수도 있습니다. 시작 시점에 `bootstrap.scss` 파일 전체를 가져오는 스택을 제안합니다.

### Variable defaults

Bootstrap4의 모든 Sass 변수에는 `!default` 플래그가 있어 Bootstrap의 소스 코드를 수정하지 않고 자신의 Sass에서 변수의 기본값을 무시할 수 있습니다. 필요에 따라 변수를 복사하고, 붙여넣고, 값을 수정하고, `!default` 플래그를 제거하십시오. 변수가 이미 할당된 경우 Bootstrap의 기본값에 의해 다시 할당되지 않습니다.

Bootstrap 변수의 전체 목록은 `sass/_variables.scss`에서 찾을 수 있습니다. 일부 변수는 `null` 로 설정되며, 이 변수는 커스텀에서 덮어쓰지 않는 한 property를 출력하지 않습니다.

같은 Sass 파일 내의 변수 오버라이드는 기본 변수(default variables)의 앞이나 뒤에 올 수 있습니다. 그러나 Sass 파일을 오버라이드 할 때 Bootstrap의 Sass 파일을 가져오기 전에 위치해야 합니다.

다음은 npm을 통해 Bootstrap을 가져오고 컴파일 할 때 `<body>` 의 배경색과 색상을 변경하는 예제입니다.

```scss
// Your variable overrides
$body-bg: #000;
$body-color: #111;

// Bootstrap and its default variables
@import "../node_modules/bootstrap/scss/bootstrap";
```

아래 전역 옵션(global options)을 포함하여 Bootstrap의 모든 변수에 대해 필요한 만큼 반복하세요.

### Maps and loops

Bootstrap4에는 관련된 CSS를 쉽게 생성할 수 있도록 도와주는 Sass 맵이 있습니다. 색상, 그리드 breakpoints 등에 Sass맵을 사용합니다. Sass 변수와 마찬가지로 모든 Sass 맵은 `!default` 플래그를 포함하며 재정의되고(ovrridden) 확장(extended)될 수 있습니다.

일부 Sass 맵은 기본적으로 빈 맵으로 병합됩니다. 이는 주어진 Sass 맵을 쉽게 확장할 수 있도록 하기 위해 수행되지만, 맵에서 항목을 *제거하는것*이 약간 더 어렵습니다.

#### Modify map

`$theme-colors` 맵의 기존 색상을 수정하려면 사용자 정의 Sass 파일에 다음을 추가하십시오

```scss
$theme-colors: (
  "primary": #0074d9,
  "danger": #ff4136
);	
```

#### Add to map

`$theme-colors` 에 새 색상을 추가하려면 새 키와 값을 추가하십시오

```scss
$theme-colors: (
  "custom-color": #900
);
```

#### Remove from map

`$theme-colors` 또는 다른 맵에서 색상을 제거하려면 `$map-remove` 를 사용하십시오. Bootstrap의 필수요소와 옵션 사이에 삽입해야 한다는 점에 유의하십시오

```scss
// Required
@import "../node_modules/bootstrap/scss/functions";
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/mixins";

$theme-colors: map-remove($theme-colors, "info", "light", "dark");

// Optional
@import "../node_modules/bootstrap/scss/root";
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/type";
...
```

#### Required keys

Bootstrap은 우리가 이것을 사용하고 확장할 때 Sass 맵 내에 특정 키가 있다고 가정합니다. 포함된 맵을 사용자 정의(customize)할 때 특정 Sass 맵의 키가 사용되는 곳에서 오류가 발생할 수 있습니다.

예를들어, 링크, 버튼 및 양식 상태에 대한 `$theme-colors` 의 `기본(primary)`, `성공(success)` 및 `위험(danger)` 키를 사용합니다. 이 키의 값을 바꾸면 문제가 없지만 제거하면 Sass 컴파일 문제가 발생할 수 있습니다. 이러한 경우 해당 값을 사용하는 Sass 코드를 수정해야합니다.

### Functions

부트 스트랩은 여러 가지 Sass 기능을 사용하지만 일부만 일반 테마에 적용 할 수 있습니다. 색상 맵에서 값을 가져 오는 세 가지 기능이 포함되었습니다.

```scss
@function color($key: "blue") {
  @return map-get($colors, $key);
}

@function theme-color($key: "primary") {
  @return map-get($theme-colors, $key);
}

@function gray($key: "100") {
  @return map-get($grays, $key);
}
```

이를 통해 v3의 색상 변수를 사용하는 것과 같은 방법으로 Sass 맵에서 하나의 색상을 선택할 수 있습니다.

```scss
.custom-element {
  color: gray("100");
  background-color: theme-color("dark");
}
```

우리는 또한 `$theme-colors` 맵에서 특정 레벨의 색상을 얻는 또 다른 함수를 가지고 있습니다. 음의 레벨 값은 색상을 밝게하고 높은 레벨은 어둡게 만듭니다.

```scss
@function theme-color-level($color-name: "primary", $level: 0) {
  $color: theme-color($color-name);
  $color-base: if($level > 0, #000, #fff);
  $level: abs($level);

  @return mix($color-base, $color, $level * $theme-color-interval);
}
```

실제로는 함수를 호출하고 `$theme-colors` (예 : 기본(primary) 또는 위험(danger))의 색상 이름과 숫자 수준의 두 매개 변수를 전달합니다.

```scss
.custom-element {
  color: theme-color-level(primary, -10);
}
```

미래의 추가 기능이나 사용자 정의 Sass에 기능을 추가하여 Sass 맵을 추가하거나, 더 자세한 기능을 원한다면 일반적인 기능을 추가 할 수 있습니다.

### Color contrast

Bootstrap에 포함 된 또 하나의 기능은 색상 대비 기능인 `color-yiq`입니다.  [YIQ color space](https://en.wikipedia.org/wiki/YIQ) 를 사용하여 지정된 기본 색상을 기반으로 밝은 색상 (`#fff`) 또는 어두운 색상 (`#111`)을 자동으로 반환합니다. 이 함수는 여러 클래스를 생성하는 믹스 또는 루프에 특히 유용합니다.

예를 들어, `$theme-colors` 맵에서 색상 견본을 생성하려면 다음을 수행하십시오.

```scss
@each $color, $value in $theme-colors {
  .swatch-#{$color} {
    color: color-yiq($value);
  }
}
```

일회서으로 필요한 대비 사항에도 사용할 수 있습니다.

```scss
.custom-element {
  color: color-yiq(#000); // returns `color: #fff`
}
```

컬러 맵 함수를 사용하여 기본 색상을 지정할 수도 있습니다.

```scss
.custom-element {
  color: color-yiq(theme-color("dark")); // returns `color: #fff`
}
```

## Sass options

기본 제공되는 사용자 정의 변수 파일을 사용하여 Bootstrap4를 커스텀하고 새 `$enable-*` Sass 변수로 전역 CSS 환경 설정을 쉽게 전환할 수 있습니다. 변수의 값을 재작성하고 `npm run test`를 사용하여 다시 컴파일하십시오.

Bootstrap의 `scss/_variables.scss` 파일에서 주요 전역 옵션에 대해 이러한 변수를 찾고 사용자 정의 할 수 있습니다.

| Variable                                     | Values                            | Description                                                  |
| -------------------------------------------- | --------------------------------- | ------------------------------------------------------------ |
| `$spacer`                                    | `1rem`(default), or any value > 0 | Specifies the default spacer value to programmatically generate our [spacer utilities](https://getbootstrap.com/docs/4.3/utilities/spacing/). |
| `$enable-rounded`                            | `true`(default) or `false`        | Enables predefined `border-radius` styles on various components. |
| `$enable-shadows`                            | `true` or `false`(default)        | Enables predefined `box-shadow` styles on various components. |
| `$enable-gradients`                          | `true` or `false`(default)        | Enables predefined gradients via `background-image` styles on various components. |
| `$enable-transitions`                        | `true`(default) or `false`        | Enables predefined `transition`s on various components.      |
| `$enable-prefers-reduced-motion-media-query` | `true`(default) or `false`        | Enables the [`prefers-reduced-motion` media query](https://getbootstrap.com/docs/4.3/getting-started/accessibility/#reduced-motion), which suppresses certain animations/transitions based on the users’ browser/operating system preferences. |
| `$enable-hover-media-query`                  | `true` or `false`(default)        | **Deprecated**                                               |
| `$enable-grid-classes`                       | `true`(default) or `false`        | Enables the generation of CSS classes for the grid system (e.g., `.container`, `.row`, `.col-md-1`, etc.). |
| `$enable-caret`                              | `true`(default) or `false`        | Enables pseudo element caret on `.dropdown-toggle`.          |
| `$enable-pointer-cursor-for-buttons`         | `true`(default) or `false`        | Add “hand” cursor to non-disabled button elements.           |
| `$enable-print-styles`                       | `true`(default) or `false`        | Enables styles for optimizing printing.                      |
| `$enable-responsive-font-sizes`              | `true` or `false`(default)        | Enables [responsive font sizes](https://getbootstrap.com/docs/4.3/content/typography/#responsive-font-sizes). |
| `$enable-validation-icons`                   | `true`(default) or `false`        | Enables `background-image` icons within textual inputs and some custom forms for validation states. |
| `$enable-deprecation-messages`               | `true` or `false`(default)        | Set to `true` to show warnings when using any of the deprecated mixins and functions that are planned to be removed in `v5`. |

## Color

Bootstrap의 다양한 구성 요소와 유틸리티는 Sass 맵에 정의된 일련의 색상을 통해 만들어집니다. Sass에서 이 지도를 반복하여 일련의 규칙 집합을 빠르게 생성 할 수 있습니다.

### All colors

Bootstrap4에서 사용할 수있는 모든 색상은 Sass 변수와 `scss/_variables.scss` 파일의 Sass 맵으로 사용할 수 있습니다. 이는 우리가 이미 포함하고있는 [grayscale palette](https://getbootstrap.com/docs/4.3/getting-started/theming/#grays) 팔레트와 마찬가지로 추가 음영을 추가하기 위해 후속 마이너 릴리즈에서 확장될 것입니다.

![스크린샷 2019-06-28 오후 5.41.41](/Users/heeyeonkang/2_STUDY/TIL/@images/스크린샷 2019-06-28 오후 5.41.41.png)

Sass에서 이것을 사용하는 방법은 다음과 같습니다.

```scss
// With variable
.alpha { color: $purple; }

// From the Sass map with our `color()` function
.beta { color: color("purple"); }
```

[Color utility classes](https://getbootstrap.com/docs/4.3/utilities/colors/) 는 `color` 및 `background-color` 을 설정할 때도 사용할 수 있습니다.

> 앞으로는 그레이 스케일 색상을 사용한 것처럼 각 색상의 쉐도우에 Sass 맵과 변수를 제공하는 것을 목표로 할 것입니다.

### Theme colors

우리는 모든 색상의 하위 집합을 사용하여 색 구성표를 생성하기위한 작은 색상 표를 만들고 부트 스트랩의 `scss/_variables.scss` 파일에서 Sass 변수와 Sass 맵으로 사용할 수도 있습니다.

![스크린샷 2019-06-28 오후 5.41.49](/Users/heeyeonkang/2_STUDY/TIL/@images/스크린샷 2019-06-28 오후 5.41.49.png)

### Grays

회색 변수의 확장 세트와 `scss/_variables.scss`의 Sass 맵은 프로젝트 전반에 일관된 회색 음영을 제공합니다. 이들은 "cool grays"이며 중립적 인 회색보다는 미묘한 푸른 색조로 향하는 경향이 있습니다.

`scss/_variables.scss`에서 Bootstrap의 색상 변수와 Sass 맵을 찾을 수 있습니다. 다음은 `$colors` Sass 맵의 예입니다.

지도 내의 값을 추가, 제거 또는 수정하여 다른 여러 구성 요소에서 사용 된 방법을 업데이트하십시오. 불행히도 현재 모든 구성 요소가이 Sass 맵을 사용하는 것은 아닙니다. 향후 업데이트는이를 개선하기 위해 노력할 것입니다. 그때까지 `${color}` 변수와 이 Sass 맵을 사용할 계획을 세우십시오.

## Components

Bootstrap의 많은 구성 요소와 유틸리티는 `@each` 루프로 구축되어 Sass 맵을 반복합니다. 이는 `$theme-colors`를 사용하여 구성 요소의 변형을 생성하고 각 중단점(breakpoint)에 대한 반응형 변형을 만드는 데 특히 유용합니다. 이 Sass 맵을 사용자 정의하고 다시 컴파일하면 변경 사항이이 루프에 반영됩니다.

### Modifiers

Bootstrap의 많은 구성 요소는 base-modifier(기본-수정자) 클래스 접근 방식으로 구축됩니다. 즉, 대부분의 스타일은 기본 클래스 (예 : `.btn`)에 포함되지만 스타일 베리에이션은 수정자 클래스 (예 : `.btn-danger`)에 한정됩니다. 이러한 수정자 클래스는 `$theme-colors` 맵에서 빌드되어 수정자 클래스의 수와 이름을 사용자 정의 할 수 있습니다.

다음은 `.alert` 구성 요소와 모든 `.bg- *` 배경 유틸리티에 대한 수정자를 생성하기 위해 `$theme-colors` 맵을 루프하는 방법의 두 가지 예입니다.

```scss
// Generate alert modifier classes
@each $color, $value in $theme-colors {
  .alert-#{$color} {
    @include alert-variant(theme-color-level($color, -10), theme-color-level($color, -9), theme-color-level($color, 6));
  }
}

// Generate `.bg-*` color utilities
@each $color, $value in $theme-colors {
  @include bg-variant('.bg-#{$color}', $value);
}
```

### Responsive

이러한 Sass 루프는 컬러 맵에만 국한되지 않습니다. 또한 콤포넌트 또는 유틸리티의 다양한 변형을 생성 할 수 있습니다. 예를 들어 반응형 텍스트 정렬 유틸리티를 사용하면 `$grid-breakpoints` Sass 맵에 대한 `@each` 루프를 미디어 쿼리 include와 혼합 할 수 있습니다.

```scss
@each $breakpoint in map-keys($grid-breakpoints) {
  @include media-breakpoint-up($breakpoint) {
    $infix: breakpoint-infix($breakpoint, $grid-breakpoints);

    .text#{$infix}-left   { text-align: left !important; }
    .text#{$infix}-right  { text-align: right !important; }
    .text#{$infix}-center { text-align: center !important; }
  }
}
```

`$grid-breakpoints`를 수정해야한다면, 그 맵을 반복하는 모든 루프에 변경사항이 적용될 것입니다.

## CSS variables

Bootstrap4에는 컴파일된 CSS에  [CSS 사용자 정의 속성 (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables) 이 약 2 더즌 포함되어 있습니다. 브라우저의 Inspector, 코드 샌드박스 또는 일반적인 프로토 타이핑에서 작업할 때 테마 색상, 브레이크 포인트 및 기본 글꼴 스택과 같이 일반적으로 사용되는 값에 쉽게 액세스할 수 있습니다.

### Available variables

우리가 포함하는 변수는 다음과 같습니다 (`:root`가 필요함에 유의하십시오). 그들은 우리의 `_root.scss` 파일에 있습니다.

```scss
:root {
  --blue: #007bff;
  --indigo: #6610f2;
  --purple: #6f42c1;
  --pink: #e83e8c;
  --red: #dc3545;
  --orange: #fd7e14;
  --yellow: #ffc107;
  --green: #28a745;
  --teal: #20c997;
  --cyan: #17a2b8;
  --white: #fff;
  --gray: #6c757d;
  --gray-dark: #343a40;
  --primary: #007bff;
  --secondary: #6c757d;
  --success: #28a745;
  --info: #17a2b8;
  --warning: #ffc107;
  --danger: #dc3545;
  --light: #f8f9fa;
  --dark: #343a40;
  --breakpoint-xs: 0;
  --breakpoint-sm: 576px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 992px;
  --breakpoint-xl: 1200px;
  --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
```

### Examples

CSS 변수는 Sass 변수와 비슷한 유연성을 제공하지만 브라우저에 제공되기 전에 컴파일 할 필요가 없습니다. 예를 들어 여기에서는 페이지의 글꼴 및 링크 스타일을 CSS 변수로 재설정합니다.

```scss
body {
  font: 1rem/1.5 var(--font-family-sans-serif);
}
a {
  color: var(--blue);
}
```

### Breakpoint variables

우리는 원래 CSS 변수에 브레이크 포인트를 포함시켰지만(예 : `--breakpoint-md`) **이는 미디어 쿼리에서 지원되지 않습니다.** 하지만  미디어 쿼리의 룰셋에서는 계속 사용할 수 있습니다. 이러한 브레이크포인트 변수는 Javascript에서 사용할 수있는 하위 호환성을 위해 컴파일 된 CSS에 남아 있습니다. [Spec에서 자세히 알아보세요.](https://www.w3.org/TR/css-variables-1/#using-variables)

**지원되지 않는 기능**의 예는 다음과 같습니다.

```scss
@media (min-width: var(--breakpoint-sm)) {
  ...
}
```

다음은 **지원 대상**에 대한 예입니다.

```scss
@media (min-width: 768px) {
  .custom-element {
    color: var(--primary);
  }
}
```



> 테마 변경 기능을 지원하는 Sass구조를 찾기 위해 시작한 스터디이다. 기존에 내가 하던 방식은 특정한 컬러 혹은 값에 변수를 선언해두고 테마별로 해당 리스트를 작성해두었다가 import하는 경로를 수정해주며 테마를 적용하는 방식이었다. 대부분의 큰 규모의 디자인 시스템(carbon design system…)은 map과 loop 기능을 활용해 테마를 변경하고 있다. 위 내용중 Sass options 섹션 이하는 도큐멘트만으로 이해가 안된다. 실제 예제를 찾아봐야지!