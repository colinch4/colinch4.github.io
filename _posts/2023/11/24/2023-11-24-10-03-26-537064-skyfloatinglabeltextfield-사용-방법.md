---
layout: post
title: "[swift] SkyFloatingLabelTextField 사용 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개
SkyFloatingLabelTextField는 Swift로 작성된 텍스트 필드 커스텀 라이브러리입니다. 이 라이브러리는 사용자가 텍스트 필드에 값을 입력할 때 라벨이 위로 올라가고, 값이 입력되지 않을 경우 다시 내려가는 동작을 제공합니다. 이 글에서는 SkyFloatingLabelTextField의 사용 방법에 대해 알아보겠습니다.

## 설치
SkyFloatingLabelTextField는 CocoaPods을 통해 설치할 수 있습니다. Podfile에 아래와 같이 추가 후 설치합니다.

```swift
pod 'SkyFloatingLabelTextField'
```

설치가 완료되면, import 문을 통해 SkyFloatingLabelTextField를 프로젝트에 가져옵니다.

```swift
import SkyFloatingLabelTextField
```

## 사용법
SkyFloatingLabelTextField를 사용하기 위해서는 먼저 해당 클래스의 인스턴스를 생성해야 합니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 50))
```

텍스트 필드의 속성을 설정하고 싶은 경우, 다음과 같이 직접 접근할 수 있습니다.

```swift
textField.placeholder = "이름"
textField.title = "이름"
textField.tintColor = UIColor.blue
```

또한, 아래와 같이 delegate 메소드를 통해 텍스트 필드의 값을 가져올 수 있습니다.

```swift
textField.delegate = self

func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    guard let text = textField.text else { return false }
    print("입력된 값: \(text)")
    return true
}
```

마지막으로, 텍스트 필드를 화면에 추가하고 레이아웃을 설정합니다.

```swift
view.addSubview(textField)
textField.translatesAutoresizingMaskIntoConstraints = false
textField.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
textField.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
```

## 마무리
이 글에서는 SkyFloatingLabelTextField의 사용 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 텍스트 필드에 동적인 라벨 효과를 쉽게 추가할 수 있습니다. 더 자세한 내용은 [공식 GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)에서 확인할 수 있습니다.