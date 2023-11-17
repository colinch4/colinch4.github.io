---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 스크롤뷰 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

스크롤뷰에 로딩 효과를 적용하려면 NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. 이 라이브러리는 다양한 스타일의 로딩 효과를 제공하여 앱에 동적이고 시각적으로 매력적인 효과를 추가할 수 있습니다. 이제 Swift에서 NVActivityIndicatorView를 사용하여 스크롤뷰에 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 라이브러리 설치하기

1. [CocoaPods](https://cocoapods.org/)를 사용하여 프로젝트에 NVActivityIndicatorView를 추가합니다. 
2. 프로젝트의 Podfile에 다음의 코드를 추가합니다:

```swift
pod 'NVActivityIndicatorView'
```
3. 터미널에서 프로젝트가 있는 위치로 이동하여 다음의 명령어를 실행합니다:

```swift
pod install
```

## NVActivityIndicatorView를 스크롤뷰에 추가하기

1. 스크롤뷰를 생성하고 화면에 추가합니다:

```swift
let scrollView = UIScrollView(frame: CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height))
view.addSubview(scrollView)
```

2. NVActivityIndicatorView를 생성하고 스크롤뷰에 추가합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
scrollView.addSubview(activityIndicatorView)
```

3. 로딩 효과를 시작하고 멈추는 메서드를 구현합니다:

```swift
func startLoading() {
    activityIndicatorView.startAnimating()
    scrollView.isScrollEnabled = false
}

func stopLoading() {
    activityIndicatorView.stopAnimating()
    scrollView.isScrollEnabled = true
}
```

## 스크롤뷰 이벤트와 연동하기

스크롤뷰에 로딩 효과를 추가했으니 이제 스크롤뷰의 이벤트와 로딩 효과를 연동해야 합니다. 이 예시에서는 스크롤뷰가 스크롤링 중일 때, 로딩 효과를 활성화하고 스크롤링이 멈출 때 로딩 효과를 비활성화하는 방법을 소개하겠습니다.

```swift
extension YourViewController: UIScrollViewDelegate {
    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        startLoading()
    }
    
    func scrollViewDidEndDecelerating(_ scrollView: UIScrollView) {
        stopLoading()
    }
}
```

## 결론

이제 NVActivityIndicatorView를 사용하여 Swift에서 스크롤뷰에 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 앱에 동적이고 시각적으로 매력적인 효과를 추가하는 데 유용한 라이브러리입니다. 이를 활용하여 앱 사용자가 로딩 중임을 시각적으로 알 수 있도록 해보세요.