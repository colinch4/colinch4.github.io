---
layout: post
title: "[swift] Swift Presentr와 함께 사용되는 Debugging 도구"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift Presentr는 iOS 개발자들에게 모달 창을 쉽게 구현할 수 있는 편리한 라이브러리입니다. 하지만 때때로 Presentr을 사용하며 디버깅이 필요할 수 있습니다. 이번 포스트에서는 Swift Presentr을 디버깅하는 도구에 대해 알아보겠습니다.

## 1. LLDB 디버거
LLDB는 Xcode에서 기본으로 제공되는 디버깅 도구입니다. Swift Presentr을 디버깅할 때 LLDB를 사용하면 손쉽게 변수의 값을 확인하거나 디버깅 문제를 해결할 수 있습니다. 아래는 LLDB를 사용하여 Presentr 코드를 디버깅하는 예시입니다.

```swift
(lldb) po presenter
<Presentr.Presentr object at 0x7fb00533cd70>
(lldb) p presenter.dismissOnSwipe
(true)
(lldb) p presenter.transitionType
{Presentr.Transition
  presenting: Presentr.iOS7CoverVerticalTransition,
  dismissing: Presentr.iOS7CoverVerticalTransition}
```

위의 예시에서는 `presenter` 객체의 속성 값을 확인하기 위해 `po`와 `p` 명령어를 사용했습니다. 이를 통해 `dismissOnSwipe`와 `transitionType`의 값을 확인할 수 있습니다.

## 2. Xcode Debug Console
Xcode Debug Console은 코드를 실행하고 디버깅하는 도중에 변수의 값을 출력하거나 확인하기 위한 도구입니다. Presentr을 사용하는 중에 디버깅이 필요할 때, Xcode Debug Console에 원하는 변수를 출력하여 값을 확인할 수 있습니다. 아래는 코드 내에서 변수 값을 출력하는 예시입니다.

```swift
print(presenter.dismissOnSwipe)
print(presenter.transitionType)
```

위의 코드를 실행하면 Debug Console에 해당 변수의 값이 출력됩니다.

## 3. Breakpoints
Breakpoints는 코드 실행 중에 특정 위치에서 일시 중지하여 변수 값을 확인하거나 코드의 흐름을 분석할 수 있는 도구입니다. Presentr 코드에서 특정 부분에서 디버깅이 필요하다면 해당 위치에 Breakpoints를 설정하여 중지할 수 있습니다. 이후에 디버그 창에서 변수와 코드 상태를 살펴볼 수 있습니다.

위의 세 가지 도구를 이용하여 Swift Presentr을 디버깅할 수 있습니다. 디버깅 도구를 사용하면 Presentr을 사용하면서 발생하는 문제를 빠르게 파악하고 해결할 수 있습니다.

더 많은 정보를 얻고 싶다면 [Swift Presentr 공식 문서](https://github.com/IcaliaLabs/Presentr)를 참조해주세요.