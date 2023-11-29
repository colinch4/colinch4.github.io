---
layout: post
title: "[swift] Swift CryptoSwift와 Swift Crypto의 차이점"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

### 소개
Swift는 많은 사람들에게 알려진 강력하고 인기 있는 프로그래밍 언어입니다. Swift는 아이폰, 아이패드, 앱 등 다양한 플랫폼에서 사용할 수 있으며, 암호화와 관련된 작업을 수행하는데도 매우 유용합니다. Swift에는 암호화 라이브러리를 사용할 수 있는 여러 옵션이 있지만, 여기서는 CryptoSwift와 Swift Crypto라는 두 가지 옵션에 초점을 맞출 것입니다.

### CryptoSwift와 Swift Crypto
CryptoSwift와 Swift Crypto는 모두 Swift 기반의 암호화 라이브러리입니다. 하지만 이 둘 사이에는 몇 가지 중요한 차이점이 있습니다.

#### 1. 진행 상태
CryptoSwift는 Swift에서 오랫동안 사용되고 있는 암호화 라이브러리입니다. CryptoSwift는 많은 사람들이 사용해 왔고, 안정적인 코드와 많은 커뮤니티 지원을 받고 있습니다.

반면에 Swift Crypto는 Swift의 공식적인 암호화 라이브러리입니다. Swift Crypto는 Swift CryptoNativeAPI 프로젝트의 일부로 개발되었으며, Swift.org의 승인을 받았습니다. Swift Crypto는 시스템에 내장되어 있으며, 최신 Swift 버전과 함께 제공됩니다.

#### 2. 암호화 알고리즘
CryptoSwift는 AES, DES, RSA 등 다양한 암호화 알고리즘을 지원합니다. 이러한 알고리즘은 CryptoSwift의 모듈 내에서 사용할 수 있으며, 강력한 보안 기능을 제공합니다.

Swift Crypto는 CryptoKit을 통해 AES-GCM, ChaChaPoly, HMAC 등 일부 암호화 알고리즘을 지원합니다. CryptoKit은 Apple 플랫폼에서 사용할 수 있는 암호화 기능 세트입니다. Swift Crypto는 모듈 내에서 사용할 수 있는 방대한 암호화 알고리즘 지원을 제공합니다.

#### 3. 플랫폼 호환성
CryptoSwift는 iOS, macOS, watchOS, tvOS 등 다양한 Apple 플랫폼에서 사용할 수 있습니다. 또한, Linux 및 Windows와 같은 일부 다른 플랫폼에서도 사용할 수 있습니다.

Swift Crypto는 주로 Apple 플랫폼에서 사용할 수 있습니다. 특히, iOS 13, macOS 10.15, watchOS 6, tvOS 13 이상의 버전에서 완벽하게 호환됩니다. Linux 및 Windows와 같은 다른 플랫폼에서는 지원되지 않을 수 있습니다.

### 요약
CryptoSwift와 Swift Crypto는 Swift에서 사용할 수 있는 두 가지 유명한 암호화 라이브러리입니다. CryptoSwift는 오랫동안 개발되어 왔으며, 다양한 플랫폼에서 사용할 수 있습니다. Swift Crypto는 Swift의 공식적인 암호화 라이브러리로, 최신 Swift 버전과 함께 제공됩니다. 두 라이브러리는 암호화 알고리즘의 지원 및 플랫폼 호환성 측면에서 차이가 있습니다.

참고 자료:
- [CryptoSwift GitHub 페이지](https://github.com/krzyzanowskim/CryptoSwift)
- [Swift Crypto GitHub 페이지](https://github.com/apple/swift-crypto)