---
layout: post
title: "[swift] Swift Presentr와 UIAlertController의 차이점"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱을 개발하는 중에 다양한 상황에서 사용자에게 알림을 제공해야 할 때가 있습니다. Swift에서는 UIAlertController와 Swift Presentr을 사용하여 알림창을 만들 수 있습니다. 이 두 가지 방법에는 몇 가지 차이점이 있으므로 어떤 상황에서 어떤 방법을 사용해야 하는지 알아보겠습니다.

## UIAlertController

UIAlertController는 iOS에서 제공하는 기본적인 알림창입니다. 다양한 유형의 알림창을 만들 수 있으며, 기본적인 알림 메시지, 선택지를 제공하는 알림창, 사용자의 입력을 받을 수 있는 알림창 등을 만들 수 있습니다.

```swift
let alertController = UIAlertController(title: "알림", message: "사용자에게 보여줄 메시지", preferredStyle: .alert)
alertController.addAction(UIAlertAction(title: "확인", style: .default, handler: nil))
present(alertController, animated: true, completion: nil)
```

이와 같이 UIAlertController를 사용하여 간단한 알림창을 만들 수 있습니다. 화면에 모달로 표시되며, 사용자의 선택 또는 확인 버튼을 클릭할 때 적절한 동작을 수행할 수 있습니다.

## Swift Presentr

Swift Presentr은 UIAlertController에 비해 좀 더 다양한 사용자 정의 옵션을 제공하는 패키지입니다. 더 많은 커스터마이제이션과 화려한 애니메이션을 원하는 경우에 유용합니다.

예를 들어, Swift Presentr를 사용하여 커스텀 알림창을 만들 수 있습니다.

```swift
let presenter = Presentr(presentationType: .popup)
let alertController = UIAlertController(title: "알림", message: "사용자에게 보여줄 메시지", preferredStyle: .alert)
let customAction = AlertAction(title: "커스텀 액션", style: .destructive) {
    print("커스텀 액션 실행")
}
alertController.addAction(UIAlertAction(title: "기본 액션", style: .default, handler: nil))
alertController.addAction(customAction)
presenter.present(alertController, animated: true, completion: nil)
```

위의 예제에서는 Swift Presentr의 Presentr 객체를 생성한 후, UIAlertController를 생성합니다. 그리고 Presentr 객체의 present 메서드를 사용하여 알림창을 화면에 표시합니다. 이렇게 함으로써 UIAlertController를 더 유연하게 커스터마이징할 수 있습니다.

## 선택하는 기준

UIAlertController는 기본적인 알림창을 만들어야 할 때 사용할 수 있습니다. 간단하고 빠르게 구현될 수 있으며, 기본적인 사용자 모델에 맞게 동작합니다.

Swift Presentr은 좀 더 복잡한 컨트롤 및 다양한 커스터마이징이 필요한 경우에 유용합니다. 특히 화려하고 멋진 애니메이션 효과를 원할 때 사용할 수 있습니다.

알림창의 목적과 UI 요구 사항에 따라 UIAlertController와 Swift Presentr 중 하나를 선택할 수 있습니다.