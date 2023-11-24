---
layout: post
title: "[swift] SkyFloatingLabelTextField 숫자 입력 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift 언어로 iOS 앱을 개발하다 보면, 숫자를 입력받아야 하는 경우가 많이 있습니다. 이때 입력 필드에 숫자만 입력되도록 제한하고 싶을 수 있습니다. 이번 포스트에서는 SkyFloatingLabelTextField를 사용하여 숫자 입력을 제한하는 방법을 알아보겠습니다.

## SkyFloatingLabelTextField란?

SkyFloatingLabelTextField는 Swift 언어로 개발된 사용하기 쉬운 UITextField의 하위 클래스입니다. 이 컴포넌트는 사용자가 입력 필드에 텍스트를 입력할 때 플레이스홀더 텍스트를 위로 이동시키는 스타일을 제공합니다. 또한, 커스텀 가능한 동적 플레이스홀더, 에러 메시지 표시 및 많은 유형의 입력 유효성 검사도 지원합니다.

## 숫자 입력 제한하기

SkyFloatingLabelTextField로 숫자 입력을 제한하려면 UITextFieldDelegate 프로토콜을 구현하여 사용자의 입력을 제어해야 합니다. 다음은 예시 코드입니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var numberTextField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        numberTextField.delegate = self
        numberTextField.keyboardType = .numberPad
    }

    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 숫자 입력만 허용
        let allowedCharacters = CharacterSet.decimalDigits
        let characterSet = CharacterSet(charactersIn: string)
        return allowedCharacters.isSuperset(of: characterSet)
    }
}
```

위 예시 코드에서 `numberTextField`는 SkyFloatingLabelTextField 인스턴스로, XIB 파일 등을 통해 사용자가 인터페이스를 만들고 연결할 수 있습니다. 이 예시에서는 `numberTextField`에 대해 delegate를 설정하고, 키보드 유형을 숫자 패드로 설정합니다.

그리고 `textField(_:shouldChangeCharactersIn:replacementString:)` 메서드를 구현하여 입력을 제어합니다. 이 메서드는 사용자가 텍스트 필드를 터치하거나 수정할 때 호출되는 UITextFieldDelegate의 메서드입니다. 여기서는 입력된 문자열이 숫자인지 확인하고, 숫자가 아닌 경우 입력을 거부하도록 합니다.

이제 앱을 실행하고 `numberTextField`에 문자를 입력하면 입력 상자에 숫자만 입력할 수 있습니다.

## 정리

SkyFloatingLabelTextField를 사용하여 Swift 언어로 iOS 앱을 개발할 때 숫자 입력을 제한하는 방법을 알아보았습니다. UITextFieldDelegate 프로토콜을 사용하여 입력을 제어하여 숫자만 입력되도록 할 수 있습니다. 이를 통해 앱의 사용자 경험을 향상시킬 수 있습니다.

더 자세한 정보는 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)의 공식 GitHub 저장소를 참고하시기 바랍니다.