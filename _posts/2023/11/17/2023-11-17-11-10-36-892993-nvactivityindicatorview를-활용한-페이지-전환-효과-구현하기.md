---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 페이지 전환 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
이번에는 NVActivityIndicatorView를 활용하여 iOS 앱에서 페이지 전환 시 부드러운 로딩 효과를 구현하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 앱 내에서 로딩 인디케이터를 사용할 때 유용한 오픈 소스 라이브러리입니다.

## NVActivityIndicatorView 설치하기
먼저, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Cocoapods를 사용하여 간단하게 설치할 수 있습니다. `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 pod을 설치합니다.

```bash
$ pod install
```

이제 `import NVActivityIndicatorView`를 사용하여 프로젝트에서 NVActivityIndicatorView를 사용할 준비가 되었습니다.

## NVActivityIndicatorView 사용하기
1. 먼저, Storyboard에서 페이지 전환 시 로딩 인디케이터를 표시할 뷰를 추가합니다. 이 뷰에 NVActivityIndicatorView를 추가할 것입니다.
2. 추가한 뷰에 Custom View를 추가합니다.
3. Custom Class를 `NVActivityIndicatorView`로 설정합니다.
4. 필요에 따라 색상, 크기, 애니메이션 속도 등을 설정할 수 있습니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    @IBOutlet weak var loadingView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let activityIndicatorView = NVActivityIndicatorView(frame: loadingView.bounds, type: .ballClipRotateMultiple, color: .white, padding: nil)
        loadingView.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()
    }
}
```

위 코드에서는 `NVActivityIndicatorView`를 `loadingView`에 추가하고 애니메이션을 시작하도록 설정하였습니다. 애니메이션 타입, 색상, 패딩 등을 원하는 대로 변경할 수 있습니다.

## 페이지 전환 시 로딩 인디케이터 사용하기
이제 실제로 페이지 전환 시에 로딩 인디케이터를 사용해보겠습니다.

```swift
import NVActivityIndicatorView

class MainViewController: UIViewController {
    @IBAction func goToNextPage(_ sender: Any) {
        let loadingVC = storyboard?.instantiateViewController(withIdentifier: "LoadingViewController") as! LoadingViewController
        loadingVC.modalPresentationStyle = .overFullScreen
        
        // 로딩 인디케이터가 숨겨진 상태로 전환
        self.present(loadingVC, animated: false) {
            // 페이지 전환에 대한 작업 수행
            
            // 페이지 전환 작업이 완료되면 로딩 인디케이터를 숨기고 이전 뷰로 돌아감
            loadingVC.dismiss(animated: false, completion: nil)
        }
    }
}
```

위 코드에서는 `MainViewController`에서 `goToNextPage` 버튼을 눌렀을 때 `LoadingViewController`를 모달 형태로 표시하면서 동시에 페이지 전환 작업을 수행합니다. 전환 작업이 완료되면 로딩 인디케이터를 숨기고 이전 뷰로 돌아갑니다.

## 결론
이제 NVActivityIndicatorView를 활용하여 iOS 앱에서 페이지 전환 시 부드러운 로딩 효과를 구현하는 방법을 알아보았습니다. NVActivityIndicatorView의 다양한 옵션을 활용하여 원하는 스타일의 로딩 인디케이터를 만들 수 있으며, 애니메이션 시작 및 종료 시점을 적절히 조절하여 사용자 경험을 향상시킬 수 있습니다.

자세한 내용은 [NVActivityIndicatorView 공식 GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.