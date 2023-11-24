---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 유효성 검사하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 개발된 오픈 소스 라이브러리로, 텍스트 필드에 부가적인 기능을 제공합니다. 이 라이브러리를 사용하면 입력 가능한 문자열의 유효성을 쉽게 검사할 수 있습니다. 이번 글에서는 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열을 유효성 검사하는 방법에 대해 알아보겠습니다.

## 1. 프로젝트에 SkyFloatingLabelTextField 추가하기

먼저, SkyFloatingLabelTextField를 사용하기 위해 프로젝트에 해당 라이브러리를 추가해야 합니다. 가장 쉬운 방법은 CocoaPods를 사용하는 것입니다. Podfile에 다음과 같이 추가한 후 `pod install`을 실행합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

Pod 설치 후에는 Xcode 프로젝트를 다시 열어서 import 구문을 추가합니다.

```swift
import SkyFloatingLabelTextField
```

## 2. 유효성 검사 기능 추가하기

SkyFloatingLabelTextField는 delegate를 통해 입력된 문자열의 유효성을 검사할 수 있습니다. UITextFieldDelegate 프로토콜을 준수하는 클래스를 만들고, 해당 클래스의 인스턴스를 텍스트 필드의 delegate로 지정합니다.

다음은 입력 가능한 문자열이 영문 대문자로만 이루어져 있는지 검사하는 예제입니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력된 문자열이 영문 대문자로만 이루어져 있는지 검사
        let regex = try! NSRegularExpression(pattern: "^[A-Z]*$")
        let text = (textField.text as NSString?)?.replacingCharacters(in: range, with: string)
        let matches = regex.matches(in: text!, range: NSRange(location: 0, length: text!.count))
        let isValid = matches.count > 0
        
        // 유효성 검사 결과에 따라 텍스트 필드 스타일 변경
        if isValid {
            textField.errorMessage = nil
        } else {
            textField.errorMessage = "영문 대문자로 입력해주세요."
        }
        
        return true
    }
}
```

위 예제에서는 textField(_:shouldChangeCharactersIn:replacementString:) 메서드를 통해 입력된 문자열의 유효성을 검사하고, 검사 결과에 따라 텍스트 필드의 스타일을 변경합니다. 정규식 패턴을 사용하여 영문 대문자로만 이루어진 문자열인지 검사하고, 결과에 따라 error message를 설정하여 유저에게 알립니다.

## 3. 추가적인 유효성 검사 기능 구현하기

위 예제에서는 영문 대문자로만 이루어진 문자열인지 검사하는 기능을 구현했지만, 다른 유효성 검사 기능도 동일한 방식으로 추가할 수 있습니다. 예를 들어, 숫자로만 이루어진 문자열인지, 이메일 형식에 맞는지, 전화번호 형식에 맞는지 등을 검사할 수 있습니다.

다음은 숫자로만 이루어진 문자열인지 검사하는 예제입니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    // 입력된 문자열이 숫자로만 이루어져 있는지 검사
    let regex = try! NSRegularExpression(pattern: "^[0-9]*$")
    let text = (textField.text as NSString?)?.replacingCharacters(in: range, with: string)
    let matches = regex.matches(in: text!, range: NSRange(location: 0, length: text!.count))
    let isValid = matches.count > 0
    
    // 유효성 검사 결과에 따라 텍스트 필드 스타일 변경
    if isValid {
        textField.errorMessage = nil
    } else {
        textField.errorMessage = "숫자로 입력해주세요."
    }
    
    return true
}
```

위와 같이 검사하고자 하는 유효성 검사 패턴을 정규식으로 정의한 후, 해당 정규식 패턴과 입력된 문자열을 비교하여 유효성 검사 결과를 판단합니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열의 유효성을 검사할 수 있습니다. 위 예제 코드를 참고하여 원하는 유효성 검사 기능을 추가하고, 유저에게 알맞은 메시지를 제공할 수 있습니다. 이를 통해 좀 더 사용자 친화적인 앱을 개발할 수 있습니다.

## 참고 자료

- [SkyFloatingLabelTextField Github Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)