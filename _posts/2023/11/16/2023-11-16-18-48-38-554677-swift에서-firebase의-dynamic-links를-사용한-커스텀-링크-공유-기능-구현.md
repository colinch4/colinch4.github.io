---
layout: post
title: "[swift] Swift에서 Firebase의 Dynamic Links를 사용한 커스텀 링크 공유 기능 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase는 Google에서 제공하는 개발 플랫폼으로, 앱 개발에 필요한 다양한 기능을 제공합니다. 그 중 Dynamic Links는 앱 내에서 커스텀 링크를 생성하고 공유할 수 있는 기능입니다. 이번 글에서는 Swift에서 Firebase의 Dynamic Links를 사용하여 커스텀 링크 공유 기능을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 로그인하고 프로젝트를 만듭니다.
2. 생성한 프로젝트에 iOS 앱을 추가합니다.
3. Firebase 콘솔에서 "Dynamic Links" 탭으로 이동하고, "시작하기" 버튼을 눌러 주요 설정을 완료합니다.
4. 앱에 Firebase SDK를 추가하고, `GoogleService-Info.plist` 파일을 다운로드하여 프로젝트에 추가합니다.

## Dynamic Links 생성

Firebase의 Dynamic Links는 커스텀 링크를 생성하고, 그 링크를 공유하여 다른 사용자를 중복 없이 앱 내의 특정 화면으로 이동시킬 수 있습니다. 아래는 Dynamic Links를 생성하는 간단한 예제 코드입니다.

```swift
import FirebaseDynamicLinks

func createDynamicLink() {
    guard let link = URL(string: "https://yourapp.com/invite?referralCode=12345") else { return }
    
    let dynamicLinksDomain = "yourapp.page.link"
    let linkBuilder = DynamicLinkComponents(link: link, domain: dynamicLinksDomain)
    
    linkBuilder.iOSParameters = DynamicLinkIOSParameters(bundleID: "com.yourapp.bundle")
    linkBuilder.androidParameters = DynamicLinkAndroidParameters(packageName: "com.yourapp.package")
    linkBuilder.socialMetaTagParameters = DynamicLinkSocialMetaTagParameters()
    linkBuilder.navigationInfoParameters = DynamicLinkNavigationInfoParameters()
    
    guard let longDynamicLink = linkBuilder.url else { return }
    
    DynamicLinkComponents.shortenURL(longDynamicLink) { (shortURL, warnings, error) in
        if let error = error {
            print("Error creating Dynamic Link: \(error.localizedDescription)")
            return
        }
        
        if let shortURL = shortURL {
            print("Generated Dynamic Link: \(shortURL.absoluteString)")
        }
        
        if let warnings = warnings {
            for warning in warnings {
                print("Dynamic Link Warning: \(warning)")
            }
        }
    }
}
```

이 예제 코드에서 "https://yourapp.com/invite?referralCode=12345"은 커스텀 링크의 기본 URL입니다. iOS 및 Android 매개 변수를 설정하고, 필요에 따라 소셜 메타 태그 및 네비게이션 정보 매개 변수를 추가로 설정할 수 있습니다. 생성한 Dynamic Link를 Firebase SDK의 `shortenURL` 메서드를 사용하여 짧은 URL로 변환시킬 수 있습니다.

## Dynamic Links를 통한 앱 내 화면 이동

앱 내에서 생성한 Dynamic Link를 다른 사용자와 공유하고, 해당 링크를 클릭하면 앱 내의 특정 화면으로 이동할 수 있습니다. 아래는 앱을 실행시키고 Dynamic Link를 처리하여 특정 화면으로 이동하는 예제입니다.

```swift
import FirebaseDynamicLinks

func handleDynamicLink() {
    DynamicLinks.performDiagnostics(completion: nil)
    
    guard let incomingURL = URL(string: "https://yourapp.page.link/abcde") else { return }
    
    DynamicLinks.dynamicLinks().handleUniversalLink(incomingURL) { (dynamicLink, error) in
        if let error = error {
            print("Error handling Dynamic Link: \(error.localizedDescription)")
            return
        }
        
        if let dynamicLink = dynamicLink {
            // 처리할 링크가 있는 경우
            if let url = dynamicLink.url {
                print("Received Dynamic Link: \(url.absoluteString)")
                // 링크 처리 및 화면 이동 로직 추가
                // ...
            }
        }
    }
}
```

이 예제 코드에서는 `handleUniversalLink` 메서드를 사용하여 앱이 실행될 때 동적 링크를 처리합니다. 링크에는 해당 링크로 이동할 때 필요한 모든 정보가 포함되어 있으므로 링크의 정보를 이용하여 앱 내에서 필요한 작업을 수행하고 특정 화면으로 이동시킬 수 있습니다.

## 결론

Swift에서 Firebase의 Dynamic Links를 사용하여 커스텀 링크 공유 기능을 구현하는 방법에 대해 알아보았습니다. Firebase의 Dynamic Links를 통해 앱 사용자 간에 링크를 공유하고, 앱 내의 특정 화면으로 이동할 수 있습니다. Firebase의 Dynamic Links API를 더 자세히 알아보고 싶다면 Firebase 공식 문서를 참조하시기 바랍니다.

**참고 자료:**
- [Firebase 공식 문서 - Dynamic Links](https://firebase.google.com/docs/dynamic-links?hl=ko)