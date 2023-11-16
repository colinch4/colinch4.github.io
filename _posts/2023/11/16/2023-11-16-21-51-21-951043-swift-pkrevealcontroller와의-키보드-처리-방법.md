---
layout: post
title: "[swift] Swift PKRevealController와의 키보드 처리 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift PKRevealController는 iOS 애플리케이션에서 사이드 메뉴를 구현하는 데 사용되는 프레임워크입니다. 이 프레임워크를 사용하여 키보드와 관련된 이슈를 처리하는 방법을 알아보겠습니다.

## 1. 키보드 표시 및 감추기 이벤트 처리

키보드가 표시되거나 감춰질 때에는 `NotificationCenter`를 사용하여 해당 이벤트에 대한 옵저버를 등록하는 것이 좋습니다. 예를 들어, 키보드가 표시될 때 사용자 인터페이스를 조정하거나, 화면을 스크롤하거나, 다른 뷰를 이동하는 것과 같은 작업을 수행할 수 있습니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow(_:)), name: UIResponder.keyboardWillShowNotification, object: nil)
    NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide(_:)), name: UIResponder.keyboardWillHideNotification, object: nil)
}

@objc func keyboardWillShow(_ notification: Notification) {
    // 키보드가 표시될 때 실행되는 코드
}

@objc func keyboardWillHide(_ notification: Notification) {
    // 키보드가 감춰질 때 실행되는 코드
}

deinit {
    NotificationCenter.default.removeObserver(self)
}
```

## 2. 키보드가 텍스트 필드를 가리는 경우 스크롤하기

키보드가 특정 텍스트 필드를 가리는 경우, 해당 텍스트 필드가 키패드와 겹치지 않도록 스크롤해야합니다. `UIScrollView`를 사용하여 스크롤 가능한 컨테이너를 만들고, `UIKeyboardWillShow` 및 `UIKeyboardWillHide` 감지자를 사용하여 스크롤 처리 로직을 구현할 수 있습니다.

```swift
@objc func keyboardWillShow(_ notification: Notification) {
    guard let keyboardFrame = notification.userInfo?[UIResponder.keyboardFrameEndUserInfoKey] as? CGRect else {
        return
    }
    
    let keyboardHeight = keyboardFrame.height
    let contentInsets = UIEdgeInsets(top: 0, left: 0, bottom: keyboardHeight, right: 0)
    scrollView.contentInset = contentInsets
    scrollView.scrollIndicatorInsets = contentInsets
    
    // 특정 텍스트 필드 위치로 스크롤
    if let activeTextField = activeTextField {
        let textFieldRect = activeTextField.convert(activeTextField.bounds, to: scrollView)
        scrollView.scrollRectToVisible(textFieldRect, animated: true)
    }
}

@objc func keyboardWillHide(_ notification: Notification) {
    let contentInsets = UIEdgeInsets.zero
    scrollView.contentInset = contentInsets
    scrollView.scrollIndicatorInsets = contentInsets
}
```

## 3. 키보드가 사이드 메뉴와 겹치는 문제 해결

PKRevealController는 화면 왼쪽에 사이드 메뉴를 표시하는데 사용되는 프레임워크입니다. 키보드가 표시될 때 PKRevealController와 키보드가 겹치는 문제가 발생할 수 있습니다. 이를 해결하기 위해 키보드 표시 및 감추기 이벤트를 처리하는 동안에는 사이드 메뉴가 화면에서 완전히 감춰지도록 해야합니다.

```swift
@objc func keyboardWillShow(_ notification: Notification) {
    // PKRevealController 닫기
    revealController?.showFrontViewController(animated: true)
    
    // 키보드 표시 로직
}

@objc func keyboardWillHide(_ notification: Notification) {
    // PKRevealController 열기
    revealController?.showViewController(for: .left, animated: true)
    
    // 키보드 감추기 로직
}
```

## 결론

Swift PKRevealController와 함께 키보드 처리를 하는 방법에 대해 알아보았습니다. 이를 통해 애플리케이션의 사용자 인터페이스를 개선하고 사용자가 더 나은 경험을 얻을 수 있습니다.

참고: [PKRevealController 문서](https://github.com/pkluz/PKRevealController)