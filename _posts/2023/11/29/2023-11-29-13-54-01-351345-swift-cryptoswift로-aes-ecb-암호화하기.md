---
layout: post
title: "[swift] Swift CryptoSwift로 AES-ECB 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

## 소개
이번 블로그 포스트에서는 Swift 프로그래밍 언어를 사용하여 AES-ECB 암호화를 수행하는 방법을 알아보겠습니다. 이를 위해 CryptoSwift 라이브러리를 사용할 것입니다.

## CryptoSwift 설치하기

CryptoSwift 라이브러리를 사용하기 위해서는 먼저 프로젝트에 라이브러리를 추가해야 합니다. 가장 간단하게 CocoaPods를 사용하여 설치할 수 있습니다. 아래의 단계를 따라 CryptoSwift를 설치해보세요.

1. 터미널을 열고 프로젝트 디렉토리로 이동합니다.
2. 프로젝트 디렉토리에서 `pod init` 명령어를 사용하여 Podfile을 생성합니다.
3. Podfile을 텍스트 편집기로 열고 아래와 같이 작성합니다.

```ruby
platform :ios, '9.0'
use_frameworks!

target 'YourTargetName' do
  pod 'CryptoSwift', '~> 1.3.0'
end
```

4. 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## AES-ECB 암호화하기

CryptoSwift를 사용하여 AES-ECB 암호화를 수행하는 예제 코드입니다.

```swift
import CryptoSwift

func encryptAES_ECB(key: [UInt8], data: String) -> String? {
    guard let aes = try? AES(key: key, blockMode: ECB()) else { return nil }
    let inputData = Array(data.utf8)
    guard let encrypted = try? aes.encrypt(inputData) else { return nil }
    let encryptedData = Data(encrypted)
    return encryptedData.base64EncodedString()
}

let key: [UInt8] = [0xFF, 0x00, 0xAB, 0xCD, 0x12, 0x34, 0x56, 0x78, 0x90, 0xEF, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
let plaintext = "Hello, CryptoSwift!"

if let encryptedText = encryptAES_ECB(key: key, data: plaintext) {
    print("Encrypted Text: \(encryptedText)")
} else {
    print("Encryption failed.")
}
```

`encryptAES_ECB` 메서드는 AES-ECB 암호화를 수행합니다. `key`는 암호화에 사용할 키입니다. `data`는 암호화할 문자열입니다. 암호화된 결과는 Base64로 인코딩되어 반환됩니다.

위의 예제 코드에서는 임의로 생성한 16바이트의 키로 `Hello, CryptoSwift!` 문자열을 암호화하고 그 결과를 출력합니다.

## 결론
이번 포스트에서는 CryptoSwift 라이브러리를 사용하여 Swift에서 AES-ECB 암호화를 수행하는 방법을 알아보았습니다. CryptoSwift를 사용하면 암호화와 관련된 작업을 쉽고 간편하게 수행할 수 있습니다. 추가적인 기능과 세부 설정을 알고 싶다면 CryptoSwift 공식 문서를 참조해보세요.