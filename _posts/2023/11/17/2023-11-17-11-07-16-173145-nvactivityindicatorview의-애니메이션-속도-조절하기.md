---
layout: post
title: "[swift] NVActivityIndicatorView의 애니메이션 속도 조절하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 작성된 간단하고 사용하기 쉬운 인디케이터 뷰입니다. 이 뷰를 사용하면 로딩 중인 상태를 시각적으로 나타낼 수 있습니다. 이번에는 NVActivityIndicatorView의 애니메이션 속도를 조절하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같은 코드를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널을 열고 프로젝트 폴더로 이동한 다음, `pod install` 명령어를 실행합니다.

```bash
$ pod install
```

이제 NVActivityIndicatorView가 설치되었습니다.

## 2. 애니메이션 속도 조절하기

NVActivityIndicatorView는 기본적으로 애니메이션 속도를 제어하는 기능을 제공하지 않습니다. 따라서 일부 수정이 필요합니다. 

NVActivityIndicatorView의 원본 코드를 열고, `NVActivityIndicatorAnimationBallRotateChase.swift` 파일을 찾습니다. 

해당 파일의 `NVActivityIndicatorAnimationBallRotateChase` 클래스를 찾아보세요. 이 클래스에는 `self.duration` 변수가 있습니다. 이 변수가 애니메이션 속도를 조절하는 데 사용됩니다.

```swift
open class NVActivityIndicatorAnimationBallRotateChase: NVActivityIndicatorAnimationDelegate {
    public func setUpAnimation(in layer: CALayer, size: CGSize, color: UIColor) {
        ...
        self.duration = 1.0 // 애니메이션 속도 조절
        ...
    }
}
```

`self.duration` 값을 조정하여 애니메이션의 속도를 더 빠르게 하거나 더 느리게 할 수 있습니다. 기본값은 1.0이며, 이 값이 낮을수록 더 빠른 속도로 애니메이션이 실행됩니다.

## 3. 결과 확인하기

위의 수정을 마치고 나면, NVActivityIndicatorView의 애니메이션 속도가 조절된 것을 확인할 수 있습니다. 변경된 속도에 맞게 로딩 인디케이터가 동작합니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)