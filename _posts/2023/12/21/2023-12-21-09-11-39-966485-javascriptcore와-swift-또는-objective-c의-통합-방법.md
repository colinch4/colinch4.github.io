---
layout: post
title: "[ios] JavaScriptCore와 Swift 또는 Objective-C의 통합 방법"
description: " "
date: 2023-12-21
tags: [ios]
comments: true
share: true
---

iOS 앱을 개발하면서 JavaScript 코드를 실행하고 해당 코드와 상호 작용해야 하는 경우가 있습니다. JavaScriptCore 프레임워크는 JavaScript 코드를 Objective-C나 Swift 애플리케이션으로 통합하고 상호 작용할 수 있도록 해줍니다. 이 기술은 웹 뷰에서 JavaScript 코드를 실행하거나 JavaScript로 작성된 사용자 정의 동작을 Native 앱에 통합하는 데 유용하게 활용됩니다.

## JavaScriptCore란?

JavaScriptCore는 WebKit 프레임워크에 포함된 JavaScript 엔진입니다. Objective-C 및 Swift 애플리케이션에서 JavaScript 코드를 실행하고, JavaScript 객체와 상호 작용할 수 있도록 지원합니다.

## Objective-C에서 JavaScriptCore 사용하기

Objective-C에서 JavaScriptCore를 사용하려면 다음 단계를 따릅니다.

1. `JSContext` 생성: JavaScript 실행 컨텍스트를 만들어 JavaScript 코드를 실행하고 상호 작용합니다. 
2. JavaScript 코드 실행: `evaluateScript:` 메서드를 사용하여 JavaScript 코드를 실행합니다.
3. JavaScript 객체와 상호 작용: Objective-C 객체를 JavaScript 환경으로 노출하거나, JavaScript 객체를 Objective-C에 전달하여 각 환경 간 상호 작용을 할 수 있습니다.

```objective-c
// Objective-C에서 JavaScriptCore 사용하기
#import <JavaScriptCore/JavaScriptCore.h>

// JSContext 생성
JSContext *context = [[JSContext alloc] init];

// JavaScript 코드 실행
JSValue *result = [context evaluateScript:@"1 + 2"];

// JavaScript 객체와 상호 작용
context[@"nativeObject"] = nativeObject;
JSValue *jsValue = context[@"jsObject"];
```

## Swift에서 JavaScriptCore 사용하기

Swift에서 JavaScriptCore를 사용하려면 Objective-C와 거의 유사한 방식으로 다음 단계를 따릅니다.

1. `JSContext` 생성
2. JavaScript 코드 실행
3. JavaScript 객체와 상호 작용

```swift
// Swift에서 JavaScriptCore 사용하기
import JavaScriptCore

// JSContext 생성
let context = JSContext()

// JavaScript 코드 실행
let result = context.evaluateScript("1 + 2")

// JavaScript 객체와 상호 작용
context.setObject(nativeObject, forKeyedSubscript: "nativeObject" as NSCopying & NSObjectProtocol)
let jsValue = context.objectForKeyedSubscript("jsObject")
```

## 결론

JavaScriptCore를 사용하여 Objective-C나 Swift와 JavaScript 간 상호 작용을 구현하는 것은 간단하고 유연한 방법입니다. 이를 통해 앱에 JavaScript 기능을 통합하고 동적으로 동작하는 기능을 추가할 수 있습니다.

더 많은 정보를 얻으려면 [JavaScriptCore 프레임워크 문서](https://developer.apple.com/documentation/javascriptcore)를 확인해보세요.

위의 방법을 통해 JavaScriptCore를 사용하여 Objective-C나 Swift에서 JavaScript 코드를 통합할 수 있습니다.