---
layout: post
title: "kotlin field annotation 예제"
description: " "
date: 2023-09-25
tags: [Kotlin, Annotations]
comments: true
share: true
---

Kotlin에서는 어노테이션을 사용하여 필드에 메타데이터를 추가할 수 있습니다. 이러한 어노테이션은 런타임 시 동작할 수도 있고, 컴파일 시 코드 생성에 사용될 수도 있습니다. 이번 예제에서는 Kotlin의 필드 어노테이션을 다루는 방법을 살펴보겠습니다.

## 어노테이션 정의하기

우선, 어노테이션을 정의해야 합니다. Kotlin에서 어노테이션을 정의하기 위해서는 `annotation` 키워드를 사용합니다. 예를 들어, `@CustomAnnotation`이라는 어노테이션을 정의하고자 한다면 다음과 같이 작성할 수 있습니다:

```kotlin
annotation class CustomAnnotation(val message: String)
```

위 예제에서는 `CustomAnnotation`이라는 어노테이션을 정의하고, `message`라는 속성을 가지도록 선언하였습니다.

## 어노테이션 사용하기

이제 정의한 어노테이션을 필드에 적용해보겠습니다. 예를 들어, 다음과 같은 `Person` 클래스가 있다고 가정해봅시다:

```kotlin
data class Person(val name: String, 
                  @CustomAnnotation("This is a custom annotation") val age: Int)
```

위 예제에서는 `age` 필드에 `@CustomAnnotation` 어노테이션을 적용하였습니다. `message` 속성은 "This is a custom annotation"으로 설정되었습니다.

## 어노테이션 사용하기

적용한 어노테이션을 읽거나 처리하기 위해서는 리플렉션을 사용해야 합니다. 다음 예제는 어노테이션이 적용된 필드를 찾고, `message` 속성 값을 출력하는 예제입니다:

```kotlin
fun processAnnotations(obj: Any) {
    val fields = obj::class.java.declaredFields
    
    for (field in fields) {
        val annotation = field.getDeclaredAnnotation(CustomAnnotation::class.java)
        if (annotation != null) {
            val message = annotation.message
            println("Field: ${field.name}, Message: $message")
        }
    }
}

fun main() {
    val person = Person("John Doe", 30)
    processAnnotations(person)
}
```

위 예제에서는 `processAnnotations` 함수가 `@CustomAnnotation`이 적용된 필드를 찾아 출력합니다. 실행 결과는 다음과 같습니다:

```
Field: age, Message: This is a custom annotation
```

위 예제를 통해 Kotlin에서 필드 어노테이션을 정의하고 사용하는 방법에 대해 알아보았습니다.

#Kotlin #Annotations