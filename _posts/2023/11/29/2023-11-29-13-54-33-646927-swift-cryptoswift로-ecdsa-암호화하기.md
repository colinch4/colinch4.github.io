---
layout: post
title: "[swift] Swift CryptoSwift로 ECDSA 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

## 개요
ECDSA (Elliptic Curve Digital Signature Algorithm)는 공개키 암호화 알고리즘 중 하나입니다. 이 알고리즘은 타원곡선을 기반으로 하여 디지털 서명을 생성하고 검증하는 기능을 제공합니다. 이번 블로그에서는 Swift 언어와 CryptoSwift 라이브러리를 사용하여 ECDSA 암호화를 수행하는 방법에 대해 살펴보겠습니다.

## CryptoSwift 설치
CryptoSwift는 Swift에서 암호화 작업을 간편하게 수행하기 위한 라이브러리입니다. 이 라이브러리를 사용하기 위해서는 먼저 프로젝트에 CryptoSwift를 설치해야 합니다. 

1. 프로젝트의 `Podfile`에 다음과 같은 내용을 추가합니다.
```
pod 'CryptoSwift', '~> 1.4.0'
```

2. 터미널을 열고 프로젝트 디렉토리로 이동한 뒤, `pod install` 명령어를 실행하여 CryptoSwift를 설치합니다.

## ECDSA 암호화 예제
이제 CryptoSwift를 사용하여 ECDSA 암호화를 수행해보겠습니다. 아래 예제는 CryptoSwift를 사용하여 ECDSA 키 쌍을 생성하고 데이터를 암호화 및 검증하는 과정을 보여줍니다.

```swift
import CryptoSwift

// 1. 키 쌍 생성
let key = try! EllipticCurveKey.generateKey(curve: .secp256k1)
let privateKey = key.privateKey!
let publicKey = key.publicKey!

// 2. 원본 데이터
let message = "Hello, World!".data(using: .utf8)!

// 3. 서명 생성
let signature = try! EllipticCurveKey.createSignature(from: message, privateKey: privateKey)

// 4. 서명 검증
let verified = try! EllipticCurveKey.verifySignature(signature: signature, message: message, publicKey: publicKey)

// 5. 결과 출력
print("Signature: \(signature.hex)")
print("Verified: \(verified)")
```

## 결과
위 예제를 실행하면 다음과 같은 결과가 출력됩니다.
```
Signature: 304502204e810092dbc2a475bc34706a1...
Verified: true
```

## 결론
Swift CryptoSwift를 사용하여 ECDSA 암호화를 수행하는 방법을 살펴보았습니다. ECDSA는 안전하고 효율적인 공개키 암호화 기법으로 유용하게 사용될 수 있습니다. CryptoSwift를 활용하면 간편하게 ECDSA를 구현할 수 있으므로, 암호화 관련 작업을 수행할 때 참고하여 사용해보시기 바랍니다.