---
layout: post
title: "[swift] SwiftyUserDefaults와 UserDefaults 사이의 차이점은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

UserDefaults는 iOS와 macOS에서 데이터를 영구 저장하기 위해 사용되는 클래스입니다. 이 클래스를 사용하여 앱 설정, 사용자 정보, 기본 데이터 등을 저장할 수 있습니다. 이렇게 저장된 데이터는 앱을 종료하고 다시 실행해도 유지됩니다.

SwiftyUserDefaults는 UserDefaults를 더욱 쉽게 사용할 수 있게 도와주는 라이브러리입니다. UserDefaults는 Objective-C 스타일의 API를 제공하며, SwiftyUserDefaults는 이를 보다 Swift한 문법으로 사용할 수 있도록 도와줍니다. 예를 들어, UserDefaults에서 값을 가져올 때는 `UserDefaults.standard.string(forKey: "key")`와 같은 형태로 사용하지만, SwiftyUserDefaults를 사용하면 `Defaults[key]`와 같이 간단하게 사용할 수 있습니다.

또한, SwiftyUserDefaults는 타입 안전성을 보장합니다. UserDefaults에서 값을 가져올 때는 어떤 타입이든 Any 타입으로 반환되는데, 이 때문에 타입 캐스팅 등의 추가적인 처리가 필요합니다. 하지만 SwiftyUserDefaults를 사용하면 컴파일러가 타입 정보를 알고 있기 때문에 타입캐스팅 없이도 간편하게 값을 사용할 수 있습니다.

사용하고자 하는 UserDefaults 속성을 SwiftyUserDefaults에서 확장해 주어야 합니다. SwiftyUserDefaults는 프로토콜 기반으로 동작하며, 해당 프로토콜을 채택한 프로퍼티를 확장해주는 방식으로 사용합니다. 이렇게 하면 해당 프로퍼티를 사용하여 저장된 값을 쉽게 가져오거나 설정할 수 있습니다.

SwiftyUserDefaults는 UserDefaults를 보다 Swift한 문법과 타입 안정성을 제공하여 개발자들에게 더 편리한 UserDefaults 사용 경험을 제공해줍니다.

참고 문서:
- [SwiftyUserDefaults GitHub Repository](https://github.com/sunshinejr/SwiftyUserDefaults)
- [UserDefaults Apple Documentation](https://developer.apple.com/documentation/foundation/userdefaults)