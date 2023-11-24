---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 정규식 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개
SkyFloatingLabelTextField는 사용자가 텍스트를 입력할 때 라벨이 텍스트 필드 위로 이동하여 사용자에게 더 나은 사용자 경험을 제공하는 아름다운 텍스트 필드 구성 요소입니다. 이 글에서는 SkyFloatingLabelTextField에서 입력 가능한 문자열을 정규식으로 제한하는 방법을 알아보겠습니다.

## 구현

SkyFloatingLabelTextField에서 입력 가능한 문자열을 정규식으로 제한하려면 다음 단계를 따르세요.

1. SkyFloatingLabelTextFieldDelegate을 구현합니다.
2. delegate 함수 textField(_:shouldChangeCharactersIn:replacementString:) 내에서 정규식을 사용하여 입력을 검증합니다.
3. isValidInput(_:) 함수를 작성하여 정규식을 사용하여 입력을 유효성 검사합니다.
4. 입력이 유효하지 않을 경우, 사용자에게 알리기 위해 적절한 작업을 수행합니다.

```swift
import SkyFloatingLabelTextField

class MyViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        let updatedText = (textField.text as NSString?)?.replacingCharacters(in: range, with: string)
        guard let text = updatedText else {
            return true
        }
        let isValid = isValidInput(text)
        
        if isValid {
            // 유효한 입력인 경우
            return true
        } else {
            // 유효하지 않은 입력인 경우
            // 사용자에게 알림을 표시하거나, 입력을 무시할 수 있습니다.
            return false
        }
    }
    
    func isValidInput(_ text: String) -> Bool {
        let regexPattern = "^[A-Za-z0-9]+$" // 영문자와 숫자만 허용
        let regex = try! NSRegularExpression(pattern: regexPattern)
        let range = NSRange(location: 0, length: text.count)
        let matchRange = regex.rangeOfFirstMatch(in: text, options: .anchored, range: range)
        
        return matchRange.location != NSNotFound
    }
}
```

위의 예제 코드에서는 `SkyFloatingLabelTextField`의 `shouldChangeCharactersIn` 메서드를 사용하여 입력을 필터링합니다. `isValidInput(_:)` 함수에서는 정규식을 사용하여 입력을 유효성을 검사합니다. 유효한 입력인 경우에는 `true`를 반환하고, 그렇지 않은 경우에는 `false`를 반환하여 입력을 유효하지 않은 것으로 표시할 수 있습니다.

## 정리

이제 SkyFloatingLabelTextField에서 입력 가능한 문자열을 정규식으로 제한하는 방법을 알게 되었습니다. 정규식을 사용하여 원하는 문자열 패턴으로 입력을 제한하면 사용자에게 더 좋은 사용자 경험을 제공할 수 있습니다. 필요한 경우 입력이 유효하지 않은 경우 사용자에게 알림을 표시하거나, 입력을 무시할 수 있습니다.