---
layout: post
title: "[kotlin] 접근 제어 지시자(public, private, protected 등)의 사용법"
description: " "
date: 2023-12-12
tags: [kotlin]
comments: true
share: true
---

Kotlin은 객체 지향 프로그래밍 언어로, 접근 제어 지시자를 사용하여 클래스 멤버에 대한 접근을 제어할 수 있습니다. Kotlin에서는 다음과 같은 접근 제어 지시자를 사용할 수 있습니다.

## 1. public
기본적으로 Kotlin 클래스의 멤버(속성, 메서드 등)는 public으로 선언됩니다. public으로 선언된 멤버는 해당 클래스 외부에서도 접근할 수 있습니다.

```kotlin
class Example {
    public val publicProperty: Int = 10
}
```

## 2. private
private으로 선언된 멤버는 해당 클래스 내부에서만 접근할 수 있습니다.

```kotlin
class Example {
    private val privateProperty: Int = 20
}
```

## 3. protected
protected로 선언된 멤버는 해당 클래스 및 해당 클래스를 상속받은 하위 클래스에서만 접근할 수 있습니다.

```kotlin
open class Base {
    protected val protectedProperty: Int = 30
}

class Derived : Base() {
    fun getProtectedProperty(): Int {
        return protectedProperty
    }
}
```

## 4. internal
internal은 같은 모듈 내에서 접근할 수 있는 범위를 가지는 제어 지시자입니다. Kotlin에서 모듈은 같은 컴파일 유닛을 의미합니다.

```kotlin
internal class InternalExample {
    internal val internalProperty: Int = 40
}
```

이와 같이 Kotlin에서는 접근 제어 지시자를 사용하여 멤버의 접근 범위를 명확히 지정할 수 있습니다.

더 자세한 내용은 [Kotlin 공식 문서](https://kotlinlang.org/docs/visibility-modifiers.html)를 참고해 주세요.