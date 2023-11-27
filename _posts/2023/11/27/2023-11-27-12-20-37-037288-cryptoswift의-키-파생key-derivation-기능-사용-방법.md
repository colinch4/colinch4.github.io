---
layout: post
title: "[swift] CryptoSwift의 키 파생(Key Derivation) 기능 사용 방법"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개

CryptoSwift는 Swift로 작성된 암호화 및 해시 라이브러리입니다. 이 라이브러리는 다양한 암호화 알고리즘과 해시 함수를 제공하며, 키 파생(key derivation) 기능도 지원합니다. 이 기능을 사용하면 마스터 키를 기반으로 하여 다른 키들을 생성할 수 있습니다.

## 키 파생 기능 사용 방법

CryptoSwift에서 키 파생 기능을 사용하려면 `Argon2` 또는 `PBKDF2` 알고리즘을 선택해야 합니다. 각 알고리즘의 사용법은 다음과 같습니다:

### Argon2

Argon2 알고리즘은 강력한 키 파생 기능으로 알려져 있습니다. CryptoSwift에서 Argon2를 사용하기 위해서는 다음과 같은 단계를 따릅니다:

1. Argon2 패키지를 설치합니다. 설치 방법은 [여기](https://github.com/krzyzanowskim/CryptoSwift/blob/main/Docs/GettingStarted.md#manual)에서 확인할 수 있습니다.

2. 아래 코드와 같이 Argon2 함수를 호출하여 키를 파생시킵니다:

```swift
import CryptoSwift

let password: Array<UInt8> = Array("my_password".utf8)
let salt: Array<UInt8> = Array("SALT".utf8)
let key = try! CryptoSwift.Argon2.password(password, salt: salt, outputLength: 32)
```

### PBKDF2

PBKDF2 알고리즘은 비밀번호 기반 키 파생에 사용되는 전통적인 알고리즘입니다. CryptoSwift에서 PBKDF2를 사용하기 위해서는 다음과 같은 단계를 따릅니다:

1. PBKDF2 패키지를 설치합니다. 설치 방법은 [여기](https://github.com/krzyzanowskim/CryptoSwift/blob/main/Docs/GettingStarted.md#manual)에서 확인할 수 있습니다.

2. 아래 코드와 같이 PBKDF2 함수를 호출하여 키를 파생시킵니다:

```swift
import CryptoSwift

let password: Array<UInt8> = Array("my_password".utf8)
let salt: Array<UInt8> = Array("SALT".utf8)
let key = try! CryptoSwift.PBKDF2(password: password, salt: salt, iterations: 100000, keyLength: 32, variant: .sha256).calculate()
```

## 결론

CryptoSwift의 키 파생 기능은 강력한 암호화 및 보안을 구현하는 데 도움을 줍니다. 위의 예제를 사용하여 Argon2 또는 PBKDF2를 이용하여 마스터 키를 파생시킬 수 있습니다. 추가적인 사용 방법과 기능에 대해서는 CryptoSwift의 공식 문서를 참조하시기 바랍니다.

## 참고 자료

- [CryptoSwift 공식 GitHub](https://github.com/krzyzanowskim/CryptoSwift)
- [CryptoSwift 설치 방법](https://github.com/krzyzanowskim/CryptoSwift/blob/main/Docs/GettingStarted.md#manual)
- [Argon2 알고리즘](https://en.wikipedia.org/wiki/Argon2)
- [PBKDF2 알고리즘](https://en.wikipedia.org/wiki/PBKDF2)