---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 색상 애니메이션 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용할 수 있는 매우 유용한 라이브러리입니다. 이번 글에서는 SkyFloatingLabelTextField의 입력 포커스 색상 애니메이션을 설정하는 방법에 대해 알아보겠습니다.

## 1. SkyFloatingLabelTextField 설치하기

SkyFloatingLabelTextField를 사용하려면 먼저 프로젝트에 해당 라이브러리를 설치해야 합니다. 이를 위해 Cocoapods를 사용할 수 있습니다. Podfile에 아래와 같이 작성한 후, `pod install` 명령어를 실행하여 설치합니다.

```swift
target 'YourProject' do
  use_frameworks!
  pod 'SkyFloatingLabelTextField'
end
```

## 2. 입력 포커스 색상 애니메이션 설정하기

SkyFloatingLabelTextField의 입력 포커스 색상 애니메이션을 설정하려면 `tintColor` 속성과 입력 포커스가 변경될 때 호출되는 delegate 메서드를 사용해야 합니다.

```swift
// SkyFloatingLabelTextFieldDelegate 선언
class MyViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {
  
  @IBOutlet weak var textField: SkyFloatingLabelTextField!
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // Delegate 설정
    textField.delegate = self
    
    // 입력 포커스 색상 설정
    textField.tintColor = .blue
  }
  
  // 입력 포커스가 변경될 때 호출되는 메서드
  func textFieldDidBeginEditing(_ textField: UITextField) {
    // 입력 포커스 색상 애니메이션 설정
    textField.tintColor = .red
  }
  
  func textFieldDidEndEditing(_ textField: UITextField) {
    // 입력 포커스가 사라질 때 색상 설정
    textField.tintColor = .blue
  }
  
}
```

위의 예제 코드에서는 `SkyFloatingLabelTextFieldDelegate` 프로토콜을 채택하여 delegate 메서드를 구현했습니다. `textFieldDidBeginEditing` 메서드는 입력 포커스가 시작될 때 호출되며, 여기서는 포커스 색상을 빨간색으로 변경하고 있습니다. 마찬가지로 `textFieldDidEndEditing` 메서드는 입력 포커스가 종료될 때 호출되며, 여기서는 포커스 색상을 파란색으로 되돌리고 있습니다.

이렇게 함으로써 SkyFloatingLabelTextField의 입력 포커스 색상을 원하는대로 애니메이션으로 설정할 수 있습니다.

## 3. 참고 자료

- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)