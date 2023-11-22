---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 공유 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift를 사용하여 이미지 뷰어 앱을 만들고, 이미지를 공유하는 기능을 추가하는 방법을 알아보겠습니다.

## Step 1: 이미지 뷰어 앱 만들기
먼저, 이미지 뷰어 앱을 만들기 위해 Xcode에서 새로운 프로젝트를 생성합니다. 프로젝트를 생성한 후, `Main.storyboard` 파일을 열고 `UIImageView` 컴포넌트를 뷰 컨트롤러에 추가합니다.

이미지 뷰어 앱에 사용할 이미지를 프로젝트에 추가하고, 이 이미지를 `UIImageView`에 설정합니다. 이렇게 하면 이미지 뷰어 앱의 초기 화면이 완성됩니다.

## Step 2: 이미지 공유 기능 추가
이미지 뷰어 앱에 이미지 공유 기능을 추가하기 위해 `UIViewController` 클래스에 다음 코드를 추가합니다:

```swift
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어에 이미지 설정
        imageView.image = UIImage(named: "image.jpg")
        
        // 이미지를 탭하면 공유 액션 호출
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(shareImage))
        imageView.addGestureRecognizer(tapGesture)
        imageView.isUserInteractionEnabled = true
    }

    @objc func shareImage() {
        guard let image = imageView.image else { return }
        
        let activityViewController = UIActivityViewController(activityItems: [image], applicationActivities: nil)
        present(activityViewController, animated: true, completion: nil)
    }
}
```

위 코드는 `UIImageView` 탭 제스처를 추가하고, 제스처가 발생하면 `shareImage` 메소드를 호출합니다. `shareImage` 메소드는 `UIActivityViewController`를 사용하여 이미지를 공유합니다.

`shareImage` 메소드 내에서는 먼저 `guard` 구문을 사용하여 이미지가 nil이 아닌지 확인합니다. 그런 다음 `UIActivityViewController` 객체를 생성하고, `image`를 `activityItems` 배열에 추가하여 이미지를 공유합니다.

## Step 3: 앱 테스트 및 실행
이제 앱을 테스트하고 실행해보십시오. 앱을 실행하고 이미지를 탭하면 공유 액션 화면이 표시됩니다. 여기서 다른 앱을 선택하여 이미지를 공유할 수 있습니다.

## 결론
Swift를 사용하여 이미지 뷰어 앱에 이미지 공유 기능을 추가하는 방법을 알아보았습니다. 이 기능을 사용하여 사용자는 앱 내에서 이미지를 선택하고 다른 앱과 공유할 수 있습니다. 이러한 이미지 공유 기능은 사용자 경험을 향상시키며, 앱의 기능을 확장할 수 있습니다.

참조:
- [UIActivityViewController Documentation](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller)
- [UIImageView Documentation](https://developer.apple.com/documentation/uikit/uiimageview)
- [UITapGestureRecognizer Documentation](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)

이제 이미지 뷰어 앱을 만들고 이미지를 공유하는 기능을 추가할 준비가 되었습니다. 코드를 직접 작성하고 테스트해보고 원하는 방식으로 수정해보십시오. 흥미로운 앱을 만들기 위해 다양한 기능들을 추가해보세요!