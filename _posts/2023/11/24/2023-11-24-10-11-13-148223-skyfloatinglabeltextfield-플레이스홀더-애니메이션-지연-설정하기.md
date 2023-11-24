---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 애니메이션 지연 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 구현된 유명한 텍스트 필드 라이브러리 입니다. 이 라이브러리는 플레이스홀더 애니메이션을 제공해주어 사용자에게 시각적인 피드백을 제공합니다. 이번에는 SkyFloatingLabelTextField에서 플레이스홀더 애니메이션의 지연을 설정하는 방법에 대해 알아보겠습니다.

SkyFloatingLabelTextField의 기본 동작은 사용자가 텍스트 필드를 터치하면 플레이스홀더 텍스트가 위로 올라가는 애니메이션을 보여줍니다. 하지만 때로는 이 애니메이션을 특정 시간 동안 지연시키고 싶을 수 있습니다.

다음은 SkyFloatingLabelTextField의 플레이스홀더 애니메이션을 지연시키는 예제 코드입니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        setupTextField()
    }

    func setupTextField() {
        textField.placeholder = "Enter your name"
        textField.placeholderColor = .gray
        textField.selectedTitleColor = .black
        textField.selectedLineColor = .black

        // 플레이스홀더 애니메이션 지연 설정
        textField.placeholderFadeDuration = 0.5
        textField.placeholderAnimationDuration = 1.0
    }
}
```

위의 예제에서 `textField`는 `SkyFloatingLabelTextField`의 인스턴스입니다. 우리는 `placeholderFadeDuration`과 `placeholderAnimationDuration` 속성을 설정하여 플레이스홀더 애니메이션의 지연을 조정하고 있습니다. `placeholderFadeDuration`은 플레이스홀더가 사라지는 애니메이션의 지속 시간을 나타내며, `placeholderAnimationDuration`은 플레이스홀더가 위로 올라가는 애니메이션의 지속 시간을 나타냅니다.

이제 위의 코드를 실행하면 `SkyFloatingLabelTextField`의 플레이스홀더 애니메이션의 지연이 설정되어 텍스트 필드를 터치했을 때 플레이스홀더가 지정된 시간 동안 나타나지 않다가 나타나는 것을 확인할 수 있습니다.

자세한 내용은 [SkyFloatingLabelTextField의 공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하시기 바랍니다.