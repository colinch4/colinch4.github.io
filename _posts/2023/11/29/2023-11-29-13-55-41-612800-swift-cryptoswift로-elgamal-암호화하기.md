---
layout: post
title: "[swift] Swift CryptoSwift로 ElGamal 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

암호화는 현대 정보보안에서 매우 중요한 기술입니다. ElGamal 암호화는 대표적인 공개키 암호화 알고리즘 중 하나로, 비대칭 키를 사용하여 데이터를 안전하게 암호화하고 복호화하는 기능을 제공합니다.

이번 블로그 포스트에서는 Swift 언어와 CryptoSwift 라이브러리를 사용하여 ElGamal 암호화를 구현하는 방법을 알아보겠습니다.

## CryptoSwift 설치하기

먼저 CryptoSwift 라이브러리를 프로젝트에 추가해야 합니다. 이를 위해 Cocoapods을 사용할 수 있습니다. 프로젝트 폴더에서 터미널을 실행하고 다음 명령어를 입력합니다:

```bash
$ pod init
```

그런 다음 Podfile 파일을 수정하여 다음과 같이 CryptoSwift를 추가합니다:

```ruby
target 'YourProject' do
  use_frameworks!
  pod 'CryptoSwift', '~> 1.4.0'
end
```

다시 터미널에서 다음 명령어를 입력하여 라이브러리를 설치합니다:

```bash
$ pod install
```

## ElGamal 암호화 구현하기

이제 CryptoSwift 라이브러리를 사용하여 ElGamal 암호화를 구현해 보겠습니다. ElGamal 암호화에는 두 가지 주요 단계가 있습니다: 키 생성 및 암호화/복호화입니다.

### 키 생성하기

키 생성 단계에서는 공개키와 개인키를 생성합니다. CryptoSwift를 사용하여 랜덤 값을 생성한 다음, 이를 기반으로 공개키와 개인키를 계산합니다.

```swift
import CryptoSwift

// 공개키와 개인키 생성
func generateKeyPair() -> (BigUInt, BigUInt, BigUInt) {
    let p = BigUInt.randomPrime(bits: 256)
    let g = BigUInt.randomInt(upperBound: p - 1)
    let x = BigUInt.randomInt(upperBound: p - 1)
    let y = g.power(x, modulus: p)
    return (p, g, y)
}
```

### 암호화하기

암호화 단계에서는 공개키를 사용하여 평문을 암호화합니다. 평문은 BigUInt로 변환한 다음, 암호화를 수행합니다.

```swift
// 평문 암호화
func encrypt(plainText: String, publicKey: (BigUInt, BigUInt, BigUInt)) -> (BigUInt, BigUInt) {
    let p = publicKey.0
    let g = publicKey.1
    let y = publicKey.2

    let m = BigUInt(plainText.utf8)
    let k = BigUInt.randomInt(upperBound: p - 2)
    let a = g.power(k, modulus: p)
    let b = m * y.power(k, modulus: p) % p

    return (a, b)
}
```

### 복호화하기

복호화 단계에서는 개인키를 사용하여 암호문을 복호화합니다. 암호문을 복호화하여 다시 평문으로 변환합니다.

```swift
// 암호문 복호화
func decrypt(encryptedValue: (BigUInt, BigUInt), privateKey: BigUInt) -> String {
    let a = encryptedValue.0
    let b = encryptedValue.1

    let p = privateKey

    let m = b * a.power(p - 1 - privateKey, modulus: p) % p
    let decryptedData = Data(BigUInt(m).serialize())
    guard let decryptedText = String(data: decryptedData, encoding: .utf8) else {
        return ""
    }

    return decryptedText
}
```

## 실행 예시

프로젝트에 위의 함수들을 추가한 다음, 아래와 같이 암호화 예시를 실행해보겠습니다:

```swift
let plainText = "This is a secret message."

let publicKey = generateKeyPair()
let encryptedValue = encrypt(plainText: plainText, publicKey: publicKey)

print("Encrypted value: \(encryptedValue)")

let privateKey = publicKey.0
let decryptedText = decrypt(encryptedValue: encryptedValue, privateKey: privateKey)

print("Decrypted text: \(decryptedText)")
```

위의 예시에서는 "This is a secret message."라는 평문을 암호화한 다음, 다시 복호화하여 원래의 평문을 얻을 수 있는지 확인합니다.

## 결론

이번 포스트에서는 Swift 언어와 CryptoSwift 라이브러리를 사용하여 ElGamal 암호화를 구현하는 방법을 알아보았습니다. ElGamal은 현대 정보보안에 많이 사용되는 암호화 알고리즘 중 하나로, 공개키 암호화를 효과적으로 구현할 수 있습니다.

더 많은 정보는 [CryptoSwift GitHub 페이지](https://github.com/krzyzanowskim/CryptoSwift)에서 확인할 수 있습니다.