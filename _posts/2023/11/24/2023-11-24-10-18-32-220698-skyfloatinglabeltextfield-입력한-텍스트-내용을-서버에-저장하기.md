---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용을 서버에 저장하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 개발에서 많이 사용되는 텍스트 필드 컴포넌트 중 하나입니다. 이번에는 SkyFloatingLabelTextField를 활용하여 사용자가 입력한 텍스트를 서버에 저장하는 방법을 알아보겠습니다.

## 1. SkyFloatingLabelTextField 설정하기

먼저, SkyFloatingLabelTextField를 프로젝트에 추가하고 설정해야 합니다. 아래의 예제 코드를 따라해주세요.

```swift
import SkyFloatingLabelTextField

class MyViewController: UIViewController {
    // SkyFloatingLabelTextField 인스턴스 생성
    let textField = SkyFloatingLabelTextField()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 텍스트 필드 속성 설정
        textField.placeholder = "이름"
        textField.title = "이름"
        textField.tintColor = .blue
        textField.selectedTitleColor = .blue
        textField.selectedLineColor = .blue
        
        // 뷰에 텍스트 필드 추가
        view.addSubview(textField)
    }
}
```

위의 코드에서는 SkyFloatingLabelTextField를 생성하고 필요한 속성들을 설정하였습니다. 나머지 설정은 프로젝트 요구 사항에 맞게 변경하면 됩니다.

## 2. 서버로 데이터 전송하기

사용자가 입력한 텍스트를 서버로 전송하는 과정을 구현해보겠습니다. 아래의 예제 코드를 참고해주세요.

```swift
import Alamofire

func saveTextToServer(text: String) {
    let parameters: [String: Any] = [
        "text": text
    ]
    
    Alamofire.request("http://example.com/save", method: .post, parameters: parameters, encoding: JSONEncoding.default)
        .responseJSON { response in
            switch response.result {
            case .success:
                print("텍스트 저장 성공")
            case .failure(let error):
                print("텍스트 저장 실패: \(error.localizedDescription)")
            }
        }
}
```

위의 코드에서는 Alamofire를 사용하여 서버에 POST 요청을 보내고, 사용자가 입력한 텍스트를 `parameters`에 담아 전송합니다. 응답 결과에 따라 성공 또는 실패 메시지를 출력합니다.

## 3. 사용자 입력값 저장하기

입력한 텍스트를 서버로 전송하기 위해서는 사용자가 입력한 값을 임시로 저장해야 합니다. 아래의 예제 코드를 참고해주세요.

```swift
class MyViewController: UIViewController {
    let textField = SkyFloatingLabelTextField()
    
    var userInput: String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 텍스트 필드 속성 설정
        textField.delegate = self
    }
}

extension MyViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        if let text = textField.text, let range = Range(range, in: text) {
            userInput = text.replacingCharacters(in: range, with: string)
        }
        return true
    }
}

extension MyViewController {
    @IBAction func saveButtonTapped() {
        saveTextToServer(text: userInput)
    }
}
```

위의 코드에서는 `userInput`이라는 변수를 사용하여 사용자가 입력한 값을 저장합니다. 텍스트 필드의 delegate 메서드를 활용하여 사용자의 입력값이 바뀔 때마다 `userInput`을 업데이트합니다. 사용자가 저장 버튼을 누를 때, `saveButtonTapped()` 메서드를 호출하여 `userInput`을 서버로 전송합니다.

## 마무리

위의 방법을 따라하면 SkyFloatingLabelTextField를 사용하여 사용자가 입력한 텍스트를 서버에 저장할 수 있습니다. 필요에 따라 코드를 수정하고, 프로젝트에 맞게 적용해보세요.