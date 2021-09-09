---
layout: post
title: "[Sass] import-once 믹스인으로 스타일 유출 방지하기"
description: " "
date: 2021-09-09
tags: [Sass]
comments: true
share: true
---


# import-once 믹스인으로 스타일 유출 방지하기

`mixin`과 `incloud`를 통해 한번 호출된 스타일이 여러번 호출 되거나 복제되는 것을 방지합니다. 콤포넌트의 캡슐화와 독립 실행을 위해 Sass파일들의 의존성을 선언할 수 있어 깔끔합니다.

먼저 `_import-once.scss`파일을 생성하여 `export`에 대한 믹스인을 정의합니다.

```scss
$imported-modules: () !default;

/// Module export mixin
/// This mixin helps making sure a module is imported once and only once.
/// @access public
/// @param {String} $name - Name of exported module
/// @param {Bool} $warn [true] - Warn when module has been already imported
/// @require $imported-modules
@mixin exports($name, $warn: true) {
  @if (index($imported-modules, $name) == null) {
    $imported-modules: append($imported-modules, $name) !global;
    @content;
  } @else if $warn == true {
    @warn "Module `#{$name}` has already been imported.";
  }
}
```

독립적으로 구성하고자 하는 모든 콤포넌트는 아래와 같은 작성 규칙을 따릅니다.

```scss
@import '../import-once';

@include exports('component-name') {
    //define component styles
}
```

추후 위 콤포넌트가 여러 Sass파일에서 호출 되더라도 `component-name`에 대한 스타일은 한번만 선언 됩니다.

## 📖 Reference

[sass-import-once](https://github.com/wilsonpage/sass-import-once)

