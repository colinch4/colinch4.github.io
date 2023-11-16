---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 외관 변경하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 다양한 형식의 로딩 애니메이션을 쉽게 구현할 수 있습니다. 이번 포스트에서는 NVActivityIndicatorView를 사용하여 애니메이션의 외관을 변경하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 이용하여 라이브러리를 설치해야 합니다. 아래의 명령어를 사용하여 Podfile에 NVActivityIndicatorView를 추가하고 설치합니다.

```bash
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해서는 해당 뷰를 먼저 생성해야 합니다. 아래의 코드는 NVActivityIndicatorView를 생성하고 화면의 중앙에 배치하는 예시입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 60, height: 60))
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 뷰 컨트롤러에 NVActivityIndicatorView를 추가합니다.
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
        
        // 애니메이션을 시작합니다.
        activityIndicatorView.startAnimating()
    }
}
```

## 3. 애니메이션 외관 변경하기

NVActivityIndicatorView는 다양한 스타일의 애니메이션을 제공합니다. 기본적으로는 각 스타일에 대한 기본 색상이 정의되어 있지만, 사용자가 직접 색상을 변경할 수도 있습니다. 변경 가능한 속성은 다음과 같습니다.

- `color`: 애니메이션의 색상을 변경합니다.
- `padding`: 애니메이션의 패딩 값을 변경합니다.
- `type`: 애니메이션의 스타일을 변경합니다.

아래의 코드는 NVActivityIndicatorView의 외관을 변경하는 예시입니다.

```swift
// 애니메이션의 컬러 설정
activityIndicatorView.color = UIColor.red

// 애니메이션의 패딩 값 설정
activityInd