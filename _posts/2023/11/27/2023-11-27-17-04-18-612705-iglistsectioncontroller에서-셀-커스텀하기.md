---
layout: post
title: "[swift] IGListSectionController에서 셀 커스텀하기"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개

IGListKit은 UICollectionView의 사용을 훨씬 쉽게 만들어주는 Swift 기반의 라이브러리입니다. IGListKit에는 IGListSectionController라는 개념이 있는데, 이는 각 섹션에 대한 데이터 모델과 뷰 처리를 캡슐화하는 역할을 합니다. 이번 포스트에서는 IGListSectionController에서 셀을 커스텀하는 방법에 대해 알아보겠습니다.

## 절차

1. IGListSectionController 서브 클래스를 만듭니다.
2. sectionController의 init 메서드에서 cellassociator를 설정합니다.
3. cellForItem(at:) 메서드를 구현하여 커스텀 셀을 반환합니다.
4. sizeForItem(at:index:) 메서드를 구현하여 셀의 크기를 설정합니다.

## 코드 예시

```swift
import IGListKit

class CustomSectionController: IGListSectionController {
    var data: CustomDataModel?
    
    override init() {
        super.init()
        cellClass = CustomCell.self // 커스텀 셀 클래스 지정
        insets = UIEdgeInsets(top: 0, left: 0, bottom: 10, right: 0) // 셀 간의 여백 설정
    }
    
    override func numberOfItems() -> Int {
        return 1
    }
    
    override func cellForItem(at index: Int) -> UICollectionViewCell {
        guard let context = collectionContext else {
            fatalError("Invalid collection context")
        }
        
        let cell = context.dequeueReusableCell(withNibName: "CustomCell", bundle: nil, for: self, at: index) as! CustomCell
        cell.configure(with: data)
        
        return cell
    }
    
    override func sizeForItem(at index: Int) -> CGSize {
        guard let context = collectionContext else {
            return .zero
        }
        
        let width = context.containerSize.width
        let height: CGFloat = 100
        
        return CGSize(width: width, height: height)
    }
}
```

위의 코드는 IGListSectionController를 상속받는 CustomSectionController 클래스 예시입니다. 코드에서는 cellClass 속성을 통해 커스텀 셀의 클래스를 지정하고, cellForItem(at:) 메서드에서 커스텀 셀을 반환합니다. sizeForItem(at:) 메서드를 사용하여 셀의 크기를 설정할 수도 있습니다.

## 결론

IGListSectionController를 사용하여 셀을 커스텀하는 방법을 살펴보았습니다. IGListKit은 UICollectionView를 사용하는 작업을 훨씬 간단하게 만들어주는 강력한 도구이며, IGListSectionController를 통해 셀의 커스터마이징을 용이하게 할 수 있습니다.

## 참고 자료

- IGListKit GitHub 레포지토리: [https://github.com/Instagram/IGListKit](https://github.com/Instagram/IGListKit)