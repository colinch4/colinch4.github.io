---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 스크롤 가능하도록 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어로 개발된 SkyFloatingLabelTextField 라이브러리를 사용하여, 입력한 텍스트를 스크롤할 수 있도록 설정하는 방법을 알아보겠습니다.

SkyFloatingLabelTextField는 유연하고 쉽게 사용할 수 있는 사용자 정의 가능한 텍스트 필드 라이브러리입니다. 기본적으로는 입력한 텍스트가 텍스트 필드의 크기를 초과하는 경우에도 자동으로 스크롤되지 않습니다. 하지만 몇 가지 간단한 설정으로 입력한 텍스트를 스크롤할 수 있도록 변경할 수 있습니다.

## 1. SkyFloatingLabelTextField 라이브러리 설치하기

SkyFloatingLabelTextField 라이브러리를 사용하기 위해 먼저 프로젝트에 라이브러리를 설치해야 합니다. 가장 흔하게 사용하는 방법은 CocoaPods를 사용하는 것입니다. Podfile에 다음과 같이 라이브러리를 추가합니다.

```swift
pod 'SkyFloatingLabelTextField'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
pod install
```

## 2. 텍스트 필드 생성하기

SkyFloatingLabelTextField를 사용하기 위해 먼저 텍스트 필드를 생성해야 합니다. 다음과 같이 코드를 작성하여 텍스트 필드를 생성합니다.

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
textField.placeholder = "Enter your text"
```

## 3. 스크롤 가능하도록 설정하기

이제 생성한 텍스트 필드를 스크롤 가능하도록 설정해야 합니다. SkyFloatingLabelTextField는 UIScrollView를 상속받기 때문에, 스크롤 가능하도록 설정하는 방법은 일반적인 UIScrollView와 동일합니다. 다음과 같이 코드를 작성하여 텍스트 필드를 스크롤 가능하도록 설정할 수 있습니다.

```swift
textField.isScrollEnabled = true
```

## 4. 추가 옵션 설정하기

SkyFloatingLabelTextField는 많은 사용자 정의 가능한 옵션을 제공합니다. 스크롤 가능한 텍스트 필드를 더욱 유지보수 가능하게 만들기 위해 다음과 같은 추가 옵션을 설정할 수 있습니다.

- 스크롤 바 표시/숨김 설정

```swift
textField.showsVerticalScrollIndicator = true
```

- 스크롤 범위 설정

```swift
textField.contentInset = UIEdgeInsets(top: 0, left: 0, bottom: 10, right: 0)
```

## 5. 결과 확인하기

이제 설정한 옵션을 적용하고 텍스트 필드를 사용해보세요. 입력한 텍스트가 텍스트 필드의 크기를 초과하면 스크롤 바가 표시되고, 스크롤하여 나머지 텍스트를 확인할 수 있게 됩니다.

이렇게 SkyFloatingLabelTextField를 사용하여 입력한 텍스트를 스크롤 가능하도록 설정하는 방법에 대해 알아보았습니다. 본인의 프로젝트에 적용하여 텍스트 필드를 더 유연하게 사용해보세요!

## 참고 자료
- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)