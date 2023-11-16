---
layout: post
title: "[swift] Firebase Cloud Functions와 Swift의 연동 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Cloud Functions는 Firebase 프로젝트를 위한 서버리스 백엔드 플랫폼으로, 클라이언트 앱의 로직을 서버에서 실행할 수 있도록 해줍니다. 이번 글에서는 Firebase Cloud Functions를 Swift 언어와 연동하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정
Firebase Console에서 Firebase 프로젝트를 생성하고, Cloud Functions를 활성화해야 합니다. Firebase CLI를 사용하여 프로젝트를 초기화하고, Cloud Functions를 설정하는 절차를 거칩니다.

```shell
$ npm install -g firebase-tools
$ firebase login
$ firebase init functions
```

## 2. Swift 프로젝트 생성
Firebase 프로젝트와 연동할 Swift 프로젝트를 생성해야 합니다. Xcode를 사용하여 iOS 앱 프로젝트를 생성하고, 기본적인 설정을 완료합니다.

## 3. Cloud Functions 생성
Firebase Console에서 Cloud Functions를 생성합니다. 이때, Cloud Functions에 필요한 코드를 작성하는 폴더가 자동으로 생성됩니다.

```shell
$ cd functions
$ npm install firebase-admin firebase-functions
```

## 4. Swift 프로젝트에 Firebase SDK 추가
Swift 프로젝트에 Firebase SDK를 추가하여 Firebase Cloud Functions와 통신할 수 있도록 합니다. Cocoapods를 사용하여 Firebase SDK를 설치합니다.

```swift
import FirebaseFunctions

...

let functions = Functions.functions()
functions.httpsCallable("myFunctionName").call(["param1": "value1"]) { (result, error) in
  // Handle the result or error
}
```

## 5. Cloud Functions 코드 작성
Cloud Functions 폴더 내에 작성된 코드를 수정하여 Swift와 연동할 수 있도록 합니다. Firebase Functions SDK를 사용하여 클라이언트 앱의 요청을 처리하고, Swift 코드와 연동하는 작업을 수행합니다.

```javascript
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

exports.myFunctionName = functions.https.onCall((data, context) => {
  const param1 = data.param1;

  // Perform some logic in Swift
  const result = ... // Call Swift code here

  return result;
});
```

## 6. Swift 코드 작성
Swift 프로젝트 내에 Cloud Functions와 연동할 Swift 코드를 작성합니다. Firebase Cloud Functions SDK를 사용하여 Cloud Functions와 통신하고, 결과를 처리하는 작업을 수행합니다.

```swift
import Foundation
import FirebaseFunctions

...

let functions = Functions.functions()
functions.useFunctionsEmulator(origin: "http://localhost:5001")
functions.httpsCallable("myFunctionName").call(["param1": "value1"]) { (result, error) in
  // Handle the result or error
}
```

이제 Firebase Cloud Functions와 Swift를 연동하는 방법을 알아보았습니다. Firebase Cloud Functions를 사용하면 서버를 구축하고 유지 관리하는 복잡한 작업 없이도 클라이언트 앱의 로직을 실행할 수 있습니다.

참고 자료:
- [Firebase Cloud Functions 공식 문서](https://firebase.google.com/docs/functions)
- [Firebase Functions SDK 공식 문서](https://firebase.google.com/docs/functions/callable)