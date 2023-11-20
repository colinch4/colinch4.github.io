---
layout: post
title: "[swift] Swift SkeletonView SwiftUI에서 사용하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

Swift SkeletonView는 더 나은 사용자 경험을 제공하기 위해 앱 또는 웹 페이지에서 로딩 중인 콘텐츠를 시각적으로 표시하는 데 사용되는 라이브러리입니다. 이 제스처은 로딩 시간 동안 사용자에게 애니메이션 효과를 제공하여 사용자의 이해를 돕습니다. 이번 글에서는 Swift SkeletonView를 SwiftUI에서 사용하는 방법에 대해 알아보겠습니다.

## SkeletonView 라이브러리 설치

Swift SkeletonView를 사용하기 위해서는 먼저 프로젝트에 해당 라이브러리를 설치해야 합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'SkeletonView'
```

설치가 끝난 후에는 `import SkeletonView` 문을 추가하여 라이브러리를 사용할 준비를 합니다.

## SwiftUI에서 SkeletonView 사용하기

SwiftUI에서 SkeletonView를 사용하는 것은 간단합니다. 먼저 로딩 중인 콘텐츠에 적용하고자 하는 View를 `SkeletonAppearance`을 이용하여 선언합니다. 예를 들어, 이미지를 로딩하는 뷰를 감싸는 경우 다음과 같이 작성할 수 있습니다.

```swift
import SwiftUI
import SkeletonView

struct ContentView: View {
    var body: some View {
        VStack {
            Image("myImage")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 200, height: 200)
                .skeleton(with: true) // Skeleton으로 감쌉니다.
                .padding()
        }
    }
}
```

이제 사용자가 이미지를 로드하는 동안 SkeletonView가 애니메이션을 실행하게 됩니다. `.skeleton(with: true)` 구문을 사용하여 SkeletonView를 적용하며, 그리고 `.padding()`을 통해 적절한 여백을 추가합니다.

## SkeletonView 커스터마이즈하기

SkeletonView를 커스터마이즈하여 앱의 디자인과 일치하도록 만들 수도 있습니다. 예를 들어, 배경 색상을 변경하거나 두께 및 모양을 조정할 수 있습니다. `skeletonAppearance` 속성을 사용하여 커스터마이즈할 수 있습니다. 다음은 간단한 예시입니다.

```swift
import SwiftUI
import SkeletonView

struct ContentView: View {
    
    init() {
        // 전역으로 Skeleton View 모양 커스터마이즈
        SkeletonAppearance.backgroundColor = .systemGray2
        SkeletonAppearance.tintColor = .gray
        SkeletonAppearance.multilineHeight = 10
    }
    
    var body: some View {
        VStack {
            Image("myImage")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .frame(width: 200, height: 200)
                .skeleton(with: true)
                .padding()
        }
    }
}
```

위의 코드에서는 `.init()` 메소드 내에 `SkeletonAppearance`의 속성을 변경하여 SkeletonView의 외관을 커스터마이즈합니다.

## 마치며

이 글에서는 Swift SkeletonView를 SwiftUI에서 사용하는 방법에 대해 알아보았습니다. Swift SkeletonView는 로딩 중인 콘텐츠를 시각적으로 표시하여 사용자 경험을 향상시키는 강력한 도구입니다. SkeletonView를 사용하여 앱의 로딩 시간 동안 사용자에게 애니메이션 효과를 제공해보세요!

**참고 자료:**
- [Swift SkeletonView GitHub 페이지](https://github.com/Juanpe/SkeletonView)
- [SwiftUI 공식 문서](https://developer.apple.com/documentation/swiftui)