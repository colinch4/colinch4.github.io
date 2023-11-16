---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 시작 시에 사용자 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 인기있는 애니메이션 라이브러리 중 하나입니다. 이 라이브러리는 다양한 유형의 로딩 애니메이션을 제공하며, 네트워크 요청이나 데이터 처리 등 오래 걸릴 수 있는 작업이 진행될 때 유용하게 사용됩니다.

사용자가 앱 인터페이스와 상호작용하는 동안 애니메이션이 발생한다면, 이는 사용자 경험을 개선하기 위해 인터랙션을 제한하는 좋은 방법입니다. 

다음은 Swift에서 NVActivityIndicatorView 애니메이션을 시작할 때 사용자 인터랙션을 제한하는 방법에 대한 코드 예시입니다.

```swift
// NVActivityIndicatorView 라이브러리를 사용하기 위해 import 합니다.
import NVActivityIndicatorView

// 화면에서 사용자 인터랙션을 제어하는 클래스를 정의합니다.
class ViewController: UIViewController {
    // NVActivityIndicatorView 인스턴스를 선언합니다.
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView의 사이즈와 색상, 스타일 등을 설정합니다.
        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame)
        activityIndicatorView.color = .red
        activityIndicatorView.type = .circleStrokeSpin
        activityIndicatorView.padding = 10

        // 애니메이션 시작 시에 사용자 인터랙션을 제한합니다.
        startLoading()
    }

    func startLoading() {
        // NVActivityIndicatorView를 현재 화면에 추가합니다.
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)

        // 사용자 인터랙션을 제한하기 위해 view.userInteractionEnabled를 false로 설정합니다.
        view.isUserInteractionEnabled = false

        // NVActivityIndicatorView 애니메이션을 시작합니다.
        activityIndicatorView.startAnimating()

        // 작업이 완료되면 애니메이션을 중지하고 사용자 인터랙션을 다시 활성화합니다.
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.activityIndicatorView.stopAnimating()
            self.view.isUserInteractionEnabled = true
        }
    }
}
```

위의 코드는 NVActivityIndicatorView를 사용하여 애니메이션을 시작할 때 사용자 인터랙션을 제한하는 방법을 보여줍니다. 애니메이션이 시작되면 `view.isUserInteractionEnabled` 속성을 false로 설정하여 사용자 인터랙션을 비활성화하고, 애니메이션이 완료되면 다시 `view.isUserInteractionEnabled`를 true로 설정하여 사용자 인터랙션을 활성화합니다.

이 코드는 NVActivityIndicatorView의 사이즈, 색상, 스타일 등을 설정하는 예제입니다. 이와 같이 필요에 따라 다양한 속성을 사용하여 애니메이션을 원하는대로 커스터마이징할 수 있습니다.

이외에도 NVActivityIndicatorView에 대한 더 자세한 정보를 알고 싶다면, [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해주세요.