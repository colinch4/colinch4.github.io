---
layout: post
title: "[swift] Swift SkeletonView Combine과 함께 사용하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift SkeletonView는 로딩 중인 상태를 시각적으로 표현하기 위한 라이브러리입니다. 보다 사용자 친화적인 앱 경험을 제공하기 위해 UITableView, UICollectionView, UIView 등에 SkeletonView를 추가할 수 있습니다. 

Combine은 Swift 5에서 도입된 새로운 프레임워크로, 비동기적인 작업의 처리를 간편하게 해줍니다. Combine은 주로 데이터 스트림의 조작, 변형, 구독, 비동기 작업과의 결합 등에 사용되며, 이러한 기능과 SkeletonView를 함께 사용하면 앱의 성능과 사용자 경험을 더욱 개선할 수 있습니다.

이번 글에서는 Swift SkeletonView를 Combine과 함께 사용하는 방법에 대해 알아보겠습니다.

## SkeletonView와 Combine 통합하기

SkeletonView를 UIKit 뷰에 적용하기 위해서는 일반적으로 UIView의 extension을 작성하고, 해당 뷰에 SkeletonView 프로토콜을 채택하여 구현하는 방법을 사용합니다. 그러나 Combine을 사용하는 경우, UI 업데이트와 관련된 작업은 주로 데이터 스트림에 의해 트리거됩니다.

SkeletonView를 Combine과 통합하기 위해서는, Combine의 Publisher와 Subscriber를 사용하여 SkeletonView에 대한 구독과 취소를 처리해야합니다. 다음은 SkeletonView를 Combine과 함께 사용하는 간단한 예제 코드입니다.

```swift
import UIKit
import SkeletonView
import Combine

class ViewController: UIViewController {

    @IBOutlet weak private var tableView: UITableView!
    
    private var cancellables = Set<AnyCancellable>()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // SkeletonView 구독 생성
        tableView.publisher(for: \.skeletonDataSource)
            .sink(receiveValue: { [weak self] _ in
                self?.tableView.showSkeleton()
            })
            .store(in: &cancellables)
    }
    
    // 뷰가 사라질 때 구독 취소
    override func viewDidDisappear(_ animated: Bool) {
        super.viewDidDisappear(animated)
        
        cancellables.forEach { $0.cancel() }
        cancellables.removeAll()
    }
    
    // SkeletonView 설정
    private func setupSkeletonView() {
        // SkeletonView global 설정
        SkeletonAppearance.default.tintColor = .gray
        SkeletonAppearance.default.gradient = SkeletonGradient(baseColor: .lightGray)
        SkeletonAppearance.default.multilineCornerRadius = 5
        //...
    }
}
```

위 코드에서는 UITableView의 `skeletonDataSource` 프로퍼티의 변경을 구독하고, 해당 프로퍼티가 변경되면 SkeletonView를 활성화합니다. 이렇게 함으로써 Combine을 이용해 SkeletonView를 관리할 수 있게 됩니다.

추가적으로, `viewDidDisappear(_:)` 메서드에서는 Combine 구독 취소를 처리합니다. 이는 해당 view controller가 해제될 때 메모리 누수를 방지하기 위한 조치입니다.

## 결론

Swift SkeletonView와 Combine을 함께 사용하면 앱의 로딩 상태를 시각적으로 표현하는데 더욱 편리하고 강력한 방법을 제공합니다. Combine의 Publisher와 Subscriber를 사용하여 SkeletonView에 대한 구독과 취소를 처리할 수 있으며, 이를 통해 사용자 경험을 개선하고 앱의 성능을 높일 수 있습니다.

Swift SkeletonView와 Combine을 통합하여 사용하는 방법에 대해 알아보았습니다. 이를 참고하여 앱 개발에 적용해보시기 바랍니다.

## 참고 자료

- [SkeletonView Github 레포지토리](https://github.com/Juanpe/SkeletonView)
- [Combine Documentation](https://developer.apple.com/documentation/combine/)