---
layout: post
title: "구글 자바 스타일 가이드(Google Java Style Guide)"
description: " "
date: 2021-06-11
tags: [코딩컨벤션]
comments: true
share: true
---

# 구글 자바 스타일 가이드(Google Java Style Guide)

## 1.소개 

이 문서는 프로그래밍 언어인 Java 의 소스코드에 대한 구글의 코딩 규약의 완벽한 정의로서 역할을 하고 있다. Java 소스 파일은 이 문서에 있는 규칙을 준수하는 경우에만 Google 스타일이고 준수하는 않는 경우는 Google 스타일이 아님을 알아두자.<br> 

### 1.1 용어 노트 

1. class라는 용어는 보통의 class나 enum class나 interface 그리고 annotation type(ex: @interface)를 의미하는 용어로 사용된다. 

2. member라는 용어는 nested class , field, method 또는 constructor를 의미한다. 즉 이니셜라이저나 주석을 제외한 한 클래스의 모든 최상위 내용을 말한다. 

3. comment란 용어는 항상 구현 주석(implementation comment)을 언급하는 것이다. 또 우리는 "documentation comments"란 용어 대신에 "Javadoc"이란 공통적인 용어를 사용한다. 

### 1.2 가이드 노트 

예제의 코드는 비 규범적이다. 즉, 예제들은 google style이지만, 이 예제들이 코드를 표현할 수 있는 세련된 유일한 방법이 아닐수도 있다는 뜻이다. **우리는 스타일(코딩 규약)만을 보기로 하자.**<br>

## 2. 소스파일 기본들 

### 2.1 파일 이름 
* 소스 파일 이름은 최상위 레벨 클래스(public class)의 대소문자가 구분이 가능한 이름(정확하게 하나가 있다)과 .java 확장자로 구성된다. 

### 2.2 파일 인코딩: UTF-8
* 소스 파일은 모두 UTF-8로 인코딩된다. 

### 2.3 특별 문자

> 2.3.1 공백 문자

* ASCII 수평 공백 문자, 즉 space bar만이 어느 자바 소드코드의 어느 영역이든 나타나는 **유일한 공백 문자**이다.이는 다음을 의미한다,

1. 문자열이나 문자 리터럴의 다른 공백 문자들은 피해야 한다.
2. Tap은 들여쓰기 할 때 사용하지 말자. 


> 2.3.2 이스케이프 시퀀스 

특수 이스케이프 시퀀스(\b , \t, \n, \f, \r, \”, \’,  \\) 8진수 이스케이프(예: \012)나 유니코드 이스케이프(예: \u000a)보다 우선순위가 높으므로 특수 이스케이프 시퀀스(\b , \t, \n, \f, \r, \”, \’,  \\)을 사용한다. <br>

> 2.3.3 Non-ASCII characters

* 유니코드나 유니코드 이스케이프를 사용하는 것은 추천되지 않지만, 유니코드를 쓰는 방법이 코드를 더 쉽게 읽고 이해할 수 있는 방법이라면 사용해야 한다.**(물론 보통의 경우 권장되지 않는다.보통의 경우는 ASCII 코드를 사용해야 한다.)** 


## 3. 소스파일 구조 

나의 소스 파일은 다음과 같이 구성된다, **순서대로**:<br> 

1. 라이센스 나 저작권 information 적기 ,있는 경우. 
2. Package 구문 
3. import 구문들 
4. 정확히 하나의 최상위 클래스(public class)

정확히 하나의 공백라인으로 각각의 섹션을 분리해야 한다.<br> 

### 3.1 라이센스 및 저작권 정보가 있는 경우.

만약 라이센스나 저작권 information이 있는 경우, 제일 위에 명시하세요. 

### 3.2 Package 문.

package 구문은 **줄바꿈이 되지 않는다.(not line-wrapped)** 열의 제한(열의 제한: 100글자)은 package 구문에 적용되지 않는다. <br>

### 3.3 Import 문.

> 3.3.1 No wildcard imports

와일드 카드 import문 ( \*가 달려있는 import문) , static import문 또 기타 등등은 사용되지 않는다. => 사용하면 안된다. <br>

> 3.3.2 No line-wrapping

import 구문들은 **줄바꿈이 되지 않는다(Package 구문처럼).** 열의 제한(100글자)은 import문에 적용되지 않는다.  

> 3.3.3 Ordering and spacing
 
import 구문들은 다음과 같은 순서대로 작성된다.<br>

1. 모든 static import 문은 한 블록에 있는다. 
2. 모든 non - static import 문은 한 블록에 있는다. 

=> static import 구문과 non- static import 구문이 다 있는 경우 공백 문장(빈 한줄)을 이용해 두 블록으로 나눠야 한다. 한 블록은 non-static import 구문만, 또 하나의 블록은 static import 구문만.  <br>
<br>

=> 각 블록 내에서 가져온 이름은 블록에서 ASCII 정렬 순서로 나타나야 한다. (주의 : 이것은 '.'가 ';'앞에 정렬되기 때문에 ASCII 정렬 순서로되어있는 import 문과 동일하지 않다.) **=> 전체적으로 아스키코드 순이 아닌 블록당 아스키 코드 순으로 정렬하라는 뜻이다.**<br>

