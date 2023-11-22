---
layout: post
title: "[swift] Swift SimpleImageViewer 웹 이미지 로딩 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

[SimpleImageViewer](https://github.com/pikachu987/SimpleImageViewer)는 Swift로 작성된 간단한 이미지 뷰어 라이브러리입니다. 이 라이브러리는 웹 이미지를 로딩하여 보여줄 수 있는 기능을 제공합니다.

## 설치 방법

SimpleImageViewer를 사용하기 위해서는 먼저 Cocoapods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. `Podfile` 파일에 아래의 내용을 추가한 후, 도트 커맨드를 실행하여 설치합니다.

```ruby
pod 'SimpleImageViewer', '~> 1.0'
```

## 사용 방법

SimpleImageViewer는 UIImageView를 간편하게 사용할 수 있도록 도와줍니다. 라이브러리를 사용하기 위해서는 먼저 UIImageView를 생성해야 합니다. 그런 다음 UIImageView의 `setImageFromURL(_:)` 메소드를 호출하여 웹 이미지를 로딩할 수 있습니다.

```swift
import SimpleImageViewer

let imageView = UIImageView()
imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)
view.addSubview(imageView)

let imageURL = URL(string: "https://example.com/image.jpg")
imageView.setImageFromURL(imageURL)
```

위의 예제에서 `imageView`는 이미지를 보여줄 UIImageView입니다. `setImageFromURL(_:)` 메소드를 사용하여 `imageURL`에서 이미지를 로딩합니다.

## 추가 옵션

SimpleImageViewer는 다양한 옵션을 제공하여 웹 이미지 로딩을 자유롭게 커스터마이징할 수 있습니다. 몇 가지 예시를 살펴보겠습니다.

### Placeholder 이미지 설정

원격 이미지 로딩 중에 보여줄 기본 이미지를 설정할 수 있습니다. `setImageFromURL(_:, placeholderImage:)` 메소드를 사용하여 Placeholder 이미지를 지정합니다.

```swift
let placeholderImage = UIImage(named: "placeholder")
imageView.setImageFromURL(imageURL, placeholderImage: placeholderImage)
```

### 캐시 설정

이미지 로딩 결과를 캐시하여 더 빠른 로딩을 위해 사용할 수 있습니다. `setImageFromURL(_:, cacheEnabled:)` 메소드의 두 번째 매개변수로 `true`를 전달하여 캐시 기능을 활성화할 수 있습니다.

```swift
imageView.setImageFromURL(imageURL, cacheEnabled: true)
```

### 이미지 로딩 실패 핸들링

이미지 로딩에 실패할 경우, 실패 상황에 대한 에러 핸들링을 할 수 있습니다. `setImageFromURL(_:, errorHandler:)` 메소드의 두 번째 매개변수로 클로저를 전달하여 에러를 처리합니다.

```swift
imageView.setImageFromURL(imageURL) { error in
    // 에러 처리
    print("이미지 로딩 실패: \(error)")
}
```

## 결론

SimpleImageViewer는 간단하고 편리한 방법으로 웹 이미지를 로딩하는 기능을 제공합니다. Cocoapods를 통해 설치하여 프로젝트에 쉽게 적용할 수 있습니다. 다양한 옵션을 사용하여 이미지 로딩을 커스터마이징할 수 있습니다. 사용하기 쉽고 가볍기 때문에 Swift 프로젝트에 적합한 라이브러리입니다.

## 참고 자료

- [SimpleImageViewer GitHub 저장소](https://github.com/pikachu987/SimpleImageViewer)