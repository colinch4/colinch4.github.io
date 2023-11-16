---
layout: post
title: "[swift] Firebase Remote Config를 활용한 Swift 앱의 다양한 환경 설정 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Remote Config는 앱의 다양한 설정을 실시간으로 업데이트하고 변경할 수 있는 기능을 제공합니다. 이를 이용하면 앱의 환경 설정을 수정하지 않고도, 사용자 경험을 개선하고 새로운 기능을 테스트하는 등의 작업을 수행할 수 있습니다.

이번 포스트에서는 Swift 앱에서 Firebase Remote Config를 어떻게 구현하는지 알아보겠습니다.

## Step 1: Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 새로운 프로젝트를 생성합니다.
2. iOS 앱을 추가하고, Bundle ID를 입력합니다.
3. 생성된 GoogleService-Info.plist 파일을 다운로드하고, 프로젝트에 추가합니다.

## Step 2: Firebase SDK 설치

1. Cocoapods를 이용하여 Firebase SDK를 설치합니다. Podfile에 아래와 같이 Firebase/Core와 Firebase/RemoteConfig를 추가합니다.

```swift
pod 'Firebase/Core'
pod 'Firebase/RemoteConfig'
```

2. `pod install` 명령어를 실행하여 Firebase SDK를 프로젝트에 추가합니다.

## Step 3: Remote Config 설정

1. AppDelegate.swift 파일에서 아래 코드를 추가하여 Firebase를 초기화합니다.

```swift
import Firebase

...
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

2. RemoteConfigManager.swift 파일을 생성하고, 아래 코드를 추가합니다.

```swift
import FirebaseRemoteConfig

class RemoteConfigManager {
    static let sharedInstance = RemoteConfigManager()
    let remoteConfig = RemoteConfig.remoteConfig()

    func fetchRemoteConfig() {
        let settings = RemoteConfigSettings()
        settings.minimumFetchInterval = 3600
        remoteConfig.configSettings = settings

        // 기본 설정 값 정의
        let defaultValues: [String: Any] = [
            "welcome_message": "Welcome to our app!",
            "button_color": "#FF0000"
        ]
        remoteConfig.setDefaults(defaultValues)

        remoteConfig.fetch { [weak self] (status, error) in
            if let error = error {
                print("Error fetching remote config: \(error)")
            } else {
                print("Remote config fetched successfully")
                self?.remoteConfig.activate { (error) in
                    if let error = error {
                        print("Error activating remote config: \(error)")
                    }
                }
            }
        }
    }

    func getStringValue(forKey key: String) -> String {
        return remoteConfig[key].stringValue ?? ""
    }
}
```

3. 앱을 실행할 때 Remote Config를 가져오도록 AppDelegate.swift 파일에 코드를 추가합니다.

```swift
...
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    RemoteConfigManager.sharedInstance.fetchRemoteConfig()
    return true
}
```

## Step 4: Remote Config 사용

Remote Config에서 설정한 값을 앱에서 사용하는 방법은 다양합니다. 예를 들어, `welcome_message`와 같은 문자열 값을 사용하고 싶다면 아래와 같이 호출할 수 있습니다.

```swift
let welcomeMessage = RemoteConfigManager.sharedInstance.getStringValue(forKey: "welcome_message")
print(welcomeMessage)
```

앱 사용자의 설정 또는 환경에 따라 `button_color`와 같은 값을 사용하여 버튼의 배경색을 동적으로 변경할 수도 있습니다.

```swift
let buttonColor = RemoteConfigManager.sharedInstance.getStringValue(forKey: "button_color")
button.backgroundColor = UIColor(hex: buttonColor)
```

## 결론

Firebase Remote Config를 활용하면 앱의 환경 설정을 실시간으로 변경하고, 다양한 기능을 테스트하는 등의 작업을 간편하게 수행할 수 있습니다. Firebase의 다른 기능과 조합하여 사용한다면, 사용자 경험을 개선하고 앱의 성능을 최적화하는데 도움이 될 것입니다. 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/remote-config/)를 참고하시기 바랍니다.