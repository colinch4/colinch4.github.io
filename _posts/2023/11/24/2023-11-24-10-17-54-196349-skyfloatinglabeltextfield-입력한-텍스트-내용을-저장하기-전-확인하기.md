---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용을 저장하기 전 확인하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 텍스트 입력을 처리하는데 도움이 되는 라이브러리입니다. 이 라이브러리를 사용하여 입력된 텍스트를 저장하기 전에 사용자에게 확인을 요청할 수 있습니다. 이번 블로그 포스트에서는 SkyFloatingLabelTextField 입력한 텍스트 내용을 저장하기 전에 사용자에게 확인하는 방법을 알아보겠습니다.

## 1. 확인 다이얼로그 추가하기

SkyFloatingLabelTextField의 내용을 저장하기 전에 사용자에게 확인 다이얼로그를 추가해야 합니다. 이를 위해 UIAlertController를 사용할 수 있습니다. 아래는 UIAlertController를 사용하여 확인 다이얼로그를 추가하는 예제 코드입니다.

```swift
let alertController = UIAlertController(title: "저장하시겠습니까?", message: nil, preferredStyle: .alert)
        
let cancelAction = UIAlertAction(title: "취소", style: .cancel, handler: nil)
alertController.addAction(cancelAction)

let saveAction = UIAlertAction(title: "저장", style: .default) { (action) in
    // 텍스트 저장 로직 구현
}
alertController.addAction(saveAction)

present(alertController, animated: true, completion: nil)
```

위 코드에서는 "저장하시겠습니까?"라는 메시지를 가진 확인 다이얼로그를 생성하고, 취소와 저장 버튼을 추가합니다. 저장 버튼을 누를 경우, 텍스트를 저장하는 로직을 구현하면 됩니다.

## 2. SkyFloatingLabelTextField와 확인 다이얼로그 연동하기

이제 SkyFloatingLabelTextField와 확인 다이얼로그를 연동하여 사용자에게 저장 여부를 확인할 수 있습니다. 아래는 SkyFloatingLabelTextField의 내용을 저장하기 전에 확인 다이얼로그를 표시하는 예제 코드입니다.

```swift
@IBAction func saveButtonTapped(_ sender: Any) {
    guard let text = textField.text, !text.isEmpty else {
        // 텍스트 필드가 비어있을 경우에는 저장하지 않고 종료
        return
    }

    let alertController = UIAlertController(title: "저장하시겠습니까?", message: nil, preferredStyle: .alert)
    
    let cancelAction = UIAlertAction(title: "취소", style: .cancel, handler: nil)
    alertController.addAction(cancelAction)

    let saveAction = UIAlertAction(title: "저장", style: .default) { (action) in
        self.saveText(text)
    }
    alertController.addAction(saveAction)

    present(alertController, animated: true, completion: nil)
}

func saveText(_ text: String) {
    // 텍스트 저장 로직 구현
    print("텍스트 저장: \(text)")
}
```

위 코드에서는 "저장하시겠습니까?"라는 메시지를 가진 확인 다이얼로그를 생성하고, 저장 버튼을 누를 경우 `saveText` 메소드를 호출하여 텍스트를 저장합니다. 취소 버튼을 누르거나 확인 다이얼로그 이외의 영역을 터치할 경우 저장하지 않고 종료됩니다.

이제 SkyFloatingLabelTextField 입력한 텍스트 내용을 저장하기 전에 사용자에게 확인하는 기능을 구현할 수 있습니다. 텍스트 저장 전에 사용자의 의견을 묻고 싶을 때 위의 코드를 참고해보세요.

## 참고 자료
- [SkyFloatingLabelTextField GitHub 레포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UIAlertController - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uialertcontroller)