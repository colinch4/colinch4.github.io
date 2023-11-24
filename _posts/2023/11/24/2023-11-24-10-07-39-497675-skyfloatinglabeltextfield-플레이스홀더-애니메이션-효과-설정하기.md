---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 애니메이션 효과 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

![SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField/raw/master/Screenshots/showcase.gif)

SkyFloatingLabelTextField는 iOS 앱에서 텍스트 필드를 구현할 때 유용한 라이브러리입니다. 이 라이브러리는 플레이스홀더에 애니메이션 효과를 적용하여 사용자에게 더 직관적이고 시각적으로 매력적인 입력 폼을 제공합니다.

이번 글에서는 SkyFloatingLabelTextField의 플레이스홀더 애니메이션 효과를 설정하는 방법에 대해 알아보겠습니다. 

## SkyFloatingLabelTextField 설정

SkyFloatingLabelTextField를 사용하기 위해서는 먼저 라이브러리를 프로젝트에 추가해야 합니다. Swift Package Manager를 사용하는 경우 `dependencies`에 추가하고, CocoaPods를 사용하는 경우 `Podfile`에 추가해주세요.

### Swift Package Manager

1. Xcode에서 프로젝트를 열고 `File` 메뉴에서 `Swift Packages` -> `Add Package Dependency`를 선택합니다.
2. 나타나는 팝업 창의 `Enter package repository URL` 입력란에 `https://github.com/Skyscanner/SkyFloatingLabelTextField.git`을 입력하고 `Next`를 클릭합니다.
3. 버전 선택을 위해 `Up to Next Major`을 선택하고, `Next`를 클릭합니다.
4. 나타나는 팝업 창에서 사용할 SkyFloatingLabelTextField 버전을 선택하고 `Next`를 클릭합니다.
5. 프로젝트에 라이브러리가 추가되었습니다.

### CocoaPods

1. 프로젝트 폴더에서 `Podfile`을 엽니다.
2. `Podfile`에 다음과 같은 코드를 추가합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

3. 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.
4. 프로젝트를 열어 `.xcworkspace` 파일을 실행합니다.

## 플레이스홀더 애니메이션 효과 사용하기

SkyFloatingLabelTextField를 사용하여 텍스트 필드를 생성하고 플레이스홀더 애니메이션을 적용하는 방법은 간단합니다.

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
textField.placeholder = "이름"
textField.title = "이름을 입력해주세요"
textField.selectedTitleColor = .blue
textField.selectedLineColor = .blue
```

위의 코드에서 `SkyFloatingLabelTextField`을 생성한 후 `placeholder`에 플레이스홀더 텍스트를 설정하고, `title`에 플레이스홀더와 관련된 제목 문자열을 설정합니다. `selectedTitleColor`와 `selectedLineColor`는 필드가 선택되었을 때의 색상을 지정하는 것입니다.

## 플레이스홀더 애니메이션 효과 커스터마이징

SkyFloatingLabelTextField는 플레이스홀더 애니메이션 효과를 사용자의 요구에 맞게 커스터마이징할 수 있습니다. 이를 위해서는 다음과 같은 프로퍼티를 사용할 수 있습니다.

- `selectedTitleColor`: 선택된 상태에서 제목(플레이스홀더)의 색상을 설정합니다.
- `selectedLineColor`: 선택된 상태에서 아래쪽 경계선의 색상을 설정합니다.
- `lineHeight`: 아래쪽 경계선의 두께를 설정합니다.

호출 가능한 메소드:

- `setTitleVisible(_:animated:)`: 제목 보이기/숨기기 여부를 설정하고, 애니메이션 효과 여부를 선택적으로 설정합니다.
- `setError(_:animated:)`: 오류 메시지를 표시하고 애니메이션 효과로 플레이스홀더와 경계선의 색상을 변경합니다.

추가적으로, SkyFloatingLabelTextField는 다양한 커스텀화 옵션과 기능을 제공하기 때문에 사용자 매뉴얼을 참고하는 것이 도움이 됩니다. 

## 마무리

SkyFloatingLabelTextField를 사용하여 플레이스홀더 애니메이션 효과를 설정하는 방법에 대해 알아보았습니다. 이를 통해 사용자 친화적이고 시각적으로 매력적인 텍스트 필드를 구현할 수 있습니다. 라이브러리의 다양한 기능과 옵션을 적용하여 프로젝트에 맞는 텍스트 필드를 만들어보세요!

[GitHub - SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)

[Swift Package Manager - SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)

[CocoaPods - SkyFloatingLabelTextField](https://cocoapods.org/pods/SkyFloatingLabelTextField)