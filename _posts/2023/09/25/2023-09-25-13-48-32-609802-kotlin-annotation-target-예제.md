---
layout: post
title: "kotlin annotation target 예제"
description: " "
date: 2023-09-25
tags: [Kotlin, Annotation]
comments: true
share: true
---

Kotlin에서는 Annotation이 소프트웨어 개발을 위해 많은 유용한 정보를 제공하는 일반적인 기능입니다. `@Target` 어노테이션은 어노테이션을 적용할 수 있는 대상을 선언할 때 사용됩니다.

```kotlin
@Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)
annotation class MyAnnotation

@MyAnnotation
class MyClass {
    @MyAnnotation
    fun myFunction() {
        // 함수 내용
    }
}
```

위의 예제에서는 `@Target` 어노테이션을 사용하여 `MyAnnotation`이 클래스와 함수에 적용될 수 있도록 선언하였습니다. `@MyAnnotation` 어노테이션은 `MyClass` 클래스와 `myFunction()` 함수에 적용되어 사용될 수 있습니다.

`@Target` 어노테이션의 매개변수로 사용할 수 있는 대상은 다음과 같습니다.

- `AnnotationTarget.CLASS`: 클래스, 인터페이스, 객체 선언
- `AnnotationTarget.ANNOTATION_CLASS`: 어노테이션 클래스
- `AnnotationTarget.TYPE_PARAMETER`: 타입 매개변수 선언
- `AnnotationTarget.CONSTRUCTOR`: 생성자 선언
- `AnnotationTarget.FIELD`: 필드 선언
- `AnnotationTarget.PROPERTY`: 프로퍼티(속성) 선언
- `AnnotationTarget.PROPERTY_GETTER`: 게터 메소드 선언
- `AnnotationTarget.PROPERTY_SETTER`: 세터 메소드 선언
- `AnnotationTarget.TYPE`: 타입 사용(클래스나 함수 파라미터로 사용되는 타입)
- `AnnotationTarget.EXPRESSION`: 표현식
- `AnnotationTarget.FILE`: 소스 파일
- `AnnotationTarget.VALUE_PARAMETER`: 함수나 생성자의 매개변수

위 예제에서는 클래스와 함수에 적용되도록 설정하였지만, 필요에 따라 다른 대상에도 적용할 수 있습니다. `@Target` 어노테이션은 어노테이션의 적용 범위를 제한하는데 유용하게 사용될 수 있습니다.

**#Kotlin #Annotation**