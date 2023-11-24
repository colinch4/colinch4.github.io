---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 주변 여백 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 사용자에게 텍스트 입력을 받을 수 있는 텍스트 필드입니다. 이 텍스트 필드를 사용하면 입력한 텍스트 주변에 여백을 설정할 수 있습니다. 이번 포스트에서는 SkyFloatingLabelTextField를 사용하여 입력한 텍스트 주변의 여백을 설정하는 방법을 알아보겠습니다.

## 예시 코드

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        textField.delegate = self
        textField.padding = UIEdgeInsets(top: 16, left: 16, bottom: 16, right: 16)
    }
}

extension ViewController: UITextFieldDelegate {

    func textFieldDidBeginEditing(_ textField: UITextField) {
        textField.padding = UIEdgeInsets(top: 16, left: 16, bottom: 16, right: 16)
    }

    func textFieldDidEndEditing(_ textField: UITextField) {
        textField.padding = UIEdgeInsets(top: 8, left: 8, bottom: 8, right: 8)
    }
}
```

위의 예시 코드에서는 ViewController 클래스에서 SkyFloatingLabelTextField를 IBOutlet으로 선언하고, viewDidLoad 메서드에서 textField의 델리게이트를 설정하고 padding 값을 설정하고 있습니다. padding 값은 UIEdgeInsets를 사용하여 상단, 좌측, 하단, 우측에 각각 여백 값을 설정할 수 있습니다.

또한, UITextFieldDelegate 프로토콜을 채택한 확장(extension)을 이용하여 textFieldDidBeginEditing과 textFieldDidEndEditing 메서드를 구현하면, 텍스트 필드가 편집 모드에 들어갈 때와 편집 모드가 종료될 때도 padding 값을 변경할 수 있습니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력한 텍스트 주변의 여백을 설정하는 방법에 대해 알아보았습니다. padding 값을 설정하여 사용자가 입력한 텍스트를 더욱 가독성 있게 표시할 수 있습니다. 자세한 내용은 [SkyFloatingLabelTextField GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)에서 확인할 수 있습니다.