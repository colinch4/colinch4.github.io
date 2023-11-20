---
layout: post
title: "[swift] Swift SkeletonView TableView에서 사용하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift SkeletonView는 데이터 로딩 중에 스켈레톤(뼈대) 형태의 UI를 표시하는 라이브러리입니다. 이를 사용하면 사용자가 데이터 로딩 중에도 화면에 유저 피드백을 제공할 수 있습니다. 이 글에서는 Swift SkeletonView를 TableView에서 사용하는 방법을 알아보겠습니다.

## 1. CocoaPods를 이용한 설치

SkeletonView를 사용하기 위해서는 CocoaPods를 이용하여 프로젝트에 라이브러리를 추가해야 합니다. `Podfile` 파일을 열고 다음과 같이 추가해주세요:

```ruby
pod 'SkeletonView'
```

그리고 터미널에서 아래의 명령어를 실행하여 라이브러리를 설치합니다:

```bash
$ pod install
```

## 2. TableView에 SkeletonView 적용하기

TableView에 SkeletonView를 적용하려면 다음과 같은 단계를 따라야 합니다:

### 2.1 SkeletonView import하기

TableView의 ViewController에서 SkeletonView를 import해야 합니다:

```swift
import SkeletonView
```

### 2.2 SkeletonView 활성화하기

TableView에 SkeletonView를 활성화하려면 TableView의 `viewDidLoad()` 메서드에서 다음과 같이 설정해야 합니다:

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // SkeletonView 활성화
    tableView.isSkeletonable = true
}
```

### 2.3 셀에 SkeletonView 적용하기

테이블 뷰 셀에 SkeletonView를 적용하려면 `UITableViewCell` 클래스를 상속 받은 셀에서 `SkeletonTableViewDelegate`를 준수하도록 설정해야 합니다. 이를 위해 TableView의 DataSource에서 다음과 같이 설정해주세요:

```swift
extension YourTableViewCell: SkeletonTableViewDelegate {
    func collectionSkeletonView(_ skeletonView: UITableView, cellIdentifierForRowAt indexPath: IndexPath) -> ReusableCellIdentifier {
        return "YourTableViewCellIdentifier"
    }
}
```

위의 코드에서 `YourTableViewCellIdentifier`는 셀의 식별자입니다. 알맞게 변경해주세요.

### 2.4 SkeletonView 설정하기

`tableView` 객체의 `showAnimatedSkeleton()` 메서드를 사용하여 SkeletonView를 활성화하고 `hideSkeleton()` 메서드를 사용하여 SkeletonView를 비활성화할 수 있습니다. 예를 들어, 데이터 로딩이 완료된 후에 SkeletonView를 숨기려면 다음과 같이 사용할 수 있습니다:

```swift
tableView.showAnimatedSkeleton()

// 데이터 로딩 후 SkeletonView 숨기기
tableView.hideSkeleton()
```

### 2.5 SkeletonView에 스타일 적용하기

SkeletonView의 스타일을 변경하려면 `SkeletonAppearance` 객체를 사용할 수 있습니다. 아래는 몇 가지 예시입니다:

```swift
// 스켈레톤 색상 변경
SkeletonAppearance.default.tintColor = .red

// 스켈레톤 진행바 두께 설정
SkeletonAppearance.default.gradient = SkeletonGradient(baseColor: .red)
```

## 3. 출처

SkeletonView의 공식 Github 저장소에서 [더 자세한 정보](https://github.com/Juanpe/SkeletonView)를 확인할 수 있습니다.

위의 방법을 따라하면 TableView에서 간단하게 SkeletonView를 사용할 수 있습니다. SkeletonView를 통해 사용자에게 데이터 로딩 중임을 시각적으로 알려주면 사용자 경험을 향상시킬 수 있습니다.