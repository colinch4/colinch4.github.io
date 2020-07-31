## DELETE

- 테이블의 레코드를 삭제

- 해당 테이블에서 WHERE절의 조건을 만족하는 레코드만을 삭제

- - **WHERE을 생략하면 모든 데이터 삭제!!**

> 문법
>
> ```mysql
> DELETE FROM 테이블이름
> WHERE 필드이름=데이터값
> ```

> 예시
>
> ```mysql
> DELETE FROM Reservation
> WHERE Name = '홍길동';
> ```