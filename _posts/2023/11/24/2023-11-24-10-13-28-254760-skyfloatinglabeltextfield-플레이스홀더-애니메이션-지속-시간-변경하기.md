---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 애니메이션 지속 시간 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

`SkyFloatingLabelTextField`는 Swift에서 사용할 수 있는 사용자 정의 텍스트 필드 라이브러리입니다. 이 라이브러리는 플로팅 레이블 효과를 가진 텍스트 필드를 만들 수 있습니다. 하지만 기본적으로 플레이스홀더 애니메이션은 일정한 시간 동안 지속됩니다.

이번 글에서는 `SkyFloatingLabelTextField`의 플레이스홀더 애니메이션의 지속 시간을 변경하는 방법을 알아보겠습니다.

## `SkyFloatingLabelTextField` 초기화

우선 `SkyFloatingLabelTextField`를 사용하기 위해 프로젝트에 해당 라이브러리를 추가해야 합니다. 이제 `SkyFloatingLabelTextField`를 초기화하는 방법을 알아보겠습니다. 

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 플레이스홀더 애니메이션 지속 시간 설정 (단위: 초)
        SkyFloatingLabelTextField.animationDuration = 0.5
        
        // 플레이스홀더 애니메이션 지속 시간 확인
        print(SkyFloatingLabelTextField.animationDuration)
        
        // SkyFloatingLabelTextField 초기화
        textField = SkyFloatingLabelTextField(frame: CGRect(x: 50, y: 100, width: 200, height: 40))
        textField.placeholder = "이름"
        view.addSubview(textField)
    }
}
```

`SkyFloatingLabelTextField.animationDuration` 프로퍼티를 통해 플레이스홀더 애니메이션의 지속 시간을 설정할 수 있습니다. 위의 예제에서는 0.5초로 설정되어 있습니다.

## Reference

- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)