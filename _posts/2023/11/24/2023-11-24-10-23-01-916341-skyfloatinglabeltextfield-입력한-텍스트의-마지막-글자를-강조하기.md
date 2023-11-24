---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트의 마지막 글자를 강조하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 개발된 사용자 정의 텍스트 필드 라이브러리입니다. 이 라이브러리를 사용하면 텍스트 필드에 부가적인 스타일링과 기능을 추가할 수 있습니다.

우리의 목표는 SkyFloatingLabelTextField에 입력된 텍스트의 마지막 글자를 강조하기 위한 기능을 구현하는 것입니다.

## 1. SkyFloatingLabelTextField 설치하기
먼저, SkyFloatingLabelTextField를 설치해야 합니다. CocoaPods를 사용하여 설치하는 것이 가장 쉬운 방법입니다. Podfile에 다음과 같이 추가한 후 `pod install`을 실행합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

## 2. 마지막 글자 강조하는 기능 추가하기
SkyFloatingLabelTextFieldDelegate를 구현하여 마지막 글자를 강조하는 기능을 추가할 수 있습니다. 아래의 예제 코드를 참고해주세요.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
        if let text = textField.text, !text.isEmpty {
            let lastCharIndex = text.index(before: text.endIndex)
            let lastChar = text[lastCharIndex]
            
            // 문자열을 동적으로 변형하여 마지막 글자를 강조하는 방식으로 변경해주세요.
            let attributedText = NSAttributedString(string: text, attributes: [NSAttributedString.Key.foregroundColor: UIColor.black])
            let mutableAttributedText = NSMutableAttributedString(attributedString: attributedText)
            mutableAttributedText.addAttributes([NSAttributedString.Key.foregroundColor: UIColor.red], range: NSRange(location: lastCharIndex.utf16Offset(in: text), length: 1))
            
            textField.attributedText = mutableAttributedText
        }
    }
}
```

위의 코드에서 `textFieldDidEndEditing` 메서드는 사용자가 텍스트 필드 편집을 마치고 포커스를 다른 곳으로 이동했을 때 호출됩니다. 이 때, 텍스트 필드에 입력된 텍스트에서 마지막 글자를 강조하려고 합니다.

문자열을 동적으로 변형하여 마지막 글자를 강조하는 방식으로 변경하였습니다. 변경한 `attributedText`를 텍스트 필드에 설정함으로써 마지막 글자가 강조되는 효과를 얻을 수 있습니다.

## 참고 자료
- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)