---
layout: post
title: "[swift] Designated 초기화와 Convenience 초기화의 차이점"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

iOS 개발을 하다 보면 초기화(initialization)와 관련된 개념들을 자주 접하게 됩니다. Swift에서는 이러한 초기화 과정을 Designated 초기화와 Convenience 초기화로 나누어 설명합니다. 이번 포스트에서는 Designated 초기화와 Convenience 초기화의 차이점에 대해 알아보도록 하겠습니다.

## Designated 초기화 (Designated Initialization)
Designated 초기화란 클래스의 주요 초기화 메서드입니다. 클래스의 모든 속성을 초기화하고, 슈퍼클래스의 초기화 메서드를 호출하거나, 서브클래스에서 재정의할 수 있도록 해줍니다. 즉, 클래스에는 반드시 하나 이상의 Designated 초기화 메서드가 있어야 합니다.

Designated 초기화 메서드는 `init` 키워드를 사용하여 정의합니다. Designated 초기화 메서드는 다른 Designated 초기화 메서드 또는 Convenience 초기화 메서드를 호출할 수 있습니다. 만약 슈퍼클래스를 상속받은 클래스라면 슈퍼클래스의 Designated 초기화 메서드도 호출해야 합니다.

## Convenience 초기화 (Convenience Initialization)
Convenience 초기화란 클래스의 편의 초기화 메서드입니다. Designated 초기화의 특정한 경우에 대한 편의 기능을 제공합니다. Convenience 초기화 메서드는 클래스 내에서 다른 초기화 메서드를 호출하여 초기화 과정을 간소화할 수 있습니다.

Convenience 초기화 메서드는 `convenience init` 키워드를 사용하여 정의합니다. Convenience 초기화 메서드는 동일한 클래스에서 다른 초기화 메서드를 호출해야 하며, 맨 마지막에는 반드시 Designated 초기화 메서드를 호출해야 합니다.

## Designated 초기화와 Convenience 초기화의 관계
Designated 초기화 메서드는 클래스의 초기화를 담당하며, Convenience 초기화 메서드는 편의적인 초기화를 제공합니다. 클래스의 초기화 메서드가 Designated 초기화 메서드와 Convenience 초기화 메서드로 구성된 경우, 여러 Convenience 초기화 메서드를 제공할 수 있으나, Designated 초기화 메서드는 하나만 제공해야 합니다.

상속 관계에서는 서브클래스의 Designated 초기화 메서드는 반드시 슈퍼클래스의 Designated 초기화 메서드를 호출해야 합니다. Convenience 초기화 메서드는 상속받은 Designated 초기화 메서드를 호출하거나 override하여 재정의할 수 있습니다.

## 마무리
Designated 초기화와 Convenience 초기화는 클래스의 초기화 과정에서 중요한 역할을 합니다. 이해하고 사용하는 것은 Swift 개발에서 기본적인 동작을 이해하는 데 필수적입니다. Designated 초기화는 주요 초기화로써 모든 속성을 초기화하고, 슈퍼클래스의 초기화 메서드를 호출하는 역할을 합니다. Convenience 초기화는 Designated 초기화의 특정한 경우에 대해 간소화된 초기화를 제공하는 역할을 합니다.

더 자세한 내용은 Swift 공식 문서를 참고하시기 바랍니다.

- [Swift 공식 문서 - Initialization](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html)