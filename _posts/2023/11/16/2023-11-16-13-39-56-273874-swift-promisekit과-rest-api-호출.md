---
layout: post
title: "[swift] Swift PromiseKit과 REST API 호출"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PromiseKit은 Swift에서 비동기 작업을 더 쉽게 처리하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 REST API 호출과 같은 비동기 작업을 보다 간결하게 처리할 수 있습니다. 

이번 글에서는 PromiseKit을 사용하여 Swift에서 REST API를 호출하는 방법에 대해 알아보겠습니다.

## 1. PromiseKit 설치하기

PromiseKit은 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음과 같이 추가한 후, `pod install` 명령어를 실행하여 설치합니다.

```
pod 'PromiseKit'
```

## 2. REST API 호출하기

REST API를 호출하기 위해 기본적으로 URLSession을 사용합니다. 우선, URLSession을 Promise와 함께 사용할 수 있도록 확장하는 작업을 진행합니다. 

```swift
import PromiseKit
import Foundation

extension URLSession {
    func dataTask(with url: URL) -> Promise<Data> {
        return Promise<Data> { seal in
            let task = self.dataTask(with: url) { (data, response, error) in
                if let error = error {
                    seal.reject(error)
                } else if let data = data {
                    seal.fulfill(data)
                }
            }
            task.resume()
        }
    }
}
```

위의 확장 코드를 작성한 후, REST API 호출 시 URLSession 인스턴스의 `dataTask(with:)` 함수를 사용하면 PromiseObj<Data>를 반환하는 것을 확인할 수 있습니다.

## 3. REST API 호출 예제

이제 실제로 REST API를 호출하는 예제를 살펴보겠습니다. 예제로는 [JSONPlaceholder](https://jsonplaceholder.typicode.com/)라는 가상의 REST API를 사용하겠습니다.

```swift
import Foundation
import PromiseKit

struct Post: Codable {
    let id: Int
    let title: String
    let body: String
}

func fetchPosts() -> Promise<[Post]> {
    guard let url = URL(string: "https://jsonplaceholder.typicode.com/posts") else {
        return Promise(error: NSError(domain: "Invalid URL", code: 0))
    }
    
    return URLSession.shared.dataTask(with: url).map { data in
        try JSONDecoder().decode([Post].self, from: data)
    }
}

fetchPosts().done { posts in
    for post in posts {
        print("\(post.id): \(post.title)")
    }
}.catch { error in
    print("Error: \(error)")
}
```

위의 코드는 JSONPlaceholder API로부터 포스트 목록을 가져와서 출력하는 예제입니다. `fetchPosts()` 함수는 데이터를 가져오는 비동기 작업을 Promise로 처리하고 있습니다. 데이터를 성공적으로 가져온 후에는 포스트 목록을 순회하며 포스트의 제목을 출력하고, 데이터 가져오는 과정에서 오류가 발생한 경우에는 에러를 출력합니다.

## 4. 결론

Swift PromiseKit을 사용하면 REST API 호출과 같은 비동기 작업을 더 간결하고 효율적으로 처리할 수 있습니다. 이를 활용하여 애플리케이션 개발 시 비동기 작업을 보다 쉽게 처리할 수 있습니다.