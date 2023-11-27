---
layout: post
title: "[swift] IGListScrollDelegateFlag와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 앱에서 복잡한 컬렉션 뷰를 관리하는 데 도움이 되는 강력한 오픈 소스 라이브러리입니다. IGListKit은 UICollectionViewDelegate 및 UICollectionViewDataSource 대신에 IGListDataSource 및 IGListScrollDelegate를 사용하여 데이터 소스 및 스크롤 관련 이벤트를 처리할 수 있습니다.

이번 블로그 포스트에서는 IGListScrollDelegateFlag와 Swift IGListKit을 연동하는 방법에 대해 알아보겠습니다.

## IGListScrollDelegateFlag 소개

IGListScrollDelegateFlag는 IGListKit에서 제공하는 스크롤 관련 이벤트에 대한 플래그 집합입니다. IGListScrollDelegateFlag를 사용하면 IGListScrollDelegate에서 발생한 이벤트의 종류를 확인하고 적절한 작업을 수행할 수 있습니다.

IGListScrollDelegateFlag는 다음과 같은 이벤트에 대한 플래그를 제공합니다:

- `.didScroll`
- `.willBeginDragging`
- `.didEndDragging`
- `.willBeginDecelerating`
- `.didEndDecelerating`
- `.didEndScrollingAnimation`

## IGListScrollDelegateFlag 사용하기

IGListScrollDelegate를 구현하는 클래스에서는 다음과 같이 IGListScrollDelegateFlag를 사용하여 원하는 이벤트를 처리할 수 있습니다:

```swift
import IGListKit

class MyListDelegate: NSObject, IGListScrollDelegate {
    
    func listAdapter(_ listAdapter: ListAdapter, didScroll sectionController: ListSectionController) {
        // 스크롤 이벤트가 발생했을 때 실행될 코드를 작성합니다.
        // ...
    }
    
    func listAdapter(_ listAdapter: ListAdapter, willBeginDragging sectionController: ListSectionController) {
        // 스크롤이 시작되기 전에 실행될 코드를 작성합니다.
        // ...
    }

    // 다른 이벤트에 대한 핸들러를 추가로 구현할 수 있습니다.
    // ...
}

```

위의 예제에서는 `didScroll`과 `willBeginDragging` 이벤트에 대한 핸들러를 구현하였습니다. 이와 마찬가지로 다른 이벤트에 대한 핸들러를 추가로 구현할 수 있습니다.

## IGListScrollDelegateFlag 사용 예제

아래는 IGListScrollDelegateFlag를 사용하여 새로운 스크롤 이벤트가 발생한 경우 콘솔에 로그를 출력하는 예제입니다:

```swift
import IGListKit

class MyListDelegate: NSObject, IGListScrollDelegate {
    
    func listAdapter(_ listAdapter: ListAdapter, didScroll sectionController: ListSectionController) {
        print("스크롤 이벤트 발생")
    }
    
    func listAdapter(_ listAdapter: ListAdapter, willBeginDragging sectionController: ListSectionController) {
        print("스크롤 시작")
    }
    
    // ...
}

```

위의 예제에서는 `didScroll` 메서드가 호출되면 "스크롤 이벤트 발생"이라는 메시지를 콘솔에 출력하고, `willBeginDragging` 메서드가 호출되면 "스크롤 시작"이라는 메시지를 콘솔에 출력합니다.

## 마무리

이번 포스트에서는 IGListScrollDelegateFlag와 Swift IGListKit을 연동하는 방법에 대해 살펴보았습니다. IGListScrollDelegateFlag는 IGListKit에서 제공하는 스크롤 관련 이벤트를 쉽게 처리할 수 있는 편리한 기능입니다. IGListScrollDelegateFlag를 활용하여 앱의 컬렉션 뷰 스크롤 이벤트를 감지하고 적절한 작업을 수행할 수 있습니다.

더 자세한 내용은 [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)를 참조해주세요.