> 3.3.4 No static import for classes

Static import문은 static nested class들을 위해 사용되선 안된다. static import class들은 normal import구문만 사용한다.

### 3.4 클래스 선언 

> 3.4.1 Exactly one top-level declaration

각각의 최상위 클래스(public class)는 자기 자신의 소스파일에 있어야 한다. : ***하나의 소스파일에 하나의 클래스만 작성한다.***

> 3.4.2 Ordering of class contents

: 너의 클래스의 멤버나 초기화에 대해 너가 선택한 순서방법은 앞으로 너의 학습 가능성을 큰 영향을 줄 수 잇다. 그러나 ,이것을 어떤 순서로 구성해야 하는지에 대한 단 하나의 옳은 방법은 없다.<br>
<br>
: **중요한 점은 각각의 클래스는 어떤 명확한 논리 순서대로 작성되어야 한다는 점이다.** 클래스를 짠 사람은 누가 물어본다면 코드의 논리 순서에 대해 설명할 수 있어야 한다.<br>  
예를 들어, **새로운 메소드는 습관적으로 클래스의 마지막에 추가되지 않아야 한다.** 왜냐하면 이 방법는 논리적 순서가 아닌 그냥 날짜순, 시간순으로 정렬된 것이기 때문이다.

> 3.4.2.1 Overloads: never split (오버로딩: 절대 나누지 마시오)

: 클래스에 여러 생성자가 있거나 동일한 이름을 가진 메소드가 여럿 있을 경우, 이들은 연달아서 작성되어야 하며 **이들 사이에 다른 생성자나 메소드를 작성하지 말아라.**<br>

=> 오버로딩된 메소드들이나 생성자들은 연속적으로 나열되어야 하며 중간에 다른 메소드나 생성자를 끼지 않게 하여라.<br>

## 4. Formatting

용어 정리: block-like construct 는 클래스,메소드나 생성자의 몸체를 의미한다. 또, 어떠한 배열 이니셜라이져도 선택적으로 block-like construct라고 취급됨을 알아두자 ( ex: int[] a = new int[]{1,2};)<br>


### 4.1 Braces(중괄호)    (소괄호는 parentheses)

> 4.1.1 Braces are used where optional 

중괄호들은 if,else,for,do 그리고 while 문과 함께 사용된다. 심지어 그들의 몸체가 비어 있거나 단 하나의 구문만이 있더라도.<br>

=> if,else,for,do,while문이 있고 그 안에 내용이 없거나 딱 한줄만  있더라도 **중괄호를 생략하지 않고 반드시 사용해야 한다.**

> 4.1.2 Nonempty blocks: K & R style

중괄호들은 비어있지 않는 블록이나 block-like construct에 대해 Kernighan & Ritchie style을 따른다("Egyptian brackets") <br>

* 여는 괄호 앞에 줄바꿈은 없다. 

* 여는 괄호 뒤에 줄바꿈을 한다. 

* 닫는 괄호 앞에 줄바꿈을 한다. 

* 닫는 괄호 뒤에 줄바꿈은, 오직 그 괄호가 한 코드를 끝내거나 메소드, 생성사 또는 named 클래스의 몸체를 끝내는 경우에만 발생한다. 예를 들어 닫는 괄호 뒤에 else나 쉼표가 오는 경우에는 줄 바꿈은 없다. -> 완결하는 경우에만 닫는 괄호 뒤에 줄바꿈을 한다.<br>


> 4.1.3 Empty blocks: may be concise

비어있는 블록이나 비어있는 block-like construct는 K&R 스타일일 거다. 하지만 empty하니깐 줄바꿈 없이 여는 괄호 다음 바로 닫는 괄호를 적는 방식으로 대체할 수 있다( {} ). (만약 이 빈 블록들이 멀티블록의 한 부분이 아니라면: if/else or try/catch/finally) <br> 

### 4.2 Block indentation: +2 spaces

새로운 블록이나 block-like construct가 열릴 때마다, 들여쓰기는 두번의 스페이스바로 해결한다. 블록이 닫힐때, 들여쓰기는 이전의 들여쓰기 단계로 회귀한다. ***들여쓰기 레벨은 블록 전체적으로 주석과 코드 모두에 적용시킨다.*** 

### 4.3 One statement per line

라인 줄바꿈을 통해 **하나의 구문은 하나의 라인이어야 한다.**

### 4.4 Column limit: 100

Java 코드는 100 글자의 열 제한을 갖고 있다. "글자"는 모든 Unicode code point를 의미한다. => **영어 말고도 다른 언어의 글자들도 유니 코드에 있다면 하나의 글자로 취급한다.**<br>
아래 저술한 것을 제외하고,  **이 한계(100개문자)를 넘는 모든 라인은 줄바꿈되어야 한다. (4.5섹션에서 설명한 것처럼)<br>**

* 각각의 유니코드의 코드는 하나의 글자로서 세어진다, 그 글자의 폭이 더 크든 얇든.( 한자의 폭은 알파벳보다 넓지만 한 글자로 취급한다)

예외: <br>

