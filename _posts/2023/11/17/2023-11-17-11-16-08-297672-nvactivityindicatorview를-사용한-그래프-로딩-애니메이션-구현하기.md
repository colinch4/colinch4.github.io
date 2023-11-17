---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 그래프 로딩 애니메이션 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개
이번 블로그 포스트에서는 Swift 프로그래밍 언어를 사용하여 NVActivityIndicatorView를 이용해 그래프 로딩 애니메이션을 구현하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 시각적으로 나타내주는 라이브러리로 널리 사용되고 있습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 로딩 인디케이터의 다양한 스타일을 제공하는 라이브러리입니다. 앱 화면에서 데이터를 가져오는 동안 로딩 상태를 사용자에게 시각적으로 표시하는 데 사용됩니다. 이 라이브러리는 다양한 크기와 색상의 로딩 인디케이터를 제공하므로 사용자의 디자인 요구에 맞게 적용할 수 있습니다.

## 구현 단계

### 1. NVActivityIndicatorView 설치하기
먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Podfile에 다음과 같은 코드를 추가하고 터미널에서 `pod install` 명령을 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

### 2. NVActivityIndicatorView 추가하기
NVActivityIndicatorView를 사용할 뷰 컨트롤러에 해당하는 파일을 열고, 다음과 같은 코드를 추가하세요.

```swift
import NVActivityIndicatorView

class GraphViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView?

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleMultiple, color: .gray, padding: nil)

        // 로딩 인디케이터 위치 설정
        activityIndicator?.center = view.center

        // 뷰에 로딩 인디케이터 추가
        if let indicator = activityIndicator {
            view.addSubview(indicator)
        }

        // 로딩 인디케이터 실행
        activityIndicator?.startAnimating()
    }
}
```

### 3. 로딩 애니메이션 실행하기
로딩 애니메이션을 실행하기 위해, 해당하는 뷰 컨트롤러에서 필요한 데이터를 가져오는 비동기 작업을 수행하는 함수를 만들어야 합니다. 이 예제에서는 간단히 `getData()` 함수라고 가정하겠습니다.

```swift
func getData() {
    // 데이터 가져오는 비동기 작업

    // 작업 완료 후 로딩 인디케이터 정지
    self.activityIndicator?.stopAnimating()
}
```

## 결론
이제 NVActivityIndicatorView를 이용해 그래프 로딩 애니메이션을 쉽게 구현할 수 있게 되었습니다. 이 라이브러리는 다양한 스타일과 설정 옵션을 제공하므로, 디자인 요구에 맞게 로딩 인디케이터를 조정할 수 있습니다. 참고로 해당 라이브러리의 모든 스타일과 사용법은 공식 문서를 참조하시기 바랍니다.

## 참고 자료
- [NVActivityIndicatorView 공식 GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView/wiki)
- [Cocoapods 공식 웹사이트](https://cocoapods.org/)