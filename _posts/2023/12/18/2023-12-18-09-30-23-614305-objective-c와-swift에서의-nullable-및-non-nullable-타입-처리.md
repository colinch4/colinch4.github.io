---
layout: post
title: "[swift] Objective-C와 Swift에서의 Nullable 및 Non-nullable 타입 처리"
description: " "
date: 2023-12-18
tags: [swift]
comments: true
share: true
---

Objective-C 및 Swift는 모두 nullable 및 non-nullable 타입을 다루는 데에 다소 차이가 있습니다. 이러한 차이를 이해하면 코드를 작성하고 협업하는 데 도움이 됩니다.

## Objective-C에서 Nullable 및 Non-nullable 타입 처리

Objective-C에서는 기본적으로 모든 객체가 nullable합니다. 하지만 null을 허용하지 않는 non-nullable 타입을 나타내기 위해 `nonnull` 키워드를 사용할 수 있습니다.

```objective-c
@property (nonnull, strong) NSString *nonNullableString;
@property (nullable, strong) NSString *nullableString;
```

위의 예제에서 `nonnull` 및 `nullable` 키워드를 사용하여 non-nullable 및 nullable 타입을 선언하고 있습니다.

## Swift에서의 Nullable 및 Non-nullable 타입 처리

Swift는 Objective-C와는 다르게 non-nullable을 기본으로 갖습니다. 변수를 optional로 만들려면 `?`를 사용합니다.

```swift
var nonNullableString: String
var nullableString: String?
```

위의 예제에서 `String` 타입은 non-nullable이며, `String?`은 nullable한 옵셔널 타입입니다.

## Conclusion

Objective-C와 Swift에서의 nullable 및 non-nullable 타입 처리에는 약간의 차이가 있습니다. 이러한 차이를 이해하고 올바르게 활용하면 코드의 안정성과 가독성을 향상시킬 수 있습니다.