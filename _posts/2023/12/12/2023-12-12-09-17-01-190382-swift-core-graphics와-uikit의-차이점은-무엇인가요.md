---
layout: post
title: "[swift] Swift Core Graphics와 UIKit의 차이점은 무엇인가요?"
description: " "
date: 2023-12-12
tags: [swift]
comments: true
share: true
---

Core Graphics는 그래픽 연산에 대한 더 직접적인 접근을 제공하며, 그래픽 컨텍스트를 사용하여 그림을 그리고 변형시키는 데 중점을 둡니다. UIView와 같은 UI 구성 요소나 이벤트 처리와 같은 동작을 처리하는 데는 적합하지 않습니다. 반면에 UIKit은 터치 이벤트 처리, 애니메이션, 레이아웃 관리 등을 포함한 사용자 인터페이스 기능에 더 중점을 둡니다.

따라서, Core Graphics는 주로 사용자 정의한 사용자 인터페이스 요소나 그래픽적인 작업을 수행하는 데 활용되며, UIKit은 앱의 전반적인 사용자 인터페이스를 개발하는 데 사용됩니다. 두 프레임워크는 서로 보완적으로 사용되어 iOS 애플리케이션의 그래픽 기능을 효과적으로 구현할 수 있습니다.