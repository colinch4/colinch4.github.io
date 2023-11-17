---
layout: post
title: "[swift] Swift PMAlertController 소개"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개

PMAlertController는 Swift에서 사용할 수 있는 iOS 팝업 뷰 컨트롤러입니다. 이 라이브러리는 UIAlertController를 더 유연하고 사용하기 쉽게 만들어주며, 다양한 사용자 정의 옵션을 제공합니다.

## 주요 기능

1. 다양한 스타일의 팝업 창 제공
2. 제목, 메시지, 이미지 및 사용자 정의 뷰를 포함한 컨텐츠를 추가할 수 있음
3. 버튼 및 액션 처리 추가 가능
4. 애니메이션 및 전환 효과 적용 가능
5. 커스텀 스타일 및 테마 지원

## 설치 및 사용법

PMAlertController는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음과 같이 추가한 후 `pod install` 명령어를 실행하세요.

```swift
pod 'PMAlertController'
```

사용법은 아래와 같습니다.

```swift
import PMAlertController

let alertVC = PMAlertController(title: "제목", description: "메시지", image: UIImage(named: "alertIcon"), style: .alert)

alertVC.addAction(PMAlertAction(title: "확인", style: .default, action: {
    // 확인 버튼을 눌렀을 때 수행할 액션
}))

alertVC.addAction(PMAlertAction(title: "취소", style: .cancel, action: {
    // 취소 버튼을 눌렀을 때 수행할 액션
}))

self.present(alertVC, animated: true, completion: nil)
```

## 예시

```swift
let alertVC = PMAlertController(title: "알림",
                                description: "회원가입을 축하합니다!",
                                image: UIImage(named: "successImage"),
                                style: .alert)


alertVC.addAction(PMAlertAction(title: "확인", style: .default, action: {
    // 확인 버튼을 눌렀을 때 수행할 액션
}))

self.present(alertVC, animated: true, completion: nil)
```

## 참고 자료

- [PMAlertController GitHub 저장소](https://github.com/Codeido/PMAlertController)
- [Cocoapods 공식 웹사이트](https://cocoapods.org/)