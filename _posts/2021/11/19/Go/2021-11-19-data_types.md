---
layout: post
title: "[Go] Data Types"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

# Data Types
Go의 자료형에 대하여.

### Table of Contents
- [Data Types](#data-types)
    - [Table of Contents](#table-of-contents)
  - [Numeric Types](#numeric-types)
    - [Integers](#integers)
    - [Floating-points](#floating-points)
    - [Complex numbers](#complex-numbers)
  - [Boolean Types](#boolean-types)
    - [Boolean with Logical Operators](#boolean-with-logical-operators)
  - [String Types](#string-types)
    - [Internal Structure](#internal-structure)
    - [Zero Value](#zero-value)
    - [Concatenate](#concatenate)
    - [Subslice](#subslice)
    - [Length](#length)
    - [Element Access](#element-access)

## Numeric Types
Go에서 숫자는 정수, 실수, 복소수로 표현할 수 있다.  
> int, uint, float의 뒤에 붙은 숫자는 bits를 말한다.

Numeric Types 에서 별칭을 가진 두 자료형이 존재한다.  
아래 자료형의 공통점은 문자(`단일문자` 또는 `문자열`)를 나타낼 때 쓰인다는 것이다.  
* **int32**  
  `int32` 의 다른 이름은 `rune` 이다.  
  단일 문자를 나타낼 때 사용.  
* **uint8**  
  `uint8` 의 다른 이름은 `byte` 이다.  
  문자열을 나타낼 때 사용.  


### Integers
* **int**  
부호 있는 정수 (integer)  
  * **int8**  
  값의 범위 : -128~127
  * **int16**  
  값의 범위 : -32768~32767
  * **int32**  
  값의 범위 : -2147483648~2147483647
  * **int64**  
  값의 범위 : -9223372036854775808~9223372036854775807.

* **rune**  
`rune` == `int32`  
  - 보통 유니코드 문자 코드를 저장할 때 사용.  
    > 유니코드를 사용하기에 전세계의 거의 모든 문자를 표현 가능하다.
  - 반드시 **single quotation marks** `''` 를 사용.   
    > Double quotation marks `""` 를 사용시 컴파일 오류 발생.
  - 문자는 저장 가능하지만 문자열은 저장할 수 없다.   
    > 문자열은 string 을 사용한다.

* **uint**  
부호 없는 정수 (unsigned interger)  
Zero 와 Positive 숫자만 표현 가능
  * **uint8**  
  값의 범위 : 0~255
  * **uint16**  
  값의 범위 : 0~65535
  * **uint32**  
  값의 범위 : 0~4294967295
  * **uint64**  
  값의 범위 : 0~18446744073709551615

* **byte**  
`byte` == `uint8`

* **uintptr**  
Pointer 저장시 사용 (unsigned integer pointer)

[↑ Return to TOC](#table-of-contents)


### Floating-points
Go에서 실수를 표현할때는 '고정소수점 방식'과 '부동소수점 방식'을 사용할 수 있다.  
주의할 것은 컴퓨터는 2진수 기반이면서 한정적인 메모리로 인해 실수를 정확하게 표현하지 못한다.
* **float**
  * **float32**
  * **float64**

[↑ Return to TOC](#table-of-contents)

### Complex numbers
실수와 허수로 이루어진 복소수.  
복소수 또한 실수이기에 계산시 정확히 표현이 불가하다.
* **complex**
  * **complex64**
  * **complex128**

[↑ Return to TOC](#table-of-contents)
  
## Boolean Types
Go 의 불리언 값은 `true` 와 `false` 로 나뉜다.  
Boolean은 논리값을 나타내는 자료형이다.  
타 언어와 마찬가지로 조건문에서 유용하게 사용된다.
  * true와 false의 크기는 1 byte.
    ```go
    var b2 bool = false
	  fmt.Println(unsafe.Sizeof(b2)) // 1
    ```

### Boolean with Logical Operators
Boolean은 논리연산자와 함께 쓰인다.
  * 논리합 AND  
    <code>&&</code>
  * 논리곱 OR  
    <code>||</code>
  * 논리 부정 NOT  
    <code>!</code>   

    ```go
    // AND, OR, NOT
    fmt.Println(true && true)   // true
    fmt.Println(true && false)  // false
    fmt.Println(false && true)  // false
    fmt.Println(false && false) // false

    fmt.Println(true || true)   // true
    fmt.Println(true || false)  // true
    fmt.Println(false || true)  // true
    fmt.Println(false || false) // false

    fmt.Println(!false) // true
    fmt.Println(!true)  // false

    fmt.Println(!!false) // false
    fmt.Println(!!true)  // true
    ```

[↑ Return to TOC](#table-of-contents)

## String Types
Go의 문자열은 `uint8` 의 series 이다.  
Go 에서 `uint8` 은 `byte` 라는 별칭을 지니고 있다. 즉, `string` 은 바이트의 나열이라고 볼 수 있다.  

제공되는 문자열 리터럴(string literal)은 총 두가지 스타일로 나뉜다.
* Interpreted literals  
  쌍 따옴표(double-quote)로 표현 : `""`
* Raw string literals  
  역 따옴표(back-quote)로 표현 : <code>``</code>

### Internal Structure
Go 문자열의 내부 구조는 아래와 같이 `str`, 과 `len` 으로 이루어져 있다.
```go
type _string struct {
  str *uint8
  len int
}
```
* **str** : `uint8` 으로 이루어진 포인터
* **len** : 문자열의 길이 (바이트의 개수)  

[↑ Return to TOC](#table-of-contents)

### Zero Value
빈문자열(`empty string`)을 통해 문자열의 zero value 를 나타낸다.  
* <code>""</code>
* <code>``</code>

위에서 알아보았듯이 문자열의 내부구조는 `str` 과 `len` 으로 이루어져 있다. 빈문자열이라 함은 `str` 은 `nil` 의 값을, `len` 은 `0` 값을 지니고 있다는 뜻이다.  

[↑ Return to TOC](#table-of-contents)

### Concatenate  
문자열은 `+` 또는 `+=` 연산자를 통해 연결시킬 수 있다.  
```go
  s1 := "Baby "
  s2 := "Tiger "
  s3 := "or 8luebottle"
	
  s1 = s1 + s2 // Baby Tiger
  s1 += s3     // Baby Tiger or 8luebottle
```

[↑ Return to TOC](#table-of-contents)

### Subslice  
`s[start:end]` 를 통해 문자열을 자를 수 있다.  

```go
  s := "Your time is limited, so don't waste it living someone else's life."
  
  start := 5
  end   := 20
  
  s[:start]    // Your
  s[start:end] // time is limited
  s[end+1:]    // so don't waste it living someone else's life.
```

[↑ Return to TOC](#table-of-contents)

### Length  
문자열의 길이 측정은 `built-in` 타입인 `len` 을 통해 한다.  
문자열에 저장된 바이트의 개수를 알 수 있다. 
```go
  s := "Your time is limited, so don't waste it living someone else's life."

  len(s) // 67
```

[↑ Return to TOC](#table-of-contents)

### Element Access
`s[i]` 를 통해 문자열의 `i` 요소에 접근할 수 있다.  
```go
  s := "It is during our darkest moments that we must focus to see the light."

  // 문자열은 uint8 의 조합이기 때문에 s[13] 은 uint8 형태인 111 로 표현된다.  
  s[13] // 111
  s[19] // 114
  
  // 고유 문자형태로 표현하고자 한다면 string 을 통해 타입변환을 해주자.  
  string(s[13]) // o
  string(s[20]) // k
```

[↑ Return to TOC](#table-of-contents)
