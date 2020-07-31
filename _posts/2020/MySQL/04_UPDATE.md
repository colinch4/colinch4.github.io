## UPDATE

- 해당 테이블에서 **WHERE**절의 조건을 만족하는 레코드의 값만을 수정

- - WHERE을 빠뜨리면 전부 바뀌니까 꼭 조심하자!!

> 문법
>
> ```mysql
> UPDATE 테이블이름
> SET 필드이름1=데이터값1, 필드이름2=데이터값2, ...
> WHERE 필드이름=데이터값
> ```

> 예시
>
> ```mysql
> UPDATE Reservation
> SET RoomNum = 2002
> WHERE Name = '홍길동';
> ```