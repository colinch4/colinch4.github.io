---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터렉션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발 중에 사용자가 어떤 작업을 기다려야 할 때 화면 로딩 상태를 시각적으로 표현하여 사용자에게 진행 상태를 알려주는 것은 중요합니다. 이를 위해 NVActivityIndicatorView를 사용하여 간편하게 화면 로딩 인디케이터를 구현할 수 있습니다. 또한, 사용자 인터렉션을 제한하여 작업이 완료될 때까지 다른 작업을 수행하지 못하도록 할 수도 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 강력한 로딩 인디케이터를 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상의 로딩 인디케이터를 제공하며, 사용하기 쉬운 인터페이스를 가지고 있습니다. 

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 

```
pod 'NVActivityIndicatorView'
```

설치가 완료되면 프로젝트 파일을 열고 `import NVActivityIndicatorView`를 추가해줍니다.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하려면 다음 단계를 따르세요.

1. NVActivityIndicatorView를 사용할 뷰 컨트롤러에서 `NVActivityIndicatorViewDelegate` 프로토콜을 적용합니다.

2. 화면 로딩 상태를 표시하려는 위치에 NVActivityIndicatorView 인스턴스를 생성합니다.

    ```swift
    private var activityIndicatorView: NVActivityIndicatorView?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // NVActivityIndicatorView 스타일과 프레임을 설정합니다.
        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .circleStrokeSpin, color: .blue)
        activityIndicatorView?.center = view.center
        
        // 뷰에 NVActivityIndicatorView를 추가합니다.
        if let indicatorView = activityIndicatorView {
            view.addSubview(indicatorView)
        }
    }
    ```

3. 로딩 상태를 표시하고 사용자 인터렉션을 제한해야 할 때 `startAnimating()` 메서드를 호출하여 인디케이터를 시작합니다.

    ```swift
    func showLoading() {
        activityIndicatorView?.startAnimating()
        view.isUserInteractionEnabled = false // 사용자 인터렉션 제한
    }
    ```

4. 로딩 상태가 완료되었을 때 `stopAnimating()` 메서드를 호출하여 인디케이터를 중지합니다.

    ```swift
    func hideLoading() {
        activityIndicatorView?.stopAnimating()
        view.isUserInteractionEnabled = true // 사용자 인터렉션 활성화
    }
    ```

## 결론

NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터렉션을 제한하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 사용하기 쉽고 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 사용자 경험을 향상시킬 수 있습니다. 앱의 유저 인터페이스 디자인에 화면 로딩 인디케이터를 추가하는 것을 고려해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)