---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트를 공유하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 UITextField의 대안으로 사용되는 커스텀 텍스트 필드입니다. 이 텍스트 필드를 사용하여 텍스트를 입력하고, 해당 텍스트를 공유하는 방법을 알아보겠습니다.

먼저, SkyFloatingLabelTextField를 프로젝트에 추가하고 설정하는 방법은 다음과 같습니다:

1. 프로젝트에서 `Podfile`을 열고 `pod 'SkyFloatingLabelTextField'`을 추가합니다. 그런 다음 터미널에서 `pod install` 명령을 실행하여 패키지를 설치합니다.
2. 필요한 파일에서 `import SkyFloatingLabelTextField`를 추가합니다.
3. 스토리보드 또는 코드에서 SkyFloatingLabelTextField를 만들고 적절한 위치와 크기로 배치합니다.

SkyFloatingLabelTextField로 사용자가 입력한 텍스트를 공유하기 위해 다음과 같은 단계를 따를 수 있습니다:

1. SkyFloatingLabelTextField의 아울렛을 생성합니다. 예를 들어, 다음과 같이 코드에서 Outlet을 생성할 수 있습니다:

```swift
@IBOutlet weak var textField: SkyFloatingLabelTextField!
```

2. 사용자가 텍스트를 입력하고 "공유" 버튼을 누를 때, 아래의 코드를 사용하여 텍스트를 공유합니다:

```swift
func shareText() {
    guard let text = textField.text else {
        return
    }
    
    let activityViewController = UIActivityViewController(activityItems: [text], applicationActivities: nil)
    present(activityViewController, animated: true, completion: nil)
}
```

위의 코드에서, `textField.text`는 사용자가 입력한 텍스트를 가져옵니다. 그리고 `UIActivityViewController`를 사용하여 텍스트를 공유하는데 사용됩니다. `activityItems` 배열에는 공유할 텍스트를 포함하고 있습니다.

이제 사용자가 입력한 텍스트를 SkyFloatingLabelTextField를 사용하여 공유하는 방법을 알았습니다. 프로젝트에 SkyFloatingLabelTextField를 추가하고, 텍스트를 공유하는 코드를 적용하여 텍스트 입력과 공유를 용이하게 만들어보세요!

参考文献:
- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)