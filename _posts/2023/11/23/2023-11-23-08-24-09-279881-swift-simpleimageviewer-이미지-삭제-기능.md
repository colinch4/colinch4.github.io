---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 삭제 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 많은 애플리케이션에서 사용되는 중요한 기능입니다. 이미지를 표시하고 조작하는 데 도움이 되는데, 이 중에서도 이미지 삭제 기능은 사용자에게 유용한 기능입니다. 이번에는 Swift에서 간단한 이미지 뷰어의 이미지 삭제 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. 이미지 삭제 버튼 추가하기

가장 먼저, 이미지 삭제 기능을 추가하기 위해 이미지 뷰어 화면에 삭제 버튼을 추가해야 합니다. 삭제 버튼은 사용자가 이미지를 삭제할 때 클릭할 수 있는 UI 요소입니다. 이 버튼을 통해 이미지를 삭제하는 기능을 추가할 것입니다.

```swift
@IBOutlet weak var imageView: UIImageView!
@IBOutlet weak var deleteButton: UIButton!

override func viewDidLoad() {
    super.viewDidLoad()

    let tapGesture = UITapGestureRecognizer(target: self, action: #selector(toggleDeleteMode))
    imageView.addGestureRecognizer(tapGesture)
}

@IBAction func deleteButtonTapped(_ sender: UIButton) {
    // 이미지 삭제 로직
}

@objc func toggleDeleteMode() {
    deleteButton.isHidden = !deleteButton.isHidden
}
```

위의 코드에서 `imageView`는 이미지 뷰어에서 이미지를 표시하는 뷰입니다. `deleteButton`은 이미지 삭제 기능을 수행할 버튼입니다. `toggleDeleteMode()` 메서드는 이미지 뷰어를 한 번 클릭하면 삭제 버튼이 나타나거나 사라지도록 하는 메서드입니다.

## 2. 이미지 삭제 로직 구현하기

이제 삭제 버튼이 추가되었으므로, 실제로 이미지를 삭제하는 로직을 구현해야 합니다. 이미지 삭제 로직은 `deleteButtonTapped(_:)` 메서드 안에 구현할 것입니다. 이 메서드는 사용자가 삭제 버튼을 클릭했을 때 호출되는 액션입니다.

```swift
@IBAction func deleteButtonTapped(_ sender: UIButton) {
    imageView.image = nil

    // 이미지 삭제 후에 다른 작업 수행
}
```

위의 코드에서 `imageView.image = nil`으로 이미지를 삭제하고 있습니다. 이렇게하면 이미지가 화면에서 사라집니다. 이후에는 다른 작업을 수행하거나 필요에 따라 추가적인 로직을 구현할 수 있습니다.

## 3. 테스트하기

이제 삭제 기능을 확인하기 위해 간단한 테스트를 수행해 보겠습니다. 애플리케이션을 실행하고 이미지 뷰어 화면으로 이동한 뒤, 이미지를 터치하여 삭제 버튼을 표시합니다. 이후에는 삭제 버튼을 클릭하여 이미지를 삭제할 수 있습니다.

## 결론

이번에는 Swift에서 간단한 이미지 뷰어의 이미지 삭제 기능을 구현하는 방법에 대해 알아보았습니다. 이미지를 삭제할 수 있도록 삭제 버튼을 추가하고, 이미지 삭제 로직을 구현하는 방법을 살펴보았습니다. 이를 통해 사용자에게 유용한 기능을 제공할 수 있습니다.

다른 흥미로운 Swift 개발 팁이나 더 깊은 내용을 알고 싶다면 공식 Swift 문서(https://swift.org/documentation/)를 참조하십시오.