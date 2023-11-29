---
layout: post
title: "[swift] Swift CryptoSwift로 AES-GCM 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 Swift CryptoSwift 라이브러리를 사용하여 AES-GCM 암호화를 수행하는 방법에 대해 알아보겠습니다.

## CryptoSwift 설치

먼저 CryptoSwift를 설치해야 합니다. 이를 위해 `Podfile` 파일에 다음의 dependency를 추가하여 CocoaPods를 통해 설치합니다.

```ruby
pod 'CryptoSwift', '~> 1.4.0'
```

그리고 콘솔에서 아래의 명령어를 실행하여 CocoaPods를 업데이트하고 라이브러리를 설치합니다.

```bash
$ pod install
```

## AES-GCM 암호화 구현하기

CryptoSwift를 사용하여 AES-GCM 암호화를 구현하려면 다음의 단계를 따라야 합니다.

1. CryptoSwift import하기:
```swift
import CryptoSwift
```

2. 암호화할 데이터와 256비트 길이의 키 및 초기화 벡터(IV) 생성하기:
```swift
let key = AES.GCM.randomIV()
let iv = AES.GCM.randomIV()
let dataToEncrypt: Data = "Hello, CryptoSwift!".data(using: .utf8)!
```

3. 암호화하기:
```swift
let aes = try AES.GCM(key: key, iv: iv)
let encryptedData = try aes.encrypt(dataToEncrypt)
```

4. 복호화하기:
```swift
let aesDecrypt = try AES.GCM(key: key, iv: iv)
let decryptedData = try aesDecrypt.decrypt(encryptedData)
```

결과 확인하기:
```swift
let decryptedString = String(data: decryptedData, encoding: .utf8)
print("Decrypted Data: \(decryptedString ?? "")")
```

## 전체 코드 예시

```swift
import CryptoSwift

let key = AES.GCM.randomIV()
let iv = AES.GCM.randomIV()
let dataToEncrypt: Data = "Hello, CryptoSwift!".data(using: .utf8)!

let aes = try AES.GCM(key: key, iv: iv)
let encryptedData = try aes.encrypt(dataToEncrypt)

let aesDecrypt = try AES.GCM(key: key, iv: iv)
let decryptedData = try aesDecrypt.decrypt(encryptedData)

let decryptedString = String(data: decryptedData, encoding: .utf8)
print("Decrypted Data: \(decryptedString ?? "")")
```

이제 Swift CryptoSwift를 사용하여 AES-GCM 암호화를 수행하는 방법에 대해 배웠습니다. CryptoSwift의 다른 기능들을 알아보고 더 복잡한 암호화 작업을 수행할 수도 있습니다.

## 참고 자료

- [CryptoSwift GitHub 레포지토리](https://github.com/krzyzanowskim/CryptoSwift)
- [CryptoSwift 문서](https://cryptoswift.io/)
- [Swift 암호화 튜토리얼](https://medium.com/flawless-app-stories/how-to-increase-security-using-swifts-built-in-encryption-ac2374461378)