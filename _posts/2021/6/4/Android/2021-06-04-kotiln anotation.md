---
layout: post
title: "[android] Kotlin에서 자주 사용하는 annotation 정리"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---

# Kotlin에서 자주 사용하는 annotation 정리

- @JvmName
- @JvmStatic
- @JvmField
- @Throws
- @JvmOverloads



## @JvmName

`@JvmName`은 코틀린을 바이트코드로 변환할 때 JVM 시그니쳐를 변경할 때 사용합니다. 즉, 자바에서 호출되는 코틀린 함수의 이름이 변경된다는 의미입니다.

다음 코드를 보시면 `@JvmName`을 왜 사용하는지 알 수 있습니다.

```kotlin
// compile error
fun foo(a : List<String>) {
    println("foo(a : List<String>)")
}

fun foo(a : List<Int>) {
    println("foo(a : List<Int>)")
}
```

위의 두개의 foo 함수는 바이트코드로 변경될 때 시그니쳐가 동일합니다. 인자가 `List<>`이기 때문입니다. 컴파일하려고 하면 다음과 같은 에러가 발생합니다. List의 Generic은 구별되지 않기 때문에 두개의 Signature는 동일합니다.

```bash
Error:(7, 1) Kotlin: Platform declaration clash: The following declarations have the same JVM signature (foo(Ljava/util/List;)V):
    fun foo(a: List<Int>): Unit defined in foo.main.kotlin in file kotlin.kt
    fun foo(a: List<String>): Unit defined in foo.main.kotlin in file kotlin.kt
```

`@JvmName`을 사용하면 Signature를 변경할 수 있습니다. 다음 코드는 문제없이 컴파일이 됩니다.

```kotlin
@JvmName("fooListString")
fun foo(a : List<String>) {
    println("foo(a : List<String>)")
}

@JvmName("fooListInt")
fun foo(a : List<Int>) {
    println("foo(a : List<Int>)")
}
```

위 코틀린 코드를 자바로 변환해서 보면 다음과 같습니다. static 함수로 선언된 것은 Top level의 함수로 정의되었기 때문입니다.

```java
public static final void fooListString(@NotNull List a) {
   String var1 = "foo(a : List<String>)";
   System.out.println(var1);
}

public static final void fooListInt(@NotNull List a) {
   String var1 = "foo(a : List<Int>)";
   System.out.println(var1);
}
```

위 코드를 코틀린에서 사용할 때는 아래처럼 꼭 코틀린에서 정의한 이름을 사용해야 합니다. 코틀린이 내부적으로 알아서 올바른 것을 연결해 줍니다.

```kotlin
val listString = listOf("foo", "bar")
foo(listString)

val listInt = listOf(0, 1, 2)
foo(listInt)
```

하지만 `@JvmName`은 바이트 코드의 시그니쳐를 변경하기 때문에, Java에서 호출할 때는 변경된 이름으로 호출해야 합니다. 다음은 자바에서 코틀린의 함수를 호출하는 코드입니다. 함수 이름 앞에 `KotlinKt`가 붙은 것은 kotlin.kt 파일의 Top level에 함수가 정의되었기 때문입니다.

```java
List<String> listString = new ArrayList<>();
KotlinKt.fooListString(listString);

List<Integer> listInt = new ArrayList<>();
KotlinKt.fooListInt(listInt);
```

정리하면, 함수 이름과 인자, 리턴 타입이 동일하기 때문에 컴파일 안되는 경우가 있습니다. `@JvmName`을 사용하면 시그니쳐를 변경하여 컴파일되도록 할 수 있습니다.

주의할 점은 코틀린은 코틀린에서 정의된 함수 이름을 사용해야 합니다. 반면에 자바는 변경된 이름으로 호출해야 합니다.

## @JvmStatic

`@JvmStatic`은 static 변수의 get/set 함수를 자동으로 만들라는 의미입니다. 예제로 알아보겠습니다.

다음 Bar 클래스는 barSize라는 변수를 `companion object`에 선언함으로써, 전역변수를 만들었습니다.

```kotlin
class Bar {
    companion object {
        var barSize : Int = 0
    }
}
```

사실 `companion object`는 자바의 `static`과 다릅니다. 자바로 변환해보면 Bar클래스에 barSize는 선언되었지만 get/set함수는 Bar.Companion 클래스에 등록되었습니다.

