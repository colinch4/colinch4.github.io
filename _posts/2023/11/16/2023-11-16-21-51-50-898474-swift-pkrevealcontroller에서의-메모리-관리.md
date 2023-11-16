---
layout: post
title: "[swift] Swift PKRevealController에서의 메모리 관리"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS에서 사용할 수 있는 오픈 소스 라이브러리로, 네비게이션 사이드 메뉴 기능을 제공합니다. 그러나 PKRevealController를 사용할 때 메모리 관리에 유의해야 합니다. 이 글에서는 Swift에서 PKRevealController를 사용할 때 메모리 누수를 방지하는 방법에 대해 알아보겠습니다.

## 1. 약한 참조 (Weak reference) 사용하기
PKRevealController의 주요 클래스인 PKRevealController는 메인 뷰 컨트롤러와 사이드 메뉴 뷰 컨트롤러 간에 참조 관계를 가지기 때문에 메모리 관리에 주의해야 합니다. 이를 위해 강한 참조 대신 약한 참조를 사용해야 합니다.

```swift
weak var revealController: PKRevealController?
```

위와 같이 `weak` 키워드를 사용하여 약한 참조로 선언하면, 메모리 누수를 방지할 수 있습니다. 이렇게 선언된 약한 참조는 참조 대상이 해제되면 자동으로 `nil`로 설정됩니다.

## 2. 델리게이트 패턴 활용하기
PKRevealController의 메인 컨트롤러와 사이드 메뉴 컨트롤러 간의 상호 작용은 델리게이트 패턴을 통해 이루어집니다. 이 때 주의할 점은 강한 참조를 사용하지 않도록 해야 합니다. 대신 약한 참조로 선언하여 메모리 누수를 방지해야 합니다.

```swift
weak var delegate: PKRevealControllerDelegate?
```

## 3. 옵저버 패턴 활용하기
PKRevealController의 상태 변화를 감지하고 싶은 경우 옵저버 패턴을 활용할 수 있습니다. 이 때도 약한 참조를 사용하여 메모리 누수를 방지해야 합니다.

```swift
weak var observer: PKRevealControllerObserver?
```

## 4. weak self 사용하기
PKRevealController를 사용하는 클로저나 비동기 작업에서는 강한 참조로 인한 메모리 누수를 방지하기 위해 `weak self`를 활용해야 합니다.

```swift
apiClient.fetchData { [weak self] result in
    guard let self = self else { return }
    // self를 사용하는 로직 작성
}
```

위와 같이 `weak self`로 클로저를 감싸고 `guard` 문을 사용하여 self를 옵셔널 바인딩하여 사용하면, self가 해제되었을 때 클로저가 실행되지 않습니다.

## 5. 메모리 해제 확인하기
메모리 누수를 방지하기 위해 약한 참조를 사용했는지 확인하기 위해 메모리를 해제하는 시점을 확인할 수 있습니다. 이를 위해 `deinit` 메서드를 사용하여 메모리 해제시 실행되는 코드를 작성할 수 있습니다.

```swift
deinit {
    print("PKRevealController 메모리 해제")
}
```

위와 같이 `deinit` 메서드 내에 로그를 출력하는 코드를 작성하면, 메모리 해제시 해당 로그가 출력됩니다.

위에서 언급한 방법들을 적절히 활용하여 PKRevealController를 사용할 때 메모리 누수를 방지할 수 있습니다. 이렇게 한 번에 모든 참조를 해제하고 메모리를 관리하기 위해 ARC(Automatic Reference Counting) 라는 메모리 관리 시스템을 활용하는 것이 중요합니다.

<br>

#### 참고 자료
- PKRevealController 공식 GitHub 저장소: [https://github.com/pkluz/PKRevealController](https://github.com/pkluz/PKRevealController)
- Swift ARC 소개 문서: [https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)