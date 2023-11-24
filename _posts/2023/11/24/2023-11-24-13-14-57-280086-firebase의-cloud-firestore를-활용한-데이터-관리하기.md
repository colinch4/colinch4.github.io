---
layout: post
title: "[swift] Firebase의 Cloud Firestore를 활용한 데이터 관리하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase는 Google의 개발 플랫폼으로, 다양한 클라우드 관리 기능을 제공합니다. 그 중에서도 Cloud Firestore는 NoSQL 데이터베이스로 구조적인 데이터 관리를 위한 솔루션입니다. 이번 글에서는 Swift 언어를 사용하여 Firebase의 Cloud Firestore를 활용하여 데이터를 관리하는 방법에 대해 알아보겠습니다.

## 전제 조건

Firebase를 사용하기 위해서는 먼저 Firebase 프로젝트를 생성하고, CocoaPods를 사용하여 Firebase SDK를 프로젝트에 추가해야 합니다. 또한 Firebase의 Authentication 기능을 사용하기 위해서는 Firebase Authentication을 활성화해야 합니다.

## Firestore 설정

먼저 Firestore를 사용하기 위해 Firebase 프로젝트에 Firestore를 추가해야 합니다. Firebase 콘솔에서 프로젝트를 선택한 후, 'Firestore 데이터베이스 만들기' 버튼을 클릭하여 Firestore를 활성화합니다.

## 데이터 추가하기

Firestore에 데이터를 추가하기 위해서는 '컬렉션(Collection)'과 '문서(Document)' 개념을 사용합니다. 컬렉션은 문서의 그룹으로 생각할 수 있고, 각 문서는 컬렉션 내에 저장됩니다.

```swift
import Firebase

let db = Firestore.firestore()

// 예제: users 컬렉션에 새로운 문서 추가하기
db.collection("users").document("user1").setData([
    "name": "John Doe",
    "email": "johndoe@example.com"
]) { err in
    if let err = err {
        print("Error adding document: \(err)")
    } else {
        print("Document added successfully")
    }
}
```

위의 예제 코드에서는 'users'라는 컬렉션에 'user1'이라는 문서를 추가하는 코드입니다. 문서 내에는 'name'과 'email' 필드가 포함되어 있습니다.

## 데이터 가져오기

Firestore에서 데이터를 가져올 때는 `addSnapshotListener` 메서드나 `getDocuments` 메서드를 사용합니다. `addSnapshotListener` 메서드를 사용하면 실시간으로 데이터 변경 사항을 감지할 수 있는 리스너를 등록할 수 있습니다.

```swift
// 예제: users 컬렉션의 모든 문서 가져오기
db.collection("users").getDocuments() { (querySnapshot, err) in
    if let err = err {
        print("Error getting documents: \(err)")
    } else {
        for document in querySnapshot!.documents {
            let data = document.data()
            print("\(document.documentID) => \(data)")
        }
    }
}
```

위의 예제 코드에서는 'users' 컬렉션의 모든 문서를 가져와서 각 문서의 데이터를 출력하는 코드입니다.

## 데이터 갱신하기

Firestore에서 데이터를 갱신하기 위해서는 `updateData` 메서드를 사용합니다.

```swift
// 예제: users 컬렉션의 user1 문서의 name 필드를 갱신하기
let user1Ref = db.collection("users").document("user1")

user1Ref.updateData([
    "name": "Jane Smith"
]) { err in
    if let err = err {
        print("Error updating document: \(err)")
    } else {
        print("Document updated successfully")
    }
}
```

위의 예제 코드에서는 'users' 컬렉션의 'user1' 문서의 'name' 필드를 'Jane Smith'로 갱신하는 코드입니다.

## 데이터 삭제하기

Firestore에서 데이터를 삭제하기 위해서는 `delete` 메서드를 사용합니다.

```swift
// 예제: users 컬렉션의 user1 문서 삭제하기
let user1Ref = db.collection("users").document("user1")

user1Ref.delete() { err in
    if let err = err {
        print("Error deleting document: \(err)")
    } else {
        print("Document deleted successfully")
    }
}
```

위의 예제 코드에서는 'users' 컬렉션의 'user1' 문서를 삭제하는 코드입니다.

## 결론

Firebase의 Cloud Firestore를 활용하면 클라우드 기반의 NoSQL 데이터베이스를 사용하여 애플리케이션의 데이터를 손쉽게 관리할 수 있습니다. 이번 글에서는 Firestore를 시작하기 위한 기본적인 데이터 추가, 가져오기, 갱신, 삭제 등의 작업을 알아보았습니다. 추가적으로 Firestore의 다양한 기능을 통해 데이터를 조작하고, 데이터베이스 규모를 확장하는 방법도 학습해보시기 바랍니다.

## References

- [Firebase Documentation](https://firebase.google.com/docs/firestore/)
- [Firebase Firestore GitHub](https://github.com/firebase/firebase-ios-sdk)