1. 열의 제한을 지키는 것이 불가능한 라인들이 있다. => 예를 들어 javadoc의 긴 URL이나 또는 긴 JSNI(JavaScript Native Interface) 함수 호출의 경우.
2. pakckage 와 import 구문. 
3.  shell에 잘라 불일 수 있는 주석의 명령 행들.

### 4.5 Line-Wrapping(줄 바꿈)

* 용어 노트 :  합법적으로 한줄인 코드가 여러개의 줄로 나뉠때, 이를 줄바꿈(Line-wrapping)이라 한다. <br>
정확히 어떠한 상황에서든 어떻게 줄바꿈해야되는 지에 대해 보편적이거 결정적인 공식은 없다. <br>
매우 흔히 같은 코드로 다양하게 줄바꿈이 이뤄지곤 한다.<br>

* 알아두기: 줄 바꿈의 일반적인 이유는 열 제한이 넘치는 것을 피하는 것이지만 실제로 열 제한 내에 들어 맞는 코드조차도 개발자의 재량에 따라 줄 바꿈 될 수 있다. <br>

* 팁: 메소드나 지역변수를 추출하는 것은 줄바꿈을 할 필요없이 문제를 해결할 수 있다.

> 4.5.1 Where to break

줄 바꿈의 주요한 지시은 다음과 같다: 더 높은 문법적 레벨에서 끊어지는 것을 선호한다.  

1. 비할당 연산자에서 줄이 끊어질 때 줄 바꿈은 그 연산자 앞에 와야 한다.

