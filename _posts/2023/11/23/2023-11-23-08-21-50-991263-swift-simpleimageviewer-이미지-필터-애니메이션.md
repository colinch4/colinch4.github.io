---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 필터 애니메이션"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift를 사용하여 간단한 이미지 뷰어 앱을 만들고, 이미지에 필터를 적용하고, 애니메이션 효과를 추가하는 방법에 대해 알아보겠습니다.

## 프로젝트 설정

먼저 Xcode에서 새로운 프로젝트를 생성합니다. "Single View App" 템플릿을 선택하고 프로젝트에 "SimpleImageViewer"라는 이름을 지정합니다.

## 이미지 뷰어 UI 구성

뷰 컨트롤러에 UIImageView를 추가하고, 이미지 뷰어를 만들기 위해 IBOutlet을 설정합니다. 또한 필터 및 애니메이션에 대한 버튼도 추가합니다.

```swift
import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화 코드
    }
}
```

## 이미지 선택 기능 추가

이미지 선택 기능을 구현하기 위해 UIImagePickerController를 사용합니다. 사용자가 사진을 선택하면 선택한 이미지를 이미지 뷰어에 설정하는 코드를 추가합니다.

```swift
import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate & UINavigationControllerDelegate {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화 코드
        
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        present(imagePickerController, animated: true, completion: nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        if let image = info[.originalImage] as? UIImage {
            imageView.image = image
        }
        
        dismiss(animated: true, completion: nil)
    }
}
```

## 이미지 필터 적용

이미지에 필터를 적용하기 위해 CIFilter를 사용합니다. 사용자가 버튼을 선택하면 해당 필터를 이미지에 적용하고, 이미지 뷰어에 업데이트하는 코드를 추가합니다.

```swift
import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate & UINavigationControllerDelegate {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화 코드
        
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        present(imagePickerController, animated: true, completion: nil)
    }
    
    func applyFilter(filterName: String) {
        guard let image = imageView.image else {
            return
        }
        
        let context = CIContext()
        let ciImage = CIImage(image: image)
        
        if let filter = CIFilter(name: filterName) {
            filter.setValue(ciImage, forKey: kCIInputImageKey)
            
            if let outputImage = filter.outputImage {
                if let cgImage = context.createCGImage(outputImage, from: outputImage.extent) {
                    imageView.image = UIImage(cgImage: cgImage)
                }
            }
        }
    }
    
    @IBAction func applySepiaFilter(_ sender: UIButton) {
        applyFilter(filterName: "CISepiaTone")
    }
    
    @IBAction func applyVintageFilter(_ sender: UIButton) {
        applyFilter(filterName: "CIPhotoEffectInstant")
    }
}
```

## 애니메이션 효과 추가

애니메이션 효과를 추가하기 위해 UIView.transition() 메소드를 사용합니다. 버튼을 선택하면 이미지 뷰어의 이미지가 애니메이션과 함께 변경되는 코드를 추가합니다.

```swift
import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate & UINavigationControllerDelegate {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화 코드
        
        let imagePickerController = UIImagePickerController()
        imagePickerController.delegate = self
        present(imagePickerController, animated: true, completion: nil)
    }
    
    func applyFilter(filterName: String) {
        // 필터 적용 코드
    }
    
    func applyAnimation() {
        UIView.transition(with: imageView, duration: 0.5, options: .transitionFlipFromLeft, animations: {
            // 애니메이션 동작 설정
        }, completion: nil)
    }
    
    @IBAction func applySepiaFilter(_ sender: UIButton) {
        // 필터 적용 코드
        applyAnimation()
    }
    
    @IBAction func applyVintageFilter(_ sender: UIButton) {
        // 필터 적용 코드
        applyAnimation()
    }
}
```

이제 위의 코드를 참고하여 간단한 이미지 뷰어 앱을 만들고, 필터 적용 및 애니메이션 효과를 적용해 보세요. 자세한 내용은 Swift 문서와 Core Image 프레임워크를 참고하면 도움이 됩니다.

- [Swift 문서](https://swift.org/documentation/)
- [Core Image 프레임워크](https://developer.apple.com/documentation/coreimage)