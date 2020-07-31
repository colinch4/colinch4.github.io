## 코틀린의 null

- 코틀린은 null을 기본적으로 허용하지 않음

- - 하지만 개발을 하다 보면 null이 필요한 경우도 있고, null이 예기치 않게 발생할 수 있음.

- Andriod Annotation을 활용하면 @Nullable와 @NotNull을 Annotations으로 적용할 수 있음

- ?. 또는 ?.let { }을 활용하여 안전하게 null을 사용할 수 있음

- - java에서는 @Nullable이 올 경우 개발자가 if()등을 활용하여 null을 명시적으로 처리해 줘야함



## ?.를 사용했을 때의 장점

- 여러 변수를 중첩적으로 호출하게 되었을 때 장점을 가진다.

- null이 포함된 변수에 물음표를 이용하여 null체크하였을 때의 장점은 다음과 같은 코드

- Java의 경우…

  > ```kotlin
  > 
  > ```

* Kotlin의 경우

  > ```kotlin
  > 
  > ```
  >
  > ```kotlin
  > 
  > ```
  >
  > java에서 보다 코드가 간결해졌을 뿐 내용은 같다.



## Java에서 null을 피하는 방법

> ```kotlin
> String temp = null;
> int size = -1;
> if (temp != null)
> {
>     size = temp.length();
> }
> 
> // 또는 TextUtils.isEmpty()를 활용
> if (!TextUtils.isEmpty(temp))
> {
>     size = temp.length();
> }
> ```



## Kotlin에서 null을 피하는 방법

> ```kotlin
> var temp: String? = null
> var size = -1
> if (temp != null)
> {
>     size = temp.length
> }
> 
> // 좀 더 줄이면 아래와 같습니다.
> var temp: String? = null
> val size = if (temp != null) temp.length else -1
> ```



## Safe Calls

- 물음표를 통해 null을 정의하고, null을 사용할 때는 ?.length와 같이 사용 가능.

  > ```kotlin
  > 
  > ```
  >
  > ```kotlin
  > 
  > ```
  >
  > - temp가 null이므로 temp.length는 성립되지 않습니다.
  > - temp?가 null 인가에서 return true이므로 size에는 null이 담기게 됩니다.



## 함수에서의 사용 방법

- 예시 : 함수는 null을 포함할 수 있는 변수 temp를 입력받아 Int?로 return하는 함수

  > ```kotlin
  > // 함수를 정의할 경우는
  > fun getSize(temp: String?): Int?
  > {
  >     return temp?.length
  > }
  > ```



## NULL을 완전히 배제하려면?

- null을 완전히 배제 하는 코드

- - Java

  - > ```kotlin
    > List<String> itemList = new ArrayList<>();
    > itemList.add("A");
    > itemList.add(null);
    > itemList.add("B");
    > 
    > for (String text : itemList)
    > {
    >     if (text != null) {
    >         Log.d("TAG", "Text : " + text);
    >     }
    > }
    > ```

- * Kotlin

    > ```kotlin
    > val listWithNulls: List<String?> = listOf("A", null, "B")
    > for (item in listWithNulls)
    > {
    >     item?.let { println(it) } // prints A and ignores null
    > }
    > ```
    >
    > .let{}는 ?.을 함께 사용하는 경우 if(type != null){}을 대체할 수 있다.

  * 두 코드 결과는 동일



## ?.을 이용하려면 null이 return되는데 다른 값을 하려면?

- if에 대체되는 문법이 ?라면, else에 대체되는 문법이 ?:이 됩니다.

  > ```kotlin
  > var temp: String? = null
  > val size = temp?.length ?: 0
  > ```
  >
  > Result : 0

  > ```kotlin
  > var temp: String? = null
  > val size = temp?.length
  > ```
  >
  > Result : null



## NPE를 발생시키려면??

- NullPointerException을 발생시키는 법

- - ?: 문법 뒤에 throw를 붙여서 Exception을 낼 수 있다.

  - > ```kotlin
    > var temp: String? = null
    > val size = temp?.length ?: throw IllegalArgumentException("temp is null")
    > ```
    >
    > ![image](images/kotlin_null_1.png)

* 단순히 NPE를 발생시키려면 !!을 사용해주면 훨씬 편해진다.

  > ```kotlin
  > var temp: String? = null
  > val size = temp!!.length
  > ```
  >
  > ![image](images/kotlin_null_2.png)



## 안전한 형 변환

- 현 변환이 불가능한 곳에서 형 변환을 시도할 경우 ?을 활용하여 오류가 발생하지 않게 할 수 있다.

- 예시

  > ```kotlin
  > val a: String? = "ABC"
  > 
  > // String을 강제로 형 변환 할 경우에는 CastException이 발생하여 이 경우 null이 저장
  > val aInt: Int? = a as? Int
  > 
  > // null이 아닌 0을 저장하려면
  > val aInt: Int? = a as? Int ?: 0
  > ```
  >
  > - String a를 aInt로 변환할 경우 null이 return됨
  > - ?: 을 함께 활용한다면 원하는 값으로 초가화도 가능



## filterNotNull

- List copy시 위에서 정의하였던 ?.let {}를 이용할 수도 있지만, 이미 구현된 코드가 filterNotNull이 있음

- null을 제외한 데이터를 새로운 list에 복사해주게 되어 null아이템을 제거하기 훨씬 변해진다.

  > ```kotlin
  > val nullableList: List<Int?> = listOf(1, 2, null, 4)
  > for (i in nullableList)
  > {
  >     print("${i} ")
  > }
  > println("")
  > 
  > // null filter
  > val intList: List<Int> = nullableList.filterNotNull()
  > for (i in intList)
  > {
  >     print("${i} ")
  > }
  > ```