---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트에 마스킹 기능 추가하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요

이번에는 SkyFloatingLabelTextField 라이브러리를 사용하여 입력한 텍스트에 마스킹 기능을 추가하는 방법을 알아보겠습니다. 마스킹 기능을 추가하면 사용자가 입력한 텍스트를 숨기거나, 특정 문자로 대체할 수 있습니다. 이를 통해 보안성을 높이고 사용자의 개인 정보를 보호할 수 있습니다.

## 사전 준비

먼저, SkyFloatingLabelTextField 라이브러리를 프로젝트에 추가해야 합니다. Cocoapods를 사용하는 경우, Podfile 파일에 다음과 같이 추가합니다.

```swift
pod 'SkyFloatingLabelTextField'
```

프로젝트 디렉토리에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 마스킹 기능 추가하기

SkyFloatingLabelTextField의 `text` 프로퍼티에 접근하여 마스킹 기능을 추가할 수 있습니다. 아래의 코드를 참고하여 마스킹 기능을 적용해보세요.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }
    
    @objc private func textFieldDidChange(_ textField: UITextField) {
        let maskedText = maskText(textField.text)
        textField.text = maskedText
    }
    
    private func maskText(_ text: String?) -> String {
        guard let text = text else { return "" }
        
        let maskedText = String(repeating: "*", count: text.count)
        return maskedText
    }
}
```

위의 코드에서는 `textField` IBOutlet을 연결하고, `textFieldDidChange` 메서드를 이용하여 `textField`의 텍스트를 마스킹한 후 다시 할당합니다. `text` 프로퍼티 값을 `maskText` 메서드로 전달하여 마스킹된 텍스트를 받아옵니다. `maskText` 메서드에서는 받은 텍스트의 길이만큼 '*' 문자를 반복하여 마스킹된 텍스트를 생성하고 반환합니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력한 텍스트에 마스킹 기능을 추가하는 방법을 알아보았습니다. 마스킹 기능을 활용하여 사용자의 개인 정보를 보호하고 보안성을 높일 수 있습니다. 이를 응용하여 프로젝트에 적용해보세요.

## 참고 자료

- [SkyFloatingLabelTextField 라이브러리 GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)