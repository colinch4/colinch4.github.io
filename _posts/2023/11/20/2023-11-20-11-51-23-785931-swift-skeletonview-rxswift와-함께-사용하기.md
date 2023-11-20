---
layout: post
title: "[swift] Swift SkeletonView RxSwift와 함께 사용하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

## 소개
SkeletonView는 iOS 앱에서 로딩 중인 내용을 시각적으로 표현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 로딩 중인 데이터나 컨텐츠를 일시적으로 희미하게 보여줄 수 있어 사용자 경험을 향상시킬 수 있습니다. 이번 포스트에서는 SkeletonView를 RxSwift와 함께 사용하는 방법에 대해 알아보겠습니다.

## 시작하기 전에
SkeletonView와 RxSwift를 함께 사용하기 위해서는 아래의 사전 요구 사항을 충족해야 합니다.
- Swift 4.0 이상의 버전
- iOS 10.0 이상의 버전
- RxSwift 및 RxCocoa 라이브러리

## 설치
SkeletonView와 RxSwift는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음과 같이 라이브러리를 추가합니다.

```ruby
pod 'SkeletonView'
pod 'RxSwift'
pod 'RxCocoa'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

## 사용 방법
SkeletonView를 사용하여 RxSwift로 데이터 로딩 중 상태를 표시하려면 다음 단계를 따르세요.

### 1. SkeletonView 설정
SkeletonView를 사용하기 위해 앱의 스타일 파일에 다음 코드를 추가하세요.

```swift
import SkeletonView

func applySkeletonViewStyle() {
    // SkeletonView 스타일을 설정하는 코드
    UITableView.appearance().defaultHeaderBackgroundColor = .white
    UITableView.appearance().defaultFooterBackgroundColor = .white
    UITableViewCell.appearance().backgroundColor = .white
}
```

### 2. RxSwift 및 RxCocoa import
SkeletonView와 함께 RxSwift를 사용하려면 RxSwift 및 RxCocoa를 import 해야 합니다.

```swift
import RxSwift
import RxCocoa
```

### 3. ViewController에 SkeletonView 적용
SkeletonView는 UIView 확장으로 제공되므로, ViewController에서 해당 확장을 사용하여 SkeletonView를 적용할 수 있습니다. 예를 들어, UITableView에 SkeletonView를 적용하려면 다음과 같이 코드를 작성하세요.

```swift
import SkeletonView

class MyViewController: UIViewController {
    @IBOutlet weak var tableView: UITableView!

    private let disposeBag = DisposeBag()

    override func viewDidLoad() {
        super.viewDidLoad()

        applySkeletonViewStyle()

        // SkeletonView를 활성화하고 tableView에 적용
        tableView.isSkeletonable = true
        tableView.showAnimatedGradientSkeleton()
        
        // 데이터 로딩 완료 후 SkeletonView 숨기기
        fetchData()
            .observeOn(MainScheduler.instance)
            .subscribe(onNext: { [weak self] data in
                self?.tableView.reloadData() // 데이터 로딩 후 tableView 업데이트
                self?.tableView.hideSkeleton(transition: .crossDissolve(0.25)) // SkeletonView 숨기기
            })
            .disposed(by: disposeBag)
    }
}
```

위의 코드에서는 `applySkeletonViewStyle()` 함수를 사용하여 SkeletonView의 스타일을 설정하고, `tableView.isSkeletonable = true`와 `tableView.showAnimatedGradientSkeleton()`를 사용하여 SkeletonView를 활성화하고 표시합니다. 그리고 `fetchData()` 함수를 사용하여 데이터를 가져온 후에는 `tableView.reloadData()`를 호출하여 tableView를 업데이트하고, `tableView.hideSkeleton()`를 사용하여 SkeletonView를 숨깁니다.

## 결론
이렇게 SkeletonView를 RxSwift와 함께 사용하여 로딩 중인 상태를 시각적으로 표현할 수 있습니다. SkeletonView는 사용자 경험을 향상시키는 간단하면서도 유용한 도구입니다. RxSwift와 함께 사용하면 비동기 작업에 쉽게 적용할 수 있습니다.

더 자세한 내용을 알고 싶다면 아래 참고 자료를 확인해보세요.

## 참고 자료
- [SkeletonView GitHub 저장소](https://github.com/Juanpe/SkeletonView)
- [RxSwift GitHub 저장소](https://github.com/ReactiveX/RxSwift)