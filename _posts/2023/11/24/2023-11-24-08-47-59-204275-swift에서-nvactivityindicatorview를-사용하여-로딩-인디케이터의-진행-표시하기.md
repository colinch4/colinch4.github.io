---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터의 진행 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

웹 페이지나 앱에서 데이터를 가져 오거나 작업을 수행 할 때, 로딩 인디케이터가 필요한 경우가 있습니다. 로딩 인디케이터는 사용자에게 작업이 진행 중임을 알림으로써 사용자 경험을 향상시키는 데 도움이 됩니다.

NVActivityIndicatorView는 Swift로 작성된 오픈 소스 라이브러리로, 여러 가지 스타일의 로딩 인디케이터를 제공합니다. 이 라이브러리를 사용하면 간편하게 로딩 인디케이터를 구현할 수 있습니다.

## 라이브러리 설치
먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 프로젝트에 추가해야 합니다. 프로젝트 디렉토리에서 `Podfile`을 열고 다음 줄을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

터미널을 열고 다음 명령을 실행하여 Cocoapods를 설치합니다:

```bash
pod install
```

## NVActivityIndicatorView 사용하기
NVActivityIndicatorView를 사용하기 위해 다음 단계를 수행해야 합니다.

1. 먼저, `import` 문을 사용하여 `NVActivityIndicatorView`를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 표시할 `UIView`를 만듭니다. 이는 로딩 인디케이터가 나타날 위치를 나타냅니다.

```swift
let containerView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
containerView.center = view.center
```

3. `NVActivityIndicatorView` 인스턴스를 생성합니다. 여기서는 스타일과 색상을 설정하고, 크기를 지정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40),
                                                    type: .circleStrokeSpin,
                                                    color: .gray,
                                                    padding: nil)
```

4. `activityIndicatorView`를 `containerView`에 추가하고, `containerView`를 뷰에 추가합니다.

```swift
containerView.addSubview(activityIndicatorView)
view.addSubview(containerView)
```

5. `activityIndicatorView`를 시작하고 중지할 수 있습니다. 예를 들어, 데이터를 가져 오는 작업을 시작할 때 인디케이터를 시작하고, 작업이 완료되면 중지합니다.

```swift
activityIndicatorView.startAnimating()

// 데이터 가져오기 작업 수행

activityIndicatorView.stopAnimating()
```

## 결론
NVActivityIndicatorView를 사용하면 간단하게 로딩 인디케이터를 구현할 수 있습니다. 이 라이브러리는 다양한 스타일의 인디케이터를 제공하며, 사용자에게 작업이 진행 중임을 시각적으로 알려줄 수 있습니다.

더 많은 정보와 예제 코드는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.