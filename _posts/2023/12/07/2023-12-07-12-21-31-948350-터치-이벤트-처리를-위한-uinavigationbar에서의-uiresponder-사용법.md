---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UINavigationBar에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UINavigationBar는 iOS 앱에서 네비게이션 기능을 제공하는 뷰 컴포넌트입니다. UINavigationBar에서 사용자의 터치 이벤트를 처리하기 위해서는 UIResponder를 사용해야 합니다. 이 글에서는 UINavigationBar에서의 UIResponder 사용법을 알아보겠습니다.

## 1. 연결된 뷰 컨트롤러에 UIResponder를 구현하기

UINavigationBar에서 터치 이벤트를 처리하기 위해서는 먼저 해당 뷰 컨트롤러에 UIResponder를 구현해야 합니다. UIResponder를 구현하기 위해서는 아래와 같은 코드를 사용합니다.

```swift
class MyViewController: UIViewController, UIResponder {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        // 터치 이벤트 처리 로직 작성
    }
}
```

위의 코드에서 `touchesBegan(_:with:)` 메소드는 터치 이벤트가 발생했을 때 호출되는 메소드입니다. 이 메소드를 오버라이드하여 원하는 터치 이벤트 처리 로직을 작성할 수 있습니다.

## 2. UINavigationBar에 사용자 정의 뷰 추가하기

UINavigationBar에 터치 이벤트를 처리하기 위해서는 추가로 사용자 정의 뷰를 UINavigationBar에 추가해야 합니다. 사용자 정의 뷰를 UINavigationBar에 추가하는 방법은 다음과 같습니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let customView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 44))
    customView.backgroundColor = UIColor.red

    let tapGesture = UITapGestureRecognizer(target: self, action: #selector(customViewTapped))
    customView.addGestureRecognizer(tapGesture)
    
    navigationItem.titleView = customView
}

@objc func customViewTapped() {
    // 터치 이벤트 처리 로직 작성
}
```

위의 코드에서 `customViewTapped()` 메소드는 사용자 정의 뷰가 터치되었을 때 호출되는 메소드입니다. 이 메소드를 사용하여 원하는 터치 이벤트 처리 로직을 작성하면 됩니다.

## 마무리

UINavigationBar에서의 터치 이벤트 처리를 위해 UIResponder를 사용하는 방법에 대해 알아보았습니다. 이를 통해 UINavigationBar에 터치 이벤트를 처리하는 다양한 기능을 추가할 수 있습니다. 자세한 내용은 [UINavigationBar documentation](https://developer.apple.com/documentation/uikit/uinavigationbar)을 참고하시기 바랍니다.