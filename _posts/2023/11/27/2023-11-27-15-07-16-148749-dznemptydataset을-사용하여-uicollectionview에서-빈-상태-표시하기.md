---
layout: post
title: "[swift] DZNEmptyDataSet을 사용하여 UICollectionView에서 빈 상태 표시하기"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

UICollectionView는 많은 데이터를 효과적으로 표시하는 데 사용되는 iOS의 유용한 컴포넌트입니다. 때로는 데이터가 없는 상황에서 빈 상태를 사용자에게 알려주는 것이 중요할 수 있습니다. 이를 위해 DZNEmptyDataSet 라이브러리를 사용하여 UICollectionView의 빈 상태를 깔끔하게 표시할 수 있습니다.

## DZNEmptyDataSet 소개

[DZNEmptyDataSet](https://github.com/dzenbot/DZNEmptyDataSet)은 UICollectionView와 UITableView를 위한 빈 상태 표시 라이브러리입니다. 이 라이브러리는 사용자 정의 뷰, 이미지, 메시지 및 애니메이션을 통해 빈 상태를 시각적으로 표현할 수 있습니다.

## DZNEmptyDataSet 사용하기

1. 첫 번째로, 프로젝트에 DZNEmptyDataSet 라이브러리를 추가합니다. 이를 위해 CocoaPods를 사용하거나 수동으로 라이브러리를 다운로드하여 프로젝트에 추가할 수 있습니다.

2. DZNEmptyDataSet을 사용하려는 UICollectionView에 대해 UICollectionViewDelegate 및 UICollectionViewDataSource 프로토콜을 구현합니다.

```swift
class MyViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {
    
    @IBOutlet weak var collectionView: UICollectionView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Delegate와 DataSource 설정
        collectionView.delegate = self
        collectionView.dataSource = self
        
        // DZNEmptyDataSet의 delegate와 dataSource 설정
        collectionView.emptyDataSetDelegate = self
        collectionView.emptyDataSetDataSource = self
    }

    //...CollectionView의 다른 메소드들...

}
```

3. 빈 상태를 표시하고자 하는 UICollectionView에 대한 DZNEmptyDataSetDelegate 및 DZNEmptyDataSetSource 프로토콜을 추가하여 ViewController에 다음 코드를 작성합니다.

```swift
extension MyViewController: DZNEmptyDataSetDelegate, DZNEmptyDataSetSource {
    
    func image(forEmptyDataSet scrollView: UIScrollView) -> UIImage? {
        return UIImage(named: "emptyImage") // 이미지를 반환하거나 nil을 반환하여 이미지를 표시하지 않음
    }
    
    func title(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
        let text = "빈 상태입니다." // 빈 상태 메시지
        let attributes = [NSAttributedString.Key.font: UIFont.boldSystemFont(ofSize: 18.0)] // 폰트 및 스타일 지정
        return NSAttributedString(string: text, attributes: attributes)
    }
    
    func description(forEmptyDataSet scrollView: UIScrollView) -> NSAttributedString? {
        let text = "데이터가 없습니다." // 빈 상태에 대한 설명 메시지
        let attributes = [NSAttributedString.Key.font: UIFont.systemFont(ofSize: 14.0)] // 폰트 및 스타일 지정
        return NSAttributedString(string: text, attributes: attributes)
    }
    
    func buttonTitle(forEmptyDataSet scrollView: UIScrollView, for state: UIControl.State) -> NSAttributedString? {
        let text = "새로고침" // 버튼에 표시될 텍스트
        let attributes = [NSAttributedString.Key.font: UIFont.systemFont(ofSize: 16.0)] // 폰트 및 스타일 지정
        return NSAttributedString(string: text, attributes: attributes)
    }
    
    func emptyDataSet(_ scrollView: UIScrollView, didTapButton button: UIButton) {
        // 버튼을 눌렀을 때 수행할 작업
    }
}
```

4. 마지막으로, 뷰 컨트롤러가 사용자 정의한 DZNEmptyDataSetDelegate 및 DZNEmptyDataSetSource 프로토콜을 채택하도록 확장합니다.

```swift
extension MyViewController: DZNEmptyDataSetDelegate, DZNEmptyDataSetSource {
    //...
}
```

이제 UICollectionView가 데이터가 없을 때 DZNEmptyDataSet이 설정한 이미지, 메시지 및 버튼을 표시할 것입니다. 또한 버튼을 누르면 `emptyDataSet(_:didTapButton:)` 메소드가 호출되어 추가 작업을 수행할 수 있습니다.

## 마치며

DZNEmptyDataSet을 사용하여 UICollectionView에서 빈 상태를 표시하는 방법을 알아보았습니다. 이를 통해 사용자에게 데이터가 없는 상황을 명확하게 알려주고 적절한 조치를 취할 수 있는 기능을 제공할 수 있습니다. 자세한 내용은 DZNEmptyDataSet의 [공식 문서](https://github.com/dzenbot/DZNEmptyDataSet)를 참조하시기 바랍니다.