```java
public final class Bar {
   private static int barSize;
   public static final class Companion {
      public final int getBarSize() {
         return Bar.barSize;
      }
      public final void setBarSize(int var1) {
         Bar.barSize = var1;
      }
   }
}
```

자바에서 get/set 함수에 접근하려면 다음처럼 Companion을 꼭 써줘야 합니다.

```java
Bar.Companion.getBarSize();
Bar.Companion.setBarSize(10);
```

`@JvmStatic`는 Bar 바로 밑에 get/set함수가 생성되게끔 만듭니다. 아래 코틀린 코드는 barSize를 선언할 때 `@JvmStatic`와 함께 선언했습니다.

```kotlin
class Bar {
    companion object {
        @JvmStatic var barSize : Int = 0
    }
}
```

위 코드를 자바로 변환해보면, 다음과 같습니다. Bar 바로 밑에 get/set함수가 생겼고, Companion은 이전과 동일하게 get/set을 같고 있습니다.

```java
public final class Bar {
   private static int barSize;
   public static final int getBarSize() {
      return barSize;
   }

   public static final void setBarSize(int var0) {
      barSize = var0;
   }

   public static final class Companion {
      public final int getBarSize() {
         return Bar.barSize;
      }
      public final void setBarSize(int var1) {
         Bar.barSize = var1;
      }
   }
}
```

자바에서 위 코드를 접근하면 Bar.Companion 도 가능하지만 Bar.getBarSize 처럼 바로 접근도 됩니다.

```java
Bar.getBarSize();
Bar.setBarSize(10);
Bar.Companion.getBarSize();
Bar.Companion.setBarSize(10);
```

정리하면, `@JvmStatic`는 Companion에 등록된 변수를 자바의 static처럼 선언하기 위한 annotation입니다.

## @JvmField

`@JvmField`는 get/set을 생성하지 말라는 의미입니다.

