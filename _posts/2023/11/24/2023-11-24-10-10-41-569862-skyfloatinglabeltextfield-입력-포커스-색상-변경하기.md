---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 색상 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

입력 폼을 디자인할 때 SkyFloatingLabelTextField는 매우 유용한 라이브러리입니다. 사용자가 입력 폼에 포커스를 줄 때마다 라벨이 위로 이동하여 가독성을 높여줍니다. 그러나 기본적으로 라이브러리에 제공되는 입력 포커스 색상을 변경하고 싶을 수도 있습니다. 이 글에서는 SkyFloatingLabelTextField 입력 포커스 색상을 변경하는 방법에 대해 알아보겠습니다.

## 준비 사항

SkyFloatingLabelTextField를 사용하기 위해 먼저 해당 라이브러리를 프로젝트에 추가해야 합니다. [CocoaPods](https://cocoapods.org)을 사용하여 다음과 같이 Podfile에 추가합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

## 입력 포커스 색상 변경하기

입력 폼의 포커스 색상을 변경하려면 UITextFieldDelegate를 구현하여 해당 메서드를 사용해야 합니다. 다음 코드를 참고하여 입력 포커스 색상을 변경해보세요.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
        configureTextField()
    }
    
    func configureTextField() {
        textField.placeholder = "이름"
        textField.title = "이름"
        textField.tintColor = .blue // 포커스 색상 변경
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
    // 포커스가 변경되었을 때 호출되는 메서드
    func textFieldDidBeginEditing(_ textField: UITextField) {
        textField.tintColor = .blue // 포커스 색상 변경
    }
}
```

위 코드에서 `configureTextField()` 메서드 내부에서 `textField.tintColor`을 원하는 색상으로 변경하면 됩니다. 또한, `textFieldDidBeginEditing()` 메서드를 통해 포커스가 변경되었을 때도 동일한 색상을 사용할 수 있습니다.

위 예제에서는 포커스 색상을 파란색으로 설정하였습니다. 원하는 색상으로 변경하여 입력 폼을 더욱 예쁘게 꾸밀 수 있습니다.

이제 SkyFloatingLabelTextField를 사용하여 입력 폼을 디자인하고 포커스 색상을 변경하는 방법을 알아보았습니다. 이를 통해 사용자 입력 폼의 가독성을 높이고, 애플리케이션의 사용자 경험을 향상시킬 수 있습니다.