=> 또한 다음의 "연산자와 같은" 심볼들에게도 이 규칙은 적용된다.<br>
* the dot separator (**.**)
* the tow colons of a method reference (**::**)
* an ampersand in a type bound ( < T extends Foo **&** Bar > )
* a pipe int catch block( catch(FooException **|** BarException e )

2. 라인이 할당 연산자에서 끊어질 때 줄바꿈은 전형적으로 할당 연산자 뒤에 끊어진다. 그러나 다음과 경우도 받아들여진다. 
   * 또한 향상된 for문의 "할당 연산자와 같은" 콜론에도 이 규칙이 적용된다. 

3. 메소드나 생성자의 이름은 뒤에 나오는 여는 소괄호( **(** )와 붙어야 한다. 

4. 컴마 (,) 는 앞에 오는 낱말(이름)과 붙어야 한다. 

5. 람다식이 중괄호가 없는 하나의 코드 구문이라면 화살표 바로 다음에 줄바꿈이 이뤄질 수 있다. 하지만 그렇지 않는 경우에는 람다의 화살표 다음 여는 괄호 뒤에 줄바꿈이 일어나야 한다. 

* 알아두기: 줄바꿈의 가장 주요한 목표는 클린 코드를 갖자는 거지, 반드시 코드를 가장 적게 작성할 필요는 없다. **길이의 최소화보단 코드의 완결성이다.**  (줄바꿈을 해야 한다면 하자. )  

> 4.5.2 Indent continuation lines at least +4 spaces

줄바꿈을 할 때, 첫 줄(각 연속 줄)이후의 각각의 라인은 본래의 라인보다 적어도 +4 스페이스바로 들여쓰기 해야 한다.<br> 
여러개의 연술 줄이 있을 때,  들여쓰기는 원하는 대로 +4 이상으로 변경될 수 있다. <br>
 일반적으로, 두개의 연속줄은 그들이 문법적으로 병렬적 요소들로 시작하는 경우에만 똑같은 레벨의 들여쓰기를 할수 있다. <br>

```java 
User user2 = new User.Builder("Kim",27)
    .address("Gimpo")
    .level(27)
    .money(2000)
    .build();

``` 
=> 스페이스 바 4번. <br>


### 4.6 Whitespace (공백)

> 4.6.1 Vertical Whitespace : 공백 라인 

싱글 공백 라인은 항상 나타난다. <br>

1. 클래스의 연속적인 멤버들이나 또는 이니셜라이져들 사이에 온다. : 필드들, 생성자들, 메소드들, 중첩 클래스들, static 선언자들, 인스턴스 선언자들.

* 예외: 두 개의 연속적인 필드( 그들 사이 다른 코드는 없음) 사이의 공백 라인은 선택적이다. **그러한 공백라인은 필드들끼리의 논리적인 그룹핑을 만드는 것이 필요할 때 사용된다.(예: 필수 필드들, 선택 필드들 사이에 공백라인..)**

* 예외: enum 구성원들 사이의 공백 라인 정책은 4.8섹션을 참고한다. 

2. 이 문서의 다른 섹션들에 의해 요구되어지는 것들.(?)

=> 싱글 공백 라인은 또한 가독성을 높일수 있는 곳이라면 나타날 수 있다. 예를 들어 논리적 서브 섹션으로 코드를 구성하는 구문들 사이에 공백 라인이 있을 수 있다. 첫번째 멤버나 첫번째 초기화의 앞이나  또는 마지막 멤버나 마지막 초기화의 뒤에 공백라인이 있는 것은 권장되지 않는다. <br>

**다수의 연속적인 공백라인은 허용은 되나, 권장되지 않는다.**

> 4.6.2 Horizontal Whitespace : 한 칸의 공백 

단일 ASCII의 수평 공백(스페이스바)는 다음의 경우에만 나타난다.

1. if , for 또는 catch 와 같은 예약어와 그 줄에서 뒤에 오는 여는 괄호와의 분리.

2.  else 또는 catch 와 같은 예약어와 해당 줄에 앞에 있는 닫는 괄호와의 분리.\

3.  여는 괄호 전에 두 가지 예외가 있다:
(1) <br>
```java
@SomeAnnotation({a, b}) (no space is used)
```
(2) <br>
```
String[][] x = {{"foo"}};
```
(no space is required between {{, by item 8 below)<br>

4. 이항 연산자나 삼항 연산자의 양쪽에 공백을 둬라. 이것은 또한 밑의 연산자와 같은 심볼에 적용된다. => 양쪽에 공백을 둬라!

(1)the ampersand in a conjunctive type bound: \<T extends Foo & Bar><br>
:접속어 타입 바운드안의 엠버센드(&)<br>

(2)the pipe for a catch block that handles multiple exceptions:catch (FooException | BarException e)<br>
: 다중 예외 처리하는 catch 블록의 파이프(|)<br>

(3)the colon (:) in an enhanced for ("foreach") statement<br>
: 향상된 for문의 콜론 (:)<br>

(4)the arrow in a lambda expression: (String str) -> str.length()<br>
: 람다식의 화살표.<br><br>

하지만 아래 두 가지 경우는 공백이 없다.<br>
(1)the two colons (::) of a method reference, which is written like Object::toString<br>
: 메소드 접근의 투 콜론 (::) , 다음과 같이 쓰일 때  Object::toString<br><br>

(2)the dot separator (.), which is written like object.toString()<br>
: 도트 세퍼레이터(.) , 다음과 같이 쓰일때 : object.toString()<br>

5.  ,:; 을 쓰고 난 이후나 강제형변환 할때의 닫는 괄호를 쓰고 난 뒤 공백해라.
6. 줄 끝 주석을 시작하는 이중 슬래쉬의 양쪽에 공백을 둬라. 여기에는 다수의 공백이 허용되지만, 요구되지는 않는다.
7. 변수 선언과 타입 사이에 공백을 둬라: List<String> list
8. 배열 초기화의 중괄호 {} 안쪽은 옵션이다.
: new int[] {5, 6} and new int[] { 5, 6 } are both valid
9. 타입 어노테이션과 [] 과 … 사이에 공백을 둬라.

이 규칙은  라인의 시작이나 끝에서 추가 여백을 금지하거나 요구하는 것으로 절대 해석되지 않는다. 이 규칙은 오직 내부 공백 만을 다루는 것이다. <br>

> 4.6.3 Horizontal alignment: never required (진짜 필요없는)

용어 노트:수평 정렬은 이전 줄의 특정 토큰 아래에 특정 토큰을 직접 표시하는 것을 목표로 너의 코드에 가변적인 수의 추가 여백을 붙이는 관습이다. => **즉 변수 명 위아래 맞추려고 공백 더 많이 사용하는 것.**

이 관습은 허용되지만, 절대 구글 스타일로서 요구되지 않는다. 이것은 심지어 이미 수평 정렬 했던 곳의 일관성을 지켜주는 것도 아니다. => 수평 정렬 이후 또 수평 정렬을 하면 이전 수평 정렬이 깨질 수 있다.    => 내 결론: 수평 정렬 하지 말자.<br>

```java
// 수평 정렬 x
private int x; // this is fine
private Color color; // this too

// 수평 정렬 o
private int   x;      // permitted, but future edits
private Color color;  // may leave it unaligned
```

### 4.7 Grouping parentheses: recommended ( 소괄호로 그룹잉하기 : 추천)

:선택적인 소괄호로 그룹잉하기는 생략된다, 저자나 리뷰어가 코드를 괄호가 없으면 오해할 합리적인 가능성이 없는 경우 그리고 괄호가 코드를 읽기 쉽게 만든다는데 동의하지 않는 경우에만. => 괄호가 없어도 코드의 오해가 없거나, 괄호가 있어도 더 가독성을 높이는 경우가 아닌 경우에는 그룹 괄호를 생략할 수 있다.( 작성자와 검토자의 동의하에)<br>

: 그러나 대부분의 경우 소괄호로 그룹잉하는 것은 추천되고 써야함을 말하고 있는 것이다. **(오해하지 않는 경우에만 생략하는 거고)**<br>

### 4.8 Specific constructs (특별한 구조들)

> 4.8.1 Enum classes

: enum 상수 다음에 나오는 각각의 comma 다음 줄바꿈은 선택적이다. 또 추가적인 공백 라인(보통 1개)도 허용된다. 다음은 하나의 가능성이다. <br>

```java
private enum Answer {
  YES {
    @Override public String toString() {
      return "yes";
    }
  },

  NO,
  MAYBE
}
```

메소드가 없고 상수에 대한 문서가 없는 enum 클래스는 선택적으로 배열 이니셜라이져처럼 지정될 수 있다.<br>

```java
private enum Suit { CLUBS, HEARTS, SPADES, DIAMONDS }
```
=> enum 클래스도 클래스이기 때문에, 클래스를 서식하는 다른 규칙들도 모두 적용된다.<br>


> 4.8.2 Variable declarations

* 4.8.2.1 선언 당 하나의 변수 (One variable per declaration)
모든 변수 선언(필드이든 로컬이든)은 오직 하나의 변수를 선언한다. int a, b; 와 같은 선언들은 허용되지 않는다. <br>

예외 : 다수의 변수 선언은 for문의 헤더에서는  접근 가능하다. Ex : for(int i,j; …) <br>

* 4.8.2.2 필요할 때 선언하는 것(Declared when needed)

지역 변수들은 포함하는 블록이나 블록과 같은 구조의 시작점에 습관적으로 선언되지 않는다. <br>
**대신, 지역 변수들은 그들의 범위를 최소화 시키기 위해 처음 사용된 지점에서 가깝게 선언된다.** 지역 변수 선언은 일반적으로 초기화를 갖고 있거나, 선언 뒤에 바로 초기화된다. 

> 4.8.3 Arrays

* 4.8.3.1 배열 초기화: 블록과 같을 수 있다. Array initializers: can be "block-like"

: 배열 초기화는 선택적으로 블록과 같은 구조인 것 마냥 서식될 수 있다. <br>
예를 들어, 다음의 예제는 모두 허용된다.(너무 큰 리스트가 아니라면)<br> 

```java
new int[] {
	0, 1, 2, 3
}

new int[] {
	0,
	1
	2,
	3,
}

new int[] {
	0, 1,
	2, 3
}

new int[] 
    {0, 1, 2, 3}
```

> 4.8.4 Switch statements

* 용어 정리:  switch 블록의 괄호 안에는 하나 또는 그 이상의 구문 그룹들(case들)이 있다. 각각의 구문 그룹은 하나 또는 그 이상의 switch 라벨(예 case F00: 또는 default:  ) 로 구성되어 있다. 

* 4.8.4.1  들여쓰기(Indentation)

다른 블록과 함께,  switch 블록의 내용들은 스페이스 바 +2 로 들여쓰기 해야 한다.<br>

```java
switch(i){
  case 0:
    j++;
    break; 
```
* 4.8.4.2 Fall-through(추락 법): 주석달아야 한다. Fall-through: commented  

Switch 블록안에, 각각의 구문 그룹(case)은 강제적으로( break, continue, return 또는 예외 던지기를 통해) 종결시키거나 또는 다음 case에도 실행이 계속 적용됨을 가리키기 위해 주석을 달아야 한다. (// fall through)  이 특별한 주석은 switch 블록의 마지막 case에는 요구되지 않는다. <br>

```java
switch (input) {
  case 1:
  case 2:
    prepareOneOrTwo();
    // fall through
  case 3:
    handleOneTwoOrThree();
    break;
  default:
    handleLargeNumber(input);
}
```
=> case1: 에는 주석이 안 달린 것을 주목해라. 추락법(fall-through)의 주석(// fall through)은  마지막 case구문의 끝에만 필요하다. <br>

* 4.8.4.3 default case는 있어야 한다 (The default case is present)

=> 각각의 switch 문은 default case를 포함한다, default case가 코드가 없는 경우에도.<br> 

> 4.8.5 Annotations
: 클래스, 메소드 또는 생성자에 적용되는 어노테이션은 문서 블록( Javadoc?) 바로 다음에 나타난다, 그리고 각각의 어노테이션은 자신만의 라인을 가져야 한다.( **즉 한 줄당 하나의 어노테이션을 적어야 한다.** ) 이러한 line-breaks는 섹션 4.5에 말했던 line-wrapping(줄 바꿈)을 구성하지 않으므로, 따라서 주석 레벨은 증가되지 않는다. <br>

```
@Override
@Nullable
public String getNameIfPresent() { ... }
```

예외: 매개변수가 없는 단 한개의 어노테이션은 시그니처의 첫줄에 함께 쓰일 수 있다. <br>

```java
@Override public int hashCode() { ... }
```

하지만 다음과 같은 경우에는 다수의 어노테이션(아마 매개변수화된)같은 줄에 리스트될 수 있다.<br>

```java
@Partial @Mock DataLoader loader;
```

* 매개변수나 ,  지역 변수, 또는 자료형에 대한 어노테이션을 서식하는 것에 대한 특정한 룰은 없다.


> 4.8.6 Comments

이번 섹션은 implementation 주석을 얘기한다. javacoc은 섹션 7에서 따로 얘기할 것이다. <br>
모든 줄 바꿈 앞에는 **임의의 공백 문자와 그 뒤에 구현 주석**이 올 수 있다. 이러한 주석은 줄을 비어있지 않게 한다.<br> 

* 4.8.6.1  블록 주석 스타일 (Block comment style)

블록 주석들은 둘러싸인 코드와 같은 레벨로 들여 쓰기 된다. 그들은 아마 /* … */ 스타일 이거나  //… 스타일이다.  이후의 줄들은 이전 줄의 *에 맞춰 *를 정렬해야 한다. <br>

```java
//(1)

/*
 * This is
 * okay.
 */

//(2)

// And so
// is this.

// (3)

/* Or you can
 * even do this. */

```

주석들은 별표 또는 기타 문자로 그려진 상자에 넣지 않는다.( \*로 꾸민 상자와 같은 경우!) <br>

* 팁: 멀티 라인 주석을 적을때, 만약 너가 필요에 의해 다시 줄들을 감싸기 위해(문단-스타일)자동적인 주석 추가를 원할 때는  /* … */ 스타일을 사용해라.  대다수의 사람들은 //… 스타일로 주석을 감싸지 않는다.

> 4.8.7 Modifiers

클래스 그리고 멤버 제한자가 여러개 있을 때는 자바 언어 사양이 가리키는 순서로 나타내라. <br>

```java
public protected private abstract default static final transient volatile synchronized native strictfp
```

> 4.8.8 Numeric Literals

: : long의 자료형을 갖는 리터럴 숫자는 L 접미사를 사용한다. 절대 소문자를 사용하지 않는다.( 숫자 1과 혼동하지 않기 위해서)<br> 예를 들어 3000000000l 보단 3000000000L을 사용해라.<br>


## 5. Naming : 이름 표기법

### 5.1 Rules common to all identifiers

: 식별자(이름)들은 모두 아스키코드의 문자와 숫자를 사용한다. 그리고 아래에서 언급하는 몇 개의 경우만 밑줄(underscore)이 표시된다. <br>
=> **Java에서는 보통 밑줄을 쓰지 않는다는 뜻.**<br>

* 구글 스타일에서는, 특별한 접미사나 접두어는 사용하지 않는다. 예를 들어 다음과 같은 이름들은 구글 스타일이 아니다: <br>

```java
name_

mName

s_name

kName
```

### 5.2 Rules by identifier type

> 5.2.1 Package names

: 패키지 이름들은 모두 소문자여야 한다. 모든 연속적인 문자들은 단순히 함께 연결된다.(\_가 없다는 뜻) <br>
: 예를 들어, com.example.deepspace 가 좋은 예이고, <br>
com.example.deepSpace (대문자 포함) 이나 com.example.deep\_space(밑줄 포함)은 허용 안된다. <br>

> 5.2.2 Class names
: 클래스 이름들은 UpperCamelCase로 작성된다.<br>
클래스 이름들은 전형적으로 **명사 또는 명사구**이다. 예를 들어 Character 나 ImmutableList. <br> 
인터페이스 이름들 또한 명사나 명사구이지만(예를 들어, List),<br>
때로는 형용사 또는 형용사 구가 대신 쓰일수 있다.(예: Readable, Cloneable )<br>

* 어노테이션 타입들에 대한 Naming은 따로 규칙이 없다. 
* 테스트 클래스의 이름은 테스트할 클래스의 이름으로 시작하여 Test로 끝난다. 예: HashTest 또는 HashIntegrationTest

> 5.2.3 Method names

: 메소드 이름들은 lowerCamelCase로 쓰인다. <br>
메소드 이름들은 전형적으로 동사나 동사구이다. 예를 들어, sendMassage 나 stop.<br>

밑줄(underscore)은 Junit의 테스트 메소드 이름들에 나타나는데, 이름의 논리적인 구성들을 나누기 위해서이다. 각각의 구성들은 lowerCamelCase로 구성된다. 하나의 전형적인 패턴은 \<methodUnderTest>\_\<state\>인데, 예를 들어 pop\_emptyStack이 있다. <br>

> 5.2.4 Constant names

상수 이름은 CONSTANT\_CASE: 모두 대문자이면서 각각의 단어를 밑줄(underscore)로 나누는 방법을 사용한다. 그러나 상수가 정확히 무엇인가?<br><br>

상수들은 **static final 필드**들인데, 구성들이 deeply 바뀔수 없고 그것들의 메소드는 따라서 부수 효과(side effect)가 없다. <br>
이것은 primitive type, Strings, immutable한 타입들, 그리고 immutable한 타입들의 immutable한 콜렉션들을 포함한다. 만약 어떤  인스턴스의 관찰가능한 상태가 변할 수 있다면, 그것은 상수가 아니다. <br>
객체를 절대 바꾸지 않는 이상 충분하지가 않다.<br> 
=> static final, immutable 한 타입들, immutable한 콜렉션을 써야한다.<br> 

```java
// Constants
static final int NUMBER = 5;
static final ImmutableList<String> NAMES = ImmutableList.of("Ed", "Ann");
static final ImmutableMap<String, Integer> AGES = ImmutableMap.of("Ed", 35, "Ann", 32);
static final Joiner COMMA_JOINER = Joiner.on(','); // because Joiner is immutable
static final SomeMutableType[] EMPTY_ARRAY = {};
enum SomeEnum { ENUM_CONSTANT }

// Not constants
static String nonFinal = "non-final";
final String nonStatic = "non-static";
static final Set<String> mutableCollection = new HashSet<String>();
static final ImmutableSet<SomeMutableType> mutableElements = ImmutableSet.of(mutable);
static final ImmutableMap<String, SomeMutableType> mutableValues =
    ImmutableMap.of("Ed", mutableInstance, "Ann", mutableInstance2);
static final Logger logger = Logger.getLogger(MyClass.getName());
static final String[] nonEmptyArray = {"these", "can", "change"};
```
: 이러한 이름들은 전형적으로 명사나 명사구이다.<br>


> 5.2.5 Non-constant field names

: 상수가 아닌 필드 이름들(static이나 기타 등등)은 lowerCamelCase로 써야 한다. <br>
: 이러한 이름들은 전형적으로 명사나 명사구이다. 예: computedValues 또는 index.<br>

> 5.2.6 Parameter names

: 매개변수(파라미터)이름은 lowerCamelCase로 쓰여야 한다.<br> 
: 퍼블릭 메소드의 **한 글자 파라미터 이름은 확실히 피해야 한다.**<br>
=> 파라미터의 이름을 한 글자로 적지 말자. <br>


> 5.2.7 Local variable names

: 지역변수 이름은 lowerCamelCase로 적어야 한다. <br>
: 심지어 final 그리고 immutable 한 지역변수도 상수로 고려되지 않으므로, 이 경우도 반드시 상수처럼 명명하면 안되고 **지역변수의 방식(lowerCamelCase)대로 명명되어야 한다.**<br>

> 5.2.8 Type variable names (타입 변수 이름)

: 각각의 타입 변수(타입 파라미터) 이름들은 다음 두 개의 스타일 중 하나로 명명되어야 한다. <br>

1. 하나의 대문자, 추가적으로 단 한개의 숫자도 붙일 수 있다.(such as E, T, X, T2)

2. 클래스들에 사용된 형식의 이름처럼 명명한다. 대문자 T 앞에. (examples: RequestT, FooBarT ).

### 5.3 Camel case: defined
: 영어 구문을 camel case로 변환하는 합리적인 방법이 여러 있는데, 두문자어(줄인말,이니셜만!예 : TED, Tell me, Explain to me, Descirbee to me)나 “IPv6”나 “iOS”와 같이 비표준의 구성들도 있다. 예측 가능성을 증가시키기 위해, 구글 스타일은 다음과 같은 결정적인 체계를 명시한다 . => 따로 표준을 만들었다.<br> 

산문 형태의 이름에서 고쳐나간다: <br>
1. 구문을 plain한 아스키코드로 변환하고 쉼표(,)를 지워라. 예를 들어 "Müller's algorithm"은   “Muellers algorithm"로 변환되어야 한다.
2.  1번의 결과의 단어들을 , 공백 그리고 남아있는 구두점(일반적으로 hypens)기준으로 나눠라. 

* 추천 사항:  만약 어떤 단어가 이미 관습적인 보통의 camel-case의 모습을 가지고 있다면 , 이 구성요소들을 분리해라. (“AdWords”는 “ad words”로 바껴야 한다. “iOS”와 같은 단어는 사실 camel caser가 아님을 알아둬라. 이것은 어떠한 규약에도 위배되므로 이 권고안에 적용되지 않는다.

3. 이제 소문자로 다 적고(두문자어를 포함해서), 그리고 첫번째 글자만 대문자를 적용시켜라, 다음 두가지 방법 중 하나로.

 ... each word, to yield upper camel case(각각의 단어에 upper camel case를 적용해라 예: 클래스명: HashTest), 또는 <br> 
 ... each word except the first, to yield lower camel case( 첫번째 단어를 제외하고 lower camel case 예: 필드명: newCustomerId)를 적용해라. <br>

4. 최종적으로, 이 모든 단어를 단 하나의 식별자에 합쳐라.





## 6. Programming Practices

### 6.1 @Override : always used

모든 오버라이딩된 메소드는 @Override 어노테이션이 반드시 명시되어야 한다. 이 경우는 부모클래스의 메소드를 재정의하는 한 자식 클래스의 메소드, 인터페이스 메소드를 구현하는 한 클래스의 메소드, 그리고 부모 인터페이스 메소드를 재지정하는 자식 인터페이스의 메소드 모두 포함된다. <br> 

예외: @Override는 아마 @Deprecated가 명시된 부모 메소드인 경우에는 생략될 수 있다. <br>



### 6.2 Caught exceptions: not ignored (예외처리 할 곳은 반드시 예외처리 해야 한다 :  not ignored)

아래 저술된 것을 제외하고, 예외 처리에 대한 응답에 대해 아예 안하는 것은 옳지 않다(전형적인 해답은 log를 하거나 , 또는 만약 “불가능한” 것이라고 고려된다면 이것은 AssertionError로서 다시 예외를 던져야 한다.)<br>

catch 블록에서 아무런 조치도 취하지 않는 것이 진정으로 적합한 경우에는 그 이유를 주석으로 명시해야 한다. <br>

```java
try {
  int i = Integer.parseInt(response);
  return handleNumericResponse(i);
} catch (NumberFormatException ok) {
  // it's not numeric; that's fine, just continue
}
return handleTextResponse(response)
```

* 예외: test들중에, catch 된 예외 중 이름이 expected으로 시작하거나 이름 자체가 expected인 경우(예외의 변수의 이름이!)는 주석없이 무시 될 수 있다. 다음은 테스트중인 코드가 예상되는 형식의 예외를 throw하도록 하는 매우 일반적인 관용구이므로 여기에는 주석이 필요하지 않다. <br>

```java
try {
  emptyStack.pop();
  fail();
} catch (NoSuchElementException expected) {
}
```


### 6.3 Static members: qualified using class ( static 멤버는 클래스 이름으로 접근하라)

정적 클래스 멤버에 대힌 접근이 허용이 되는 경우는, 그 클래스의 이름으로서 접근할 때이다. 해당 클래스의 인스턴스로의 접근은 안된다.<br>

```java
Foo aFoo = ...;
Foo.aStaticMethod(); // good
aFoo.aStaticMethod(); // bad
somethingThatYieldsAFoo().aStaticMethod(); // very bad
```

### 6.4 Finalizers: not used

## 7.Javadoc
java Document의 줄임말로 자바 문서이다. JavaDoc은 자바에서 제공하는 클래스와 메소드를 문서화 하며 API 문서를 제작할 수 있다.<br>
      
## 7.1 Formatting

> 7.1.1 General form

Javadoc 블록의 기본 서식은 다음 예에서 보여진다 :<br>

```java
 /**
  * Multiple lines of Javadoc text are written here,
  * wrapped normally...
  */
public int method(String p1) { ... }
```
또는 한줄의 예도 있다. <br>

```java
/** An especially short bit of Javadoc. */
```
기본 형식은 항상 받아들여진다. 한줄 형식은 아마 Javadoc 블록 전체(주석 표식 포함)가 한 행에 들어갈수 있을 때 대체될 수 있다.  이것은 오직 @return 과 같은 블록태그가 없을 때만 적용됨을 알아둬라.<br>


> 7.1.2 Paragraphs

하나의 공백 라인 – 즉,  정렬된 선행 별표(\*)가 포함되어 있는 공백라인은 문단 사이에 나타난다, 그리고 블록 태그가 있다면, 블록 태그의 앞에  있다. 첫 번째 단락을 제외한 각 단락은 첫 단어 바로 앞에 \<p> 표시되며 뒤에 공백이 없다.<br>


> 7.1.3 블록 태그 Block tags

: 표준 블록 태그(block tags)들은 @param, @return, @throws, @deprecated의 순서로 사용된다. 그리고 이 4 가지 타입은 절대 설명 없이는 사용해선 안된다.(쓸려면 설명을 적어야 한다.) block tag가 한 줄로는 맞지 않을 때, 연속 줄은 @의 위치로부터 +4 space로 주석 처리된다.<br>

## 7.2 The summary fragment(요약 조각)
: 각각의 자바독 블록은 짧은 요약 조각(summary fragment)로 시작한다. 이 조각은 매우 중요하다. 이것은 클래스 및 메소드 인덱스와 같은 특정 컨텍스트에 나타나는 텍스트의 유일한 부분이다.  <br>

: 완전한 문장이 아닌 명사구 또는 동사구가 바로 조각이다.  이것은 A \{@code Foo\} is a..., 또는 This method returns… 로 시작하지 않고 , 또 Save the record. 와 같이 완전한 명령어도 아니다. 그러나, 이 조각은 완벽한 문장 마냥 대문자와 두점(.)을 사용한다. 
팁: 심플한 Javadoc 을 적는 공통의 실수는 /\*\* @return the customer ID \*/의 형식으로 적는 것이다.  이것은 옳지 않고  /\*\* Returns the customer ID. \*/. 로 바꿔야 한다.<br>


## 7.3 Where Javadoc is used
: 최소한으로, javadoc은 아래 명시된 몇개의 예외를 제외하고 모든 public class와 public한 클래스의 모든 public 또는 protected 멤버에서 사용된다. <br>


> 7.3.1 Exceptions: self-explanatory methods (자명한 방법들)

:자바독은 “단순한, 확실한” 메소드들에는 선택적이다. (getFoo와 같은 메소드) . 이 경우 확실히 진실로 foo를 리턴하고 다른 것은 없는 메소드이기 때문이다.<br>

* 중요:  일반적인 독자가 알 필요가 있는 관련 정보를 생략하는 걸 정당화하기 위해 이 예외를 인용하는 것(사용하는 것)은 적절하지 않다.  예를 들어, getCanonicalName으로 명명된 메소드는 javadoc(문서)을 생략할수 없다.  **만약 일반적인 독자가 “canonical name”에 대해 배경지식이 없는 경우라면 꼭 문서를 써야 한다!**

> 7.3.2 Exception: overrides

Javadoc은 항상 부모 메소드를 재정의하는 메소드에 대해 항상 존재하지는 않는다.

> 7.3.4 Non-required Javadoc

다른 클래스나 멤버들은 필요할 때 혹은 적고 싶을때 javadoc을 갖는다.<br>

Implementation 주석이 클래스나 멤버의 전반적인 목적이나 행위에 대해 정의하기 위해 사용되곤 할 때 마다, 해당 주석은 대신  javadoc으로 작성될 수 있다.(/\*\*을 사용해서)<br> 

꼭 필수가 아닌 Javadoc 의 경우는 7.1.2, 7.1.3, 그리고 7.2 섹션의 서식 규칙을 엄격히 따지지 않아도 된다, 이 섹션들이 추천되어도.<br>





