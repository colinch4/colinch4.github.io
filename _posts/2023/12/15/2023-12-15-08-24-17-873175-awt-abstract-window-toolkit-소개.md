---
layout: post
title: "[java] AWT (Abstract Window Toolkit) 소개"
description: " "
date: 2023-12-15
tags: [java]
comments: true
share: true
---

자바의 AWT (Abstract Window Toolkit)는 그래픽 사용자 인터페이스(GUI)를 만들기 위한 도구입니다. AWT는 윈도우, 버튼, 텍스트 필드, 체크박스 등과 같은 GUI 구성 요소를 제공하여 다양한 플랫폼에서 동일한 모양과 동작을 제공합니다.

## AWT의 주요 기능

AWT는 다음과 같은 주요 기능을 제공합니다:
- 그래픽 및 동작 관리
- 이벤트 처리
- 컴포넌트 (버튼, 텍스트 상자 등) 및 레이아웃 관리

## AWT의 장점과 단점

### 장점
- AWT는 자바의 일부이기 때문에, 브라우저나 운영 체제에 상관없이 동일한 모양과 동작을 제공합니다.
- 소스 코드가 간단하고 직관적입니다.

### 단점
- AWT의 컴포넌트는 운영 체제에서 제공하는 기본적인 GUI 컴포넌트와 같은 모양을 가지며, 특정 운영 체제에 종속될 수 있습니다.
- 세부적인 디자인을 다루기에는 부족할 수 있습니다.

자바 1.2부터 Swing과 같은 더 나은 대안이 나오면서, AWT는 거의 사용되지 않게 되었지만, AWT는 아직도 기본적인 그래픽 사용자 인터페이스를 만들기 위한 간단한 도구로 사용될 수 있습니다.

더 자세한 내용은 [Oracle Java AWT Documentation](https://docs.oracle.com/en/java/javase/11/docs/api/java.desktop/java/awt/package-summary.html)를 참고하세요.