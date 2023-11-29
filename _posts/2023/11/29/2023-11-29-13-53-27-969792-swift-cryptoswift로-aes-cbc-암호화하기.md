---
layout: post
title: "[swift] Swift CryptoSwift로 AES-CBC 암호화하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift CryptoSwift 라이브러리를 사용하여 AES-CBC 암호화 방식을 적용하는 방법에 대해 알아보겠습니다. 

## 1. CryptoSwift 라이브러리 설치하기

CryptoSwift를 사용하기 위해 먼저 프로젝트에 라이브러리를 추가해야 합니다. 

### CocoaPods를 사용하는 경우

Podfile에 다음과 같이 추가합니다.

```ruby
target 'YourProject' do
    pod 'CryptoSwift', '~> 1.4'
end
```

터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

### Swift Package Manager를 사용하는 경우

Xcode에서 File -> Swift Packages -> Add Package Dependency...를 선택합니다. 

다음 URL을 입력하고 Add 버튼을 클릭합니다.

```
https://github.com/krzyzanowskim/CryptoSwift.git
```

## 2. AES-CBC 암호화 구현하기

다음은 CryptoSwift를 사용하여 AES-CBC 암호화를 구현하는 예제 코드입니다.

```swift
import CryptoSwift

func encryptAES(key: String, iv: String, plaintext: String) throws -> String {
    let key = try AES.key(fromPassword: key, salt: iv) // 키와 초기화 백터 생성
    let iv = try AES.randomIV() // 초기화 백터 생성
    
    let aes = try AES(key: key, blockMode: CBC(iv: iv), padding: .pkcs7)
    let ciphertext = try aes.encrypt(Array(plaintext.utf8))
    
    return ciphertext.toBase64() ?? ""
}

func decryptAES(key: String, iv: String, ciphertext: String) throws -> String {
    let key = try AES.key(fromPassword: key, salt: iv) // 키와 초기화 백터 생성
    let iv = try AES.randomIV() // 초기화 백터 생성
    
    let aes = try AES(key: key, blockMode: CBC(iv: iv), padding: .pkcs7)
    let decrypted = try aes.decrypt(Array(base64: ciphertext))
    
    return String(data: Data(decrypted), encoding: .utf8) ?? ""
}
```

위 코드에서 `encryptAES` 함수는 주어진 키와 초기화 백터를 사용하여 평문을 암호화하고, `decryptAES` 함수는 주어진 키와 초기화 백터를 사용하여 암호문을 복호화합니다.

## 3. 사용 예시

이제 위에서 작성한 암호화 함수를 사용해보겠습니다.

```swift
let key = "myEncryptionKey"
let iv = "myInitializationVector"
let plaintext = "Hello, World!"
do {
  let ciphertext = try encryptAES(key: key, iv: iv, plaintext: plaintext)
  print("Ciphertext:", ciphertext)
  
  let decryptedText = try decryptAES(key: key, iv: iv, ciphertext: ciphertext)
  print("Decrypted Text:", decryptedText)
} catch {
  print("Error:", error)
}
```

위 코드에서는 `key`, `iv`, 그리고 `plaintext` 변수를 설정한 후, `encryptAES` 함수를 사용하여 평문을 암호화하고 `ciphertext` 변수에 저장합니다. 그 다음 `decryptAES` 함수를 사용하여 `ciphertext`를 복호화하여 `decryptedText` 변수에 저장합니다.

## 참고 자료

- [CryptoSwift GitHub 페이지](https://github.com/krzyzanowskim/CryptoSwift)
- [AES Encryption in Swift with CryptoSwift](https://www.devaddicted.com/articles/aes-encryption-in-swift-with-cryptoswift)