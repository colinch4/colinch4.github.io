---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 이미지 로딩 애니메이션 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이미지 로딩 시 사용자에게 진행 상태를 시각적으로 보여주는 애니메이션은 사용자 경험을 향상시키는 데 중요한 역할을 합니다. NVActivityIndicatorView는 Swift에서 이미지 로딩 애니메이션을 구현하는데 도움을 주는 유용한 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 기본적으로 로딩 상태를 표시하는 일련의 애니메이션을 제공합니다. 여러 가지 스타일과 색상을 사용하여 로딩 인디케이터를 사용자 정의할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. Podfile을 열고 아래와 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설치를 완료한 후, Xcode의 프로젝트 디렉토리에서 `pod install` 명령어를 실행합니다.

## NVActivityIndicatorView 사용법

1. 먼저, NVActivityIndicatorView를 import합니다.
```swift
import NVActivityIndicatorView
```

2. 상황에 맞게 설정한 뒤, 로딩 애니메이션을 표시할 뷰를 생성합니다.
```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .white, padding: nil)
```
여기서 `frame`은 로딩 애니메이션의 크기와 위치를 지정하고, `type`은 로딩 애니메이션의 스타일을 선택합니다. `color`는 로딩 애니메이션의 색상을 지정합니다. `padding`은 로딩 인디케이터의 패딩을 지정하는 옵셔널 매개변수입니다.

3. 로딩 애니메이션을 표시할 뷰에 추가합니다.
```swift
view.addSubview(activityIndicatorView)
```

4. 필요한 시점에 로딩 애니메이션을 시작하고 정지합니다.
```swift
activityIndicatorView.startAnimating()
activityIndicatorView.stopAnimating()
```

## NVActivityIndicatorView 사용 예제

다음은 NVActivityIndicatorView를 사용하여 이미지 로딩 애니메이션을 구현하는 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let imageView = UIImageView()
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .white, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        
        imageView.frame = CGRect(x: 100, y: 100, width: 200, height: 200)
        imageView.backgroundColor = .lightGray
        view.addSubview(imageView)
        
        view.addSubview(activityIndicatorView)
    }
    
    func loadImage() {
        activityIndicatorView.startAnimating()
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.activityIndicatorView.stopAnimating()
            self.imageView.image = UIImage(named: "example-image")
        }
    }
    
    @IBAction func startButtonTapped(_ sender: UIButton) {
        loadImage()
    }
}
```

위 예제에서는 `loadImage()` 함수에서 이미지 로딩 시간 동안 로딩 애니메이션을 표시하며, 로딩이 완료된 후 애니메이션을 정지하고 이미지를 표시합니다.

더 다양한 스타일과 설정 옵션을 사용하려면 NVActivityIndicatorView의 문서를 참조하시기 바랍니다.

참고: [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)