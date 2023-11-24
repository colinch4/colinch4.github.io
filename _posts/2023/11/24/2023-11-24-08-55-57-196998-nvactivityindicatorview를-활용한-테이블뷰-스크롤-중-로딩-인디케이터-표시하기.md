---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 테이블뷰 스크롤 중 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

테이블뷰에서 많은 양의 데이터를 로드할 때, 사용자 경험을 향상시키기 위해 로딩 인디케이터를 표시하는 것은 중요합니다. 이 때 NVActivityIndicatorView 라이브러리를 사용하여 간단하게 로딩 인디케이터를 구현할 수 있습니다. 

## NVActivityIndicatorView란?

NVActivityIndicatorView는 간단하고 커스터마이즈 가능한 로딩 인디케이터를 제공하는 오픈 소스 라이브러리입니다. 다양한 스타일과 색상 옵션을 포함하고 있어 다양한 사용자 인터페이스에 적용할 수 있습니다.

## 라이브러리 설치

먼저, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. Podfile에 다음과 같은 라인을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 의존성을 설치합니다:

```bash
pod install
```

## 로딩 인디케이터 구현하기

먼저, NVActivityIndicatorView를 import하여 사용할 수 있도록 합니다:

```swift
import NVActivityIndicatorView
```

다음으로, 테이블뷰의 스크롤 이벤트를 감지하기 위해 UITableViewDelegate 프로토콜을 구현합니다:

```swift
class ViewController: UIViewController, UITableViewDelegate {
    // 테이블뷰 아웃렛 연결 및 데이터 소스 설정 생략
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.delegate = self
    }

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        let isScrolledToBottom = scrollView.contentOffset.y >= (scrollView.contentSize.height - scrollView.frame.size.height)
        
        if isScrolledToBottom {
            showLoadingIndicator()
            
            // 데이터 로드 로직 추가
        }
    }
    
    func showLoadingIndicator() {
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: tableView.bounds.size.width / 2 - 25, y: tableView.bounds.size.height / 2 - 25, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
        activityIndicatorView.startAnimating()
        
        tableView.addSubview(activityIndicatorView)
    }
}
```

위의 코드에서 `scrollViewDidScroll` 메소드는 테이블뷰가 스크롤되는 동안 호출되며, `isScrolledToBottom` 변수를 사용하여 테이블뷰가 화면 아래로 스크롤되었는지 여부를 확인합니다. 

화면이 아래로 스크롤되면 `showLoadingIndicator` 메소드를 호출하여 로딩 인디케이터를 생성하고 테이블뷰의 하단에 추가합니다. 이후 데이터 로드 로직을 추가하여 데이터를 가져올 수 있습니다.

## 커스터마이징

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공하여 로딩 인디케이터의 스타일과 색상을 변경할 수 있습니다. 자세한 내용은 [레퍼런스 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.

이제 NVActivityIndicatorView를 활용하여 테이블뷰 스크롤 중에 로딩 인디케이터를 표시할 수 있습니다. 사용자는 스크롤 동작을 지속적으로 확인할 수 있기 때문에 사용성을 향상시킬 수 있습니다.