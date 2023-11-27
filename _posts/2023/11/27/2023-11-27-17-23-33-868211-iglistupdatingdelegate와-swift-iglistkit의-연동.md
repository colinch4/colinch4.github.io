---
layout: post
title: "[swift] IGListUpdatingDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개
IGListUpdatingDelegate는 IGListKit을 사용하여 데이터 업데이트를 수행하는 데 사용되는 프로토콜입니다. IGListKit은 UICollectionView를 대체할 수 있는 도구로서, 복잡한 데이터 표시 및 업데이트 작업을 처리할 수 있습니다. IGListUpdatingDelegate는 IGListDiffKit을 기반으로 동작하며, 데이터 업데이트 작업을 효율적으로 수행할 수 있도록 도와줍니다.

## IGListUpdatingDelegate과의 연동 방법
Swift에서 IGListKit을 사용하기 위해 먼저 [CocoaPods](https://cocoapods.org/)를 사용하여 IGListKit을 프로젝트에 추가해야 합니다. 아래와 같이 Podfile에 IGListKit을 추가합니다:

```swift
platform :ios, '11.0'
use_frameworks!

target 'YourApp' do
  pod 'IGListKit'
end
```

그런 다음, Terminal을 열어 프로젝트 디렉토리로 이동하여 `pod install` 명령을 실행합니다. 이렇게 하면 IGListKit이 프로젝트에 설치됩니다.

다음으로, IGListUpdater 객체를 생성하고 IGListUpdatingDelegate 프로토콜을 구현합니다. 이 프로토콜은 다음과 같은 메서드를 포함합니다:

```swift
func performUpdateWithCollectionView(
    collectionView: UICollectionView?,
    fromDataSource oldDataSource: [Any],
    toDataSource newDataSource: [Any],
    completion: @escaping (Bool) -> Void
) {
    // 데이터 소스 변경 작업을 수행하고 완료되면 completion 핸들러를 호출합니다.
}
```

이 메서드를 사용하여 데이터 변경 작업을 수행하고, 작업이 완료되면 completion 핸들러를 호출하여 변경 사항을 컬렉션 뷰에 반영합니다.

예를 들어, 다음은 IGListUpdatingDelegate 메서드를 구현하는 예입니다:

```swift
class MyUpdaterDelegate: NSObject, IGListUpdatingDelegate {
    // IGListUpdatingDelegate protocol method
    func performUpdateWithCollectionView(
        collectionView: UICollectionView?,
        fromDataSource oldDataSource: [Any],
        toDataSource newDataSource: [Any],
        completion: @escaping (Bool) -> Void
    ) {
        // 데이터 변경 작업을 수행합니다.

        // 변경 작업이 완료되면 completion 핸들러를 호출합니다.
        completion(true)
    }
}
```

## 참고 자료
- [IGListKit Documentation](https://instagram.github.io/IGListKit/)

위의 예제는 IGListKit과 IGListUpdatingDelegate를 Swift에서 사용하기 위한 기본적인 방법을 보여주고 있습니다. IGListKit에 대해 더 자세한 내용은 공식 문서를 참조하시기 바랍니다.