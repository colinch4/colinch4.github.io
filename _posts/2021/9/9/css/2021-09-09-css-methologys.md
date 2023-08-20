---
layout: post
title: "[css] CSS 방법론"
description: " "
date: 2021-09-09
tags: [css]
comments: true
share: true
---

## CSS 방법론

한 2년전에 공부했던 내용이지만, 복기하는 차원에서 TIL에 올려본다.
이중 BEM을 제일 유용하게 활용했고 Atomic을 추가로 학습했으며 최근에는 Utility-first CSS에 대해 관심을 갖고 있다.

## [OOCSS(Object Oriented CSS)](https://www.keycdn.com/blog/oocss/)

OOCSS의 목적은 코드 재사용성을 높이고, 궁극적으로는 더 빠르고 효율적이며 유지보수하기 용이한 스타일시트를 만드는 것이다. **결합도 낮추기(decoupling)**, **단일 책임의 원칙(single responsibility principle)**, **캡슐화(encapsulation)** 를 강조하는 방법론이다.

OOCSS는 스타일의 특징(feature)에 따라 범주를 분리하여 구조적으로 선택자들을 적용할 수 있게한다.

- Separation of structure from skin - 스킨으로부터 구조분리
- Separation of containers and content - 컨테이너와 콘텐츠의 분리

## [SMACSS (Scalable and Modular Architecture for CSS) - Jonathan Snook](http://smacss.com/)

SMACSS는 엄격한 프레임워크 보다는 스타일 가이드에 초점을 맞추며, 디자인 프로세스 진단과 기존의 경직된 프레임워크를좀 더 유연하게 만드는 것을 목표로 하고 있다.

SMACSS의 핵심은 범주화(categorization)를 통한 패턴화이다.

CSS를 베이스base, 레이아웃layout, 모듈module, 상태state, 테마theme의 5개 범주로 분류할 수 있다. 각 범주는 엄격한 분리는 아니고 느슨한 분리이므로 공통 범위가 있을 수 있다

[Base rules](https://smacss.com/book/type-base)

- 요소 선택자(element selector)에 적용하는 스타일
- Reset, Variable등을 포함하는 기본스타일

[Layout rules](https://smacss.com/book/type-layout)

- 페이지를 섹션으로 구조적으로 나누는 것
- 레이아웃은 하나 이상의 모듈을 포함한다
- prefix `l-`를 붙인다

[Module rules](https://smacss.com/book/type-module)

- 모듈 관련 스타일로 재사용을 위한 요소
- table, icon, box같이 재사용성 높은 요소를 정의한다
- 재사용을 위해 id 선택자와 element를 사용하지 않는다

[State rules](https://smacss.com/book/type-state)

- 요소의 상태 전환을 표현하기 위한 스타일
- prefix `is-`나 `s-`를 붙인다

[Theme rules](https://smacss.com/book/type-theme)

- 전반적인 Look and feel을 정의한다
- 색상, 배경, 글꼴, 테두리 등을 불변하는 스타일과 분리
- prefix `theme-`을 붙이거나 `theme/`과 같은 디렉토리로 계층 분리

## [BEM(Block-Element-Modifier)](https://en.bem.info/methodology/key-concepts/)

BEM은 웹페이지를 컴포넌트들의 조합으로 바라보고 접근한 방법론이다. CSS의 일관성과 재사용성을 고려했다.

### [Block](https://en.bem.info/methodology/key-concepts/#block)

재사용이 가능하며 기능적으로 독립적인 페이지 컴포넌트

- [블록(Block) 이름](https://en.bem.info/methodology/naming-convention/#block-name)은 `상태`가 아닌 `목적` "어떤 것인가?" (`menu` 또는 `button`)를 설명한다
- 블록은 외부 여백`margin`이나 `position`을 설정할 수 없다
- `ID 선택자` 사용을 금지한다

### [Element](https://en.bem.info/methodology/key-concepts/#element)

블록 안에서 특정 기능을 수행하는 컴포넌트. 외부에서 혹은 독립적으로 사용할 수 없다

- [요소(Element) 이름](https://en.bem.info/methodology/naming-convention/#element-name)은 `상태`가 아닌 `용도` "어떤것인가?" (`item`, `text` 등)를 설명한다
- 요소 이름은 블록 이름과 duble underscore (`__`)로 구분된다
  ```css
  block-name__element-name
  ```
- 요소는 항상 블록의 일부이며 블록과 분리될 수 없으며, 요소끼리 중첩될 수 있다

### [Modifier](https://en.bem.info/methodology/key-concepts/#modifier)

Block, Element의 모양(외관)과 동작(상태)을 정의한다

- [modifier 이름](https://en.bem.info/methodology/naming-convention/#block-modifier-name)은 `외관` "어떤 크기인가?", "어떤 디자인 테마인가?" (`size_s` 또는 `theme_islands`), `상태` "다른 것과 어떻게 다른가?" (`disabled`, `focused` 등) 그리고 `행동` "동작은 어떠한가?"또는 "사용자에게 어떻게 반응하는가?" (`directions_left-top` 등)을 정의한다
- modifier의 이름은 요소 이름과 single underscore(`_`)로 구분한다
- 수정자는 수정 된 블록 또는 요소와 분리하여 사용할 수 없다.

BEM은 다시 한번 전체 복습하는 시간을 가져야지.