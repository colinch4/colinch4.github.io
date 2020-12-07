---
layout: post
title: "[안드로이드 기초] Android는 어떻게 UI를 구성할까?(2) - View"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


사실 Inflate하는 과정은 Activity에서 View 객체가 어떻게 눈에 보이게 되는지에 대한 내용이었다. 그렇다면 개별적인 View 객체들은 어떻게 화면에 **그려지고 배치되는** 것일까?

![](https://developer.android.com/images/viewgroup_2x.png)

## Measure, Layout, Draw

뷰는 layout의 root node부터 그리기를 시작한다. Tree 구조로 구성된 뷰의 계층은 전위 탐색을 통해 차례대로 그려지기 때문에 parent 부터 차례대로 그려지기 시작한다.

뷰를 그리는 과정은 Measure, Layout, Draw 순서대로 일어난다.

Measure는 뷰의 크기를 정하는 과정,

Layout은 뷰의 위치를 정하는 과정,

Draw는 최종적으로 View를 Canvas 위에 실제로 그리는 과정이다.

### Measure

measure(int widthMeasureSpec, int heightMeasureSpec)

부모 노드에서 자식 노드를 경유하면서 실행되며, 뷰의 크기를 알아내기 위해 호출된다. 이것은 뷰의 크기를 측정하는 것은 아니며 실제 크기 측정은 onMeasure(int, int)를 통해 이루어진다. measure(int, int)의 내부에서는 onMeasure(int, int)를 호출함으로써 뷰의 크기를 알아낸다.

측정 과정에서는 부모 뷰와 자식 뷰 간의 크기정보를 주고 받기 위해 2가지의 클래스를 사용한다.

**ViewGroup.LayoutParams**

측정되는 View가 부모 View에게 자신이 어떻게 측정되고 위치가 정해지고 싶은지 전달하기 위해 쓰인다. 보통  width와 height가 얼마나 되기를 원하는지 묘사한다. RelativeLayout이나 LinearLayout 같은 ViewGroup의 Subclass를 위한 고유의 ViewGroup.LayoutParams의 SubClass가 존재한다. 자식 View는 자신이 속한 ViewGroup의 Subclass의 LayoutParams를 변경해야한다.

- 숫자 (ex. android:layout_width=”320dp”)
- MATCH_PARENT (ex.android:layout_width=”match_parent”)
- WRAP_CONTENT (ex.android:layout_width=”wrap_content”)

**ViewGroup.MeasureSpec**

부모 View가 자식 View에게 요구사항을 전달하는데 사용된다.

- UNSPECIFIED - 부모 View는 자식 View가 원하는 치수대로 결정한다.
- EXACTLY - 부모 View가 자식 View에게 정확한 크기를 강요한다.
- AT MOST - 부모 View가 자식 View에게 최대 크기를 강요한다.

### Layout

layout(int l, int t, int r, int b)

부모 노드에서 자식 노드를 경유하면서 실행되며, measure에서 측정된 크기를 기반으로 뷰와 자식 뷰들의 위치와 크기를 지정할 때 사용된다. 내부적으로 onLayout()을 호출하고 onLayout()에서 실제 뷰의 위치를 할당하는 구조로 되어있다. onLayout()을 오버라이딩 할 때, 자식 뷰의 layout()을 호출해야한다.

measure()와 layout()함수는 내부적으로 각각 onMeasure()와 onLayout()함수를 호출한다. 이것은 final로 선언된 measure()와 layout() 대신 onMeasure()와 onLayout()을 구현(override)할 것을 장려하기 위해서이다.

뷰의 measure()함수가 반환될 때, 뷰의 getMeasureWidth()와 getMeasureHeight()값이 설정된다. 만약 자식 뷰 측정 값의 합이 너무 크거나 작을 경우 다시 measure()함수를 호출하여 크기를 재측정한다.

### Draw

사이즈와 위치 지정 후에, 뷰가 그려지기 시작한다. onDraw(Canvas)에서 Canvas 객체가 GPU로 보내기 위한 OpenGL-ES 명령어 리스트를 생성하거나 업데이트한다.

---

이를 이용하여 커스텀뷰를 그려보도록 하자.