다음 코틀린 코드에서 [프로퍼티](https://codechacha.com/ko/kotlin-property/) `var barSize`는 get/set함수를 생성합니다.

```kotlin
class Bar {
    var barSize = 0
}
```

자바로 변환해보면 다음처럼 get/set 함수가 생성되었습니다.

```java
public final class Bar {
   private int barSize;
   public final int getBarSize() {
      return this.barSize;
   }
   public final void setBarSize(int var1) {
      this.barSize = var1;
   }
}
```

이번엔 위와 동일한 코드에서 프로퍼티에 `@JvmField`를 붙였습니다.

```kotlin
class Bar {
    @JvmField
    var barSize = 0
}
```

자바로 변환해보면 get/set 함수가 생성되지 않은 것을 볼 수 있습니다.

```java
public final class Bar {
   @JvmField
   public int barSize;
}
```

## @Throws

`@Throws`는 코틀린 함수가 예외를 던질 수 있다는 것을 표시합니다. 사실 코틀린에는 자바의 `throws`와 같은 코드가 없습니다.

아래는 자바코드이고, 함수에서 `NumberFormatException` 예외를 던질 수 있다고 명시되어있습니다. 이 함수를 사용하려면 try-catch로NumberFormatException에 대한 예외처리를 해야 합니다.

```java
void convertStringToInt(String str) throws NumberFormatException {
  ...
}
```

코틀린에서 위와 같이 함수에 예외를 던진다고 명시하고 싶으면, `@Throws`를 사용하면 됩니다. 아래 코드처럼 `@Throws`에 인자로 `NumberFormatException::class`와 같은 형태로 예외를 명시해주면 됩니다.

```kotlin
@Throws(NumberFormatException::class)
fun convertStringToInt(str: String) {
  ....
}
```

위 코드를 자바로 변환해보면, 아래처럼 `throws NumberFormatException`이 함께 함수가 정의됩니다.

```java
public static final void convertStringToInt(@NotNull String str) throws NumberFormatException {
  ....
}
```

## @JvmOverloads

`@JvmOverloads`는 코틀린 함수의 오버로딩 메소드들을 생성해주는 annotation입니다.

예를들어, 아래 코드는 [생성자](https://codechacha.com/ko/kotlin-constructor/)의 인자가 3개이지만, 2개는 [기본인자(default arguments)](https://codechacha.com/ko/kotlin-default-arguments/)로 선언되어있습니다.

```kotlin
class Bar(var name: String, var size: Int = 0, var max: Int = 0) {
    init {
        println("Bar init: $name, $size, $max")
    }
}
```

따라서, 코틀린에서 아래처럼 Bar 객체를 생성할 수 있습니다. 인자를 써주지 않으면 기본으로 설정된 값이 들어갑니다.

```kotlin
Bar("aa")
Bar("aa", 10)
Bar("aa", 10, 11)
```

하지만 위의 코틀린 클래스를 자바로 변환하면 다음처럼 3개의 인자를 갖고 있는 생성자만 생성됩니다. 그 이유는 자바는 [기본인자](https://codechacha.com/ko/kotlin-default-arguments/) 개념이 없기 때문입니다.

```java
public final class Bar {
   private String name;
   private int size;
   private int max;

   public Bar(String name, int size, int max) {
      String var4 = "Bar init: " + this.name + ", " + this.size + ", " + this.max;
      System.out.println(var4);
   }
```

그래서 자바에서 위의 클래스를 생성하려면 아래처럼 모든 인자를 입력해줘야 합니다.

```java
new Bar("aa", 10, 11);
```

그렇지 않으면 아래 코드처럼 코틀린에서 오버로딩 메소드를 만들어줘야 합니다.

```kotlin
class Bar (var name: String, var size: Int = 0, var max: Int = 0) {
    constructor(name: String, size: Int): this(name, size, 0)
    constructor(name: String): this(name, 0, 0)

    init {
        println("Bar init: $name, $size, $max")
    }
}
```

`@JvmOverloads`은 위의 오버로딩 메소드를 자동으로 생성해주는 annotation입니다. 이것을 함수 앞에 붙여주면, 바로 위에서 오버로딩 메소드를 만든 것처럼 코드를 자동 생성해줍니다.

다음은 위의 코틀린 클래스에 이 annotation을 붙여 오버로딩 메소드를 생성한 코드입니다.

```kotlin
class Bar
    @JvmOverloads constructor(
        var name: String, var size: Int = 0, var max: Int = 0) {

    init {
        println("Bar init: $name, $size, $max")
    }
}
```

자바로 변환해서 보면 아래 처럼 오버로딩 메소드들이 자동으로 생성된 것을 볼 수 있습니다. 인자가 4개짜리인 생성자가 있는데, 내부적으로 이런식으로 구현되었을 뿐이고 자바에서는 이 생성자는 드러나지 않습니다.

```java
public final class Bar {
   @NotNull
   private String name;
   private int size;
   private int max;

   @JvmOverloads
   public Bar(@NotNull String name, int size, int max) {
      Intrinsics.checkParameterIsNotNull(name, "name");
      super();
      this.name = name;
      this.size = size;
      this.max = max;
      String var4 = "Bar init: " + this.name + ", " + this.size + ", " + this.max;
      System.out.println(var4);
   }

   @JvmOverloads
   public Bar(@NotNull String name, int size) {
      this(name, size, 0, 4, (DefaultConstructorMarker)null);
   }

   @JvmOverloads
   public Bar(@NotNull String name) {
      this(name, 0, 0, 6, (DefaultConstructorMarker)null);
   }

   @JvmOverloads
   public Bar(String var1, int var2, int var3, int var4, DefaultConstructorMarker var5) {
      ....
      this(var1, var2, var3);
   }
}
```

정리하면, `@JvmOverloads`는 오버로딩 메소드를 자동 생성해주는 annotation입니다. 코틀린 코드만 사용하면 사용할 필요가 없는 annotation입니다. 자바에서 코틀린 코드를 사용할 때 코틀린의 [기본인자](https://codechacha.com/ko/kotlin-default-arguments/) 개념을 적용하기 위해 사용되는 것입니다.

## 정리

코틀린에서 자주 사용되는 annotaiton들을 알아보았습니다. 코틀린만 사용하면 자주 사용되지 않겠지만 코틀린이 JVM에서 동작하고 자바와 함께 사용되는 경우가 많기 때문에 이런 annotation들이 자주 보입니다. 이런 annotaiton들을 알고 있다면 자바와 코틀린을 함께 사용하는데 도움이 될 수 있습니다.

## 참고

- [kotlinlang - annotations](https://kotlinlang.org/docs/reference/annotations.html)

[kotlin](https://codechacha.com/ko/tags/kotlin/)