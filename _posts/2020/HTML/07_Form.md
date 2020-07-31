# Form



- 사용자가 서버로 정보를 전송할 때 사용

- 사용자가 웹사이트에 데이터를 전송하는 것을 허용하는 태그

- 일반적으로 데이터는 웹 서버로 전송되지만 웹페이지가 데이터를 사용하기 위해 사용할 수도 있음

- - method = "get"

    - 서버로부터 사용자가 데이터를 가져올 때 사용
    - url로 데이터 전송
    - querystring으로 값을 전달

  - method = "post"

    - 서버의 데이터를 수정, 삭제, 생성할 때 사용

- `form`태그의 내용은`submit`을 만나면 `action`의 주소로 값을 전달한다.

  - `form`태그는 `action`속성과 함께 와야한다.

- `input`태그는 `name`을 가지고 있어야 한다

  - 그래야 구분하니까..

- 예시

  > ```HTML
  > <form action = "https://localhost:3000/process_create" method = "post">
  >     <p><input type="text" name = "title"></p>
  >     <p>
  >         <textarea name = "description"></textarea>
  >     </p>
  >     <p>
  >         <input type="submit">
  >     </p>
  > </form>
  > ```

  > ```html
  > <form action="regist.html" method="POST">
  >     이름 : <input type="text" placeholder="이름을 입력하십시오" name="name"> <br/>
  >     아이디 : <input type="text" placeholder="아이디를 입력하십시오" name="id"> <br/>
  >     비밀번호 : <input type="password" placeholder="비밀번호를 입력하십시오"name="pwd"> <br/>
  >     남성 : <input type="radio" name="gender">
  >     여성 : <input type="radio" name="gender"> <br/>
  >     사용하는 SNS :
  >     <input type="checkbox" name="sns"> Facebook
  >     <input type="checkbox" name="sns"> Twitter
  >     <input type="checkbox" name="sns"> Instagram
  >     <input type="checkbox" name="sns"> Google+
  >     <br/>
  >     연령 : 
  >     <select name="age">
  >         <option value="10">10대</option>
  >         <option value="20">20대</option>
  >         <option value="30">30대</option>
  >     </select>
  >     <br/>
  >     사진 : 
  >     <input type="file" name="profile"> <br/>
  >     자기소개 : 
  >     <textarea cols = "40" rows="5" name="intro"> </textarea><br/>
  >     <input type="submit" value="회원가입">
  >     <input type="reset" value="초기화">
  >     <input type="button" value="임시 저장">
  > </form>
  > ```

