---
layout: post
title: "[swift] Swift SimpleImageViewer 설치 가이드"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 iOS 애플리케이션에서 이미지 뷰어 기능을 구현하는 라이브러리입니다.

이 가이드에서는 Swift 패키지 매니저인 CocoaPods를 이용하여 SimpleImageViewer를 설치하는 방법을 안내합니다.

## CocoaPods 설치하기

CocoaPods를 사용하기 위해서는 먼저 CocoaPods를 설치해야 합니다. 터미널에서 다음 명령어를 실행하여 설치할 수 있습니다:

```shell
$ sudo gem install cocoapods
```

## CocoaPods 초기화

1. 프로젝트의 루트 폴더로 이동하고 터미널에서 다음 명령어를 실행하여 Podfile을 생성합니다:

   ```shell
   $ pod init
   ```

2. 생성된 Podfile을 텍스트 편집기로 열고 다음과 같이 수정합니다:

   ```ruby
   platform :ios, '10.0'

   target 'YourProjectName' do
     use_frameworks!

     # Add the SimpleImageViewer pod
     pod 'SimpleImageViewer', '~> 1.0.0'
   end
   ```

3. 터미널에서 다음 명령어를 실행하여 Podfile에 명시된 라이브러리를 설치합니다:

   ```shell
   $ pod install
   ```

4. 설치가 완료되면 프로젝트 폴더 내에 생성된 `.xcworkspace` 파일을 열어서 작업을 계속합니다.

## SimpleImageViewer 사용하기

SimpleImageViewer를 사용하기 위해서는 다음과 같은 단계를 따라야 합니다:

1. 이미지 뷰어를 사용할 ViewController에서 다음 코드를 추가합니다:

   ```swift
   import SimpleImageViewer
   
   class ViewController: UIViewController {
       
       // 이미지를 보여줄 이미지 뷰
       @IBOutlet weak var imageView: UIImageView!
       
       override func viewDidLoad() {
           super.viewDidLoad()
           
           // 이미지 뷰어 인스턴스 생성
           let imageViewer = ImageViewer()
           
           // 이미지 뷰어 델리게이트 설정
           imageViewer.delegate = self
           
           // 이전 화면에서 전달받은 이미지 설정
           let image = UIImage(named: "example_image")
           imageView.image = image
           
           // 이미지 뷰를 탭하면 이미지 뷰어 표시
           imageView.isUserInteractionEnabled = true
           imageView.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(showImageViewer)))
       }
       
       @objc private func showImageViewer() {
           let image = imageView.image
           let imageProvider = SimpleImageProvider(image: image)
           ImageViewer.present(imageProvider: imageProvider, from: self)
       }
   }

   // SimpleImageViewerDelegate 메서드 구현
   extension ViewController: SimpleImageViewerDelegate {
       func didDismissImageViewer() {
           // 이미지 뷰어가 사라질 때 호출되는 함수
       }
   }
   ```

2. 이미지를 보여줄 ViewController에서 위의 코드를 구현합니다. `imageView`는 이미지 뷰어를 표시할 이미지 뷰입니다.

3. 이제 빌드하고 실행한 후, `imageView`를 탭하면 SimpleImageViewer가 나타나고 이미지를 확대/축소하거나 스와이프로 다른 이미지로 전환할 수 있게 됩니다.

## 결론

위의 가이드를 따라하면 Swift 애플리케이션에서 SimpleImageViewer를 손쉽게 설치하고 사용할 수 있습니다. SimpleImageViewer를 통해 사용자들에게 편리한 이미지 뷰어 기능을 제공할 수 있습니다.

더 많은 정보와 옵션에 대해서는 [SimpleImageViewer GitHub 페이지](https://github.com/Krisiacik/ImageViewer)를 참고하세요.