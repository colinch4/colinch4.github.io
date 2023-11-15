---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 활용한 RESTful API 통신 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 프로그래밍 언어를 사용하여 RESTful API와 통신하는 방법을 알아보겠습니다. 특히, Moya와 ObjectMapper라는 두 가지 라이브러리를 사용하여 API 요청과 응답 데이터의 매핑을 쉽게 처리하는 방법을 소개합니다.

## Moya 소개

Moya는 Alamofire를 기반으로한 네트워크 추상화 라이브러리입니다. RESTful API 통신을 위한 간단한 인터페이스를 제공하며, 네트워크 관련 코드를 간결하게 작성할 수 있습니다. Moya는 Target, Provider, Endpoint 등의 개념을 사용하여 API 요청을 정의하고 수행합니다.

Moya의 설치 방법은 아래와 같습니다. 

```
pod 'Moya'
```

## ObjectMapper 소개

ObjectMapper는 Swift에서 JSON 데이터를 객체로 변환하기 위한 라이브러리입니다. JSON 데이터와 Swift 객체 간의 매핑을 지원하며, JSON의 키와 객체의 프로퍼티를 매핑하여 객체를 생성합니다. 이를 통해 JSON 데이터를 직접 다루는 번거로움 없이 객체를 다룰 수 있습니다.

ObjectMapper의 설치 방법은 아래와 같습니다.

```
pod 'ObjectMapper'
```

## 예제 코드

이제 실제로 Moya와 ObjectMapper을 사용하여 RESTful API 통신을 하는 예제 코드를 살펴보겠습니다. 이 예제에서는 영화 정보를 제공하는 RESTful API와 통신하여 영화의 제목과 개봉일을 출력하는 기능을 구현합니다.

```swift
import Moya
import ObjectMapper

struct Movie: Mappable {
    var title: String?
    var releaseDate: String?
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        title <- map["title"]
        releaseDate <- map["release_date"]
    }
}

// API Provider 생성
let provider = MoyaProvider<MovieAPI>()

// 영화 정보를 요청하여 출력하는 함수
func printMovieInfo() {
    provider.request(.getMovieInfo) { result in
        switch result {
        case .success(let response):
            do {
                let movie = try response.mapObject(Movie.self)
                print("영화 제목: \(movie.title ?? "")")
                print("개봉일: \(movie.releaseDate ?? "")")
            } catch {
                print("Error: \(error.localizedDescription)")
            }
            
        case .failure(let error):
            print("Error: \(error.localizedDescription)")
        }
    }
}

// API 요청
printMovieInfo()
```

위 코드에서 `Movie` 구조체는 ObjectMapper의 Mappable 프로토콜을 구현하여 JSON 데이터와의 매핑을 정의합니다. `mapping` 메서드에서 JSON의 키와 객체의 프로퍼티를 매핑하고, `title`과 `releaseDate` 프로퍼티를 매핑합니다.

`printMovieInfo` 함수에서는 MoyaProvider로부터 API 응답을 받아와 ObjectMapper를 사용하여 영화 정보를 매핑한 후 출력합니다.

## 마무리

이번에는 Swift의 Moya와 ObjectMapper를 사용하여 RESTful API와 통신하는 예제 코드를 살펴보았습니다. Moya를 사용하면 API 요청과 응답 처리가 편리해지며, ObjectMapper를 사용하면 JSON 데이터를 객체로 간편하게 매핑할 수 있습니다. 이러한 두 라이브러리를 함께 사용하면 API 통신을 보다 쉽고 효율적으로 구현할 수 있습니다.

- [Moya GitHub 저장소](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)