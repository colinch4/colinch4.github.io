---
layout: post
title: "[swift] ObservableObject와 @Published 속성"
description: " "
date: 2023-12-15
tags: [swift]
comments: true
share: true
---

SwiftUI에서 상태 관리를 하기 위해 ObservableObject와 @Published 속성을 사용할 수 있습니다. 이 두 가지 요소는 SwiftUI 앱에서 데이터를 관리하고 감시하는 데 사용됩니다. 

## ObservableObject

ObservableObject는 SwiftUI에서 **감시 가능한 객체**를 정의하기 위해 사용됩니다. 이 프로토콜을 준수하는 객체는 해당 객체가 변경될 때 SwiftUI 뷰에 자동으로 알림을 보낼 수 있습니다.

```swift
import SwiftUI

class MyModel: ObservableObject {
    @Published var name: String = "John"
    @Published var age: Int = 25
}
```

위의 예제에서 MyModel은 ObservableObject 프로토콜을 준수하는 클래스입니다. @Published 속성을 사용하여 해당 속성의 변경 사항을 알릴 수 있도록 표시합니다.

## @Published 속성

@Published 속성은 ObservableObject를 통해 감시 가능한 객체의 속성을 정의할 때 사용됩니다. 해당 속성의 값이 변경될 때마다 SwiftUI는 이를 감지하고 자동으로 UI를 업데이트합니다.

```swift
import SwiftUI

class MyModel: ObservableObject {
    @Published var name: String = "John"
    @Published var age: Int = 25
}
```

위의 예제에서 name과 age는 @Published 속성으로 정의되어 있으므로 이 속성들의 값이 변경될 때마다 SwiftUI가 이를 감지하고 자동으로 UI를 업데이트합니다.

ObservableObject와 @Published 속성을 사용하여 SwiftUI 앱에서 데이터를 효과적으로 관리하고 UI 업데이트를 자동화할 수 있습니다.

이러한 기능들은 SwiftUI 앱을 더욱 동적이고 반응형으로 만들어주며, 복잡한 상태 관리를 간편하게 처리할 수 있도록 도와줍니다.

## 결론

ObservableObject와 @Published 속성은 SwiftUI에서 상태 관리를 쉽게 만들어주는 강력한 도구입니다. 이들을 적절히 활용하면 SwiftUI 앱을 보다 효과적으로 구축할 수 있습니다.

이상으로 ObservableObject와 @Published 속성에 대한 간단한 소개를 마치도록 하겠습니다. 감사합니다.

[SwiftUI 소스 코드](https://developer.apple.com/documentation/swiftui)