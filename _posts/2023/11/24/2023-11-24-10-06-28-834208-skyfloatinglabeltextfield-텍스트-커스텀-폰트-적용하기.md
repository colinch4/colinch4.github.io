---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 커스텀 폰트 적용하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 사용할 수 있는 고급 텍스트 필드 컨트롤이다. 이 컨트롤을 사용하면 사용자가 입력하는 텍스트의 유효성을 검사하고, 텍스트 필드 주위에 부드러운 애니메이션 효과를 적용할 수 있다. 

이번에는 SkyFloatingLabelTextField에 커스텀 폰트를 적용하는 방법에 대해 알아보겠다.

## 폰트 파일 추가하기

먼저, 커스텀 폰트를 앱에 추가해야 한다. 폰트 파일(.ttf 또는 .otf)을 프로젝트에 드래그 앤 드롭하고, **Copy items if needed** 옵션을 선택하여 폰트 파일을 앱 번들에 복사한다.

## UIFontExtension 생성하기

다음으로, 폰트 파일을 사용하기 위해 `UIFontExtension` 클래스를 생성한다. 이 클래스는 폰트를 로드하고 `UIFontDescriptor`로 폰트 속성을 구성하는 역할을 한다.

```swift
extension UIFont {
    enum CustomFont: String {
        case regular = "CustomFont-Regular"
        case bold = "CustomFont-Bold"
        // 필요한 폰트 스타일을 추가로 선언한다.
    }
    
    static func customFont(style: CustomFont, size: CGFloat) -> UIFont {
        guard let font = UIFont(name: style.rawValue, size: size) else {
            return UIFont.systemFont(ofSize: size)
        }
        return font
    }
}
```

## SkyFloatingLabelTextField에 커스텀 폰트 적용하기

이제 SkyFloatingLabelTextField에서 커스텀 폰트를 사용할 수 있다. 폰트를 설정하기 전에 `editingChanged` 이벤트 핸들러에서 커스텀 폰트를 로드해야 한다. 폰트를 설정하려는 뷰 컨트롤러에서 다음과 같이 코드를 작성한다.

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.addTarget(self, action: #selector(textFieldEditingChanged(_:)), for: .editingChanged)
    }
    
    @objc func textFieldEditingChanged(_ textField: UITextField) {
        textField.font = UIFont.customFont(style: .regular, size: 16)
    }
}
```

SkyFloatingLabelTextField 객체의 폰트 속성을 업데이트하려면 `editingChanged` 이벤트를 사용해야 한다. 위의 코드에서 `textFieldEditingChanged` 메서드는 텍스트 필드가 편집될 때마다 호출되며, 폰트를 커스텀 폰트로 설정하고 있다.

이제 커스텀 폰트가 SkyFloatingLabelTextField에 적용된 것을 확인할 수 있다.

## 마무리

이번에는 SkyFloatingLabelTextField에 커스텀 폰트를 적용하는 방법에 대해 알아보았다. 커스텀 폰트를 적용하면 앱의 디자인을 더욱 개성적으로 꾸밀 수 있으며, 사용자 경험을 향상시킬 수 있다.