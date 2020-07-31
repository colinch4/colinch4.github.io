



## 기본

* `$.ajax()`메서드는 다음 두 가지 형태

  * `$.ajax(options);`

    > ```javascript
    > $.ajax({
    >     url:"./data.html",
    >     success:function(data){},
    >     error:function(){}
    > })
    > ```

  * `$.ajax(url, options);`

    > ```javascript
    > $.ajax("./data.html",{
    >     success:function(data){},
    >     error:function(){}
    > });
    > ```







| 메서드 이름                    | 설명                                                    |
| ------------------------------ | ------------------------------------------------------- |
| `$.ajax()`                     | 범용적인 Ajax 관련 메서드                               |
| `$.get()`                      | get방식으로 Ajax 수행                                   |
| `$.post()`                     | post방식으로 Ajax 수행                                  |
| `$.getJSON()`                  | ㅎㄷㅅqkdtlrdmfh 멈ㅌtngodgo                            |
| `$.getScrpit()`                | get방식으로 Ajax를 수행해 Script데이터를 가져옴         |
| `$(<선택자>).load()`           | Ajax를 수행하고 선택자료 선택한 문서 객체 안에 집어넣음 |
| `$(<선택자>).serialize()`      | 입력 양식의 내용을 요청 매개벼수 문자열로 만듦          |
| `$(<선택자>).serializeArray()` | 입력 양식의 내용을 객체로 만듦                          |
| `$.param()`                    | 객체의 내용을 요청 매개변수 문자열로 만듦               |

