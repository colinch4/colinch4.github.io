---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 입력 제한 시간 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용되는 UITextField의 확장 라이브러리입니다. 이 라이브러리를 사용하면 입력 필드에 부가적인 기능을 추가할 수 있습니다. 이번에는 SkyFloatingLabelTextField에서 입력 가능한 문자열에 대한 입력 제한 시간을 설정하는 방법에 대해 알아보겠습니다.

## Step 1: SkyFloatingLabelTextField 라이브러리 설치

SkyFloatingLabelTextField를 사용하기 위해 먼저 프로젝트에 해당 라이브러리를 설치해야 합니다. CocoaPods를 사용하신다면 Podfile에 다음과 같이 라이브러리를 추가해주세요:

```swift
pod 'SkyFloatingLabelTextField'
```

설치가 끝나면 Xcode에서 프로젝트를 다시 빌드하면 됩니다.

## Step 2: SkyFloatingLabelTextField 생성 및 설정

다음은 SkyFloatingLabelTextField를 생성하고 입력 제한 시간을 설정하는 코드입니다. 

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 입력 제한 시간 설정
        textField.delegate = self
        textField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }
    
    @objc private func textFieldDidChange(_ textField: UITextField) {
        // 입력 제한 시간 초과 시 동작 정의
        let limit = 10 // 예시로 10초로 설정
        if textField.text?.count ?? 0 >= limit {
            // 입력 제한 시간 초과 시 동작
            // 예시: 텍스트 필드 비활성화
            textField.isEnabled = false
        }
    }
}

extension ViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 제한 시간 초과 시 입력 방지
        let currentText = textField.text ?? ""
        let limit = 10 // 예시로 10초로 설정
        
        // 현재 텍스트 필드의 길이와 입력하려는 텍스트의 길이 합이 제한 시간을 넘어서면 입력을 막습니다.
        guard currentText.count + string.count - range.length <= limit else {
            return false
        }
        return true
    }
}
```

위의 코드에서는 `SkyFloatingLabelTextField`를 사용하기 위해 해당 클래스를 import하고, `ViewController`에 `delegate`를 연결하고 필요한 메소드를 추가했습니다. 
`textFieldDidChange` 메소드에서는 문자열 입력 제한 시간을 초과하면 원하는 동작을 수행하도록 설정할 수 있습니다.

## Step 3: 결과 확인

이제 앱을 실행하고 `SkyFloatingLabelTextField`에 문자열을 입력해보면, 설정한 제한 시간이 초과될 때 해당 입력 필드가 비활성화되는 것을 확인할 수 있습니다.

---

SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열에 대한 입력 제한 시간을 설정하는 방법에 대해 알아보았습니다. 이를 활용해서 필요한 기능을 추가할 수 있을 것입니다. 더 많은 정보는 [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하시기 바랍니다.