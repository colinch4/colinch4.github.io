---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 카레시피 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift 프로젝트에 NVActivityIndicatorView를 사용하여 로딩 효과를 추가하는 방법에 대해 알아보겠습니다. 

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 효과 라이브러리로, 다양한 스타일의 로딩 인디케이터를 제공합니다. 이 라이브러리는 설치 및 사용이 간단하고, 많은 커스터마이제이션 옵션을 제공하여 프로젝트에 따라 다양한 로딩 효과를 적용할 수 있습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 설치 방법은 다음과 같습니다:

1. Cocoapods을 사용하는 경우, `Podfile`에 다음과 같은 라인을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

2. CocoaPods를 설치하기 전에, 터미널에서 프로젝트 디렉토리로 이동한 후 `pod install` 명령을 실행합니다.

3. CocoaPods가 종속성을 다운로드 및 설치한 후, 프로젝트에 생성된 `.xcworkspace` 파일을 엽니다.

4. 이제 NVActivityIndicatorView를 사용할 준비가 되었습니다.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하려면 다음 단계를 따르세요:

1. Storyboard 또는 XIB 파일에서 로딩 효과가 표시될 UIView를 추가합니다.

2. 해당 UIView의 클래스를 `NVActivityIndicatorView`로 설정합니다.

3. 필요한 경우, 너비 및 높이를 조정하여 로딩 효과의 크기를 변경할 수 있습니다.

4. UIView의 `color` 속성을 설정하여 로딩 효과의 색상을 변경할 수 있습니다.

5. UIView의 `type` 속성을 설정하여 로딩 효과의 스타일을 변경할 수 있습니다. NVActivityIndicatorType 열거형을 사용하여 다양한 스타일 중 하나를 선택할 수 있습니다.

6. 코드에서 해당 UIView를 참조하여 로딩 효과를 관리합니다. 예를 들어, 로딩 효과를 시작할 때에는 `startAnimating()` 메서드를 호출하고, 종료할 때에는 `stopAnimating()` 메서드를 호출합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    @IBOutlet weak var loadingView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 효과의 스타일 설정
        loadingView.type = .ballRotateChase
        // 로딩 효과의 색상 설정
        loadingView.color = UIColor.red
    }

    @IBAction func startLoadingButtonTapped(_ sender: UIButton) {
        // 로딩 효과 시작
        loadingView.startAnimating()
    }

    @IBAction func stopLoadingButtonTapped(_ sender: UIButton) {
        // 로딩 효과 종료
        loadingView.stopAnimating()
    }

}
```

## 3. 추가 커스터마이제이션

NVActivityIndicatorView는 많은 커스터마이제이션 옵션을 제공합니다. API 문서를 참조하여 로딩 효과에 원하는 스타일, 색상, 크기 등을 적용할 수 있습니다. 옵션을 변경하기 위해 해당 속성들을 조정하면 되며, 앞에서 소개한 `type` 및 `color` 속성 외에도 다양한 속성들이 있으니 참고하시기 바랍니다.

## 4. 마치며

이제 NVActivityIndicatorView를 사용하여 Swift 프로젝트에 로딩 효과를 추가하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 설치 및 사용이 쉽고 커스터마이제이션 옵션도 다양하기 때문에, 다양한 프로젝트에 유용하게 사용될 수 있습니다. 참고 자료와 공식 문서를 활용하여 원하는 스타일의 로딩 효과를 적용해보세요.

## 참고 자료
- [NVActivityIndicatorView 공식 GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView API 문서](https://docs.ninjaprox.com/nvactivityindicatorview)