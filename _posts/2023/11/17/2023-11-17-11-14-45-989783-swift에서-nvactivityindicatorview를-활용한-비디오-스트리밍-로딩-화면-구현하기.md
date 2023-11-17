---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 활용한 비디오 스트리밍 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 활용하여 비디오 스트리밍 로딩 화면을 만드는 방법을 알아보겠습니다.

## NVActivityIndicatorView 소개

NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터(Loading Indicator)입니다. 다양한 스타일과 크기의 로딩 인디케이터를 제공하며, 사용하기 간편합니다.

## NVActivityIndicatorView 설치하기

1. 먼저, CocoaPods을 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. `Podfile`에 다음과 같은 내용을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널에서 프로젝트의 디렉토리로 이동한 후, 다음 명령을 실행하여 CocoaPods을 업데이트합니다:

```shell
pod install
```

3. 프로젝트 파일을 열고 `import NVActivityIndicatorView`를 추가합니다.

## NVActivityIndicatorView 사용하기

1. 로딩 화면을 표시할 뷰 컨트롤러를 생성합니다. 예를 들어, `LoadingViewController`라는 클래스를 만들어 보겠습니다.

```swift
import UIKit
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    private var activityIndicatorView: NVActivityIndicatorView?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 설정
        let frame = CGRect(x: view.center.x - 25, y: view.center.y - 25, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballRotateChase, color: .white, padding: nil)
        
        if let activityIndicatorView = activityIndicatorView {
            // 로딩 인디케이터를 뷰에 추가
            view.addSubview(activityIndicatorView)
        }
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        // 로딩 인디케이터 애니메이션 시작
        activityIndicatorView?.startAnimating()
        
        // 비디오 스트리밍 로딩 작업 실행
        startVideoStreaming()
    }
    
    private func startVideoStreaming() {
        // 비디오 스트리밍 작업 수행 로직을 추가하세요.
        // 예시: 비디오 스트리밍 작업 완료 후, 로딩 화면을 종료하는 방법
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) { [weak self] in
            self?.activityIndicatorView?.stopAnimating()
            self?.dismiss(animated: true, completion: nil)
        }
    }
}
```

2. 앱에서 비디오 스트리밍으로 넘어가기 전에 `LoadingViewController`를 present합니다. 예를 들어, 버튼을 터치할 때 로딩 화면을 표시할 수 있습니다.

```swift
@IBAction func startVideoStreamingButtonTapped(_ sender: UIButton) {
    let loadingViewController = LoadingViewController()
    loadingViewController.modalPresentationStyle = .overFullScreen
    present(loadingViewController, animated: true, completion: nil)
}
```

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 비디오 스트리밍 로딩 화면을 구현할 수 있는 방법을 알아보았습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하므로, 앱에 맞는 스타일을 선택하여 사용할 수 있습니다.