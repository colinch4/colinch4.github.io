---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 컬러 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 텍스트 필드와 함께 사용하기 좋은 커스텀 UI 라이브러리입니다. 이 라이브러리를 사용하면 텍스트 필드의 플레이스홀더 컬러를 쉽게 설정할 수 있습니다.

### 1. SkyFloatingLabelTextField 추가하기
SkyFloatingLabelTextField를 프로젝트에 추가하기 위해 먼저 CocoaPods를 이용하여 다운로드 합니다. Podfile에 다음과 같은 라인을 추가한 다음 터미널에서 `pod install`을 실행하세요.

```ruby
pod 'SkyFloatingLabelTextField'
```

### 2. UITextField 대신 SkyFloatingLabelTextField 사용하기
기존의 UITextField를 SkyFloatingLabelTextField로 변경하기 위해 인터페이스 빌더에서 텍스트 필드를 선택하고 클래스를 `SkyFloatingLabelTextField`로 변경합니다.

### 3. 플레이스홀더 컬러 설정하기
플레이스홀더 컬러를 설정하기 위해 아래 코드를 사용합니다.

```swift
textField.placeholderColor = UIColor.red
```

위의 코드에서 `textField`는 `SkyFloatingLabelTextField`의 인스턴스입니다. `placeholderColor` 속성을 원하는 컬러로 설정하면 플레이스홀더의 색상이 변경됩니다.

### 4. 예제 코드

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField! 

    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.placeholderColor = UIColor.red
    }
}
```

위의 예제에서 `textField`는 Storyboard에서 생성한 `SkyFloatingLabelTextField`의 IBOutlet입니다. `viewDidLoad()` 메서드에서 `placeholderColor`를 설정하여 플레이스홀더의 컬러를 변경합니다.

SkyFloatingLabelTextField 라이브러리를 사용하면 간편하게 텍스트 필드의 플레이스홀더 컬러를 설정할 수 있습니다. 이를 통해 앱의 디자인을 더욱 개성있게 표현할 수 있습니다.

### 참고 자료
- [SkyFloatingLabelTextField GitHub](https://github.com/Skyscanner/SkyFloatingLabelTextField)