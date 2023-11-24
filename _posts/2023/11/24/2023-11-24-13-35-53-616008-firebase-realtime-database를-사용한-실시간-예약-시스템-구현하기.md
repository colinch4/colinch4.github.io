---
layout: post
title: "[swift] Firebase Realtime Database를 사용한 실시간 예약 시스템 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Realtime Database는 실시간 데이터를 저장하고 동기화할 수 있는 클라우드 호스팅 데이터베이스입니다. 이번 예시에서는 Firebase Realtime Database를 사용하여 실시간 예약 시스템을 구현하는 방법에 대해 설명하겠습니다.

## 목차
1. Firebase 프로젝트 생성
2. Firebase Realtime Database 설정
3. 예약 데이터 모델링
4. 예약 시스템 구현하기
   * 예약 생성
   * 예약 조회
   * 예약 삭제
5. 마무리

## 1. Firebase 프로젝트 생성
Firebase Realtime Database를 사용하기 위해선 먼저 Firebase 프로젝트를 생성해야 합니다. Firebase 콘솔에 로그인한 후 새 프로젝트를 만들고, 프로젝트 설정에서 앱을 추가합니다. iOS 앱을 추가하고, 패키지 이름을 입력한 후 `구성 파일 추가` 버튼을 클릭해 GoogleService-Info.plist 파일을 다운로드합니다.

## 2. Firebase Realtime Database 설정
Firebase Realtime Database를 사용하려면 먼저 앱과 데이터베이스를 연결해야 합니다. 다운로드 받은 GoogleService-Info.plist 파일을 Xcode 프로젝트에 추가한 후, AppDelegate.swift 파일에 아래 코드를 추가합니다.

```swift
import Firebase

// ...

FirebaseApp.configure()
```

이렇게 하면 앱이 시작될 때 Firebase가 초기화되고, Realtime Database에 연결됩니다.

## 3. 예약 데이터 모델링
예약 데이터를 저장할 데이터 모델을 만들어보겠습니다. 예약을 나타내는 Reservation 클래스를 생성하고, 필요한 속성들을 추가합니다.

```swift
class Reservation {
    var id: String?
    var username: String
    var date: String
    var time: String
    
    init(username: String, date: String, time: String) {
        self.username = username
        self.date = date
        self.time = time
    }
}
```

## 4. 예약 시스템 구현하기
### 예약 생성
먼저 예약을 생성하는 기능을 구현해보겠습니다. 사용자가 예약 정보를 입력하고 `예약하기` 버튼을 누르면, 데이터베이스에 예약 정보를 저장합니다.

```swift
func createReservation(username: String, date: String, time: String) {
    let reservationRef = Database.database().reference().child("reservations").childByAutoId()
    let reservation = Reservation(username: username, date: date, time: time)
    
    reservationRef.setValue(reservation.toDictionary())
}
```

### 예약 조회
다음으로 예약을 조회하는 기능을 구현해보겠습니다. 데이터베이스에 저장된 모든 예약 정보를 가져와서 화면에 표시합니다.

```swift
func fetchReservations(completion: @escaping ([Reservation]) -> Void) {
    let reservationsRef = Database.database().reference().child("reservations")
    
    reservationsRef.observe(.value) { snapshot in
        var reservations: [Reservation] = []
        
        for child in snapshot.children {
            if let snapshot = child as? DataSnapshot, let reservation = Reservation(snapshot: snapshot) {
                reservations.append(reservation)
            }
        }
        
        completion(reservations)
    }
}
```

### 예약 삭제
마지막으로 예약을 삭제하는 기능을 구현해보겠습니다. 사용자가 예약을 선택하고 `삭제하기` 버튼을 누르면, 해당 예약 정보를 데이터베이스에서 삭제합니다.

```swift
func deleteReservation(reservation: Reservation) {
    guard let reservationId = reservation.id else { return }
    
    let reservationRef = Database.database().reference().child("reservations").child(reservationId)
    reservationRef.removeValue()
}
```

## 5. 마무리
이제 Firebase Realtime Database를 사용하여 실시간 예약 시스템을 구현하는 방법을 알아보았습니다. Firebase의 강력한 실시간 동기화 기능을 활용하여 사용자들이 실시간으로 예약 정보를 공유하고 업데이트할 수 있습니다.

Firebase 공식 문서에서 더 많은 정보와 자세한 예제를 확인할 수 있으니, 참고하기 바랍니다.

**참고 자료:**
- [Firebase Realtime Database 공식 문서](https://firebase.google.com/docs/database)
- [Firebase Realtime Database iOS 시작 가이드](https://firebase.google.com/docs/database/ios/start)