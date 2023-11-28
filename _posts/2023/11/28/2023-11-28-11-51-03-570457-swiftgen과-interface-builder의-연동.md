---
layout: post
title: "[swift] SwiftGen과 Interface Builder의 연동"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

인터페이스 빌더는 iOS 앱을 만들 때 사용되는 시각적인 도구입니다. 인터페이스를 만들고 구성하는 데 도움이 되는 기능을 제공합니다. SwiftGen은 리소스 파일을 자동으로 생성해주는 도구로, 코드에서 리소스에 접근하는 것을 더 쉽게 만들어줍니다. 이번 포스트에서는 SwiftGen과 인터페이스 빌더를 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. SwiftGen 설치하기

먼저 SwiftGen을 설치해야 합니다. SwiftGen은 CocoaPods, Carthage, Swift Package Manager 중 하나를 사용하여 설치할 수 있습니다. 여기서는 CocoaPods를 사용하는 방법을 설명하겠습니다.

```
pod 'SwiftGen', '~> 6.1'
```

Podfile에 위의 코드를 추가한 뒤, 터미널에서 `pod install` 명령어를 실행하여 SwiftGen을 설치합니다.

## 2. SwiftGen 설정하기

SwiftGen을 설치한 후에는 프로젝트 설정을 해야 합니다. 터미널에서 프로젝트 디렉토리로 이동한 뒤, 다음 명령어를 실행합니다.

```
swiftgen config init
```

이 명령어는 SwiftGen의 설정 파일을 생성해줍니다. 생성된 설정 파일(`swiftgen.yml`)을 열어서 다음과 같이 수정합니다.

```yaml
strings:
  inputs: Resources/Localizable.strings
  outputs:
    - templateName: structured-swift5
      output: Sources/Generated/Strings.swift
```

이렇게 수정한 후에는 터미널에서 다음 명령어를 실행하여 SwiftGen을 실행합니다.

```
swiftgen strings
```

SwiftGen은 `swiftgen.yml` 파일에 설정된 경로에서 리소스 파일을 찾아서, 해당 리소스 파일을 기반으로 코드를 생성합니다.

## 3. Interface Builder에서 SwiftGen 사용하기

SwiftGen을 설정했으니 이제 인터페이스 빌더에서 SwiftGen을 사용해보겠습니다. 먼저 인터페이스 빌더에서 사용할 리소스 파일을 추가합니다. 예를 들어, `Localizable.strings` 파일을 추가한 뒤, 해당 파일을 열어서 문자열을 정의합니다.

인터페이스 빌더에서는 이제 문자열을 참조하여 레이블, 버튼 등에 적용할 수 있습니다. 이 때 SwiftGen을 사용하면 간단하게 리소스에 접근할 수 있습니다.

예를 들어, 인터페이스 빌더의 레이블 텍스트 속성을 다음과 같이 수정합니다.

```
L10n.helloWorld
```

여기서 `L10n`은 SwiftGen이 생성한 문자열 리소스 구조체를 의미합니다. `helloWorld`는 리소스 파일에서 정의한 문자열 키입니다.

이렇게 수정한 뒤 앱을 실행하면, 인터페이스 빌더에서 정의한 문자열이 레이블에 표시됩니다.

## 4. 참고 자료

- SwiftGen 공식 홈페이지: [https://github.com/SwiftGen/SwiftGen](https://github.com/SwiftGen/SwiftGen)
- 인터페이스 빌더 가이드: [https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/InterfaceBuilder.html](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/InterfaceBuilder.html)

위의 링크에서 더 자세한 내용을 확인할 수 있으니 참고해주세요.