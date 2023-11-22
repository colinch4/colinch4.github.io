---
layout: post
title: "[lib] FlexLayout란?"
description: " "
date: 2021-05-14
tags: [swift]
comments: true
share: true
---

## FlexLayout
- AutoLayout을 사용하지 않고 레이아웃을 만들 수 있는 flex yoga 관련 프레임워크

## 사용해야하는 이유
- ios의 UI 종류에는 Xib, StoryBoard, Autolayout, StackView, SwiftUI등이 있다.  이 중에 AutoLayout은 뷰 렌더링시 계산이 많을 수 밖에 없는 구조고 상대적으로 느리고 협업이 어려우며 유지 보수, 코드 리뷰에 어려움이 있다. 또한 SwiftUI도 아직까지 오류가 있어 레이아웃을 짤 때 어려움이 있다.

## FlexLayout의 특징
- Flexbox 레이아웃은 간단하고 강력하며 빠르다.
- FlexLayout 구문은 간결하고 연결 가능하다.
- FlexLayout/Yoga는 빠른 속도로 기존 레이아웃보다 훨씬 빠르다.
- 소스 코드 구조는 플렉스 박스 구조와 일치하므로 쉽게 이해하고 수정할 수 있다. 플렉스 컨테이너는 한 줄에 정의되고 해당 항목(하위)이 삽입된다. 따라서 플렉스박스 구조가 훨씬 더 시각적이고 이해하기 쉽다.
- 왼쪽에서 오른쪽으로(LTR) 및 오른쪽에서 왼쪽으로(RTL) 방향의 언어를 지원한다.

## FlexLayout Performance

<img width="653" alt="스크린샷 2021-05-14 오전 10 28 17" src="https://user-images.githubusercontent.com/45002556/118207202-1a5c7a00-b49f-11eb-83d4-4d59cdd8dc87.png">

- 렌더링 시간이 훨씬 빠른것을 확인할 수 있다.

## 사용법
### Creation, modification and definition of flexbox items      
**1. addItem(:UIView)**    
- Applies to: flex containers
- Returns: FlexLayout interface of the newly added flex item.
**Method:**    
- addItem(_: UIView) -> Flex
**Example:**

```swift
  view.flex.addItem(imageView).width(100).aspectRatio(1)
```

**2. addItem()**    
- Applies to: flex containers
- Returns: FlexLayout interface of the newly created flex item.
**Method:**    
- addItem() -> Flex
**Example:**

```swift
  view.flex.addItem().direction(.row).padding(10)
```

**3. define()**
- Applies to: flex containers
- Parameter: Closure of type (flex: Flex) -> Void
**Method:**    
- define(_ closure: (_ flex: Flex) -> Void)
**Example:**

```swift
  view.flex.addItem().define { (flex) in
      flex.addItem(imageView).grow(1)
        
      flex.addItem().direction(.row).define { (flex) in
          flex.addItem(titleLabel).grow(1)
          flex.addItem(priceLabel)
      }
  }
```

The same results can also be obtained without using the define() method, but the result is not as elegant:
```swift
  let columnContainer = UIView()
  columnContainer.flex.addItem(imageView).grow(1)
  view.flex.addItem(columnContainer)
        
  let rowContainer = UIView()
  rowContainer.flex.direction(.row)
  rowContainer.flex.addItem(titleLabel).grow(1)
  rowContainer.flex.addItem(priceLabel)
  columnContainer.flex.addItem(rowContainer)
```

**4. layout()**
- Applies to: flex containers
-  Values: fitContainer / adjustWidth / adjustHeight
-  Default value: fitContainer
**Method:**
- layout(mode: LayoutMode = . fitContainer)
- The method will layout the flex container's children.

Layout modes:

- fitContainer: This is the default mode when no parameter is specified. Children are layouted inside the container's size (width and height).
- adjustHeight : In this mode, children are layouted using only the container's width. The container's height will be adjusted to fit the flexbox's children
- adjustWidth : In this mode, children are layouted using only the container's height. The container's width will be adjusted to fit the flexbox's children
**Example:**

```swift
rootFlexContainer.flex.layout(mode: .adjustHeight)
```

### Flexbox containers properties
**1. direction()**
- Applies to: flex containers
- Values: column / columnReverse / row / rowReverse
- Default value: column
- CSS name: flex-direction
**Method:**
- direction(_: Direction)

<img width="602" alt="스크린샷 2021-05-14 오후 3 47 59" src="https://user-images.githubusercontent.com/45002556/118232593-c3b96500-b4cb-11eb-9295-831ea3742628.png">

**Example:**

```swift
view.flex.direction(.column)  // Not required, default value. 
view.flex.direction(.row)
```

**2. justifyContent()**
- Applies to: flex containers
- Values: start / end / center / spaceBetween / spaceAround / spaceEvenly
- Default value: start
- CSS name: justify-content
**Method:**
- justifyContent(_: JustifyContent)

<img width="853" alt="스크린샷 2021-05-14 오후 3 49 50" src="https://user-images.githubusercontent.com/45002556/118232781-0713d380-b4cc-11eb-87c6-838e05be44f9.png">

**Example:**

```swift
view.flex.justifyContent(.start)  // default value. 
view.flex.justifyContent(.center)
```

**3. alignItems()**
- Applies to: flex containers
- Values: stretch / start / end / center / baseline
- Default value: stretch
- CSS name: align-items
**Method:**
- alignItems(_: AlignItems)

<img width="523" alt="스크린샷 2021-05-14 오후 3 51 26" src="https://user-images.githubusercontent.com/45002556/118232954-3f1b1680-b4cc-11eb-9d7d-5dc90f6f534e.png">

**4. alignSelf()**
- Applies to: flex containers
- Values: auto / stretch / start / end / center / baseline
- Default value: auto
- CSS name: align-self
**Method:**
- alignSelf(_: AlignSelf)

**5. wrap()**
- Applies to: flex containers
- Values: noWrap / wrap / wrapReverse
- Default value: noWrap
- CSS name: flex-wrap
**Method:**
- wrap(_: Wrap)

<img width="852" alt="스크린샷 2021-05-14 오후 3 53 12" src="https://user-images.githubusercontent.com/45002556/118233155-7ee1fe00-b4cc-11eb-8bbe-0fb91149b989.png">

**Example:**

```swift
view.flex.wrap(.nowrap)  // Not required, default value. 
view.flex.wrap(.wrap)
```

**6. alignContent()**
- Applies to: flex containers
- Values: start / end / center / stretch / spaceBetween / spaceAround
- Default value: start
- CSS name: align-content
**Method:**
- alignContent(_: AlignContent)

<img width="526" alt="스크린샷 2021-05-14 오후 3 54 16" src="https://user-images.githubusercontent.com/45002556/118233274-a5079e00-b4cc-11eb-9603-554e8fa3105a.png">

**7. layoutDirection()**
- FlexLayout supports left-to-right (LTR) and right-to-left (RTL) languages.

Using start or end properties, you can position views without having to think about whether your item will show up on the left or the right side of the screen (depending on the person’s language

**Method:**
- layoutDirection(_: LayoutDirection)

## FlexLayout git 주소
<img width="207" alt="스크린샷 2021-05-14 오전 10 21 11" src="https://user-images.githubusercontent.com/45002556/118206748-1c720900-b49e-11eb-9cfb-8b23c28de32e.png">

https://github.com/layoutBox/FlexLayout

