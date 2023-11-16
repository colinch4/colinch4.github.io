---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 컴포넌트 디자인 및 유동적인 사용자 인터렉션 처리하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

로딩 화면은 사용자에게 작업이 진행 중임을 알려주고, 대기 시간을 최소화하는 데 도움을 줍니다. 이번 기사에서는 Swift의 NVActivityIndicatorView 라이브러리를 사용하여 로딩 화면을 디자인하고, 사용자 인터랙션에 유연하게 대응하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 및 macOS 앱에서 사용자에게 로딩 상태를 시각적으로 표시하는 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 사용하기 간편하고 유연한 커스터마이징이 가능합니다.

## 2. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 통해 라이브러리를 설치해야 합니다. Podfile에 다음 코드를 추가하고, 터미널에서 pod install을 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

## 3. 로딩 화면 디자인하기

NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법은 간단합니다. 먼저, 사용할 스타일과 크기를 지정하여 NVActivityIndicatorView의 인스턴스를 생성합니다.

```swift
import NVActivityIndicatorView

let loadingIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                              type: .circleStrokeSpin,
                                              color: .white,
                                              padding: nil)
```

위의 코드에서는 .circleStrokeSpin 스타일의 로딩 인디케이터를 생성하고, 크기는 50x50으로 지정하였습니다. 또한, 인디케이터의 색상은 흰색으로 설정하였습니다.

이제 화면에 로딩 인디케이터를 추가하고 애니메이션을 실행할 준비를 합니다.

```swift
// 화면에 로딩 인디케이터 추가
view.addSubview(loadingIndicator)

// 로딩 애니메이션 시작
loadingIndicator.startAnimating()
```

## 4. 사용자 인터랙션 처리하기

로딩 화면을 사용하는 가장 일반적인 시나리오는 백그라운드 작업이 완료될 때까지 사용자의 인터랙션을 제한하는 것입니다. 이를 위해 화면에 뷰를 덮어서 사용자 입력을 막으면 됩니다.

```swift
// 로딩 인디케이터를 담을 컨테이너 뷰 생성
let overlayView = UIView(frame: view.bounds)
overlayView.backgroundColor = UIColor(white: 0, alpha: 0.5)

// 로딩 인디케이터 컨테이너 뷰를 화면 위에 추가
view.addSubview(overlayView)
view.bringSubviewToFront(overlayView)
```

위의 코드에서는 로딩 인디케이터를 담을 컨테이너 뷰를 생성하고, 뒷 배경을 흐리게 만들기 위해 알파 값을 설정했습니다. 이후에 컨테이너 뷰를 화면에 추가하고, 화면의 맨 앞으로 가져오도록 설정합니다.

로딩이 완료되면 컨테이너 뷰를 화면에서 제거하여 사용자의 인터랙션을 다시 활성화할 수 있습니다.

```swift
// 로딩이 완료되었을 때 컨테이너 뷰를 화면에서 제거
overlayView.removeFromSuperview()
```

## 5. 커스터마이징 및 추가 기능

NVActivityIndicatorView를 사용하면 다양한 스타일의 로딩 인디케이터를 지원하며, 원하는 대로 커스터마이징할 수 있습니다. 라이브러리의 문서를 참조하여 원하는 스타일과 옵션을 설정할 수 있습니다. 

- [NVActivityIndicatorView GitHub repository](https://github.com/ninjaprox/NVActivityIndicatorView)

또한, 로딩 화면 외에도 다른 사용자 피드백, 메시지 또는 애니메이션을 추가로 표시할 수 있습니다. 예를 들어, 성공 또는 실패 메시지를 띄우거나, 진행 중인 작업의 진행 상태를 나타낼 수도 있습니다.

## 결론

NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하고 사용자 인터랙션을 처리하는 방법을 알아보았습니다. 이를 통해 사용자에게 작업이 진행 중임을 시각적으로 전달하고, 대기 시간을 최소화할 수 있습니다. 적절한 로딩 화면의 사용은 앱 사용자 경험을 향상시키고, 더 나은 사용자 인터랙션을 제공하는 데 도움이 될 것입니다.