---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 터치 이벤트 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 Swift 프로그래밍 언어를 사용하여 터치 이벤트 중 로딩 표시를 구현하는 방법을 알아보겠습니다. 이를 위해 `NVActivityIndicatorView` 라이브러리를 사용할 것입니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 iOS 앱에서 사용할 수 있는 고성능 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 사용자에게 로딩 중임을 시각적으로 알려줄 수 있습니다.

## NVActivityIndicatorView 설치

먼저, 프로젝트의 `Podfile`에 다음과 같이 `NVActivityIndicatorView`를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음, 터미널을 열고 프로젝트의 디렉토리로 이동한 후 `pod install` 명령어를 실행합니다.

```bash
$ cd [프로젝트 디렉토리]
$ pod install
```

이제 `NVActivityIndicatorView`가 프로젝트에 추가되었으므로, 이제부터 로딩 표시를 구현할 수 있습니다.

## 로딩 표시하기

1. 먼저, 사용할 ViewController에 `import NVActivityIndicatorView` 코드를 추가합니다.
2. `NVActivityIndicatorViewDelegate` 프로토콜을 구현합니다.
3. `NVActivityIndicatorView` 인스턴스를 생성하고 원하는 스타일과 색상을 적용합니다.
4. 터치 이벤트 발생 시 로딩 인디케이터를 화면에 표시합니다.
5. 터치 이벤트가 완료되면 로딩 인디케이터를 제거합니다.

다음은 위 단계를 구체적으로 설명한 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController, NVActivityIndicatorViewDelegate {
    
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // NVActivityIndicatorView를 초기화합니다.
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)
        activityIndicatorView.center = self.view.center
        self.view.addSubview(activityIndicatorView)
        
        // 터치 이벤트를 처리하고자 하는 View에 gesture recognizer를 추가합니다.
        let tapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(handleTap(_:)))
        self.view.addGestureRecognizer(tapGestureRecognizer)
    }
    
    @objc func handleTap(_ sender: UITapGestureRecognizer) {
        // 터치 이벤트가 발생하면 로딩 인디케이터를 화면에 표시합니다.
        activityIndicatorView.startAnimating()
        
        // 터치 이벤트를 처리하는 작업을 수행합니다. (예: 네트워크 요청, 데이터 처리)
        
        // 터치 이벤트가 완료되면 로딩 인디케이터를 제거합니다.
        activityIndicatorView.stopAnimating()
    }

}
```

위 예제 코드에서 `NVActivityIndicatorView`의 인스턴스를 만들 때 원하는 스타일과 색상을 선택할 수 있습니다. 또한 로딩 인디케이터의 크기와 위치를 조정할 수 있습니다.

추가로, `NVActivityIndicatorViewDelegate` 프로토콜을 채택하여 로딩 인디케이터의 상태 변화를 감지하고 처리할 수도 있습니다.

## 결론

이렇게 Swift에서 `NVActivityIndicatorView`를 사용하여 터치 이벤트 중 로딩 표시를 구현하는 방법을 알아보았습니다. 이 라이브러리를 사용하면 앱의 사용자가 언제 어떤 작업이 진행 중인지 알 수 있게 됩니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.