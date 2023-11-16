---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 로딩 화면 만들기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱을 개발할 때, 데이터를 가져오거나 처리할 때 사용자에게 로딩 화면을 제공하는 것은 좋은 사용자 경험을 제공하는 중요한 요소입니다. 이번에는 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 로딩 화면을 만드는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 애니메이션 로딩 인디케이터를 만들기 위한 오픈 소스 라이브러리입니다. 많은 다양한 스타일의 로딩 인디케이터를 제공하며, 간편하게 사용할 수 있습니다.

## 설치하기

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. 프로젝트의 `Podfile`에 아래와 같이 추가해주세요.

```ruby
pod 'NVActivityIndicatorView'
```

터미널에서 프로젝트 디렉토리로 이동한 후, `pod install` 명령어를 실행하여 라이브러리를 설치해주세요.

## 사용하기

1. NVActivityIndicatorView 추가하기

   로딩 화면을 사용할 화면에 `NVActivityIndicatorView`를 추가해야 합니다. Interface Builder를 사용하거나 코드로 추가할 수 있습니다.

   ```swift
   import NVActivityIndicatorView

   class LoadingViewController: UIViewController {
       var activityIndicatorView: NVActivityIndicatorView!

       override func viewDidLoad() {
           super.viewDidLoad()

           activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
           activityIndicatorView.color = .gray
           view.addSubview(activityIndicatorView)
           activityIndicatorView.center = view.center
       }
   }
   ```

   `NVActivityIndicatorView`를 이용해 로딩 화면의 크기, 색상 등을 설정할 수 있습니다. 위의 예시에서는 화면 중앙에 50x50 크기의 회색 로딩 인디케이터를 추가하였습니다.

2. 로딩 화면 보이기

   데이터를 가져오는 등의 로딩 작업을 시작할 때, 아래와 같이 `NVActivityIndicatorView`를 시작하여 로딩 화면을 보여줄 수 있습니다.

   ```swift
   activityIndicatorView.startAnimating()
   ```

3. 로딩 화면 숨기기

   작업이 완료된 후 로딩 화면을 숨기고 싶을 때에는 `stopAnimating()` 메서드를 사용합니다.

   ```swift
   activityIndicatorView.stopAnimating()
   ```

## 추가 설정하기

`NVActivityIndicatorView`를 좀 더 세부적으로 조정하고 싶을 때에는 다양한 설정 옵션을 사용할 수 있습니다. 아래는 일부 예시입니다.

- `type`: 로딩 인디케이터의 스타일을 설정합니다. `circleStrokeSpin`과 같은 다양한 스타일을 제공합니다.
- `color`: 로딩 인디케이터의 색상을 설정합니다.
- `padding`: 로딩 인디케이터의 외부 공간을 설정합니다.
- `backgroundColor`: 로딩 인디케이터의 배경색을 설정합니다.

자세한 설정 옵션은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 마치며

이번에는 NVActivityIndicatorView를 사용하여 Swift에서 로딩 화면을 만드는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 사용하기 쉽고 다양한 스타일의 로딩 인디케이터를 제공하기 때문에, 앱의 사용자 경험을 향상시키는 데 유용하게 활용할 수 있습니다.