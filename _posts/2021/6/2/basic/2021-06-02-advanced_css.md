---
layout: post
title: "[css] Advanced CSS"
description: " "
date: 2021-06-02
tags: [css]
comments: true
share: true
---

## Advanced CSS

<br>

## 1. Transitions

> 트랜지션이란?
>
> 어떤 상태에서 다른 상태로의 "변화"를 애니메이션으로 만드는 방법이다

<br>

### Transitions의 속성

- 어떤 효과가 필요할 때 쓰인다.

- state가 없는 요소에 붙어야 된다.

  - 변화가 처음 생겨난 곳(root), element에 `transition`이 있어야 된다. (변화한 곳(state)에 있으면 안된다.)

- 순서

  - 먼저 어떤 것을 변화하게 만들 것인지 써야된다.
  - 그다음엔 얼마나 오래동안 변화가 일어나게 할지 정한다.
  - ex)

  ```css
  a {
    background-color: violet;
    color: white;
    text-decoration: none;
    padding: 3px 5px;
    border-radius: 5px;
    font-size: 50px;
    /* 
      transition은 root인 element에 작성해야된다. 
      transition: `변화를 주고싶은 상태 or all` `변화지속시간` `효과`
      */
    transition: background-color 0.5s ease-in-out;
  }

  a:hover {
    color: black;
    /* background-color의 변화가 없으면 transition변화를 주어도 소용이 없다. */
    background-color: wheat;
  }
  ```

- 원한다면 더 많은 transition을 추가할 수 있다.

<br>

### 효과

> 애니메이션이 어떻게 변할지 말해주는 것

- 기본 효과 종류

  - linear
  - ease-in
  - ease-out
  - ease-in-out

- 또한 `cubic-bezier`를 통해 효과를 customizing 할 수 있다.

  - ```css
    transition: background-color 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    ```

- 효과를 따로주고 싶으면 `,(콤마)`를 이용하여 따로 적용한다.

  - ```css
    transition: background-color 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55),
    border-radius 5s ease-in-out;

    background-color는 0.5s 동안 변하고
    border-radius는 5s 동안 변한다.
    ```

- [Transition 효과 참조 사이트](https://matthewlein.com/tools/ceaser)

<br><br>

## 2. Transformations

> `transform` 이란?
>
> 어떤 형태이든지 변화 시킬 수 있는 것을 말한다.

<br>

### 특징

- transformation은 box element를 변형시키지 않는다.

- padding, margin이 적용되지 않는다. 일종의 3D transformation이기 때문이다.

- 즉, 다른 요소의 box를 변형시키지 않고 원하는 요소를 이동시키기 위해서 사용

- 예시
  ```css
  img {
    transform: scale(2, 2) translateX(300px);
  }
  ```

<br><br>

## 3. Animation

> 마우스 위에 올리거나, transition 없이 자동으로 변화시킬려면 엇떻게 해야될까?

- 우리는 `animation`을 통해 원하는 만큼 애니메이션을 만들고 재생시킬 수 있다.

<br>

### 한 지점에서 부터 다른 두 번째 지점까지의 애니메이션을 만들고 싶을 때

- rotateY(0)인 지점에서 rotateY(360deg)까지의 변화를 애니메이션으로 만들 때

  - ```css
    @keyframes 애니메이션 이름 {
        from {
            처음 지점
        }
        to {
            다른 두 번째 지점
        }
    }

    animation: 애니메이션이름 변화시간 효과;
    ```

  - ```css
    @keyframes superSexyCoinFlip {
      from {
        transform: rotateY(0);
      }

      to {
        transform: rotateY(360deg);
      }
    }
    img {
      border: 5px solid black;
      border-radius: 50%;
      <!-- infinite를 빼면 한번만 효과가 나타나고 쓰면 무한반복 -->
      animation: superSexyCoinFlip 3s ease-in-out infinite;
    }
    ```

<br>

### 되돌리기도 애니메이션으로 만들고 싶을 때

- 퍼센테이지로 단계를 나눠서 애니메이션을 만들 수 있다.

- 단계를 0%, 50%, 100% 나눠서 애니메이션을 만들어 되돌릴때도 애니메이션이 적용되고 만들 수 있다.
- 단계는 원하는 대로 만들 수 있다. (10%, 20%, 35%...)

- ```css
  @keyframes superSexyCoinFlip {
    0% {
      transform: rotateY(0);
    }

    50% {
      transform: rotateY(360deg) translateY(-100px);
    }

    100% {
      transform: rotateY(0);
    }
  }
  img {
    border: 5px solid black;
    border-radius: 50%;
    animation: superSexyCoinFlip 3s ease-in-out infinite;
  }
  ```

<br>

### 참조 사이트

- https://animista.net/

<br><br>

## Media Queries

### Media query란?

- Media query는 오직 CSS만을 이용해서 스크린의 사이즈를 알 수 있는 방법이다.
- 그리고 이를 이용하여 우리는 스크린의 사이즈에 따라서 CSS를 바꿀 수 있고 이것을 `Responsive Website` 라고 한다.

<br>

### 예시

- ```css
    @media screen and (원하는 사이즈) {
      원하는 CSS 스타일 작성
    }
  ```
- ```css
    @media screen and (max-width: 800px) {
      div {
        background-color: violet;
      }
    }

    스크린의 사이즈가 최대 스크린의 너비가 800px까지는 background-color:violet; 이라는 뜻
  ```

- ```css
  @media screen and (min-width: 900px) and (max-width: 1300px) {
    div {
      background-color: turquoise;
    }
  }
  이 조건은 스크린의 너비가 900px ~ 1300px 사이에 있을때만 적용 된다는 뜻
  ```

- ```css
  @media screen and (min-width: 800px) and (max-width: 1000px) and (orientation: landscape) {
    background-color: black;
  }

  스크린의 너비가 800 ~ 1000px 이고 스크린이 가로모드일때 background-color가 black이라는 뜻
  ```
