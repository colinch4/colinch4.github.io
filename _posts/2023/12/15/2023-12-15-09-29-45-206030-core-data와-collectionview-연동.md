---
layout: post
title: "[ios] Core Data와 CollectionView 연동"
description: " "
date: 2023-12-15
tags: [ios]
comments: true
share: true
---

Core Data는 iOS 앱에서 데이터를 관리하고 지속적으로 저장하는 데 사용되는 프레임워크입니다. CollectionView는 다양한 레이아웃으로 데이터를 표시하는 데 사용되며, 주로 리스트나 그리드 형식의 데이터를 표시하는 데 활용됩니다. 이번 글에서는 Core Data와 CollectionView를 연동하여 데이터를 보여주는 방법에 대해 다루겠습니다.

## Core Data 설정

먼저, Core Data를 설정해야 합니다. Core Data 모델을 만들고, 엔티티와 속성을 정의합니다. 그리고 데이터 저장소(예: SQLite)를 설정하여 데이터를 영구적으로 보관할 수 있습니다.

```swift
// Core Data 모델 및 데이터 저장소 설정 예시
```

## CollectionView와 Core Data 연동

### 데이터 소스 구현

CollectionView를 활용하기 위해서는 UICollectionViewDataSource 프로토콜을 구현해야 합니다. Core Data의 데이터를 CollectionView에 표시하기 위해서는 다음과 같은 방법을 따릅니다.

```swift
// UICollectionViewDataSource 프로토콜 구현 예시
```

### 데이터 로딩

Core Data에서 데이터를 가져와 CollectionView에 로드해야 합니다. NSFetchedResultsController를 이용하여 데이터를 로드하고, CollectionView에 반영합니다.

```swift
// NSFetchedResultsController를 이용한 데이터 로딩 및 CollectionView에 반영하는 예시
```

## CollectionView 업데이트

Core Data에 데이터가 추가되거나 변경될 때, CollectionView를 업데이트해야 합니다. NSFetchedResultsControllerDelegate를 활용하여 데이터 변경에 따른 CollectionView 업데이트를 처리합니다.

```swift
// NSFetchedResultsControllerDelegate를 이용한 CollectionView 업데이트 예시
```

## 결론

이렇게 Core Data와 CollectionView를 연동하여 데이터를 표시하는 방법에 대해 알아보았습니다. CollectionView와 Core Data를 함께 사용하면 앱의 데이터 표시 및 관리를 효율적으로 할 수 있습니다.

더 자세한 내용은 Apple의 [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html)를 참고하시기 바랍니다.