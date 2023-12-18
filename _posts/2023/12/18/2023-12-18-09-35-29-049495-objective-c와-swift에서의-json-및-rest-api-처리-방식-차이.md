---
layout: post
title: "[swift] Objective-C와 Swift에서의 JSON 및 REST API 처리 방식 차이"
description: " "
date: 2023-12-18
tags: [swift]
comments: true
share: true
---

Objective-C와 Swift는 iOS 및 macOS 애플리케이션 개발에 널리 사용되는 프로그래밍 언어입니다. 이 두 언어는 JSON 및 REST API를 다루는 방식에서 다소 차이가 있습니다. 이 글에서는 Objective-C와 Swift에서의 JSON 및 REST API 처리 방식을 비교하고자 합니다.

## Objective-C에서의 JSON 처리

Objective-C에서는 `NSJSONSerialization` 클래스를 사용하여 JSON 데이터를 처리합니다. 다음은 Objective-C에서의 JSON 데이터 파싱 예제입니다.

```objective-c
NSError *error;
NSData *jsonData = [@"{\"key\": \"value\"}" dataUsingEncoding:NSUTF8StringEncoding];
NSDictionary *jsonDictionary = [NSJSONSerialization JSONObjectWithData:jsonData options:NSJSONReadingMutableContainers error:&error];
if (error) {
    NSLog(@"Error parsing JSON: %@", error.localizedDescription);
} else {
    NSString *value = jsonDictionary[@"key"]; // value에는 "value"가 저장됨
}
```

## Swift에서의 JSON 처리

Swift에서는 `Codable` 프로토콜과 `JSONDecoder`, `JSONEncoder` 클래스를 사용하여 JSON 데이터를 처리합니다. 다음은 Swift에서의 JSON 데이터 파싱 예제입니다.

```swift
struct MyData: Codable {
    var key: String
}

let jsonData = Data("{\"key\": \"value\"}".utf8)
do {
    let decodedData = try JSONDecoder().decode(MyData.self, from: jsonData)
    let value = decodedData.key // value에는 "value"가 저장됨
} catch {
    print("Error parsing JSON: \(error.localizedDescription)")
}
```

## REST API 호출 방식

Objective-C와 Swift에서의 REST API 호출 방식은 크게 다르지 않습니다. `NSURLSession`을 사용하여 HTTP 요청을 보내고, 응답을 처리합니다. 다음은 Objective-C에서의 REST API 호출 예제입니다.

```objective-c
NSURL *url = [NSURL URLWithString:@"https://api.example.com/data"];
NSMutableURLRequest *request = [NSMutableURLRequest requestWithURL:url];
NSURLSessionDataTask *task = [[NSURLSession sharedSession] dataTaskWithRequest:request completionHandler:^(NSData *data, NSURLResponse *response, NSError *error) {
    if (error) {
        NSLog(@"Error fetching data: %@", error.localizedDescription);
    } else {
        // 데이터 처리 로직
    }
}];
[task resume];
```

Swift에서의 REST API 호출 방식은 Objective-C와 유사하며, `URLSession`을 사용하여 HTTP 요청을 보냅니다. 

## 결론

Objective-C와 Swift에서의 JSON 및 REST API 처리 방식에는 일부 차이가 있지만, 두 언어 모두 뛰어난 기능을 제공하여 개발자들이 효율적으로 데이터를 다룰 수 있습니다.

참고문헌:
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Swift Codable](https://developer.apple.com/documentation/swift/codable)
- [Objective-C Foundation Framework](https://developer.apple.com/documentation/foundation)