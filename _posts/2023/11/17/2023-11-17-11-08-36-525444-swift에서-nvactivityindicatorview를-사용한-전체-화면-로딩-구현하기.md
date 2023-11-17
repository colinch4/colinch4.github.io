---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 전체 화면 로딩 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 개발 과정에서 사용자가 기다려야 할 때 화면 로딩 표시를 추가하는 것이 중요합니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 오픈 소스 라이브러리로, 프로그램의 실행 중에 로딩 인디케이터를 표시할 수 있습니다. 이번 포스트에서는 NVActivityIndicatorView를 사용하여 전체 화면 로딩을 구현하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. Swift Package Manager를 통해 간단히 설치할 수 있습니다.

1. Xcode에서 프로젝트를 열고, 프로젝트 네비게이터에서 프로젝트를 선택합니다.
2. "Swift Packages" 탭을 선택하고 "+" 버튼을 클릭합니다.
3. "https://github.com/ninjaprox/NVActivityIndicatorView.git"을 입력하여 라이브러리를 추가합니다.
4. "Branch" 필드에 브랜치를 입력하지 않고 "master"를 선택합니다.
5. "Finish"를 클릭하여 설치를 완료합니다.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음 단계를 따라주세요.

1. 로딩 인디케이터를 표시할 ViewController를 만듭니다.
2. ViewController 클래스에 다음 코드를 추가하여 NVActivityIndicatorView를 초기화합니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let frame = CGRect(x: 0, y: 0, width: 80, height: 80)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .circleStrokeSpin, color: .white, padding: 20)
        activityIndicatorView.center = view.center
        activityIndicatorView.startAnimating()
        view.addSubview(activityIndicatorView)
    }
}
```

3. 이제 로딩 인디케이터를 표시하려는 곳에서 `LoadingViewController`를 present합니다.

```swift
let loadingViewController = LoadingViewController()
present(loadingViewController, animated: true, completion: nil)
```

4. 로딩이 완료되면 `dismiss` 메서드를 호출하여 로딩 인디케이터를 제거합니다.

```swift
dismiss(animated: true, completion: nil)
```

## 마무리

이제 Swift에서 NVActivityIndicatorView를 사용하여 전체 화면 로딩을 구현하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하여 사용자에게 로딩 프로세스를 시각적으로 표시함으로써 앱의 사용성을 향상시킬 수 있습니다. 더 많은 NVActivityIndicatorView 옵션을 통해 로딩 인디케이터를 사용자 정의할 수 있으니 필요에 따라 검색하여 적용해 보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)