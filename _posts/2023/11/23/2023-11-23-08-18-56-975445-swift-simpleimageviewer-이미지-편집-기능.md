---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 편집 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 편집은 모바일 앱 개발에서 중요한 부분 중 하나입니다. 사용자는 이미지를 자르고 회전시키며, 색상과 효과를 변경하고, 그림을 그릴 수 있는 등 다양한 편집 기능을 원합니다. 이번에는 Swift를 사용하여 앱에 간단한 이미지 편집 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. 이미지 불러오기

첫 번째로, 이미지를 앱에 불러와야 합니다. Swift에서는 `UIImagePickerController`를 사용하여 사용자의 사진 앨범에서 사진을 선택할 수 있습니다. 다음은 이미지 선택을 위한 코드입니다.

```swift
if UIImagePickerController.isSourceTypeAvailable(.photoLibrary) {
   let imagePicker = UIImagePickerController()
   imagePicker.delegate = self
   imagePicker.sourceType = .photoLibrary
   self.present(imagePicker, animated: true, completion: nil)
}
```

위 코드는 앱에서 사진 앨범을 열고 이미지를 선택할 수 있는 `UIImagePickerController`를 생성합니다. `UIImagePickerControllerDelegate`를 구현하여 사용자가 이미지를 선택한 후의 동작을 처리할 수 있습니다.

## 2. 이미지 편집 기능 추가하기

이제 이미지를 불러왔으니 편집 기능을 추가해보겠습니다. `UIImageView`를 사용하여 이미지를 표시하고, 간단한 편집 기능을 구현해볼 것입니다. 다음은 이미지를 표시하는 코드입니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.image = selectedImage
self.view.addSubview(imageView)
```

위 코드는 `UIImageView`를 생성하고 선택한 이미지를 할당하여 화면에 표시합니다.

편집 기능을 추가하기 위해 `UIGestureRecognizer`를 사용하여 이미지를 탭하고 드래그하여 이동할 수 있도록 할 수 있습니다. 또한 이미지를 회전시키고 확대/축소할 수 있는 기능도 구현할 수 있습니다.

```swift
func addPanGesture() {
   let panGesture = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
   imageView.addGestureRecognizer(panGesture)
}

@objc func handlePan(_ gesture: UIPanGestureRecognizer) {
   let translation = gesture.translation(in: view)
   imageView.center = CGPoint(x: imageView.center.x + translation.x, y: imageView.center.y + translation.y)
   gesture.setTranslation(CGPoint.zero, in: view)
}
```

위 코드는 `UIPanGestureRecognizer`를 추가하고, 사용자의 패닝 동작에 따라 이미지 뷰를 이동시킵니다. 마찬가지로, 이미지 회전과 확대/축소에 대한 기능을 추가할 수 있습니다.

## 3. 이미지 저장하기

마지막으로, 편집된 이미지를 저장하는 방법에 대해 알아보겠습니다. 수정된 이미지를 저장하기 위해 `UIImageWriteToSavedPhotosAlbum` 함수를 사용할 수 있습니다.

```swift
UIImageWriteToSavedPhotosAlbum(imageView.image!, self, #selector(image(_:didFinishSavingWithError:contextInfo:)), nil)
```

위 코드는 `imageView`에 표시된 이미지를 사진 앨범에 저장합니다. 이때, `image(_:didFinishSavingWithError:contextInfo:)` 메서드를 사용하여 저장이 완료된 후에 원하는 동작을 수행할 수 있습니다.

## 결론

이제 Swift를 사용하여 앱에 간단한 이미지 편집 기능을 구현하는 방법에 대해 알아보았습니다. 이미지 불러오기, 편집 기능 추가, 이미지 저장하기 등의 기능을 구현하는 방법을 소개했습니다. 이를 바탕으로 개발자들은 앱에 다양한 이미지 편집 기능을 추가할 수 있을 것입니다.
```

참고 자료:
- [UIImagePickerController - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagepickercontroller)
- [UIImageView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)
- [UIGestureRecognizer - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigesturerecognizer)
- [UIImageWriteToSavedPhotosAlbum - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimagewritetosavedphotosalbum)