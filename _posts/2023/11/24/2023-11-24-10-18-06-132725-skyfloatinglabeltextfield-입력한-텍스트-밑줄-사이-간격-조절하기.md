---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 밑줄 사이 간격 조절하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField은 Swift에서 많이 사용되는 UITextField의 확장 라이브러리입니다. 이 라이브러리는 입력한 텍스트에 아름답게 애니메이션과 스타일을 적용할 수 있는 기능을 제공합니다. 이번에는 SkyFloatingLabelTextField에서 입력한 텍스트의 밑줄 사이 간격을 조절하는 방법에 대해 알아보겠습니다.

## Step 1: SkyFloatingLabelTextField 가져오기

먼저, Cocoapods을 사용하여 SkyFloatingLabelTextField 라이브러리를 프로젝트에 추가합니다. `Podfile`에 아래와 같이 라이브러리를 추가합니다. 

```ruby
pod 'SkyFloatingLabelTextField', '~> 4.0'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## Step 2: 코드 작성하기

SkyFloatingLabelTextField를 사용하는 ViewController에 해당하는 파일을 열고, `import SkyFloatingLabelTextField`를 추가합니다. 그리고 IBOutlet으로 SkyFloatingLabelTextField를 연결합니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 밑줄 사이 간격 조절
        let lineGap: CGFloat = 8.0
        textField.lineHeight = textField.font!.lineHeight + lineGap
    }
}
```

위의 코드에서는 텍스트 필드의 `lineHeight` 프로퍼티를 조절하여 밑줄 사이의 간격을 조절하고 있습니다. 원하는 간격을 설정한 후, 해당 값을 `textField.lineHeight`에 대입하면 됩니다.

## Step 3: 결과 확인하기

앱을 빌드하고 실행하여 SkyFloatingLabelTextField가 정상적으로 화면에 표시되는지 확인합니다. 텍스트를 입력하고 밑줄 사이의 간격이 조절되는 것을 확인할 수 있습니다.

## 결론

SkyFloatingLabelTextField 라이브러리를 사용하여 입력한 텍스트의 밑줄 사이 간격을 조절하는 방법에 대해 알아보았습니다. 위의 단계를 따라하고 원하는 간격으로 밑줄 사이 간격을 조절해보세요.

관련 레퍼런스:
- [SkyFloatingLabelTextField GitHub 레포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)