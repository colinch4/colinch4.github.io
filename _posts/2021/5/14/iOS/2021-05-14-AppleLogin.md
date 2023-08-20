---
layout: post
title: "[iOS] 애플 로그인"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

## 애플 로그인
- 애플에서 제공해주는 회원가입 및 로그인 시스템
- 다른 소셜 로그인을 사용하면 무조건 애플 로그인 기능도 있어야한다.
- 애플로그인은 iOS 13 이상에서 사용가능

## 사용법
1. 버튼 생성 방법

```swift
@available(iOS 13.0, *)
private func setAppleLoginButton() {
    let appleLoginButton = ASAuthorizationAppleIDButton()
    appleLoginButton.addTarget(
        self,
        action: #selector(appleLoginBtnTap),
        for: .touchUpInside
    )
    
    self.view.addSubview(appleLoginButton)
    
    // snapkit을 이용하여 constraint 설정
    appleLoginButton.snp.makeConstraints {
        $0.centerX.equalTo(self.view.safeAreaLayoutGuide.snp.centerX)
        $0.top.equalTo(stackView).offset(120)
        $0.width.equalTo(350)
        $0.height.equalTo(50)
    }
}
```
<img width="547" alt="스크린샷 2021-05-07 오전 10 05 54" src="https://user-images.githubusercontent.com/45002556/117383786-875e9580-af1c-11eb-86cc-79fe3b307528.png">

- 위의 사진과 같이 버튼 생성 가능
- ASAuthorizationAppleIDButton를 사용하여 시스템에서 제공해주는 버튼을 불러올 수 있다.
- 버튼의 타겟과 엑션을 지정해준 뒤 view에 추가

<img width="774" alt="스크린샷 2021-05-07 오전 10 07 03" src="https://user-images.githubusercontent.com/45002556/117383791-89c0ef80-af1c-11eb-9dbb-b7df682c0569.png">

- 버튼의 속성을 이용해 여러 디자인의 버튼을 만들 수 있다.

2. 애플 로그인 화면을 호출하고 인증하는 과정
```swift
@available(iOS 13.0, *)
extension AppleLogin: ASAuthorizationControllerDelegate,
                      ASAuthorizationControllerPresentationContextProviding {
    
    // 어떤 화면에서 애플 로그인 화면이 호출될지 지정해주는 메소드
    func presentationAnchor(for controller: ASAuthorizationController) -> ASPresentationAnchor {
        return self.view.window    
    }
    
    public func runAppleLogin() {
        let provider = ASAuthorizationAppleIDProvider()
        provider.getCredentialState(forUserID: UserDefaultsManager.userId) { credentialState, error in
            switch credentialState {
            case .authorized:
                // Apple ID Credential is valid
                loginWithApple()
            case .revoked:
                // Apple ID Credential revoked, handle unlink
            case .notFound:
                // Credential not found, show login UI
                loginWithApple()
            default:
                break
            }
        }
    }
    
    private func loginWithApple() {
        let request = ASAuthorizationAppleIDProvider().createRequest()
        request.requestedScopes = [.fullName, .email]
        let controller = ASAuthorizationController(authorizationRequests: [request])
        controller.delegate = self
        controller.presentationContextProvider = self
        controller.performRequests()
    }

    // 애플 로그인 성공시 호출되는 메소드
    func authorizationController(controller _: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization) {
        
        // 애플에서 제공해주는 정보를 받아서 사용 가능
        guard let credential = authorization.credential as? ASAuthorizationAppleIDCredential else {
            return
        }
        
        let fullName = (credential.fullName?.familyName ?? "") + (credential.fullName?.givenName  ?? "")
        print("FullName: \(fullName)")
        
        print(String(data: credential.identityToken!, encoding: .utf8)!)

    }
    
    // 애플 로그인 에러시 호출되는 메소드
    func authorizationController(controller: ASAuthorizationController, didCompleteWithError error: Error) {
        guard let error = error as? ASAuthorizationError else {return}
        
        switch error.code {
        case .canceled:
            print("Canceled")
        case .unknown:
            print("Unknow")
        case .invalidResponse:
            print("invalid Respone")
        case .notHandled:
            print("Not Handled")
        case .failed:
            print("Failed")
        default:
            print("Default")
        }
    }
}
```
- ASAuthorizationControllerDelegate, ASAuthorizationControllerPresentationContextProviding 이 두가지 메소드를 상속받고 구현해야 한다.

```Swift
let request = ASAuthorizationAppleIDProvider().createRequest()
request.requestedScopes = [.fullName, .email]
let controller = ASAuthorizationController(authorizationRequests: [request])
controller.delegate = self
controller.presentationContextProvider = self
controller.performRequests()
```
- 위 코드를 사용하면 다음과 같이 로그인하는 화면을 호출

<img width="769" alt="스크린샷 2021-05-07 오전 10 08 15" src="https://user-images.githubusercontent.com/45002556/117383793-89c0ef80-af1c-11eb-9ce6-1906f9225f99.png">


3. 프로젝트 설정 추가
- Signing & Capabilities -> + capability -> Sign in with Apple 추가
- 패키지 폴더에 entitlements 파일이 생긴것을 확인

4. 애플 디벨로퍼 사이트에 sign in with apple 기능 추가
