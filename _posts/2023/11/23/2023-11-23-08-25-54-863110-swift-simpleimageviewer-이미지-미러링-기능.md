---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 미러링 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 SwiftUI를 사용하여 이미지 파일을 화면에 표시하는 간단한 앱입니다. 이 앱에는 이미지를 미러링하는 기능을 추가하고자 합니다. 미러링 기능은 이미지를 좌우로 반전시켜 원본 이미지의 거울 이미지를 생성하는 것입니다. 

## 1. UIImageView 확장

이미지뷰어 앱에서 UIImageView의 확장을 통해 미러링 기능을 구현해보겠습니다. 먼저, UIImageView의 확장을 정의하고 `mirrorImage`라는 메서드를 추가합니다.

```swift
extension UIImageView {
    func mirrorImage() {
        guard let image = self.image else { return }
        
        let mirroredImage = UIImage(cgImage: image.cgImage!, scale: image.scale, orientation: .upMirrored)
        self.image = mirroredImage
    }
}
```

위의 코드에서 `mirrorImage` 메서드는 현재 UIImageView에 표시된 이미지를 가져와 좌우로 반전한 이미지를 생성합니다. 생성된 이미지는 UIImageView에 다시 설정됩니다.

## 2. 이미지 미러링 적용

이제 뷰어 앱에서 이미지를 미러링하는 기능을 사용해보겠습니다. 먼저, SwiftUI에서 이미지를 표시할 수 있는 `Image` 뷰를 사용합니다.

```swift
struct ImageViewer: View {
    @State private var isMirrored = false
    
    var body: some View {
        VStack {
            Image("sample_image")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 200, height: 200)
                .rotationEffect(.degrees(isMirrored ? 180 : 0))
            
            Button(action: {
                isMirrored.toggle()
            }, label: {
                Text(isMirrored ? "Unmirror" : "Mirror")
            })
        }
    }
}
```

위의 코드에서 `isMirrored`라는 상태 변수를 추가하여 이미지가 미러링되었는지 여부를 추적합니다. `Button`을 통해 사용자가 이미지를 미러링/미러링 해제할 수 있도록 합니다.

## 3. 결과 확인

이제 앱을 실행시키고 이미지를 선택한 후, "Mirror" 버튼을 클릭하여 이미지가 미러링되는지 확인해봅니다.

```swift
@main
struct SimpleImageViewerApp: App {
    var body: some Scene {
        WindowGroup {
            ImageViewer()
        }
    }
}
```

위의 코드는 앱을 실행하는 진입점입니다. `ImageViewer` 뷰를 기본 뷰로 설정하고 앱 창에 표시합니다.

## 결론

위의 단계를 따라 가면 SwiftUI를 사용하여 이미지를 미러링하는 간단한 이미지 뷰어 앱을 만들 수 있습니다. 미러링 기능을 추가하여 이미지를 좌우로 반전시킬 수 있습니다. 이를 통해 사용자는 이미지를 다양한 방향으로 볼 수 있습니다.

참고 자료:
- [SwiftUI 공식 문서](https://developer.apple.com/documentation/swiftui)
- [iOS Developer 공식 문서](https://developer.apple.com/documentation/ios)