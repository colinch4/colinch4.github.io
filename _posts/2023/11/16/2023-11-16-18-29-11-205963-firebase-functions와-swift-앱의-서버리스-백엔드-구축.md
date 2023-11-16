---
layout: post
title: "[swift] Firebase Functions와 Swift 앱의 서버리스 백엔드 구축"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

서버리스 아키텍처는 최근에 많은 앱 개발자들 사이에서 인기를 끌고 있습니다. 이 아키텍처를 사용하면 클라우드 기반 함수를 사용하여 앱의 백엔드 로직을 구현할 수 있습니다. Firebase Functions는 JavaScript를 사용하여 클라우드 기반 함수를 만들고 실행할 수 있는 기능을 제공합니다. 그러나 Swift로 작성된 앱의 경우에도 Firebase Functions를 활용하여 서버리스 백엔드를 구축할 수 있습니다.

## Firebase Functions 설정

Firebase를 사용하려면 먼저 프로젝트에 Firebase를 추가해야 합니다. Firebase 콘솔에서 새 프로젝트를 생성하고 Firebase SDK를 프로젝트에 추가하세요.

Firebase Functions를 사용하려면 Firebase CLI를 설치해야 합니다. 설치를 완료한 후, 터미널에서 프로젝트 폴더로 이동하여 다음 명령을 실행하여 Firebase Functions 초기화를 수행합니다.

```
firebase init functions
```

이 명령은 Firebase Functions 프로젝트를 설정하는 데 필요한 파일과 디렉토리를 자동으로 생성합니다.

## Swift 앱과의 통신

Firebase Functions는 RESTful API 방식을 통해 클라이언트 앱과 통신합니다. Swift 앱에서 Firebase Functions와 통신하려면 `URLSession`을 사용하여 해당 함수의 URL에 HTTP 요청을 보내면 됩니다. 다음은 Firebase Functions로 Get 요청을 보내는 Swift 코드의 예입니다.

```swift
guard let url = URL(string: "https://us-central1-your-project-name.cloudfunctions.net/your-function-name") else { return }

URLSession.shared.dataTask(with: url) { (data, response, error) in
    if let error = error {
        print("Error: \(error.localizedDescription)")
        return
    }
    
    if let data = data {
        let json = try? JSONSerialization.jsonObject(with: data, options: [])
        print("Response: \(json ?? "")")
    }
}.resume()
```

## Firebase Functions에서 Swift 사용하기

Swift로 Firebase Functions를 작성하려면 `functions` 폴더에서 `index.js` 파일을 생성하고, 해당 파일 안에 Swift 함수를 작성하세요. 다음 예제는 인자로 전달된 이름에 대한 인사말을 반환하는 간단한 Firebase Function의 Swift 코드입니다.

```swift
import Foundation
import FirebaseFunctions

let functions = Functions.functions(region: "us-central1")

@objc func sayHello(_ req: HTTPRequest, _ res: HTTPResponse) throws -> HTTPResponse {
    guard let name = req.queryParameters["name"], !name.isEmpty else {
        return res.status(.badRequest).send("No name provided!")
    }
    
    let message = "Hello, \(name)!"
    return res.send(message)
}

functions.https.onRequest { (request, response) in
    try? sayHello(request, response)
}
```

이 Swift 함수에서 `functions` 객체를 사용하여 Firebase Functions의 `https.onRequest` 메서드를 호출하여 함수를 등록합니다. 이 함수는 클라이언트 요청을 수신할 때마다 실행됩니다.

## 결론

Firebase Functions와 Swift를 사용하면 앱의 서버리스 백엔드를 쉽게 구축할 수 있습니다. Firebase Functions를 사용하여 클라우드 기반 함수를 작성하고 Swift 앱과의 통신을 설정하는 방법을 알아보았습니다. 이를 통해 앱의 백엔드 로직을 서버리스 아키텍처로 구축할 수 있으며, 효율적이고 확장 가능한 앱을 개발할 수 있습니다.

## 참고 자료
- [Firebase Documentation](https://firebase.google.com/docs/functions/)
- [Swift Package Index](https://swiftpackageindex.com/Package/firebase/firebase-functions)