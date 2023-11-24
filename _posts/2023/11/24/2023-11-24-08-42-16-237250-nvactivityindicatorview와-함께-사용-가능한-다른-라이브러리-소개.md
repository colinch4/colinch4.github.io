---
layout: post
title: "[swift] NVActivityIndicatorView와 함께 사용 가능한 다른 라이브러리 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 애플리케이션에서 로딩 인디케이터를 구현할 수 있는 강력한 라이브러리입니다. 이 라이브러리를 사용하면 다양한 스타일과 애니메이션 효과를 가진 인디케이터를 쉽게 추가할 수 있습니다.

하지만 NVActivityIndicatorView만으로는 모든 상황에 적합하지 않을 수 있습니다. 따라서 다른 라이브러리를 함께 사용하여 보다 다양한 인디케이터를 구현할 수 있습니다. 이번 블로그에서는 NVActivityIndicatorView와 함께 사용 가능한 몇 가지 라이브러리를 소개하겠습니다.

## 1. SVProgressHUD

SVProgressHUD는 로딩 인디케이터뿐만 아니라 경고 메시지, 성공 메시지 등 다양한 상태 메시지를 표시할 수 있는 라이브러리입니다. NVActivityIndicatorView와 함께 사용하면 로딩 중에 메시지를 표시할 수 있습니다. 

**예시 코드:**

```swift
SVProgressHUD.show()
SVProgressHUD.show(withStatus: "Loading")
```

## 2. JGProgressHUD

JGProgressHUD는 다양한 스타일과 애니메이션 효과를 가진 인디케이터를 제공하는 라이브러리입니다. NVActivityIndicatorView와 함께 사용하면 인디케이터의 스타일을 더욱 다양하게 변경할 수 있습니다.

**예시 코드:**

```swift
let hud = JGProgressHUD(style: .dark)
hud.textLabel.text = "Loading"
hud.show(in: self.view)
```

## 3. MBProgressHUD

MBProgressHUD는 인디케이터와 메시지 표시, 진행 상태 바 등 다양한 기능을 제공하는 라이브러리입니다. NVActivityIndicatorView와 함께 사용하면 로딩 인디케이터뿐만 아니라 다양한 기능을 구현할 수 있습니다.

**예시 코드:**

```swift
MBProgressHUD.showAdded(to: self.view, animated: true)
MBProgressHUD.showHUDAddedTo(self.view, animated: true).labelText = "Loading"
```

## 4. Lottie

Lottie는 Adobe After Effects로 만든 애니메이션을 iOS 애플리케이션에 쉽게 적용할 수 있는 라이브러리입니다. NVActivityIndicatorView와 함께 사용하면 더욱 다양하고 멋진 애니메이션 인디케이터를 구현할 수 있습니다.

**예시 코드:**

```swift
let animationView = AnimationView(name: "loading_animation")
animationView.play()
```

이 외에도 다양한 인디케이터 라이브러리가 있으며, NVActivityIndicatorView와 함께 사용할 수 있습니다. 어떤 라이브러리를 선택할지는 프로젝트에 따라 다를 수 있으므로, 사용 목적과 요구 사항에 따라 적합한 라이브러리를 선택하는 것이 중요합니다.

> 참고 문서:
> - [SVProgressHUD GitHub Repository](https://github.com/SVProgressHUD/SVProgressHUD)
> - [JGProgressHUD GitHub Repository](https://github.com/JonasGessner/JGProgressHUD)
> - [MBProgressHUD GitHub Repository](https://github.com/jdg/MBProgressHUD)
> - [Lottie GitHub Repository](https://github.com/airbnb/lottie-ios)