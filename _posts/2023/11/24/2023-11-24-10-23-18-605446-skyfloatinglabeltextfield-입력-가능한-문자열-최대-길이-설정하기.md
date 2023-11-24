---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 최대 길이 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

작성일: 2021년 5월 15일

## 소개

SkyFloatingLabelTextField는 매우 유용한 사용자 지정 텍스트 필드입니다. 이 텍스트 필드를 사용하여 사용자가 텍스트를 입력할 수 있게 할 수 있지만, 때로는 입력 가능한 문자열의 최대 길이를 제한하고 싶을 수도 있습니다. 이 글에서는 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열의 최대 길이를 설정하는 방법에 대해 알아보겠습니다.

## 구현

SkyFloatingLabelTextField를 사용하기 전에, 먼저 SkyFloatingLabelTextField를 설치하고 프로젝트에 추가해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'SkyFloatingLabelTextField'
```

설치가 완료되었다면, 다음과 같이 Swift 코드로 최대 문자열 길이를 설정할 수 있습니다:

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
        
        // 최대 길이 설정
        textField.maxLength = 10
    }
}

extension ViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let text = textField.text else { return true }
        
        // 현재 길이 계산
        let newLength = text.count + string.count - range.length
        
        // 최대 길이를 초과하면 입력을 허용하지 않음
        return newLength <= textField.maxLength
    }
}
```

위 코드에서 `textField.maxLength` 속성을 사용하여 최대 길이를 설정할 수 있습니다. 그리고 `UITextFieldDelegate`를 구현하여 `shouldChangeCharactersIn` 메서드를 사용하여 현재 텍스트 필드에 텍스트를 입력할 때마다 길이를 체크하여 최대 길이를 초과하는지 확인합니다.

## 예제

다음은 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열의 최대 길이를 설정하는 방법을 보여주는 간단한 예제입니다.

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
        textField.maxLength = 10
    }

}

extension ViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let text = textField.text else { return true }
        
        let newLength = text.count + string.count - range.length
        
        return newLength <= textField.maxLength
    }
}
```

이 예제에서는 길이가 10자인 SkyFloatingLabelTextField를 만들고, 최대 길이를 10으로 설정합니다. 사용자가 텍스트를 입력할 때마다 입력한 텍스트의 길이를 체크하여 최대 길이를 초과하면 입력을 허용하지 않습니다.

## 결론

이번에는 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열의 최대 길이를 설정하는 방법에 대해 알아보았습니다. 이 기능을 사용하면 사용자의 입력을 제한할 수 있으므로 텍스트 필드의 유효성을 관리하기에 편리합니다.