---
layout: post
title: "[swift] DZNEmptyDataSet을 사용하여 UIScrollView에서 빈 상태 표시하기"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

많은 경우 UIScrollView에는 데이터가 없을 때 빈 상태를 나타내는 기능이 필요합니다. 이를 위해 DZNEmptyDataSet 라이브러리를 사용할 수 있습니다. DZNEmptyDataSet은 UIView 또는 UIScrollView의 서브 클래스에서 사용할 수 있으며, 데이터가 없을 때 사용자에게 알림을 표시하는 기능을 제공합니다.

## DZNEmptyDataSet 설치하기

DZNEmptyDataSet은 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음 코드를 추가한 후 `pod install` 명령어를 실행하세요.

```ruby
pod 'DZNEmptyDataSet'
```

## DZNEmptyDataSet 적용하기

DZNEmptyDataSet을 사용하기 위해서는 다음 단계를 따르세요:

1. UIScrollView의 서브 클래스를 만듭니다. 예를 들어, UITableView를 사용한다고 가정하고 `EmptyTableView`라는 클래스를 만들어 보겠습니다.

```swift
import UIKit
import DZNEmptyDataSet

class EmptyTableView: UITableView, DZNEmptyDataSetSource, DZNEmptyDataSetDelegate {
    
    override func awakeFromNib() {
        super.awakeFromNib()
        self.emptyDataSetSource = self
        self.emptyDataSetDelegate = self
    }
    
    // 빈 상태의 데이터 세트를 구성하기 위한 함수
    func title(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
        let text = "데이터가 없습니다."
        let attributes = [NSAttributedString.Key.font: UIFont.boldSystemFont(ofSize: 18.0),
                          NSAttributedString.Key.foregroundColor: UIColor.black]
        return NSAttributedString(string: text, attributes: attributes)
    }
    
    func description(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
        let text = "데이터를 추가하여 빈 상태를 채우세요."
        let attributes = [NSAttributedString.Key.font: UIFont.systemFont(ofSize: 14.0),
                          NSAttributedString.Key.foregroundColor: UIColor.gray]
        return NSAttributedString(string: text, attributes: attributes)
    }
}
```

2. EmptyTableView의 awakeFromNib() 메서드에서 `emptyDataSetSource`와 `emptyDataSetDelegate`를 설정합니다. 이 두 프로퍼티는 DZNEmptyDataSetSource와 DZNEmptyDataSetDelegate 프로토콜을 준수하는 객체여야 합니다.

3. EmptyTableView에 DZNEmptyDataSetSource와 DZNEmptyDataSetDelegate를 구현합니다. 위의 예제에서는 `title(forEmptyDataSet:)`과 `description(forEmptyDataSet:)` 함수를 구현하여 빈 상태의 데이터 세트에 표시할 제목과 설명을 반환합니다. 필요에 따라 다른 함수들을 구현할 수도 있습니다.

4. 이제 EmptyTableView를 사용하여 데이터가 없는 경우에 빈 상태를 표시할 수 있습니다. 예를 들어, UIViewController에서 EmptyTableView를 추가하고 데이터를 설정한 후, 데이터가 없을 때 빈 상태가 표시되도록 다음과 같이 코드를 작성할 수 있습니다.

```swift
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var tableView: EmptyTableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self // 테이블 뷰 데이터 소스 설정
        
        // 데이터가 없을 경우의 처리
        if data.isEmpty {
            tableView.reloadData()
        }
    }
}

extension ViewController: UITableViewDataSource {
    // UITableViewDataSource의 함수들을 구현
    // ...
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data.count
    }
    
    // ...
}
```

## 결론

DZNEmptyDataSet을 사용하면 UIScrollView 기반의 뷰에서 데이터가 없을 때 빈 상태를 표시할 수 있습니다. 위의 예제를 참고하여 프로젝트에 DZNEmptyDataSet을 적용해 보세요. 자세한 내용은 [DZNEmptyDataSet의 GitHub 페이지](https://github.com/dzenbot/DZNEmptyDataSet)를 참조하십시오.