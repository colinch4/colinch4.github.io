## jQuery란?

* 자바스크립트를 쉽게 사용하기 위한 라이브러리

  * 가볍고, 적게 쓰고 더 많은 기능

* HTML태그를 선택하고 태그의 액션을 수행하는데 안성맞춤

* 가장 기본적인 문법은 `$(selector).action()`이다

  * `$`기호는 jQuery를 정의/접근하는 기호다

  * 예시

    > ```javascript
    > $(this).hide() // 현재 태그를 숨긴다
    > $("p").hide() // p 태그를 숨긴다
    > $(".test).hide() // "test" 클래스의 모든 태그를 숨긴다
    > $("#test").hide() // id가 "test"인 모든 태그를 숨긴다
    > ```





## $(document).ready()

* jQuery를 사용한 모든 웹 페이지는 다음 코드로 시작

  > ```javascript
  > $(document).ready(function () {
  > 	// jQuery Method go here ...
  > })
  > ```

  > ```javascript
  > $(function(){
  >    // jQuery methods go here...
  > });
  > ```
  >
  > 약식으로 이렇게 쓸 수도 있다



## 선택자

* jQuery 메서드의 가장 기본적인 형태

* 선택자는 jQuery에서 가장 중요한 역할

* jQuery 메서드의 기본 형태

  - $ + 선택자 + 메서드

    >
    > ```javascript
    > $('h1').css('color','red');
    > // 선택자 : $('h1')
    > // 메서드 : .css('color,'red');
    > ```
    

#### 기본 선택자

> ```javascript
> // ID 셀렉터를 단독으로 사용할 경우에는 하나의 요소만 선택 된다. why? ID는 고유하게 사용하기 때문
> $("#a").css("color", "blue");
> // 클래스는 . 을 사용한다
> $(".test").css("border", "solid 1px gray");
> // 해당 태그의 속성을 준다
> $("h1").css("font-style", "italic");
> ```

> ```javascript
> // ID 셀렉터를 복수로 사용하면 모두 선택
> $("div#a").css("color", "blue");
> // 클래스는 . 을 사용한다 and 조건
> $(".test.main").css("border", "solid 1px gray");
> // 해당 태그의 속성을 준다 or 조건
> $("#a, h1").css("font-style", "italic");
> ```



#### 계층 선택자

* 기본 선택자의 앞에 붙여 사용하며 기본 선택자의 범위를 제한

- 자식선택자 : 바로 아래 계층

  > ```javascript
  > // 다음 형제들 중 div만 선택
  > $("#korean > div").css("border", "dashed 3px gray");
  > ```

- 후손선택자 : 아래 계층 전부

  > ```javascript
  > // 한칸 공백은 후손선택자
  > $("#foods tr").css("background-color", "aqua");
  > ```



#### 필터 선택자

- jQuery확장 필터라서 매우 느림

  - 가능하면 안쓰는게 좋음

  > ```javascript
  > $("#foods tr:odd").css("background-color", "aqua");
  > $("#foods tr:even").css("background-color", "#FFCCCC");
  > $("#foods tr:first").css("background-color", "purple").css("color", "yellow");
  > $("#foods tr:eq(3)").css("font-style", "italic");
  > ```



#### 속성 성택자

* 입력 양식과 관련된 태그를 선택할 때 많이 사용됨

| 선택자 형태        | 설명                                                    |
| ------------------ | ------------------------------------------------------- |
| 요소[속성=값]      | 속성과 값이 같은 문서 객체 선택                         |
| 요소[속성!=값]     | 속성 안의 값이 특정 값과 같은 문서 객체 선택            |
| 요소[속성~=값]     | 속성 안의 값이 특정 값을 단어로 시작하는 문서 객체 선택 |
| **요소[속성^=값]** | 속성 안의 값이 특정 값으로 시작하는 문서 객체 선택      |
| **요소[속성$=값]** | 속성 안의 값이 특정 값으로 끝나는 문서 객체 선택        |
| 요소[속성*=값]     | 속성 안의 값이 특정 값을 포함하는 문서 객체 선택        |



#### 필터 선택자

* 선택자중에 `:`기호를 포함하는 선택자

| 선택자 형태   | 설명                              |
| ------------- | --------------------------------- |
| 요소:checked  | 체크되어있는 입력 양식 선택       |
| 요소:disabled | 비활성화된 입력 양식 선택         |
| 요소:enabled  | 활성화된 입력 양식 선택           |
| 요소:focus    | 초점이 맞춰져 있는 입력 양식 선택 |
| 요소:input    | 모든 입력 양식 선택               |
| 요소:selected | option객체 중 선택된 태그 선택    |




## 이벤트 메서드



#### DOM이벤트 몇개..

| Mouse Events | Keyboard Events | Form Events | Document/Window Events |
| :----------- | :-------------- | :---------- | :--------------------- |
| click        | keypress        | submit      | load                   |
| dblclick     | keydown         | change      | resize                 |
| mouseenter   | keyup           | focus       | scroll                 |
| mouseleave   |                 | blur        | unload                 |



#### 사용 예시

> ```javascript
> $("p").click(function(){
>   // action goes here!!
> });
> ```

> ```javascript
> $("p").on({
>   mouseenter: function(){
>     $(this).css("background-color", "lightgray");
>   },
>   mouseleave: function(){
>     $(this).css("background-color", "lightblue");
>   },
>   click: function(){
>     $(this).css("background-color", "yellow");
>   }
> });
> ```



## 배열관리

* jQuery로 배열을 관리할 때는 `each()`메서드를 사용
* `each()`메서드는 매개변수로 입력한 함수로 for in반복문처럼 객체나 배열의 요소를 검사하는 메서드
* `each()`메서드는 다음과 같이 두가지 형태로 사용됨
  * `$.each(obejct, function(index, item) { ... })`
  * `$(selector).each(function(index, item) { ... })`



## Get and Set CSS Classes

- jQuery는 CSS요소를 쉽게 조작할 수 있으며 조작을 위한 여러 메소드를 제공하고 있음
  - `addClass()` : 선택된 요소를 위한 하나 또는 그 이상의 클래스를 더한다.

    > ```javascript
    > $("button").click(function(){
    >     $("h1, h2, p").addClass("blue");
    >     $("div").addClass("important");
    > });
    > ```

  - `removeClass()` : 선택된 클래스로부터 하나 또는 그 이상을 제거한다. 

    > ```javascript
    > $("button").click(function(){
    >     $("h1, h2, p").removeClass("blue");
    > });
    > ```

  - `toggleClass()` : Toggle 선택된 클래스로부터 더거나 지운다.

    > ```javascript
    > $("button").click(function(){
    >     $("h1, h2, p").toggleClass("blue");
    > });
    > ```

  - `css()` : 스타일 속성을 set 또는 리턴한다. 

    

## jQuery Dimensions

* jQuery는 윈도우 브라우저 요소의 면적, 치수를 쉽게 작업할 수 있음
  * `width()`
  * `height()`
  * `innerWidth()`
  * `innerHeight()`
  * `outerWidth()`
  * `outerHeight()`



