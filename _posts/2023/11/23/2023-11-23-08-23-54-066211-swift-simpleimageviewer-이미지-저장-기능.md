---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 저장 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어 앱을 개발 중이고, 사용자가 현재 보고 있는 이미지를 저장할 수 있는 기능을 추가하고 싶다면 어떻게 해야 할까요? 이 문서에서는 Swift를 사용하여 SimpleImageViewer 앱에 이미지 저장 기능을 구현하는 방법을 안내합니다.

## UIImagePickerController를 사용하여 이미지 선택하기

우선, 사용자가 저장할 이미지를 선택하기 위해 UIImagePickerController를 사용해야 합니다. UIImagePickerController는 iOS 기기의 카메라 롤로부터 이미지를 선택하거나 캡처할 수 있는 기능을 제공합니다.

```swift
import UIKit

class ImagePickerViewController: UIImagePickerController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    // 이미지 선택이 완료되었을 때 호출되는 메소드
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        
        if let pickedImage = info[.originalImage] as? UIImage {
            // 이미지 선택 완료 후의 처리 로직을 구현합니다.
        }
        
        picker.dismiss(animated: true, completion: nil)
    }
    
    // 이미지 선택이 취소되었을 때 호출되는 메소드
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        picker.dismiss(animated: true, completion: nil)
    }
    
}
```

## 이미지 저장 기능 구현하기

이제 이미지를 선택한 후에 선택한 이미지를 저장하는 기능을 구현해야 합니다. 이미지를 저장하기 위해서는 PHPhotoLibrary를 사용해야 합니다.

```swift
import Photos

func saveImageToPhotoLibrary(image: UIImage) {
    PHPhotoLibrary.requestAuthorization { (status) in
        if status == .authorized {
            PHPhotoLibrary.shared().performChanges({
                PHAssetChangeRequest.creationRequestForAsset(from: image)
            }, completionHandler: { (success, error) in
                if success {
                    // 이미지 저장 성공 시의 처리 로직을 구현합니다.
                } else {
                    // 이미지 저장 실패 시의 처리 로직을 구현합니다.
                }
            })
        }
    }
}
```

위의 `saveImageToPhotoLibrary` 함수는 사용자가 선택한 이미지를 앱의 사진 라이브러리에 저장하는 기능을 구현한 것입니다. 함수를 호출하면 사용자에게 권한 요청이 나타나고, 권한이 허용된 경우에만 이미지 저장이 진행됩니다.

## 이미지 저장 기능 연동하기

이제 앞서 구현한 `ImagePickerViewController`와 `saveImageToPhotoLibrary` 함수를 연동하여 사용자가 이미지를 선택하고 저장할 수 있는 기능을 구현해 보겠습니다.

```swift
import UIKit

class ViewController: UIViewController {
    
    let imagePicker = ImagePickerViewController()
    
    @IBAction func selectImage(_ sender: Any) {
        imagePicker.sourceType = .photoLibrary
        imagePicker.delegate = imagePicker
        present(imagePicker, animated: true, completion: nil)
    }
    
}

extension ImagePickerViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // 이미지 선택 완료 시의 처리 로직을 구현합니다.
        self.delegate = self
    }
    
    override func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        super.imagePickerController(picker, didFinishPickingMediaWithInfo: info)
        
        if let pickedImage = info[.originalImage] as? UIImage {
            saveImageToPhotoLibrary(image: pickedImage)
        }
    }
    
}
```

위의 코드에서 `ViewController`는 사용자가 이미지 선택 버튼을 누를 때 `selectImage` 함수가 호출되어 `ImagePickerViewController`를 표시합니다. 선택한 이미지는 `saveImageToPhotoLibrary` 함수를 통해 저장되며, 저장 성공 시에는 추가적인 처리를 할 수 있습니다.

## 결론

위의 예제를 참고하여 SimpleImageViewer 앱에 이미지 저장 기능을 구현해보세요. 사용자가 이미지 선택 후 저장할 수 있도록 구현하면 더욱 유용한 앱을 만들 수 있을 것입니다.