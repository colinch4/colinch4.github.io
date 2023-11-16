---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 재사용 가능한 로딩 화면 컴포넌트 만들기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발 중에는 사용자가 데이터를 로딩하거나 작업을 실행할 때 로딩 화면을 보여주는 것이 일반적입니다. 이것은 사용자 경험을 향상시키는 중요한 요소입니다. 이번 기술 블로그에서는 NVActivityIndicatorView 라이브러리를 사용하여 iOS 앱에서 재사용 가능한 로딩 화면 컴포넌트를 만드는 방법을 알아보겠습니다.

## NVActivityIndicatorView란 무엇인가요?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 인디케이터 뷰 라이브러리입니다. 이 라이브러리는 다양한 로딩 애니메이션을 제공하며, 인터페이스를 간편하게 구현할 수 있습니다. 또한 NVActivityIndicatorView는 다양한 색상, 크기 및 애니메이션 속도 설정 등 맞춤 설정 옵션도 제공합니다.

## 프로젝트 설정

먼저, 프로젝트에 NVActivityIndicatorView를 추가해야 합니다. NVActivityIndicatorView는 CocoaPods를 사용하여 쉽게 설치할 수 있습니다. Podfile에 다음 줄을 추가하고 터미널에서 `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView', '~> 5.1.1'
```

이제 프로젝트를 열고 `import NVActivityIndicatorView`를 추가하여 NVActivityIndicatorView를 사용할 준비를 마쳤습니다.

## 로딩 화면 컴포넌트 만들기

로딩 화면 컴포넌트를 만들기 위해 다음과 같은 단계를 따라주세요.

1. 뷰 컨트롤러에 NVActivityIndicatorView 인스턴스를 추가합니다. 
   ```swift
   private var activityIndicatorView: NVActivityIndicatorView!
   ```

2. 뷰 컨트롤러의 viewDidLoad() 메서드에서 NVActivityIndicatorView에 적절한 설정을 적용합니다.
   ```swift
   override func viewDidLoad() {
       super.viewDidLoad()

       let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
       activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .gray, padding: nil)

       // 로딩 화면을 뷰의 가운데에 보이도록 설정
       activityIndicatorView.center = view.center

       view.addSubview(activityIndicatorView)
   }
   ```

3. 로딩 화면 컴포넌트를 시작하고 중지하는 메서드를 구현합니다.
   ```swift
   func startLoading() {
       activityIndicatorView.startAnimating()
   }

   func stopLoading() {
       activityIndicatorView.stopAnimating()
   }
   ```

## 사용 예시

로딩 화면 컴포넌트를 사용하는 예시를 살펴보겠습니다.

1. 데이터 로딩 시작 시 로딩 화면 컴포넌트를 보여줍니다.
   ```swift
   startLoading()
   ```

2. 데이터 로딩이 완료되면 로딩 화면 컴포넌트를 숨깁니다.
   ```swift
   stopLoading()
   ```

## 결론

이제 이제 NVActivityIndicatorView를 사용하여 재사용 가능한 로딩 화면 컴포넌트를 만들 수 있습니다. 사용자가 앱에서 작업을 실행하는 동안 로딩 화면을 표시하여 사용자 경험을 향상시킬 수 있습니다. NVActivityIndicatorView는 간편하게 사용할 수 있고 다양한 커스터마이징 옵션을 제공합니다. 앱에 로딩 화면 컴포넌트를 추가하여 앱의 전반적인 사용자 경험을 향상시키세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://cocoapods.org/pods/NVActivityIndicatorView)