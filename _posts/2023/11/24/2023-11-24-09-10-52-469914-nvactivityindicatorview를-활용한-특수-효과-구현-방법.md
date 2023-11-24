---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 특수 효과 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 또는 웹 사이트에서 특수 효과를 구현하고 싶을 때, NVActivityIndicatorView는 매우 유용한 도구입니다. NVActivityIndicatorView는 로딩 인디케이터의 다양한 스타일을 제공하여 애니메이션 효과를 쉽게 추가할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 및 macOS에서 사용할 수 있는 Swift 라이브러리입니다. 이 라이브러리는 로딩 인디케이터를 구현하기 위한 다양한 스타일과 설정 옵션을 제공합니다.

이 라이브러리의 사용 방법은 다음과 같습니다:

1. NVActivityIndicatorView 라이브러리를 프로젝트에 추가합니다. (CocoaPods를 사용하는 경우, Podfile에 `pod 'NVActivityIndicatorView'`를 추가하고 `pod install` 명령을 실행합니다.)
2. NVActivityIndicatorView를 사용하고 싶은 뷰 컨트롤러에서 `NVActivityIndicatorView` 인스턴스를 생성합니다.
3. 인스턴스를 원하는 위치에 추가하고, 시작 및 정지 메서드를 호출하여 애니메이션을 제어합니다.

### 예제 코드

다음은 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 구현하는 예제 코드입니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    var activityIndicator: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 스타일과 크기 설정
        let frame = CGRect(x: 0, y: 0, width: 80, height: 80)
        activityIndicator = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .blue, padding: 0)
        activityIndicator.center = view.center
        
        // 뷰에 로딩 인디케이터 추가
        view.addSubview(activityIndicator)
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        // 애니메이션 시작
        activityIndicator.startAnimating()
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        
        // 애니메이션 정지
        activityIndicator.stopAnimating()
    }
}
```

### 변수 설명

- `type`: 로딩 인디케이터의 스타일을 설정합니다. NVActivityIndicatorType 열거형의 다양한 스타일 중 하나를 선택할 수 있습니다.
- `color`: 로딩 인디케이터의 색상을 설정합니다.
- `padding`: 로딩 인디케이터의 패딩을 설정합니다. (기본값은 0)

## 참고 자료

- NVActivityIndicatorView GitHub 저장소: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)
- NVActivityIndicatorView 문서: [https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)

이런 식으로 NVActivityIndicatorView를 사용하여 특수 효과를 구현할 수 있습니다. 이러한 효과를 사용하여 앱 또는 웹 사이트의 사용자 경험을 향상시킬 수 있습니다.