---
layout: post
title: "[swift] SkyFloatingLabelTextField 키보드 타입 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---
SkyFloatingLabelTextField는 iOS 앱에서 사용자 입력을 받기 위한 텍스트 필드 컴포넌트입니다. 이번에는 SkyFloatingLabelTextField 컴포넌트를 사용하여 키보드 타입을 설정하는 방법에 대해 알아보겠습니다.

### 키보드 타입 설정하기
SkyFloatingLabelTextField 컴포넌트는 UITextField를 상속하고 있기 때문에, UITextField에서 제공되는 키보드 타입을 설정할 수 있습니다. 다음은 키보드 타입을 설정하는 예제 코드입니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 키보드 타입 설정
        textField.keyboardType = .emailAddress
    }
}
```

위의 예제 코드에서는 `textField`라는 SkyFloatingLabelTextField 인스턴스를 생성하고, `keyboardType` 속성을 `.emailAddress`로 설정하였습니다. 이렇게 설정된 키보드 타입은 사용자가 해당 텍스트 필드를 터치했을 때 나타나는 키보드의 종류를 결정합니다.

### 지원되는 키보드 타입
UITextField 클래스에서 제공하는 다양한 키보드 타입 중에서 필요한 타입을 선택할 수 있습니다. 일반적으로 사용되는 키보드 타입은 다음과 같습니다.

- `.default`: 기본 키보드 타입
- `.asciiCapable`: ASCII 문자만 입력 가능한 키보드 타입
- `.numbersAndPunctuation`: 숫자와 구두점 입력 가능한 키보드 타입
- `.URL`: URL 주소 입력 가능한 키보드 타입
- `.emailAddress`: 이메일 주소 입력 가능한 키보드 타입
- `.phonePad`: 전화번호 입력 가능한 키보드 타입
- `.decimalPad`: 소수점 입력 가능한 키보드 타입

그 외에도 다양한 키보드 타입이 제공되니 필요에 따라 선택하여 사용하면 됩니다.

### 결론
SkyFloatingLabelTextField 컴포넌트를 사용하여 키보드 타입을 설정하는 방법에 대해 알아보았습니다. UITextField의 `keyboardType` 속성을 이용하여 원하는 키보드 타입을 설정할 수 있으며, 다양한 타입을 지원하므로 특정 입력에 맞는 키보드를 선택하여 사용할 수 있습니다.