---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트의 대소문자 구분 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField은 사용자가 입력한 텍스트를 입력 창에 표시하고 레이블로 위로 올려주는 텍스트 필드 라이브러리입니다. 이 라이브러리를 사용하여 입력한 텍스트의 대소문자 구분을 설정하고자 할 때 아래의 방법을 따를 수 있습니다.

1. `SkyFloatingLabelTextFieldDelegate`를 구현하기 위해 클래스에 `UITextFieldDelegate`를 상속합니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    // TextField에 입력된 텍스트가 변경될 때마다 호출되는 메서드
    func textFieldDidChangeSelection(_ textField: UITextField) {
        // 대소문자 구분을 설정하고자 할 때
        textField.autocapitalizationType = .none
    }
}
```

2. 대소문자 구분을 설정하기 위해 `textFieldDidChangeSelection` 메서드에서 `autocapitalizationType` 속성을 `.none`으로 설정해줍니다. 이렇게 하면 사용자가 입력한 텍스트의 대소문자 구분이 유지됩니다.

```swift
textField.autocapitalizationType = .none
```

위의 코드를 이용하여 SkyFloatingLabelTextField에서 입력한 텍스트의 대소문자 구분을 설정할 수 있습니다.

## 참고 자료
- [SkyFloatingLabelTextField 공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)