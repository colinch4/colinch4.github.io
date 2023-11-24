---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용 암호화하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 자주 사용되는 사용자 인터페이스 컴포넌트입니다. 이 튜토리얼에서는 SkyFloatingLabelTextField에 입력한 텍스트 내용을 암호화하는 방법에 대해 알아보겠습니다.

## Step 1: CryptoSwift 라이브러리 추가하기

보안 관련 작업을 수행하기 위해 CryptoSwift 라이브러리를 사용할 것입니다. 따라서 Cocoapods를 사용하여 프로젝트에 해당 라이브러리를 추가해야 합니다. Podfile에 다음 라인을 추가하세요:

```ruby
pod 'CryptoSwift'
```

그리고 터미널을 열어 해당 폴더로 이동한 후 다음 명령어를 실행하세요:

```
pod install
```

## Step 2: 암호화 메소드 추가하기

SkyFloatingLabelTextField로부터 입력된 텍스트를 암호화하기 위해 암호화 메소드를 추가해야 합니다. 이 메소드는 CryptoSwift 라이브러리를 사용하여 입력된 텍스트를 암호화합니다.

```swift
import CryptoSwift

extension String {
    func aesEncrypt(key: String, iv: String) throws -> String {
        let data = Data(self.utf8)
        let encrypted = try AES(key: key, iv: iv, padding: .pkcs7).encrypt(data)
        return encrypted.base64EncodedString()
    }
}
```

이 확장(extension)을 String 클래스에 추가하여 입력된 텍스트 문자열을 암호화하는 aesEncrypt 메소드를 정의합니다. 이 메소드는 AES-256 암호화 알고리즘을 사용하며, key와 iv(초기화 벡터) 파라미터를 받아 텍스트를 암호화한 후 Base64로 인코딩하여 반환합니다.

## Step 3: SkyFloatingLabelTextField에 암호화 적용하기

SkyFloatingLabelTextField에 암호화를 적용하기 위해 UITextFieldDelegate를 구현한 후 텍스트 입력이 완료되었을 때 암호화 메소드를 호출하도록 합니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }

    // TextField 입력 완료 시 호출
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()

        if let text = textField.text {
            do {
                let encryptedText = try text.aesEncrypt(key: "mySecretKey12345678", iv: "myInitializationVector")
                print("Encrypted Text: \(encryptedText)")
            } catch {
                print("Encryption failed: \(error)")
            }
        }

        return true
    }
}
```

ViewController 클래스에 UITextFieldDelegate를 구현한 후 textFieldShouldReturn 메소드를 오버라이드하여 암호화 코드를 추가해줍니다. 이 예제에서는 텍스트 필드를 누르면 키보드가 사라지고, 입력된 텍스트를 암호화한 후 결과를 콘솔에 출력합니다. 이때 사용된 key와 iv 값은 본인의 암호화 설정에 맞게 변경해야 합니다.

## 결론

이제 SkyFloatingLabelTextField에 입력한 텍스트를 암호화하는 방법을 알아보았습니다. CryptoSwift 라이브러리를 사용하여 간단히 암호화 작업을 수행할 수 있습니다. 이를 통해 암호화된 데이터를 안전하게 다룰 수 있고, 사용자의 개인 정보를 보호할 수 있습니다.

더 자세한 내용은 [CryptoSwift 라이브러리 GitHub 페이지](https://github.com/krzyzanowskim/CryptoSwift)를 참고하세요.