---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UICollectionView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UICollectionView는 iOS 애플리케이션에서 아이템 목록을 표시하기 위한 유용한 컴포넌트입니다. 대부분의 경우, UICollectionView에서 아이템을 선택하거나 터치하는 경우에 대한 이벤트 처리가 필요합니다. UIResponder를 사용하여 이러한 이벤트를 처리하는 방법에 대해 알아보겠습니다.

## 1. UIResponder 서브 클래스 만들기
UICollectionView에서 발생한 터치 이벤트를 처리하기 위해 우선 UIResponder를 상속한 서브 클래스를 만들어야 합니다. 다음과 같이 코드를 작성해보겠습니다.

```swift
import UIKit

class CustomResponder: UIResponder {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 시작될 때 처리할 동작 작성
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 끝났을 때 처리할 동작 작성
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 이동하는 중일 때 처리할 동작 작성
    }
}
```

CustomResponder 클래스에서는 UIResponder의 touch 관련 메서드를 오버라이드하여 실제로 처리할 동작을 작성합니다. touchesBegan 메서드는 터치가 시작되었을 때 동작하며, touchesEnded 메서드는 터치가 끝났을 때 동작하고, touchesMoved 메서드는 터치가 이동하는 중일 때 동작합니다.

## 2. UICollectionViewDelegate에 CustomResponder 등록하기
UICollectionViewDelegate 프로토콜을 구현한 클래스에서 CustomResponder를 등록해야 합니다. 다음과 같이 코드를 작성해보겠습니다.

```swift
import UIKit

class ViewController: UIViewController, UICollectionViewDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()

        let collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: UICollectionViewFlowLayout())
        collectionView.delegate = self
        // UICollectionViewDelegate를 구현한 클래스의 인스턴스를 UICollectionView의 delegate로 설정
        view.addSubview(collectionView)
    }

    // UICollectionViewDelegate의 메서드 구현
    // ...
}
```

위의 코드에서 ViewController는 UICollectionViewDelegate 프로토콜을 구현하고 있습니다. collectionView.delegate에 CustomResponder 인스턴스를 설정하여 CustomResponder의 터치 이벤트를 처리하도록 합니다.

## 3. 터치 이벤트 처리하기
이제 CustomResponder에 작성한 터치 이벤트 처리 메서드를 구현하기만 하면 됩니다. 다음은 터치가 시작되었을 때 아이템을 선택하고, 터치가 끝났을 때 아이템 선택을 해제하는 예제입니다.

```swift
import UIKit

class CustomResponder: UIResponder {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first, let collectionView = self.next as? UICollectionView else {
            return
        }

        let touchPoint = touch.location(in: collectionView)
        if let indexPath = collectionView.indexPathForItem(at: touchPoint) {
            collectionView.selectItem(at: indexPath, animated: true, scrollPosition: .centeredVertically)
        }
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first, let collectionView = self.next as? UICollectionView else {
            return
        }

        let touchPoint = touch.location(in: collectionView)
        if let indexPath = collectionView.indexPathForItem(at: touchPoint) {
            collectionView.deselectItem(at: indexPath, animated: true)
        }
    }
}
```

위의 예제에서는 터치가 발생한 좌표를 이용하여 UICollectionView의 indexPathForItem 메서드를 호출하여 선택된 아이템을 찾습니다. 터치가 시작되었을 때는 해당 아이템을 선택하고, 터치가 끝났을 때는 선택된 아이템을 해제합니다.

이렇게 UIResponder를 사용하여 UICollectionView에서의 터치 이벤트를 처리할 수 있습니다. UIResponder는 다른 UI 컴포넌트에서도 사용할 수 있는 범용적인 이벤트 처리 방법이므로, 다른 컴포넌트에서도 유용하게 활용할 수 있습니다.

참고 자료:
- [UIKit - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)