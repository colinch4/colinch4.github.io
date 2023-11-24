---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용 검색하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자로부터 입력받는 텍스트를 보여주는 데 사용되는 UITextField의 하위 클래스입니다. 이를 사용하여 텍스트 필드에 입력한 내용을 검색하는 것은 매우 간단합니다.

먼저, SkyFloatingLabelTextField 인스턴스를 만들고 적절한 프로퍼티를 설정합니다. 예를 들어, 다음과 같이 검색 버튼을 눌렀을 때 입력한 텍스트를 출력하는 예제를 살펴볼 수 있습니다.

```swift
import SkyFloatingLabelTextField

// SkyFloatingLabelTextField 인스턴스 생성
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))

// 필요한 설정을 적용 (예를 들어, 플레이스홀더 텍스트, 색깔, 폰트 등)
textField.placeholder = "검색어를 입력하세요"
textField.textColor = .black
textField.font = UIFont.systemFont(ofSize: 14)

// 검색 버튼을 눌렀을 때 호출되는 메소드
@objc func searchButtonTapped() {
    guard let searchText = textField.text else {
        return
    }
    
    print("검색어: \(searchText)")
}
```

위의 예제에서는 SkyFloatingLabelTextField 인스턴스를 생성하고, 필요한 설정을 적용한 후, 검색 버튼을 눌렀을 때 해당 텍스트 필드의 text 속성을 사용하여 검색어를 가져온 뒤 출력합니다.

이제 검색 버튼을 사용하여 텍스트 필드에 입력한 내용을 검색할 수 있습니다. 이를 활용하여 원하는 기능을 개발할 수 있을 것입니다.

참고 자료:
- [SkyFloatingLabelTextField GitHub 레포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)