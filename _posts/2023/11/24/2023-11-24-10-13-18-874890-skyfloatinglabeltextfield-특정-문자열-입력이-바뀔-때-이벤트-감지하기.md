---
layout: post
title: "[swift] SkyFloatingLabelTextField 특정 문자열 입력이 바뀔 때 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 사용자에게 텍스트 입력을 받는 데 사용되는 간편한 UI 컨트롤이다. 이 컨트롤을 사용할 때 특정 문자열 입력이 바뀔 때 이벤트를 감지하고 싶은 경우가 있다. 이번 블로그 포스트에서는 SkyFloatingLabelTextField에서 문자열 입력 변경 이벤트를 감지하는 방법에 대해 알아보겠다.

## SkyFloatingLabelTextFieldDelegate 사용하기

SkyFloatingLabelTextFieldDelegate는 SkyFloatingLabelTextField 이벤트를 관리하는 프로토콜이다. 문자열 입력 변경 이벤트를 감지하기 위해 먼저 컨트롤러에서 해당 delegate를 설정해야 한다. 

```swift
class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }

    // 문자열 입력이 변경될 때 호출됨
    func textField(textField: SkyFloatingLabelTextField, didChange text: String?) {
        // 입력된 텍스트를 사용하여 원하는 작업 수행
        if let text = text {
            print("입력된 텍스트: \(text)")
        }
    }
}
```

위 코드에서는 ViewController에서 SkyFloatingLabelTextFieldDelegate를 구현하고, viewDidLoad() 메소드에서 textField의 delegate를 설정하여 이벤트를 관리한다. 이후에 문자열 입력이 변경될 때마다 textField(_:didChange:) 메소드가 호출되며, 원하는 작업을 수행할 수 있다.

만약 해당 메소드가 호출되지 않는다면, UITextFieldDelegate를 상속하고 있는지 확인해보고, 해당 델리게이트 메소드를 정확하게 구현했는지 확인해야 한다.

## 결론

SkyFloatingLabelTextField에서 특정 문자열 입력 변경 이벤트를 감지하는 방법에 대해 알아보았다. SkyFloatingLabelTextFieldDelegate를 사용하여 문자열 입력이 변경될 때 호출되는 메소드를 구현하여 원하는 작업을 수행할 수 있다.

더 자세한 내용은 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField) GitHub 레포지토리를 참고하면 도움이 될 것이다.