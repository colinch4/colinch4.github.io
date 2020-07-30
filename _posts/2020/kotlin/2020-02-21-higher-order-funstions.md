---
layout: post
title: "[Kotlin] Higher-Order-Function 이란 ?"
date: 2020-02-21 10:05
category: kotlin
author: kwonsik 
tags: [kotlin]
description: "Higher-Order Functions은 함수를 변수로 넘겨주거나, 이를 반환하는 것을 말합니다."
---


Kotlin에는  [Higher-Order Functions](https://kotlinlang.org/docs/reference/lambdas.html)이 제공됩니다.

Higher-Order Functions은 함수를 변수로 넘겨주거나, 이를 반환하는 것을 말합니다. 아래 코드는 레퍼런스 문서에 나와있는 lock 함수를 그대로 옮겨왔습니다.

```
fun <T> lock(lock: Lock, body: () -> T): T {
    lock.lock()
    try {
        return body()
    }
    finally {
        lock.unlock()
    }
}

```

lock 함수에 포함된 파라메터 중  `body: () -> T`는 Higher-Order Functions에 해당합니다.  `body`와  `:`  뒷부분을 아래와 같이 나누어 설명하겠습니다.

-   `body`  : 파라메터 이름
-   `() -> T`  :  `()`  파라메터가 없는 함수를 정의하였고,  `-> T`는 return 타입을 정의합니다. 여기에서는 Generics  `T`를 사용하였기에  `T`를 Generics T를 리턴합니다.

body 변수는 파라메터가 없고, T를 리턴하는 메소드를 넘겨주도록 정의하였습니다.

위에 정의한 lock 메소드를 호출할 때는 아래와 같이 사용할 수 있게 되는데, 여기서는  `toBeSynchronized()`을 그대로 넘겨줍니다. 이때  `::`  두개로 함수를 직접 가리킬 수 있어,  `::toBeSynchronized`으로 지정합니다.

```
fun toBeSynchronized() = sharedResource.operation()

val result = lock(lock, ::toBeSynchronized)

```

이러한 형태를 통해 실제  `body()`를 호출하면  `toBeSynchronized()`  메소드가 호출되게 되는 형태입니다.

  

## 이러한 형태는

이러한 형태는 kotlin의 Standard.kt 레퍼런스 클래스에서 흔하게 확인할 수 있는데, 아래는 let 확장 함수입니다.

```
/**
 * Calls the specified function [block] with `this` value as its argument and returns its result.
 */
@kotlin.internal.InlineOnly
public inline fun <T, R> T.let(block: (T) -> R): R = block(this)

```

let 안에 있는 ` block: (T) -> R`을 구분해서 보면

-   block : 파라메터 이름
-   `(T) -> R`  : 파라메터에 T를 받고, 이를 R로 리턴하는 함수를 정의

결국 block은 (this)의 Generics 타입을 넘겨주고, 결과는 Generics R을 리턴합니다.

  

## 파라메터 정의 - 없을 경우

Higher-Order Functions을 사용할 때는  `()`안에 파라메터를 N 개 정의할 수 있죠.(그냥 함수와 동일) 그렇기에 1개일 때와 N 개일 때 처리하는 방법이 다릅니다.

다음의 코드를 통해 간단하게 살펴보겠습니다.

```
fun print(body: () -> String) {
  println(body())
}

@Test
fun test() {
  print({
    "리턴되는 값을 정의"
  })
}

```

위와 같이 파라메터가 없다면  `print = {}`을 정의합니다. 그리고  `-> String`을 정의하였습니다. lambdas 식에서는 마지막 줄이 리턴이기 때문에  `"리턴되는 값을 정의"`이 리턴되며,  `println()`에 의해  `리턴되는 값을 정의`가 출력됩니다.

  

## 파라메터 정의 - 1개인 경우

이번에는 파라메터 하나를 추가하여  `(String)`  정의하고, 이를  `print`에 정의하였습니다. print는 람다식으로 정의되어, 변수 이름을  `a ->`를 추가하였습니다.

여기에서  `a ->`는  `body: (String)`과 매칭 됩니다.

```
fun print(body: (String) -> String) {
  println(body("이걸 더해서"))
}

@Test
fun test() {
  print({ a ->
    "$a 리턴되는 값을 정의"
  })
}

```

실행하면 결과는  `이걸 더해서 리턴되는 값을 정의`라고 출력됩니다.

kotlin에는 넘어오는 파라메터가 1개인 경우  `it`으로 대체 가능하여 아래와 같이 정의할 수 있죠.

```
fun print(body: (String) -> String) {
  println(body("이걸 더해서"))
}

@Test
fun test() {
  print({ // a -> 생략하고, it으로 대체
    "$it 리턴되는 값을 정의"
  })
}

```

  

## 파라메터 정의 - 1개 이상인 경우

파라메터가 1개 이상인 경우를 살펴보겠습니다. 이 경우도 람다식으로 정의되어, a/b 변수는 다음을 가리키고 있습니다.

-   `a ->`는 body의 첫 번째 String과 매칭
-   `b ->`는 body의 두 번째 String과 매칭

```
fun print(body: (String, String) -> String) {
  println(body("이걸 더해서", "이것도 더해서"))
}

@Test
fun test() {
  print({ a, b ->
    "$a $b 리턴되는 값을 정의"
  })
}

```

  

## 사용하는 쪽 코드를 좀 더 lambdas로 줄여보자

이버는 Higher-Order Functions을 lambdas식을 통해 코드 양을 줄여보겠습니다. 먼저 아래 코드에서  `print`  호출시에  `()`을 제거해보죠.

```
@Test
fun test() {
  print({ a, b ->
    "$a $b 리턴되는 값을 정의"
  })
}

```

위의 코드에서 print 뒤에 있는  `()`을 단순히 제거하면 아래와 같습니다.  `if`문을 연상할 수 있겠네요.

```
@Test
fun test() {
  print { a, b ->
    "$a $b 리턴되는 값을 정의"
  }
}

```

### Higher-Order Functions을 1개 이상 사용할 경우

하지만 Higher-Order functions 정의가 1개 이상으로 늘어나면 결국  `()`가 필요한데, 아래와 같이 사용할 수 있습니다.

```
fun print(body: (String) -> String, body2: (String) -> String) {
    println(body("이걸 더해서"))
}

@Test
fun test() {
    print({ a ->
        "$a 리턴되는 값을 정의"
    }, {
        "BBBB"
    })
}

```

Higher-Order Functions 정의가 N 개라면, 마지막의 Higher-Order Functions은  `()`  안에 포함하지 않고,  `()`  밖에 위치시킬 수 있습니다. 그래서  `({첫 번째}, {두 번째})`을 하지 않고,  `({첫 번째}) {두 번째}`을 만들어줄 수 있습니다.

```
@Test
fun test() {
    print({ a ->
        "$a 리턴되는 값을 정의"
    }) {
        "BBBB"
    }
}

```

### 다른 메소드 참조

이번에는 직접 구현하는 게 아닌 다른 메소드를 참조하게 만들어보겠습니다. kotlin 문서에 나와있는 첫 번째 샘플처럼 콜론 2개를 붙여서 직접 호출할 수 있습니다.

먼저 아래와 같이 sample을 직접 호출하는 식으로 사용해보겠습니다. 이 경우 파라메터 수는 문제가 없습니다.

```
fun print(body: (String, String) -> String) {
    println(body("이걸 더해서", "이것도 더해서"))
}

fun sample(a: String, b: String) = "$a $b 리턴되는 값을 정의"

@Test
fun test() {
  print { a, b ->
    sample(a, b)
  }
}

```

`::`을 이용해서 부르려는 함수의 파라메터가 서로 같아야 합니다. 만약 파라메터가 1개라도 다르면 코드 오류가 발생합니다.

아래의 코드에서 print에 String, String 2개의 파라메터를 body에 넘겨주고 있습니다. 그래서 호출하는 sample도 String, String 2개의 파라메터가 존재해야 하며, String, Int 식으로 접근할 수 없습니다.

```
@Test
fun test() {
  print(::sample)
}

```

  

## 더하기, 빼기, 곱하기, 나누기를 만들어볼까요?

Higher-Order functions에 대해서 각각을 살펴보았습니다. 이번에는 Higher-Order Functions을 이용해서 간단하게 더하기, 빼기, 곱하기, 나누기를 만들어보겠습니다.

먼저 print에는 2개의 Int 변수를 받아서, 이를 Int 형태로 리턴하는 Higher-Order Functions을 정의해보았습니다.

```
fun print(body: (Int, Int) -> Int) {
  println(body(1, 2))
}

```

body의 정의는 호출하는 쪽에서 해야 하기 때문에  `print {}`를 부르는 쪽에서 함수 4개를 다음과 같이 정의해보죠.

```
fun sum(a: Int, b: Int) = a + b
fun minus(a: Int, b: Int) = a - b
fun multiply(a: Int, b: Int) = a * b
fun division(a: Int, b: Int) = a / b

```

위와 같이 미리 함수를 만들어두고, 이를  `test()`에서 각각을  `::`으로 묶어 넘겨주었습니다.

```
@Test
fun test() {
  print(::sum)
  print(::minus)
  print(::multiply)
  print(::division)
}

```

실행 결과는 print 메소드에 정의한 1, 2에 대한 처리를 한 후 출력됩니다.

```
3
-1
3
0.33333

```

위 코드의 전체 Test 코드는 아래와 같습니다.

```
class ExampleUnitTest {

    private fun showResult(body: (Int, Int) -> Int) {
        println(body(1, 2))
    }

    @Test
    fun test() {
        showResult(::sum)
        showResult(::minus)
        showResult(::multiply)
        showResult(::division)
    }
}

fun sum(a: Int, b: Int) = a + b
fun minus(a: Int, b: Int) = a - b
fun multiply(a: Int, b: Int) = a * b
fun division(a: Int, b: Int) = a / b

```

  

## Higher-Order Functions을 디컴파일 해보면?

bytecode를 디컴파일 해보면 아래와 같은데, 결국  `Function1`  메소드로 값을 넘기는 것을 확인해볼 수 있습니다.

```
public final class ExampleUnitTest {
   public final void print(@NotNull Function1 body) {
      Intrinsics.checkParameterIsNotNull(body, "body");
      Object var2 = body.invoke("이걸 더해서");
      System.out.println(var2);
   }

   @Test
   public final void test() {
      this.print((Function1)null.INSTANCE);
   }
}

```

  

## 변수에 Higher-Order Functions을 정의하는 방법

Higher-Order Functions은 파라메터로 전달할 수 있을 뿐 아니라 변수에도 Higher-Order Functions을 사용할 수 있습니다.

val로 변수를 생성함과 동시에  `= {}`  안에 정의할 수 있습니다.

```
class Sample {
  val higherOrder: () -> Unit = {
    println("Higher order functions")
  }

  @Test
  fun test() {
    higherOrder()
  }
}

```

이번에는 가장 많이 활용하게 될  `lateinit`으로 아래와 같이 정의할 수 있습니다. 보통 onClick을 대신 구현할 때 사용하게 될 겁니다.

```
class Sample {
  private lateinit var higherOrder: (String) -> Unit

  @Test
  fun test() {
    higherOrder = {
      println("$it print higherOrder")
    }

    higherOrder("print message")
  }
}

```

이 경우 interface로 onClickListener을 정의하지 않고, Higher-Order Functions을 함께 사용하여 간단하게 click을 처리할 수 있게 됩니다. 저는 adapter에서 onClick이 발생하면, Position을 넘겨받는  `onItemClick`에 주로 활용하고 있습니다.

```
lateinit var onItemClick: (Int) -> Unit

```

  

## Higher-Order Functions을 Java에서 사용하려면?

이러한 Higher-Order Functions을 Java에서도 호출하는 게 가능합니다. Java에서는 Function으로 시작하고, 0~N까지의 클래스 정의가 있습니다. 이를 활용하게 되어, 넘어오는 파라메터의 숫자에 따라 자동으로 0~N까지 지정됩니다.

아래 샘플은 1개의 String을 전달받기에 Function1을 사용하고 있으며, 아래처럼 return하는 게 가능합니다.

![java-higher-order-fucntions](https://thdev.tech/images/posts/2017/10/Kotlin-Higher-Order-Function/java-higher-order-fucntions.png)

```
public class Sample {

    @Test
    public void test() {
        ExampleUnitTest test = new ExampleUnitTest();
        test.print(new Function1<String, String>() {
            @Override
            public String invoke(String s) {
                return "ABC";
            }
        });
    }
}

```

  

## 마무리

Higher-Order Functions에 대해서 살펴보았습니다. class 내부에서 정의하는 메소드를  `::`형태로 넘기는 경우 일부분은 아래와 같은 오류가 발생하는데 kotlin 1.2에서 제공할 예정이라고 합니다, 테스트 코드 확인 시 참고하세요.

![exception](https://thdev.tech/images/posts/2017/10/Kotlin-Higher-Order-Function/exception.png)

Higher-Order Functions을 사용하면 재미있는 문법 활용이 가능하며, Generics과 함께 사용할 때 더 유용하게 사용이 가능합니다. Kotlin의 Interface 정의를 간단하게 하는데도 많은 도움이 됩니다.