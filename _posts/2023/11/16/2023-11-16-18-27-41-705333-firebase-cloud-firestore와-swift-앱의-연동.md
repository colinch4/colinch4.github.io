---
layout: post
title: "[swift] Firebase Cloud Firestore와 Swift 앱의 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase는 Google에서 개발한 모바일 및 웹 애플리케이션을 위한 플랫폼입니다. Firebase의 다양한 기능 중 하나인 Cloud Firestore는 실시간 데이터베이스로서, Swift 앱과의 연동을 통해 데이터를 쉽게 저장 및 동기화할 수 있습니다.

## Cloud Firestore 설정하기
1. Firebase 콘솔에 로그인하고, 프로젝트를 생성합니다.
2. Firebase 프로젝트를 설정한 후, "Cloud Firestore"를 선택하고 "활성화" 버튼을 클릭합니다.
3. "데이터베이스" 탭으로 이동하여 "네트워크 위치" 설정을 확인합니다. 

## Swift 프로젝트에 Firebase 추가하기
1. CocoaPods를 사용하여 Firebase를 프로젝트에 추가합니다. `Podfile`에 아래와 같이 Firebase 및 Firestore 팟을 추가합니다.

```swift
platform :ios, '10.0'
use_frameworks!

target '<Your Target Name>' do
  pod 'FirebaseFirestore'
end
```

2. 터미널에서 `pod install` 명령어를 실행하여 Firebase를 설치합니다.

## Swift 앱과 Cloud Firestore 연동하기
1. Swift 프로젝트에서 `FirebaseFirestore`를 import 합니다.

```swift
import FirebaseFirestore
```

2. Firestore 인스턴스를 초기화합니다.

```swift
let db = Firestore.firestore()
```

3. Firestore에 데이터를 추가하거나 읽어올 수 있습니다. 아래는 Firestore에 데이터를 추가하는 예제입니다.

```swift
// Firestore 컬렉션 'users'에 사용자 정보 추가
db.collection("users").addDocument(data: [
    "name": "John Doe",
    "age": 25,
    "email": "johndoe@example.com"
]) { err in
    if let err = err {
        print("Error adding document: \(err)")
    } else {
        print("Document added with ID: \(ref!.documentID)")
    }
}
```

4. 데이터를 읽어오는 예제입니다.

```swift
// Firestore 컬렉션 'users'에서 모든 문서 가져오기
db.collection("users").getDocuments { (snapshot, err) in
    if let err = err {
        print("Error getting documents: \(err)")
    } else {    
        for document in snapshot!.documents {
            print("\(document.documentID) => \(document.data())")
        }
    }
}
```

이렇게 Swift 앱과 Firebase Cloud Firestore를 연동하여 데이터를 저장하고 읽어올 수 있습니다.

더 많은 Firebase Cloud Firestore 기능에 대해 알아보려면 [Firebase 공식 문서](https://firebase.google.com/docs/firestore)를 참조하세요.