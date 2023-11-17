---
layout: post
title: "[swift] Swift Presentr와 UIAlertController를 함께 사용하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
UIAlertController는 iOS에서 다이얼로그를 표시하기 위해 주로 사용되는 클래스입니다. 그러나 기본적으로 제공되는 UIAlertController의 스타일과 레이아웃은 사용자 정의하기가 어렵습니다. 이때 Swift Presentr 라이브러리를 사용하면 UIAlertController의 스타일과 레이아웃을 쉽게 변경할 수 있습니다.

## Step 1: Swift Presentr 라이브러리 설치
Swift Presentr는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음 코드를 추가하고, `pod install` 명령어를 실행하세요.

```ruby
pod 'SwiftPresentr'
```

## Step 2: UIAlertController를 Presentr을 사용하여 표시하기
Swift Presentr을 사용하여 UIAlertController를 표시하는 방법은 매우 간단합니다. 다음은 예시 코드입니다.

```swift
import SwiftPresentr

...

// Presentr 객체 생성
let presentr = Presentr(presentationType: .popup)

// UIAlertController 객체 생성
let alert = UIAlertController(title: "알림", 
                              message: "이것은 경고 메시지입니다.", 
                              preferredStyle: .alert)

// UIAlertAction 객체 생성
let action = UIAlertAction(title: "확인", style: .default) { action in
    // 확인 버튼이 눌렸을 때 수행할 동작
}

// UIAlertAction 객체를 UIAlertController에 추가
alert.addAction(action)

// Presentr을 사용하여 UIAlertController 표시
presentr.presentViewController(alert, animated: true, completion: nil)
```

위의 코드에서는 Presentr 객체를 생성하여 표시하는 UIAlertController의 스타일을 설정합니다. UIAlertController를 생성하고 UIAlertAction(확인 버튼)을 추가한 후, Presentr을 사용하여 UIAlertController를 표시합니다.

## 결론
Swift Presentr를 사용하면 UIAlertController의 스타일과 레이아웃을 쉽게 변경할 수 있습니다. Presentr은 다양한 표시 스타일 및 애니메이션을 제공하여 iOS 애플리케이션의 다이얼로그를 보다 사용자 정의할 수 있도록 도와줍니다.

참고: [Swift Presentr Github 페이지](https://github.com/IcaliaLabs/Presentr)