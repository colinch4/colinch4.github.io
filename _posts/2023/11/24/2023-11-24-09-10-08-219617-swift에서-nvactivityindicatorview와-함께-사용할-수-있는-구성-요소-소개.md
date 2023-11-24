---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 구성 요소 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

[NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)는 Swift로 작성된 원형 로딩 인디케이터 라이브러리입니다. 이 라이브러리를 사용하면 앱에서 간편하게 로딩 인디케이터를 추가할 수 있습니다. 이번 포스트에서는 NVActivityIndicatorView와 함께 사용할 수 있는 몇 가지 구성 요소를 소개하겠습니다.

## 1. 로딩 버튼

로딩 버튼은 사용자에게 액션을 취할 때 로딩 인디케이터를 표시하여 작업이 진행 중임을 알려주는 요소입니다. 다음과 같이 NVActivityIndicatorView와 UIButton을 결합하여 로딩 버튼을 만들 수 있습니다:

```swift
import NVActivityIndicatorView

class LoadingButton: UIButton {
    private var activityIndicatorView: NVActivityIndicatorView!

    override func awakeFromNib() {
        super.awakeFromNib()
        
        // 버튼에 NVActivityIndicatorView 추가
        activityIndicatorView = NVActivityIndicatorView(
            frame: CGRect(x: 0, y: 0, width: bounds.height, height: bounds.height),
            type: .circleStrokeSpin,
            color: .white,
            padding: 0
        )
        
        addSubview(activityIndicatorView)
    }
    
    func showLoadingIndicator() {
        isEnabled = false // 버튼 비활성화
        setTitle("", for: .normal) // 버튼 타이틀 제거
        
        activityIndicatorView.startAnimating() // 로딩 인디케이터 시작
    }
    
    func hideLoadingIndicator() {
        isEnabled = true // 버튼 활성화
        setTitle("확인", for: .normal) // 버튼 타이틀 설정
        
        activityIndicatorView.stopAnimating() // 로딩 인디케이터 정지
    }
}
```

위 코드에서는 LoadingButton 클래스가 UIButton을 상속하고, awakeFromNib() 메서드에서 NVActivityIndicatorView를 버튼에 추가합니다. showLoadingIndicator() 메서드를 호출하면 버튼이 비활성화되고 로딩 인디케이터가 시작됩니다. hideLoadingIndicator() 메서드는 로딩 인디케이터를 정지하고 버튼을 다시 활성화합니다.

## 2. 커스텀 로딩 뷰

NVActivityIndicatorView를 사용하여 커스텀 로딩 뷰를 만들 수도 있습니다. 다음은 UIView를 상속한 CustomLoadingView 예시입니다:

```swift
import NVActivityIndicatorView

class CustomLoadingView: UIView {
    private var activityIndicatorView: NVActivityIndicatorView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        // 로딩 인디케이터 설정
        activityIndicatorView = NVActivityIndicatorView(
            frame: CGRect(x: 0, y: 0, width: 40, height: 40),
            type: .circleStrokeSpin,
            color: .white,
            padding: 0
        )
        
        addSubview(activityIndicatorView)
        activityIndicatorView.center = center
    }
    
    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
    
    func startLoading() {
        activityIndicatorView.startAnimating() // 로딩 인디케이터 시작
    }
    
    func stopLoading() {
        activityIndicatorView.stopAnimating() // 로딩 인디케이터 정지
    }
}
```

CustomLoadingView 클래스는 UIView를 상속하고, 생성자에서 NVActivityIndicatorView를 초기화합니다. startLoading() 메서드를 호출하면 로딩 인디케이터가 시작되고, stopLoading() 메서드로 인디케이터를 정지할 수 있습니다.

이는 NVActivityIndicatorView를 사용하여 Swift 앱에서 로딩 인디케이터를 커스터마이징하는 두 가지 방법을 보여줍니다. NVActivityIndicatorView는 사용하기 쉽고 다양한 스타일과 색상으로 로딩 인디케이터를 제공합니다. 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.