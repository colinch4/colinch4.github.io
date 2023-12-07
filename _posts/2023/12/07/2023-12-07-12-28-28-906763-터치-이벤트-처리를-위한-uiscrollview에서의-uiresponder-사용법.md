---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIScrollView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIScrollView는 iOS 앱에서 스크롤 가능한 컨텐츠 영역을 제공하는 뷰입니다. 이 뷰에서 사용자의 터치 이벤트를 처리하기 위해서는 UIResponder를 사용해야 합니다.

다음은 UIScrollView에서 UIResponder를 사용하여 터치 이벤트를 처리하는 방법을 알아보겠습니다.

## 1. UIScrollView 서브 클래스 만들기

UIScrollView에서 터치 이벤트를 처리하기 위해서는 UIScrollView를 상속받는 서브 클래스를 만들어야 합니다. 다음은 이를 위한 예제 코드입니다.

```swift
class TouchScrollView: UIScrollView {

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        
        // 터치 시작 시 동작할 코드 작성
        // 예시: 스크롤 뷰의 배경색을 변경
        self.backgroundColor = UIColor.red
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesEnded(touches, with: event)
        
        // 터치 종료 시 동작할 코드 작성
        // 예시: 스크롤 뷰의 배경색을 원래대로 변경
        self.backgroundColor = UIColor.white
    }
    
}
```

## 2. TouchScrollView 사용하기

위에서 만든 TouchScrollView를 사용하여 스크롤이 가능한 뷰를 만들어보겠습니다.

```swift
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // TouchScrollView 인스턴스 생성
        let scrollView = TouchScrollView(frame: self.view.bounds)
        scrollView.contentSize = CGSize(width: self.view.bounds.width, height: 1000)
        
        // 스크롤 뷰에 컨텐츠 추가
        let contentView = UIView(frame: CGRect(x: 0, y: 0, width: self.view.bounds.width, height: 1000))
        contentView.backgroundColor = UIColor.gray
        scrollView.addSubview(contentView)
        
        // 루트 뷰에 스크롤 뷰 추가
        self.view.addSubview(scrollView)
    }

}
```

위의 코드를 실행하면 TouchScrollView로 구현된 스크롤이 가능한 뷰가 생성됩니다. 이 뷰에서 터치를 시작하면 배경색이 빨간색으로 변경되고, 터치를 종료하면 배경색이 원래대로 흰색으로 변경될 것입니다.

이제 UIScrollView에서 UIResponder를 사용하여 터치 이벤트를 처리하는 방법에 대해 알아봤습니다. 이를 활용하여 다양한 기능을 구현할 수 있습니다.

참고 자료:
- [Apple Documentation](https://developer.apple.com/documentation/uikit/uiscrollview)
- [WWDC18: Advanced ScrollView Techniques](https://developer.apple.com/videos/play/wwdc2018/231/)