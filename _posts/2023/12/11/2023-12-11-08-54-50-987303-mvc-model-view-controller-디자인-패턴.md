---
layout: post
title: "[swift] MVC (Model-View-Controller) 디자인 패턴"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

MVC 디자인 패턴은 소프트웨어 개발에서 사용되는 일반적인 아키텍처이며, 애플리케이션의 코드를 간결하게 유지하고 유지보수를 용이하게 하기 위해 설계되었습니다. MVC는 "Model-View-Controller"의 약자로, 애플리케이션의 기능을 세 부분으로 나누어 관리합니다.

## 목차
1. [Model](#model)
2. [View](#view)
3. [Controller](#controller)
4. [MVC의 장단점](#장단점)

## Model
Model은 애플리케이션의 데이터를 처리하고 상태를 관리하는 부분입니다. 데이터의 구조, 유효성 검사, 데이터베이스 연동 등과 같은 업무 로직이 Model에 속합니다.

```swift
struct User {
    let name: String
    let age: Int
}
```

## View
View는 사용자 인터페이스를 나타내는 부분이며, 주로 화면에 표시될 내용과 사용자의 입력에 대한 반응을 담당합니다. iOS 애플리케이션에서는 주로 Storyboard 또는 코드로 작성된 UI가 View에 속합니다.

```swift
class UserView: UIView {
    // UI 요소들을 구성하고 사용자 입력에 대한 이벤트를 처리하는 로직
}
```

## Controller
Controller는 사용자 입력 및 이벤트를 처리하고 Model과 View 간의 상호작용을 조율하는 부분입니다. 사용자가 입력한 정보를 Model에 전달하거나, Model의 상태 변화를 감지하여 이를 View에 반영하는 역할을 수행합니다.

```swift
class UserController: UIViewController {
    var userModel: User
    var userView: UserView
    
    // 사용자 입력 및 Model-View 간의 연결 로직을 구현
}
```

## MVC의 장단점
MVC 디자인 패턴은 각 부분이 독립적으로 유지되기 때문에 유연하고 확장성이 뛰어나며, 코드의 재사용성이 용이합니다. 하지만 이로 인해 프로젝트 규모가 커지면서 각 부분 간의 의존성이 복잡해질 수 있고, 이로 인해 유지보수가 어려워질 수도 있습니다.

MVC는 iOS 애플리케이션 개발에서 널리 사용되는 디자인 패턴 중 하나이며, 올바르게 적용할 경우 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

이상으로 MVC 디자인 패턴에 대한 소개를 마치겠습니다.

[참조 링크 : Apple Developer Documentation](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Model-View-Controller/Model-View-Controller.html)