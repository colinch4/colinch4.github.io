---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용 이메일 주소로 보내기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift의 SkyFloatingLabelTextField를 사용하여 입력한 텍스트를 이메일 주소로 보내는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextField 소개
SkyFloatingLabelTextField는 유연한 사용자 입력 및 미리 보기 기능을 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 텍스트 필드에 레이블과 플레이스홀더를 통합할 수 있으며, 사용자가 입력한 내용을 쉽게 얻을 수 있습니다.

## 이메일 주소로 보내기 기능 구현
1. 프로젝트에 SkyFloatingLabelTextField 라이브러리를 추가합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가합니다:
   ```
   pod 'SkyFloatingLabelTextField'
   ```
   이후 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

2. 이메일 주소를 입력할 수 있는 SkyFloatingLabelTextField를 인터페이스 빌더 또는 코드로 생성합니다.

3. 텍스트를 입력하고 이메일 전송 버튼을 누르면 입력된 텍스트를 이메일 주소로 보내는 기능을 구현합니다. 아래는 기본적인 구현 방법입니다.
   ```swift
    import MessageUI

    class ViewController: UIViewController, MFMailComposeViewControllerDelegate {

        @IBOutlet weak var emailTextField: SkyFloatingLabelTextField!

        override func viewDidLoad() {
            super.viewDidLoad()
        }

        @IBAction func sendEmailButtonTapped(_ sender: UIButton) {
            guard MFMailComposeViewController.canSendMail() else {
                // 이 기기에서 이메일을 보낼 수 없는 상황 처리
                return
            }

            let mailComposer = MFMailComposeViewController()
            mailComposer.mailComposeDelegate = self

            mailComposer.setToRecipients([emailTextField.text!])
            mailComposer.setSubject("이메일 제목")
            mailComposer.setMessageBody("이메일 내용", isHTML: false)

            present(mailComposer, animated: true, completion: nil)
        }

        func mailComposeController(_ controller: MFMailComposeViewController, didFinishWith result: MFMailComposeResult, error: Error?) {
            controller.dismiss(animated: true, completion: nil)
        }

    }
   ```
   
4. `sendEmailButtonTapped` 메소드는 `MFMailComposeViewController`를 사용하여 이메일을 보내는 함수입니다. 사용자의 이메일 주소를 가져와 메일 수신자로 설정하고, 제목과 내용을 설정합니다. 이후 `present` 메소드를 사용하여 메일 작성 화면을 표시합니다.

5. `MFMailComposeViewControllerDelegate` 프로토콜을 채택하여 이메일 작성이 완료됐을 때 액션을 처리하는 메소드들을 구현합니다. `mailComposeController(_:didFinishWith:error:)` 메소드를 사용하여 메일 작성 화면을 닫습니다.

이제 SkyFloatingLabelTextField를 사용하여 입력한 텍스트 내용을 이메일 주소로 보낼 수 있는 기능을 구현할 수 있습니다. 많은 사용자들이 더 편리하게 입력할 수 있게 도와줄 것입니다.

## 참고 자료
- [SkyFloatingLabelTextField Github](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [Apple 공식 문서 - MFMailComposeViewController](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)