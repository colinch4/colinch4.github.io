---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 자동 재시도 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper를 함께 사용하여 네트워크 요청과 JSON 매핑을 쉽게 처리할 수 있는 라이브러리입니다. 이번에는 AlamofireObjectMapper를 사용하여 네트워크 요청의 자동 재시도를 처리하는 방법에 대해 알아보겠습니다.

## 자동 재시도란?

네트워크 요청을 보낼 때는 다양한 이유로 실패할 수 있습니다. 서버의 문제, 네트워크 연결의 불안정성 등 여러 가지 이유로 인해 요청이 실패할 수 있습니다. 이때 자동 재시도 기능을 사용하면 요청이 실패했을 때 자동으로 지정된 횟수만큼 재시도를 시도할 수 있습니다.

## AlamofireObjectMapper를 사용한 자동 재시도 처리 방법

1. Alamofire 및 AlamofireObjectMapper를 프로젝트에 추가합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 추가합니다.

~~~
pod 'Alamofire'
pod 'AlamofireObjectMapper'
~~~

2. 네트워크 요청을 보내는 메소드를 작성합니다. 이때 `Alamofire.request` 메소드를 사용하여 요청을 처리하고, `validate` 메소드를 사용하여 응답의 상태 코드를 확인합니다.

~~~swift
import Alamofire
import AlamofireObjectMapper

func sendRequest(completion: @escaping (Result<Model, Error>) -> Void) {
    let url = "https://api.example.com/my-endpoint"
    
    Alamofire
        .request(url)
        .validate()
        .responseObject { (response: DataResponse<Model, AFError>) in
            switch response.result {
            case .success(let model):
                completion(.success(model))
            case .failure(let error):
                completion(.failure(error))
            }
        }
}
~~~

3. 요청이 실패했을 때 재시도를 수행할 수 있도록 메소드를 수정합니다. 예외 처리를 추가로 구현하여 재시도를 시도할 수 있습니다. 다음은 최대 재시도 횟수를 3회로 설정한 예제입니다.

~~~swift
func sendRequest(completion: @escaping (Result<Model, Error>) -> Void) {
    let url = "https://api.example.com/my-endpoint"
    let maxRetryCount = 3
    var currentRetryCount = 0
    
    Alamofire
        .request(url)
        .validate()
        .responseJSON { response in
            switch response.result {
            case .success(let value):
                // JSON 매핑 코드 작성
                completion(.success(model))
            case .failure(let error):
                if currentRetryCount < maxRetryCount {
                    currentRetryCount += 1
                    sendRequest(completion: completion)
                } else {
                    completion(.failure(error))
                }
            }
        }
}
~~~

위의 예제에서는 요청이 실패했을 때 최대 3회까지 재시도를 시도합니다. 재시도 횟수에 제한을 두지 않으려면 조건문을 삭제하면 됩니다.

## 결론

AlamofireObjectMapper를 활용하여 네트워크 요청의 자동 재시도를 처리할 수 있습니다. 자동 재시도 기능을 사용하면 특정 이유로 네트워크 요청이 실패하더라도 안정적으로 데이터를 받아올 수 있습니다. 이렇게 구현된 코드는 앱의 신뢰성과 안정성을 높여줄 것입니다.

### 참고 자료

- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper)