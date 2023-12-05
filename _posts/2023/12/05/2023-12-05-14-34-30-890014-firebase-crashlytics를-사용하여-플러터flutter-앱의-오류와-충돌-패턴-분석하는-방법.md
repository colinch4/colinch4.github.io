---
layout: post
title: "[flutter] Firebase Crashlytics를 사용하여 플러터(Flutter) 앱의 오류와 충돌 패턴 분석하는 방법"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

앱 개발은 종종 사용자들이 마주칠 수 있는 다양한 문제들을 포함합니다. 이러한 문제들을 효과적으로 파악하고 해결하기 위해서는 앱의 오류와 충돌 패턴을 분석할 수 있는 도구가 필요합니다. Firebase Crashlytics는 이러한 도구 중 하나로, 앱의 오류와 충돌 데이터를 수집하여 개발자가 문제를 신속하게 파악하고 수정할 수 있도록 도와줍니다.

## Firebase Crashlytics 설정하기

먼저, Firebase Console에서 프로젝트를 생성하고 Crashlytics를 활성화해야 합니다. 이를 위해서는 Firebase SDK를 프로젝트에 추가해야 합니다.

1. Firebase Console에 로그인하고 프로젝트를 생성합니다.
2. 생성한 프로젝트로 이동한 다음, "프로젝트 설정"으로 이동합니다.
3. "프로젝트 설정"에서 Firebase SDK 설정을 클릭합니다.
4. "안드로이드 앱 추가" 버튼을 클릭하여 앱을 등록합니다. 필요한 정보를 입력하고, 패키지 이름을 입력한 후에는 Firebase용 google-services.json 파일을 다운로드합니다.
5. "iOS 앱 추가" 버튼을 클릭하여 앱을 등록합니다. 필요한 정보를 입력하고, GoogleService-Info.plist 파일을 다운로드합니다.

Firebase SDK를 추가하고 앱을 등록한 후에는 Crashlytics를 활성화해야 합니다.

### 안드로이드 설정

1. Android 프로젝트의 `build.gradle` 파일의 dependencies 블록에 다음 코드를 추가합니다:

```groovy
classpath 'com.google.firebase:firebase-crashlytics-gradle:2.5.2'
```

2. Android 모듈의 `build.gradle` 파일의 최상위에 다음 코드를 추가하고, 파일의 맨 아래에 다음 코드를 추가합니다:

```groovy
apply plugin: 'com.google.firebase.crashlytics'

dependencies {
  implementation 'com.google.firebase:firebase-crashlytics:17.5.1'
}
```

### iOS 설정

1. iOS 프로젝트의 `Podfile`에 다음 코드를 추가합니다:

```ruby
pod 'Firebase/Crashlytics'
```

2. 터미널을 열고 프로젝트의 루트 디렉토리로 이동한 다음, 다음 명령어를 실행합니다:

```bash
pod install
```

Firebase Crashlytics를 사용하기 위한 설정은 이제 완료되었습니다.

## 앱에서 오류 및 충돌 데이터 수집하기

Firebase Crashlytics를 사용하여 앱의 오류와 충돌 데이터를 수집하려면 몇 가지 추가 작업을 해야 합니다.

### 안드로이드 설정

1. App 클래스를 만들거나 기존 App 클래스를 열고, 다음 코드를 추가합니다:

```kotlin
import com.google.firebase.crashlytics.FirebaseCrashlytics

class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        FirebaseCrashlytics.getInstance().setCrashlyticsCollectionEnabled(true)
    }
}
```

2. `AndroidManifest.xml`에서 App 클래스를 사용하도록 수정합니다:

```xml
<application
    android:name=".MyApp"
    ...
```

### iOS 설정

1. `AppDelegate.swift` 파일을 열고, 다음 코드를 추가합니다:

```swift
import FirebaseCrashlytics

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    Crashlytics.crashlytics().setCrashlyticsCollectionEnabled(true)
    return true
}
```

Firebase Crashlytics를 사용하여 앱의 오류와 충돌 데이터를 수집하기 위한 설정은 이제 완료되었습니다.

## 오류 및 충돌 데이터 사용하기

Firebase Crashlytics를 통해 수집한 오류와 충돌 데이터는 Firebase Console의 Crashlytics 섹션에서 확인할 수 있습니다. 여기에서 데이터를 분석하고 문제를 신속하게 파악하여 수정할 수 있습니다.

Firebase Console에서는 다양한 필터링 및 정렬 옵션을 제공하여 원하는 데이터를 선택적으로 확인할 수 있습니다. 또한, 각 오류 및 충돌 항목에 대한 세부 정보와 스택 추적을 확인할 수 있습니다.

Firebase Crashlytics는 앱의 오류와 충돌 분석에 매우 유용한 도구입니다. 이를 통해 앱의 안정성과 사용자 경험을 개선할 수 있습니다. Firebase Crashlytics를 통해 앱의 오류와 충돌을 파악하고 신속하게 수정하여 사용자들에게 원활한 앱 경험을 제공하세요.

참고: [Firebase Crashlytics 문서](https://firebase.google.com/docs/crashlytics)