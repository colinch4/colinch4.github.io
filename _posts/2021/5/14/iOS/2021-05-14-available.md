---
layout: post
title: "[iOS] available"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---


## available

**#available**

```swift
if #available(iOS 11.0, *){
    // do something
}else{
    // do something
}
```

#available은 여러 플랫폼에서 서로 다른 논리 처리를 결정하기 위해서 if 또는 guard문과 같이 사용됩니다. →bool을 반환하는 런타임 검사 *은 필수이다.

해당 버전을 포함하여 그 이상의 버전인지를 확인하는 기능

```swift
if #available(iOS 11.0, *){
    // iOS 11 이상을 의미
}else{
    // iOS 11 이상이 아닌 버전들
}
```

**@available**

@available은 함수, 클래스 또는 프로토콜 앞에 놓입니다. 타입 또는 프로토콜이 적용되는 플랫폼 및 os를 나타낸다. 이건 deployment target과 관련이 깊습니다. #available과 다르게 컴파일타임에 경고 또는 오류를 생성

```swift
@available(iOS 12, *)
func setTestButton(){}

```

이렇게 되면 iOS 12를 포함한 그 이상의 버전에서만 함수를 호출할 수 있습니다. 

```swift
@available(iOS 12, *)
func setTestButton(){}

```

이렇게 여러개도 가능하다.

```swift
@available(iOS 12, unavailable)
func setTestButton(){}

```
이렇게하면 iOS12는 사용 할 수 없는 메소드이다.

unavailable는 지정된 플랫폼에서 선언을 사용할 수 없음을 나타냅니다. 이 argument는 Swift버전 가용성을 지정할 때 사용 할 수 없습니다.

introduced: version number     
버전번호는 1~3개의 양의 정수로 구성되며, 마침표로 구분됩니다.    
introduced는 선언이 도입 된 지정된 플랫폼 또는 언어의 첫번째 버전을 나타냅니다.    

deprecated: version number    
deprecated는 선언이 사용되지 않는 지정된 플랫폼 또는 언어의 첫번째 버전을 나타냅니다.

optional 버전번호는 1~3개의 양의 정수로 구성되며, 마침표로 구분됩니다. 버전 번호를 생략하면, 해당 선언이 더이상 사용되지 않으므로 정보는 제공되지않습니다.

obsoleted: version number     
버전번호는 1~3개의 양의 정수로 구성되며, 마침표로 구분됩니다.    
obsoleted는 선언이 폐기된 지정된 플랫폼 또는 언어의 첫번째 버전을 나타냅니다.
선언이 obsoleted로 지정되면, 지정된 플랫폼 또는 언어에서 제거되고, 더 이상 사용할 수 없습니다.

message: message     
메세지는 문자열 리터럴로 구성됩니다.   
message는 사용되지 않거나 더 이상 사용되지 않는 선언을 사용하는 것에 대한 경고 또는 오류를 표시 할 때,
컴파일러가 표시하는 텍스트 메세지를 제공하는데 사용됩니다.

renamed: new name     
새 이름은 문자열 리터럴로 구성됩니다.    
renamed는 이름이 바뀐 선언의 새 이름을 나타내는 텍스트 메세지를 제공하는데 사용됩니다.
새로운 이름은, 이름이 바뀐 선언의 사용에 관헤 오류를 낼 때 컴파일러에 의해 표시됩니다.
