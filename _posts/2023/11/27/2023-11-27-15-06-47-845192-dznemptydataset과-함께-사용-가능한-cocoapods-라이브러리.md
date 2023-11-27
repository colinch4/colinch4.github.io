---
layout: post
title: "[swift] DZNEmptyDataSet과 함께 사용 가능한 Cocoapods 라이브러리"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift 프로젝트에서 DZNEmptyDataSet과 함께 사용할 수 있는 Cocoapods 라이브러리에 대해서 알아보겠습니다.

## DZNEmptyDataSet이란?

DZNEmptyDataSet은 UITableView와 UICollectionView에서 데이터가 없는 상황에서 표시해주는 라이브러리입니다. 데이터가 없을 때 화면에 나타내는 메시지, 이미지, 버튼 등을 쉽게 설정할 수 있습니다.

## Cocoapods 설치 방법

Cocoapods는 패키지 의존성 관리 도구로, Swift 프로젝트에서 외부 라이브러리를 손쉽게 추가할 수 있게 도와줍니다. Cocoapods를 설치하려면 다음 명령어를 터미널에 입력하세요:

```bash
$ sudo gem install cocoapods
```

Cocoapods 설치가 완료되면, 프로젝트 폴더로 이동하여 Podfile를 생성하세요:

```bash
$ cd your_project_directory
$ pod init
```

Podfile을 열어서 다음과 같이 추가해주세요:

```ruby
pod 'DZNEmptyDataSet'
```

Podfile에 이 라인을 추가한 후에는 터미널에서 다음 명령어를 입력하여 라이브러리를 설치하세요:

```bash
$ pod install
```

설치가 완료되면, Xcode 프로젝트를 열어서 `.xcworkspace` 파일을 실행하세요.

## DZNEmptyDataSet 사용하기

DZNEmptyDataSet을 사용하기 위해서는 먼저 해당 뷰 컨트롤러에 `DZNEmptyDataSetSource`와 `DZNEmptyDataSetDelegate` 프로토콜을 채택해야 합니다.

```swift
class ViewController: UIViewController, DZNEmptyDataSetSource, DZNEmptyDataSetDelegate {
    // ...
}
```

다음으로, DZNEmptyDataSet과 관련된 설정을 추가해보겠습니다. 예를 들어, UITableView에 DZNEmptyDataSet을 적용하려면 다음과 같이 코드를 작성하세요:

```swift
@IBOutlet weak var tableView: UITableView!

override func viewDidLoad() {
    super.viewDidLoad()

    tableView.emptyDataSetSource = self
    tableView.emptyDataSetDelegate = self
}

func title(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
    let attributes = [NSAttributedString.Key.font: UIFont.boldSystemFont(ofSize: 18.0)]
    return NSAttributedString(string: "데이터가 없습니다.", attributes: attributes)
}

func description(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
    let attributes = [NSAttributedString.Key.font: UIFont.systemFont(ofSize: 14.0)]
    return NSAttributedString(string: "데이터를 불러올 수 없습니다.", attributes: attributes)
}

func image(forEmptyDataSet scrollView: UIScrollView) -> UIImage? {
    return UIImage(named: "no_data_image")
}

func emptyDataSetShouldAllowScroll(_ scrollView: UIScrollView) -> Bool {
    return true
}
```

위의 코드에서는 DZNEmptyDataSetSource와 DZNEmptyDataSetDelegate 프로토콜의 메소드를 구현하여 빈 데이터 상태에서 화면에 표시할 메시지와 이미지를 설정하고 있습니다. 이외에도 다양한 설정을 할 수 있으니, 필요에 따라 추가로 구현해보세요.

## 참고 자료

- [DZNEmptyDataSet GitHub Repository](https://github.com/dzenbot/DZNEmptyDataSet)
- [DZNEmptyDataSet Documentation](https://dzenbot.github.io/DZNEmptyDataSet/)

이상으로 DZNEmptyDataSet과 함께 사용 가능한 Cocoapods 라이브러리에 대해 알아보았습니다. 이 라이브러리를 사용하여 데이터가 없는 상황에서 친절한 안내 메시지를 유저에게 제공해보세요!