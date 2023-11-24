---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트를 파일로 저장하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어로 개발된 SkyFloatingLabelTextField를 이용하여 사용자가 입력한 텍스트를 파일로 저장하는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextField란?
SkyFloatingLabelTextField는 텍스트 입력 필드 시각적인 효과를 추가하여 더 쉽게 사용자 입력을 받을 수 있도록 도와주는 라이브러리입니다. 텍스트 필드 위에 라벨이 부유하도록 표시되며, 사용자가 값을 입력하면 라벨이 위로 올라가는 효과를 제공합니다.

## 프로젝트 설정
먼저, SkyFloatingLabelTextField를 프로젝트에 추가해야 합니다. Cocoapods를 사용하고 있다면 `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

SkyFloatingLabelTextField를 다운로드하고 설치한 후 `.xcworkspace` 파일을 열어주세요.

## 사용자 입력 저장하기
SkyFloatingLabelTextField에서 사용자가 입력한 텍스트를 파일로 저장하는 방법은 다음과 같습니다.

1. 먼저, 입력 값을 받을 SkyFloatingLabelTextField를 인터페이스 빌더에서 추가합니다.
2. 해당 텍스트 필드와 연결된 IBOutlet을 만들어 줍니다.

```swift
@IBOutlet weak var textField: SkyFloatingLabelTextField!
```

3. 사용자 입력 값을 저장할 함수를 작성합니다.

```swift
func saveTextToFile() {
    guard let text = textField.text else {
        return
    }

    let fileURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0].appendingPathComponent("input.txt")

    do {
        try text.write(to: fileURL, atomically: true, encoding: .utf8)
        print("Text saved to file successfully.")
    } catch {
        print("Failed to save text to file:", error.localizedDescription)
    }
}
```

위의 코드는 입력 값을 `input.txt` 파일에 저장합니다. 파일 경로는 문서 디렉터리에 위치하며, 파일이 없을 경우 자동으로 생성됩니다. 만약 이미 파일이 존재한다면 덮어쓰기가 됩니다.

4. 사용자 입력 값을 저장하는 버튼의 IBAction 메서드에서 `saveTextToFile()` 함수를 호출합니다.

```swift
@IBAction func saveButtonTapped(_ sender: UIButton) {
    saveTextToFile()
}
```

이제 사용자가 입력한 텍스트는 `input.txt` 파일에 저장됩니다.

## 결론
이번 글에서는 Swift 언어의 SkyFloatingLabelTextField를 이용하여 사용자가 입력한 텍스트를 파일로 저장하는 방법을 알아보았습니다. 사용자가 입력한 값을 파일로 저장함으로써 데이터를 영구적으로 보존하거나 나중에 불러와 사용할 수 있습니다.