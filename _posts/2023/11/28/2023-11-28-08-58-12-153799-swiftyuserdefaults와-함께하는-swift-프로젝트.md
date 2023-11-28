---
layout: post
title: "[swift] SwiftyUserDefaults와 함께하는 Swift 프로젝트"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

안녕하세요! Swift 프로젝트에서 UserDefaults를 사용하기 위한 간편한 라이브러리인 SwiftyUserDefaults를 소개합니다.

## SwiftyUserDefaults란?

SwiftyUserDefaults는 UserDefaults를 조작하기 위한 래퍼(wrapper) 라이브러리입니다. Swift의 강력한 기능 중 하나인 `@propertyWrapper`를 사용하여 UserDefaults 키-값 쌍을 손쉽게 다룰 수 있도록 해줍니다. 이를 통해 복잡한 코드를 간소화하고 가독성을 높일 수 있습니다.

## 설치 방법

SwiftyUserDefaults를 사용하기 위해서는 먼저 프로젝트의 `Podfile`에 다음과 같이 추가해야 합니다.

```ruby
pod 'SwiftyUserDefaults'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 사용 방법

1. 먼저, UserDefaults 키를 정의합니다.

```swift
import SwiftyUserDefaults

extension DefaultsKeys {
    static let isFirstLaunch = DefaultsKey<Bool>("isFirstLaunch")
    static let userName = DefaultsKey<String?>("userName")
    static let age = DefaultsKey<Int>("age")
}
```

2. UserDefaults에 값을 저장하거나 가져올 수 있습니다.

```swift
Defaults[.isFirstLaunch] = true
let isFirstLaunch = Defaults[.isFirstLaunch]
```

3. Optional 타입을 다룰 때에도 편리하게 사용할 수 있습니다.

```swift
Defaults[.userName] = nil
let userName = Defaults[.userName]
```

4. 기본값을 지정하여 값을 가져올 수도 있습니다.

```swift
let age = Defaults[.age, defaultValue: 0]
```

## 장점

- 가독성: SwiftyUserDefaults는 기존의 UserDefaults 코드를 간소화하여 가독성을 향상시킵니다.
- 안전성: 타입 안정성을 지원하기 때문에, 잘못된 타입으로 인한 오류를 예방할 수 있습니다.
- 편의성: SwiftyUserDefaults를 통해 다양한 타입의 데이터를 간단히 저장하고 불러올 수 있습니다.

## 결론

SwiftyUserDefaults는 UserDefaults를 다루기 위한 간편하고 효율적인 방법을 제공해주는 라이브러리입니다. 기존의 번거로운 코드 작성을 최소화하여 개발자가 더욱 직관적으로 UserDefaults를 다룰 수 있도록 도와줍니다. 많은 프로젝트에서 활용되고 있는 SwiftyUserDefaults를 사용하여 코드 작성의 효율성을 높여보세요!

더 자세한 내용은 [SwiftyUserDefaults](https://github.com/sunshinejr/SwiftyUserDefaults) 공식 GitHub 페이지에서 확인하실 수 있습니다.