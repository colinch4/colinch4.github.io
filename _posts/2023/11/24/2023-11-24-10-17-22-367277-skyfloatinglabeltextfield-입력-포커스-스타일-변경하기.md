---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 스타일 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용할 수 있는 사용자 정의 가능한 텍스트 필드입니다. 이 텍스트 필드는 입력된 텍스트에 라벨을 부착하여 사용자에게 좀 더 직관적인 입력 경험을 제공합니다.

이번에는 SkyFloatingLabelTextField의 입력 포커스 스타일을 변경하는 방법에 대해 알아보겠습니다.

## 설치

SkyFloatingLabelTextField를 사용하려면 먼저 CocoaPods나 Swift Package Manager를 통해 해당 라이브러리를 설치해야 합니다.

CocoaPods에서 설치하기:

```ruby
pod 'SkyFloatingLabelTextField'
```

Swift Package Manager를 사용하여 설치하기:

1. Xcode에서 프로젝트를 열고 "File" -> "Swift Packages" -> "Add Package Dependency"를 선택합니다.
2. 패키지 URL에 `https://github.com/Skyscanner/SkyFloatingLabelTextField.git`를 입력하고 "Next"를 클릭합니다.
3. 최신 버전의 SkyFloatingLabelTextField를 선택하고 "Next"를 클릭합니다.
4. 필요한 대상에 SkyFloatingLabelTextField를 추가하고 "Finish"를 클릭합니다.

## 입력 포커스 스타일 변경하기

SkyFloatingLabelTextField에서 입력 포커스 스타일을 변경하려면 다음과 같은 단계를 따릅니다:

1. SkyFloatingLabelTextField의 인스턴스를 만듭니다.

   ```swift
   let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
   ```

2. 입력 포커스 스타일을 설정합니다.

   SkyFloatingLabelTextField의 `selectedTitleColor` 속성을 사용하여 텍스트 필드의 제목 색상을 변경할 수 있습니다. 이 속성을 사용하여 입력 포커스가 있는 경우 제목의 색상을 변경할 수 있습니다.

   ```swift
   textField.selectedTitleColor = UIColor.red
   ```

   또한 `selectedLineColor` 속성을 사용하여 텍스트 필드의 밑줄 색상도 변경할 수 있습니다.

   ```swift
   textField.selectedLineColor = UIColor.red
   ```

   추가적으로 `selectedTitleFont` 속성을 사용하여 선택된 상태에서 글꼴을 변경할 수도 있습니다.

   ```swift
   textField.selectedTitleFont = UIFont.boldSystemFont(ofSize: 14)
   ```

3. 변경된 스타일을 적용합니다.

   ```swift
   textField.layoutSubviews()
   ```

4. 변경된 스타일이 적용된 SkyFloatingLabelTextField를 화면에 추가합니다.

   ```swift
   view.addSubview(textField)
   ```

이제 SkyFloatingLabelTextField의 입력 포커스 스타일을 변경하는 방법을 알게 되었습니다. 이를 통해 보다 다양하고 맞춤화된 사용자 인터페이스를 구현할 수 있습니다.

더 많은 정보와 사용 예제는 [공식 GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)에서 확인할 수 있습니다.