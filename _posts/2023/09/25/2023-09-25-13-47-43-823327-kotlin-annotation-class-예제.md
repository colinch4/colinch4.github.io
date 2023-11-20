---
layout: post
title: "kotlin annotation class 예제"
description: " "
date: 2023-09-25
tags: [kotlin]
comments: true
share: true
---

Kotlin에서는 Annotation(주석)을 표시하기 위한 Annotation Class를 사용할 수 있습니다. Annotation을 사용하면 코드를 더욱 유연하게 만들어주고, 컴파일러에게 추가 정보를 전달할 수 있습니다. 이번 포스트에서는 Kotlin에서 Annotation Class를 작성하는 예제를 살펴보겠습니다.

## Annotation Class 정의하기

아래는 Annotation Class를 정의하는 예제입니다.

```kotlin
annotation class CustomAnnotation(val value: String)
```

위의 예제에서 `CustomAnnotation`은 Annotation을 정의하는 클래스입니다. `value`라는 속성을 가지고 있으며, 이 속성은 문자열 값을 받습니다.

## Annotation 사용하기

이제 `CustomAnnotation`을 사용하는 예제를 살펴보겠습니다.

```kotlin
@CustomAnnotation("Hello")
class MyClass {
    // 클래스 내용
}
```

위의 예제는 `MyClass`라는 클래스에 `CustomAnnotation`을 적용하는 예제입니다. Annotation은 클래스, 메소드, 필드 등 다양한 요소에 적용할 수 있습니다.

## Annotation 읽기

Annotation은 실행 시간에도 읽을 수 있습니다. 아래는 Annotation을 읽는 예제입니다.

```kotlin
fun readAnnotation(obj: Any) {
    val annotation = obj::class.annotations.find { it.annotationClass == CustomAnnotation::class }
    if (annotation != null) {
        val value = annotation?.let { it as CustomAnnotation }?.value
        println("Annotation value: $value")
    }
}
```

위의 예제는 `readAnnotation`이라는 함수를 정의하고 있습니다. 이 함수는 주어진 객체의 Annotation을 읽고, Annotation을 가진 경우 그 값을 출력합니다.

## 실행 결과

아래는 예제 코드를 실행한 결과입니다. 

```
Annotation value: Hello
```

## 요약

이번 예제를 통해 Kotlin에서 Annotation Class를 작성하고 사용하는 방법을 알아보았습니다. Annotation은 Kotlin 코드의 유연성을 높여주고, 컴파일러에게 추가 정보를 전달하는 데 유용합니다. 많은 프레임워크와 라이브러리에서 Annotation을 사용하므로, 앞으로 Kotlin 코드를 작성할 때 이를 활용해보세요!

#### #Kotlin #Annotation #예제