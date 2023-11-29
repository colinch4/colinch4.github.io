---
layout: post
title: "[swift] Swift CryptoSwift와 CommonCrypto의 비교"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

암호화는 모바일 앱 및 웹 애플리케이션에서 매우 중요합니다. 많은 개발자들은 Swift로 작성된 코드에서 암호화를 적용하는 방법을 찾고 있습니다. 이 때 주로 사용되는 두 개의 라이브러리는 CryptoSwift와 CommonCrypto입니다. 이렇게 두 가지 라이브러리를 비교하여 어떤 것을 선택해야 할지 알아보겠습니다.

## CryptoSwift

CryptoSwift는 순수 Swift로 작성된 암호화 라이브러리입니다. 이 라이브러리는 다양한 대칭 및 비대칭 알고리즘을 지원합니다. 또한, 다양한 해시 함수, HMAC, PBKDF 등의 기능을 제공합니다.

CryptoSwift는 사용하기 쉬운 API를 제공하며, Swift의 강력한 컬렉션 기능을 활용하여 데이터의 처리를 손쉽게 할 수 있도록 도와줍니다. 또한, 암호화 작업에 특화된 최적화된 코드를 제공하여 성능을 향상시킬 수 있습니다.

```swift
import CryptoSwift

let key = "mysecretkey" // 암호화 키
let plainText = "Hello, World!" // 평문

do {
    // AES-256 암호화
    let aes = try AES(key: key, iv: nil)
    let ciphertext = try aes.encrypt(Array(plainText.utf8))
    print(ciphertext.toHexString()) // 암호문 출력
    
    // AES-256 복호화
    let decrypted = try aes.decrypt(ciphertext)
    let decryptedText = String(data: Data(decrypted), encoding: .utf8)
    print(decryptedText) // 복호화된 평문 출력
} catch {
    print("Error: \(error)")
}
```

## CommonCrypto

CommonCrypto는 C 언어로 작성된 암호화 라이브러리입니다. 이 라이브러리는 macOS 및 iOS에서 제공되는 C 라이브러리로서, 많은 암호화 기능을 제공합니다. CommonCrypto는 대칭 및 비대칭 암호화뿐만 아니라, 해시 함수 및 HMAC 기능도 포함하고 있습니다.

이 라이브러리는 Swift에서 사용하기 위해 직접적인 지원을 제공하지는 않지만, Swift에서 사용할 수 있는 Bridging Header를 통해 C 언어 함수를 호출할 수 있습니다.

```swift
#include <CommonCrypto/CommonCryptor.h>

NSString *encryptAES256(NSString *key, NSString *plainText) {
    NSData *plainData = [plainText dataUsingEncoding:NSUTF8StringEncoding];
    
    uint8_t *buffer = malloc(plainData.length + kCCBlockSizeAES128);
    size_t numBytesEncrypted = 0;
    
    NSData *keyData = [key dataUsingEncoding:NSUTF8StringEncoding];
    NSData *ivData = nil; // 초기화 벡터
    
    CCCryptorStatus status = CCCrypt(kCCEncrypt,
                                     kCCAlgorithmAES,
                                     kCCOptionPKCS7Padding,
                                     keyData.bytes,
                                     keyData.length,
                                     ivData.bytes,
                                     plainData.bytes,
                                     plainData.length,
                                     buffer,
                                     plainData.length + kCCBlockSizeAES128,
                                     &numBytesEncrypted);
    
    if (status == kCCSuccess) {
        NSData *encryptedData = [NSData dataWithBytesNoCopy:buffer length:numBytesEncrypted];
        return [encryptedData base64EncodedStringWithOptions:0];
    } else {
        free(buffer);
        return nil;
    }
}

NSString *decryptAES256(NSString *key, NSString *cipherText) {
    NSData *cipherData = [[NSData alloc] initWithBase64EncodedString:cipherText options:0];
    
    uint8_t *buffer = malloc(cipherData.length + kCCBlockSizeAES128);
    size_t numBytesDecrypted = 0;
    
    NSData *keyData = [key dataUsingEncoding:NSUTF8StringEncoding];
    NSData *ivData = nil; // 초기화 벡터
    
    CCCryptorStatus status = CCCrypt(kCCDecrypt,
                                     kCCAlgorithmAES,
                                     kCCOptionPKCS7Padding,
                                     keyData.bytes,
                                     keyData.length,
                                     ivData.bytes,
                                     cipherData.bytes,
                                     cipherData.length,
                                     buffer,
                                     cipherData.length + kCCBlockSizeAES128,
                                     &numBytesDecrypted);
    
    if (status == kCCSuccess) {
        NSData *decryptedData = [NSData dataWithBytesNoCopy:buffer length:numBytesDecrypted];
        return [[NSString alloc] initWithData:decryptedData encoding:NSUTF8StringEncoding];
    } else {
        free(buffer);
        return nil;
    }
}
```

## 결론

CryptoSwift와 CommonCrypto는 모두 사용하기 편리하고 강력한 암호화 기능을 제공하는 라이브러리입니다. 선택은 개인의 선호도 및 프로젝트의 요구사항에 따라 다를 수 있습니다.

- CryptoSwift는 Swift로 작성되어 있으며, 현대적인 암호화 알고리즘과 다양한 기능을 제공합니다. 또한, 간결하고 사용하기 쉬운 API를 가지고 있습니다.
- CommonCrypto는 C 라이브러리로 작성되어 있으며, 여러 암호화 알고리즘과 기능을 제공합니다. 다만, Swift에서 직접 사용하기 위해서는 Bridging Header를 사용해야 합니다.

프로젝트에 맞게 라이브러리를 선택하여 안전하고 강력한 암호화를 구현하길 바랍니다.

---

참조:
- CryptoSwift: [https://github.com/krzyzanowskim/CryptoSwift](https://github.com/krzyzanowskim/CryptoSwift)
- CommonCrypto: [https://developer.apple.com/documentation/security/commoncrypto](https://developer.apple.com/documentation/security/commoncrypto)