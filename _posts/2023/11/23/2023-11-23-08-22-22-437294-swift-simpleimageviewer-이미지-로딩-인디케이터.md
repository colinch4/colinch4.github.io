---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 로딩 인디케이터"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 로딩할 때 사용자에게 진행 상황을 시각적으로 표시하는 인디케이터를 추가하는 것은 좋은 사용자 경험을 제공하는 데 도움이 됩니다. Swift에서는 `UIActivityIndicatorView` 클래스를 사용하여 이미지 로딩 인디케이터를 구현할 수 있습니다.

## 단계 1: UIActivityIndicatorView 추가하기

먼저 `UIActivityIndicatorView`를 추가해야 합니다. 인디케이터를 원하는 위치에 배치하고 알맞은 크기로 조정합니다. 예를 들어, 이미지를 표시할 `UIImageView`와 함께 인디케이터를 추가하고 중앙에 위치시키는 코드는 다음과 같습니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
let indicator = UIActivityIndicatorView(style: .gray)
indicator.center = imageView.center
imageView.addSubview(indicator)
```

## 단계 2: 이미지 로딩 시 인디케이터 표시하기

이제 이미지를 로딩할 때 인디케이터를 표시하고 로딩이 완료되면 인디케이터를 숨기는 코드를 작성해야 합니다. 아래는 `UIImage`의 확장(extension)을 사용하여 이미지를 로딩하는 동안 인디케이터를 표시하는 예입니다.

```swift
extension UIImage {
    static func loadImage(withURL url: URL, completion: @escaping (UIImage?) -> Void) {
        let indicator = UIActivityIndicatorView(style: .gray)
        indicator.startAnimating()
        
        URLSession.shared.dataTask(with: url) { (data, response, error) in
            DispatchQueue.main.async {
                indicator.stopAnimating()
                
                if let data = data {
                    completion(UIImage(data: data))
                } else {
                    completion(nil)
                }
            }
        }.resume()
    }
}
```

위 코드에서 `loadImage(withURL:completion:)` 메소드는 이미지 URL과 완료 후 실행할 클로저(completion closure)를 매개변수로 받습니다. 이 메소드는 `URLSession.shared.dataTask(with:completionHandler:)`를 사용하여 비동기적으로 이미지 데이터를 로드합니다. 로딩이 시작되면 인디케이터를 표시하고, 로딩이 완료되면 인디케이터를 숨기고 완료 클로저를 호출합니다.

## 사용 예시

이제 인디케이터가 있는 이미지 로딩 방법을 사용하는 예시를 살펴보겠습니다.

```swift
let imageURL = URL(string: "https://example.com/image.jpg")!

UIImage.loadImage(withURL: imageURL) { image in
    if let image = image {
        imageView.image = image
    } else {
        // 로딩 실패 시 처리 로직 추가
    }
}
```

위 예시에서는 위에서 작성한 `UIImage.loadImage(withURL:completion:)`를 사용하여 이미지를 로딩하고, 성공적으로 로드되면 `UIImageView`에 이미지를 설정합니다. 만약 로딩에 실패하면 실패 처리 로직을 추가할 수 있습니다.

이제 Swift에서 이미지 로딩 인디케이터를 사용하는 방법을 알게 되었습니다. 이를 구현하여 사용자가 즉시 로딩 상태를 인지할 수 있는 사용자 친화적인 환경을 제공할 수 있습니다.

## 참고 자료

1. [UIActivityIndicatorView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiactivityindicatorview)
2. [URLSession - Apple Developer Documentation](https://developer.apple.com/documentation/foundation/urlsession)