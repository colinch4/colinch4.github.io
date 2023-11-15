---
layout: post
title: "[swift] Swift Moya와 ObjectMapper의 설치 및 설정 방법"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 포스트에서는 Swift에서 Moya와 ObjectMapper를 사용하여 네트워킹과 객체 매핑을 하는 방법에 대해 알아보겠습니다. Moya는 Alamofire를 기반으로 한 네트워킹 라이브러리이며, ObjectMapper는 JSON과 객체 간의 매핑을 쉽게 처리해주는 라이브러리입니다.

## Moya 설치하기

Moya를 프로젝트에 설치하기위해 다음의 단계를 따릅니다.

1. 프로젝트의 Podfile을 열고 다음 라인을 추가합니다.

   ```
   pod 'Moya'
   ```

2. 터미널을 열고 프로젝트의 Podfile이 있는 디렉토리로 이동합니다.

3. 다음 명령어를 실행하여 CocoaPods를 통해 Moya를 설치합니다.

   ```
   pod install
   ```

4. 설치가 완료되면 `.xcworkspace` 파일을 열어 프로젝트를 실행합니다.

## ObjectMapper 설치하기

ObjectMapper를 프로젝트에 설치하기위해 다음의 단계를 따릅니다.

1. 프로젝트의 Podfile을 열고 다음 라인을 추가합니다.

   ```
   pod 'ObjectMapper'
   ```

2. 터미널을 열고 프로젝트의 Podfile이 있는 디렉토리로 이동합니다.

3. 다음 명령어를 실행하여 CocoaPods를 통해 ObjectMapper를 설치합니다.

   ```
   pod install
   ```

4. 설치가 완료되면 `.xcworkspace` 파일을 열어 프로젝트를 실행합니다.

## Moya와 ObjectMapper 사용하기

이제 Moya와 ObjectMapper가 설치되었으므로 사용해보겠습니다. 

1. 먼저, 모델 클래스를 생성합니다. 예를 들어, User라는 모델 클래스를 생성하겠습니다.

   ```swift
   import ObjectMapper

   class User: Mappable {
       var id: Int?
       var name: String?

       required init?(map: Map) {}

       func mapping(map: Map) {
           id <- map["id"]
           name <- map["name"]
       }
   }
   ```

2. MoyaProvider를 설정합니다. 예를 들어, GitHub API를 사용하여 사용자 정보를 가져오는 코드를 작성하겠습니다.

   ```swift
   import Moya

   enum GitHubAPI {
       case getUser(username: String)
   }

   extension GitHubAPI: TargetType {
       var baseURL: URL {
           return URL(string: "https://api.github.com")!
       }

       var path: String {
           switch self {
           case .getUser(let username):
               return "/users/\(username)"
           }
       }

       var method: Moya.Method {
           return .get
       }

       var task: Task {
           return .requestPlain
       }

       var headers: [String: String]? {
           return nil
       }
   }

   let provider = MoyaProvider<GitHubAPI>()
   ```

3. 사용자 정보 요청 코드를 작성합니다.

   ```swift
   provider.request(.getUser(username: "JohnDoe")) { result in
       switch result {
       case .success(let response):
           do {
               let user = try response.mapObject(User.self)
               print(user.name)
           } catch {
               print(error)
           }
       case .failure(let error):
           print(error)
       }
   }
   ```

위의 예제는 사용자 이름이 "JohnDoe"인 사용자의 정보를 요청하고 받아온 데이터를 User 모델로 매핑하여 사용자의 이름을 출력하는 간단한 예제입니다.

이제 위의 코드를 사용하여 Moya와 ObjectMapper를 사용하여 네트워킹과 객체 매핑을 할 수 있습니다.

## 참고 자료

- Moya GitHub 페이지: [https://github.com/Moya/Moya](https://github.com/Moya/Moya)
- ObjectMapper GitHub 페이지: [https://github.com/tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)