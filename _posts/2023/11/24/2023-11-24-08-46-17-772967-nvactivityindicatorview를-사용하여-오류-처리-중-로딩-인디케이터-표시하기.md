---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 오류 처리 중 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

애플리케이션에서 오류 처리 중 화면에 로딩 인디케이터를 표시하는 것은 사용자에게 진행 중인 작업을 알리는 좋은 방법입니다. 이러한 기능을 구현하기 위해 `NVActivityIndicatorView`를 사용할 수 있습니다. 이 라이브러리는 많은 다양한 스타일의 로딩 인디케이터를 제공하므로 애플리케이션에 맞게 선택할 수 있습니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 빠르고 쉽게 사용할 수 있는 iOS용 로딩 인디케이터입니다. 다양한 스타일과 색상의 로딩 인디케이터를 제공하여 애플리케이션에 통일성을 부여할 수 있습니다. 또한, 소스 코드에 적용하기 간단하며, 다양한 커스터마이징 옵션을 제공합니다.

## NVActivityIndicatorView 설치

`NVActivityIndicatorView`를 사용하기 위해 먼저 Cocoapods를 이용하여 프로젝트에 라이브러리를 설치해야 합니다. `Podfile`을 열고 다음과 같이 라이브러리를 추가하고 저장합니다.

```swift
pod 'NVActivityIndicatorView'
```

터미널에서 프로젝트 폴더로 이동한 후 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용법

1. 먼저, `NVActivityIndicatorView`를 import 합니다.
```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터의 기본 뷰를 생성합니다. 이 뷰는 로딩 인디케이터가 나타날 화면에 추가됩니다.
```swift
var activityIndicatorView: NVActivityIndicatorView!
```

3. 로딩 인디케이터를 초기화하고 설정합니다.
```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

4. 로딩 인디케이터를 화면에 추가합니다.
```swift
view.addSubview(activityIndicatorView)
```

5. 로딩 인디케이터를 시작하고 정지합니다.
```swift
activityIndicatorView.startAnimating() // 로딩 인디케이터 시작
activityIndicatorView.stopAnimating() // 로딩 인디케이터 정지
```

`type` 매개 변수를 사용하여 로딩 인디케이터의 스타일을 선택할 수 있으며, `color` 매개 변수를 사용하여 로딩 인디케이터의 색상을 선택할 수 있습니다. 또한, `padding` 매개 변수를 사용하여 인디케이터의 안쪽 여백을 설정할 수 있습니다.

## 예시

애플리케이션에서 데이터를 로딩하는 중에 로딩 인디케이터를 표시하는 예시를 살펴보겠습니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {
    
    var activityIndicatorView: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 초기화 및 설정
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
        view.addSubview(activityIndicatorView)
        
        // 데이터 로딩 시작
        loadData()
    }
    
    func loadData() {
        // 로딩 인디케이터 시작
        activityIndicatorView.startAnimating()
        
        // 네트워크 요청 등 데이터 로딩 작업 수행
        
        // 데이터 로딩 완료 후 로딩 인디케이터 정지
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예시에서는 `loadData()` 메서드에서 네트워크 요청이나 데이터 로딩 작업을 수행하는 동안에 로딩 인디케이터가 화면에 표시됩니다. 데이터 로딩이 완료된 후에는 `activityIndicatorView.stopAnimating()`을 호출하여 로딩 인디케이터를 정지시킵니다.

이제 애플리케이션에서 오류 처리 중에 로딩 인디케이터를 표시하는 방법을 알게 되었습니다. `NVActivityIndicatorView`를 사용하면 간편하게 로딩 인디케이터를 구현할 수 있으므로, 애플리케이션의 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)