---
layout: post
title: "[swift] Swift에서 Firebase Dynamic Links를 활용한 링크 공유 기능 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Dynamic Links는 앱 간에 링크를 공유하고 사용자를 원하는 대상 화면으로 이동시킬 수 있는 강력한 도구입니다. 이 기능을 Swift 앱에서 구현하는 방법을 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성합니다.
2. iOS 앱을 추가하고, 앱 번들 ID를 입력합니다.
3. `GoogleService-Info.plist` 파일을 다운로드하여 Xcode 프로젝트에 추가합니다.

## Firebase Dynamic Links 설정

1. Firebase 콘솔에서 Dynamic Links를 선택합니다.
2. "도메인 설정" 탭에서 도메인을 추가하고, 도메인 구성을 완료합니다.
3. "동적 링크" 탭에서 링크 생성 옵션을 구성합니다. 예를 들어, 대상 앱의 오픈 링크를 설정할 수 있습니다.
4. 생성된 Dynamic Link에서 "URL 미리보기"를 통해 링크가 제대로 작동하는지 확인합니다.

## Swift 앱에서 Dynamic Link 처리

1. Firebase SDK를 프로젝트에 설치합니다. (CocoaPods, Carthage, 수동 설치 등)
2. `AppDelegate` 파일을 열고, `didFinishLaunchingWithOptions` 메소드에서 Firebase를 초기화합니다. 코드 예시:

```swift
import Firebase

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    // 나머지 초기화 코드
    return true
}
```

3. Dynamic Link 처리를 위해 `AppDelegate` 파일에 다음 메소드를 추가합니다:

```swift
import FirebaseDynamicLinks

func handleIncomingDynamicLink(_ dynamicLink: DynamicLink) {
    // 동적 링크 처리 로직 구현
    // 예: 링크에서 원하는 정보를 추출하여 화면 전환 등을 처리
}

func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard let incomingURL = userActivity.webpageURL else {
        return false
    }
    
    let dynamicLink = DynamicLinks.dynamicLinks().dynamicLink(fromCustomSchemeURL: incomingURL)
    handleIncomingDynamicLink(dynamicLink)
    
    return true
}

func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let dynamicLink = DynamicLinks.dynamicLinks().dynamicLink(fromCustomSchemeURL: url)
    handleIncomingDynamicLink(dynamicLink)

    return true
}
```

4. 링크를 생성하여 공유하는 부분에서 Firebase Dynamic Links SDK를 사용하여 링크를 생성합니다. 예를 들어:

```swift
import FirebaseDynamicLinks

// 링크 생성
func generateDynamicLink() {
    guard let link = URL(string: "https://yourapp.page.link") else { return }
    
    let dynamicLinksDomain = "yourapp.page.link"
    let linkBuilder = DynamicLinkComponents(link: link, domain: dynamicLinksDomain)
    
    // 링크에 대한 추가 구성 가능
    
    guard let longDynamicLink = linkBuilder.url else { return }
    DynamicLinkComponents.shortenURL(longDynamicLink) { (shortURL, warnings, error) in
        if let error = error {
            // 에러 처리
        } else if let shortURL = shortURL {
            // 단축된 링크를 사용하여 공유
        }
    }
}
```

## 결론

Swift 앱에서 Firebase Dynamic Links를 활용하여 링크 공유 기능을 구현하는 방법에 대해 알아보았습니다. Firebase의 강력한 기능을 활용하여 사용자의 환경에 따라 동적으로 링크를 처리할 수 있습니다. Firebase 문서와 예제 코드를 참고하여 원하는 기능을 구현해보세요.

## 참고 자료

- Firebase 공식 문서: https://firebase.google.com/docs/dynamic-links
- Firebase Dynamic Links 설정 가이드: https://firebase.google.com/docs/dynamic-links/create-manually
- Firebase iOS SDK 설치 가이드: https://firebase.google.com/docs/ios/setup