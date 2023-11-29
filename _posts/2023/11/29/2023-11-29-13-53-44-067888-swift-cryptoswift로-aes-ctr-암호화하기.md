---
layout: post
title: "[swift] Swift CryptoSwift로 AES-CTR 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

암호화는 데이터를 안전하게 보호하기 위한 중요한 과정입니다. 이번 블로그 포스트에서는 Swift에서 [CryptoSwift](https://github.com/krzyzanowskim/CryptoSwift) 라이브러리를 사용하여 AES-CTR (Advanced Encryption Standard - Counter Mode) 알고리즘을 사용하는 방법을 알아보겠습니다.

## CryptoSwift 설치하기

먼저 CryptoSwift를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'CryptoSwift'
```

그리고 `pod install`을 실행하여 의존성을 설치합니다.

만약 Swift Package Manager를 사용한다면, Xcode 프로젝트에 다음의 종속성을 추가합니다:

```swift
dependencies: [
    .package(url: "https://github.com/krzyzanowskim/CryptoSwift.git", from: "1.3.8"),
],
targets: [
    .target(name: "MyApp", dependencies: ["CryptoSwift"]),
]
```

이제 CryptoSwift를 사용할 준비가 되었습니다.

## AES-CTR로 암호화하기

CryptoSwift를 사용하여 AES-CTR로 암호화하는 예제 코드를 살펴보겠습니다.

```swift
import CryptoSwift

func encryptAESCTR(message: String, key: String, iv: String) -> String? {
    guard let keyData = key.data(using: .utf8) else { return nil }
    guard let ivData = iv.data(using: .utf8) else { return nil }
    
    do {
        let aes = try AES(key: keyData.bytes, blockMode: CTR(iv: ivData.bytes), padding: .noPadding)
        let encrypted = try aes.encrypt(Array(message.utf8))
        return Data(encrypted).base64EncodedString()
    } catch {
        print("Encryption failed: \(error)")
        return nil
    }
}

let message = "Hello, World!"
let key = "MySecretKey123456"
let iv = "0123456789abcdef"

if let encryptedMessage = encryptAESCTR(message: message, key: key, iv: iv) {
    print("Encrypted message: \(encryptedMessage)")
} else {
    print("Encryption failed")
}
```

위의 예제 코드에서 `encryptAESCTR` 함수는 입력된 메시지, 암호화에 사용할 키(key), 초기화 벡터(iv)를 인자로 받습니다. AES 객체를 생성하고 해당 객체를 사용하여 메시지를 암호화합니다. 이후 암호화된 바이트 배열을 Base64로 인코딩하여 문자열로 반환합니다.

위의 코드를 실행하면 "Hello, World!"라는 메시지가 AES-CTR로 암호화되어 출력됩니다.

CryptoSwift를 사용하여 AES-CTR 암호화를 손쉽게 구현할 수 있습니다. 이제 암호화 된 메시지를 안전하게 전송하거나 저장할 수 있습니다.

CryptoSwift에 대한 자세한 내용은 [공식 GitHub 저장소](https://github.com/krzyzanowskim/CryptoSwift)를 참조하세요.