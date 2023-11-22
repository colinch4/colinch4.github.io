---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 파일 갯수 제한"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift로 작성된 SimpleImageViewer는 간단하고 사용하기 쉬운 이미지 뷰어 라이브러리입니다. 이 라이브러리를 사용하면 앱에서 이미지를 로드하고 원하는 대로 확대/축소 및 스와이프하여 이미지를 네비게이션할 수 있습니다.

이미지 뷰어를 사용하면 사용자가 많은 수의 이미지를 열고 메모리를 소비하게 할 수 있으므로, 때로는 이미지의 파일 갯수를 제한하는 것이 유용할 수 있습니다. 이 글에서는 Swift SimpleImageViewer에서 이미지 파일 갯수를 제한하는 방법을 알아보겠습니다.

### 1. 변수 추가
이미지 파일 갯수를 제한하기 위해 먼저 `SimpleImageViewController` 클래스에 변수를 추가해야 합니다. 아래와 같이 `maxImageCount` 변수를 추가합니다.

```swift
class SimpleImageViewController: UIViewController, UIScrollViewDelegate {
    // ...

    var maxImageCount: Int = 0
    
    // ...
}
```

### 2. 이미지 추가 시 제한 체크
이제 이미지를 추가할 때마다 `maxImageCount` 변수를 체크하여 제한을 적용할 수 있습니다. 아래와 같이 `addImage` 메서드를 수정합니다.

```swift
func addImage(image: UIImage) {
    // 이미지 파일 갯수 체크
    if maxImageCount > 0 && self.images.count >= maxImageCount {
        return
    }

    // 이미지 추가 로직
    // ...
}
```

### 3. 글로벌 변수 등록
마지막으로, 이미지 뷰어를 사용하는 코드에서 `maxImageCount` 변수에 원하는 값(제한할 이미지 파일 갯수)을 설정해야 합니다.

```swift
let imageViewer = SimpleImageViewController()
imageViewer.maxImageCount = 5 // 이미지 파일 갯수 제한을 5개로 설정
imageViewer.addImage(image: UIImage(named: "image1")!)
imageViewer.addImage(image: UIImage(named: "image2")!)
// 이미지 추가 코드 계속 작성
```

이제 SimpleImageViewer를 사용할 때 이미지 파일 갯수를 제한할 수 있습니다. 위의 예제에서는 `maxImageCount` 변수를 5로 설정하여 최대 5개의 이미지만 추가할 수 있도록 제한했습니다.

이 방법을 사용하여 SimpleImageViewer에서 이미지 파일 갯수를 제한할 수 있습니다. 이외에도 필요한 다른 기능을 추가하거나 수정할 수 있으며, SimpleImageViewer의 소스 코드를 확인하여 더 많은 기능을 사용할 수 있습니다.

### 참고 자료
- [SimpleImageViewer GitHub Repository](https://github.com/Krisiacik/SimpleImageViewer)