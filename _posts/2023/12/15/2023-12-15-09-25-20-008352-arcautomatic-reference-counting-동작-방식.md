---
layout: post
title: "[swift] ARC(Automatic Reference Counting) 동작 방식"
description: " "
date: 2023-12-15
tags: [swift]
comments: true
share: true
---

ARC는 Swift에서 메모리를 관리하기 위한 기술 중 하나로, 자동 참조 계산이라고도 합니다. ARC는 앱이 메모리를 더 이상 사용하지 않을 때 자동으로 메모리를 해제하여 효율적인 메모리 관리를 제공합니다. 이 기술은 Swift 언어의 핵심적인 부분이며, 올바른 사용에 따라 메모리 누수를 방지할 수 있습니다.

## ARC의 동작 원리
ARC는 객체가 참조된 횟수를 추적하고, 해당 객체를 더 이상 참조하지 않을 때 메모리에서 해제합니다. 이를 통해 메모리를 효율적으로 관리할 수 있습니다. ARC는 strong 참조, weak 참조, unowned 참조와 같은 다양한 종류의 참조를 제공하여 메모리 관리에 유용하게 활용됩니다.

## Strong 참조와 메모리 해제
객체 간의 strong 참조는 서로를 참조하는 경우에 발생합니다. 이 때 각 객체는 다른 객체를 강하게 참조하게 되며, 해당 참조가 끊기지 않는 한 메모리에서 제거되지 않습니다. 이러한 경우에 메모리 누수가 발생할 수 있으므로 주의가 필요합니다.

## Weak 참조와 메모리 관리
weak 참조는 다른 객체를 가리키지만, 해당 객체를 강하게 참조하지 않는 경우에 사용됩니다. weak 참조는 순환 참조(retain cycle)를 방지하여 메모리 누수를 방지한다는 점에서 유용합니다.

ARC는 Swift의 핵심 기술이며, 올바른 참조 관리를 통해 안정적인 애플리케이션을 구축할 수 있도록 도움을 줍니다.

참조:
- [Swift 공식 문서](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)
- [애플 개발자 문서](https://developer.apple.com/library/archive/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html)