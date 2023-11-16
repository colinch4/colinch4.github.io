---
layout: post
title: "[swift] Firebase Functions를 사용하여 Swift 앱의 서버리스 아키텍처 구축"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

[Firebase Functions](https://firebase.google.com/docs/functions)는 서버리스 백엔드를 구축하기 위한 Google Cloud의 기능을 활용한 서비스입니다. Swift 앱에서 Firebase Functions를 사용하면 클라이언트 측에서 서버리스 아키텍처를 구축하여 데이터 처리, 비즈니스 로직 실행 등의 작업을 수행할 수 있습니다.

## Firebase Functions 설정

1. Firebase 프로젝트를 생성하고 Firebase 콘솔로 이동합니다.

2. Functions 섹션으로 이동하여 Firebase Functions를 활성화합니다. 

3. `functions` 폴더를 생성한 후 해당 폴더에서 터미널을 열고 `firebase init` 명령을 입력합니다. 기본 설정으로 설정 파일(`.firebaserc`, `firebase.json`)이 생성됩니다.

4. `functions` 폴더 안에 `index.js` 파일을 생성하고 Firebase Functions의 로직을 작성합니다.

## Firebase Functions에 Swift 코드 추가하기

1. Firebase Functions에서 Swift 코드를 실행하려면 Firebase Functions을 TypeScript로 작성하고 Firebase SDK를 활용하여 Swift 코드를 호출하는 방식으로 구성해야 합니다.

2. `functions` 폴더 안에 Swift 파일을 생성하고 Firebase Functions와의 인터페이스를 구현합니다. 예를 들어, `MyFunctions.swift` 파일에 `MyFunctions` 클래스를 작성합니다.

3. `MyFunctions` 클래스 안에 Firebase Functions에서 호출될 때 실행되는 메서드를 구현합니다.

```swift
import Foundation
import FirebaseFunctions
import Firebase

class MyFunctions {
    let functions = Functions.functions()

    func myFunction(data: [String: Any], completion: @escaping (String?, Error?) -> Void) {
        functions.httpsCallable("myFunction").call(data) { (result, error) in
            if let error = error {
                completion(nil, error)
                return
            }
            
            guard let result = result?.data as? [String: Any],
                  let message = result["message"] as? String else {
                completion(nil, nil)
                return
            }
            
            completion(message, nil)
        }
    }
}
```

4. `index.js` 파일에 `myFunction`을 호출하는 함수를 작성합니다.

```javascript
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

exports.myFunction = functions.https.onCall(async (data, context) => {
    // Swift 코드와 상호 작용할 수 있는 로직을 작성합니다.
    const message = `Hello, ${data.name}!`;

    return {
        message: message
    };
});
```

5. Firebase Functions를 배포합니다. 터미널에서 `firebase deploy --only functions` 명령을 실행하여 Firebase Functions를 배포합니다.

## Swift 앱에서 Firebase Functions 사용하기

1. Swift 앱에서 Firebase Functions를 사용하기 위해서는 Firebase SDK를 설치해야 합니다. `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'Firebase/Functions'
```

2. `AppDelegate.swift` 파일에 Firebase를 초기화합니다.

```swift
import Firebase

// ...

class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        FirebaseApp.configure()
        return true
    }

    // ...
}
```

3. Swift 코드에서 Firebase Functions를 사용하여 서버로부터 데이터를 가져올 수 있습니다.

```swift
let myFunctions = MyFunctions()

myFunctions.myFunction(data: ["name": "John"]) { (message, error) in
    if let error = error {
        print("Error: \(error)")
        return
    }
    
    if let message = message {
        print("Message: \(message)")
    }
}
```

Firebase Functions를 사용하여 Swift 앱의 서버리스 아키텍처를 구축하는 방법에 대해 알아보았습니다. Firebase Functions를 활용하면 클라이언트 측에서 간편하게 서버 기능을 실행할 수 있으며, 더 유연하고 확장 가능한 앱을 개발할 수 있습니다.