---
layout: post
title: "[swift] Swift와 UICollectionView를 이용한 애니메이션 셀 변경 구현하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

### 소개
UICollectionView는 iOS 앱에서 다양한 형태의 그리드나 리스트 형태의 뷰를 구현하기 위해 사용되는 유용한 컴포넌트입니다. 이번에는 Swift 언어와 UICollectionView를 함께 사용하여 애니메이션 효과를 적용한 셀 변경을 구현하는 방법에 대해 알아보겠습니다.

### 준비물
1. Xcode 설치
2. Swift 언어 기본 지식
3. UICollectionView의 기본 구성 요소에 대한 이해

### 구현 방법

#### 단계 1: UICollectionView 생성
먼저, 적절한 위치에 UICollectionView를 생성합니다. Storyboard를 사용하거나 코드로 직접 생성할 수 있습니다. UICollectionView의 dataSource와 delegate를 적절히 설정하는 것을 잊지 마세요.

```swift
// UIViewController 내부에 UICollectionView 인스턴스 생성
@IBOutlet weak var collectionView: UICollectionView!

// UICollectionViewDelegateFlowLayout을 채택한 ViewController에서 위임을 설정
collectionView.delegate = self
collectionView.dataSource = self
```

#### 단계 2: UICollectionViewCell 구현
UICollectionViewCell을 커스텀으로 구현합니다. 셀의 디자인과 함께 애니메이션 효과를 적용할 요소들을 구성합니다. 예를 들어, 셀 내부에 이미지뷰를 추가하고 움직임 효과를 주기 위해 CGAffineTransform을 사용할 수 있습니다.

```swift
class CustomCell: UICollectionViewCell {
    
    @IBOutlet weak var imageView: UIImageView!
    
    func animateCell() {
        // 애니메이션을 구현할 로직 작성
    }
}
```

#### 단계 3: UICollectionViewDelegateFlowLayout 구현
UICollectionViewDelegateFlowLayout을 채택하여 UICollectionView의 레이아웃 설정 및 셀 크기를 지정합니다. 셀 크기를 결정하는 메서드 `sizeForItemAt`을 오버라이딩하여 셀의 크기를 반환합니다.

```swift
extension ViewController: UICollectionViewDelegateFlowLayout {
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 각 셀의 크기를 지정하는 로직 작성
        return CGSize(width: 100, height: 100)
    }
}
```

#### 단계 4: UICollectionViewDataSource 구현
UICollectionViewDataSource를 채택하여 데이터 소스를 구현합니다. 셀의 개수, 셀의 내용 및 이미지 등을 반환하는 메서드들을 오버라이딩하여 구현합니다.

```swift
extension ViewController: UICollectionViewDataSource {
    
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        // 섹션의 개수 반환
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        // 각 섹션의 셀 개수 반환
        return data.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "CustomCell", for: indexPath) as! CustomCell
        // 셀에 데이터를 채워넣는 로직 작성
        cell.imageView.image = UIImage(named: data[indexPath.item])
        
        return cell
    }
}
```

#### 단계 5: 애니메이션 효과 적용
셀 변경 애니메이션을 적용하기 위해서는 `collectionView(_:willDisplay:forItemAt:)` 메서드를 사용합니다. 이 메서드는 셀이 화면에 표시되기 직전에 호출됩니다. 이 메서드를 오버라이딩하여 적절한 애니메이션 효과를 구현합니다.

```swift
func collectionView(_ collectionView: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt indexPath: IndexPath) {
    guard let cell = cell as? CustomCell else { return }
    cell.animateCell()
}
```

### 결론
이렇게만 해도 UICollectionView를 사용하여 애니메이션 효과를 적용한 셀 변경을 구현할 수 있습니다. 추가적으로 셀 선택에 대한 이벤트 처리, 셀 간격 및 여백 조정 등 다양한 기능을 구현할 수도 있습니다. UICollectionView과 Swift를 함께 사용하여 다양한 UI 요소를 구현해보세요!

### 참고 자료
- [Apple Developer Documentation - UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview)
- [Hacking with Swift - How to animate when your UICollectionView cells appear](https://www.hackingwithswift.com/example-code/uikit/how-to-animate-when-your-uicollectionview-cells-appear)