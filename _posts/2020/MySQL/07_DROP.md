## DROP

- MySQL에서는 DROP을 이용하여 데이터베이스와 테이블 삭제 가능



## 데이터베이스 삭제

> 문법
>
> ```mysql
> DROP DATABASE 데이터베이스이름
> ```

> 예시
>
> ```mysql
> DROP DATABASE Hotel;
> ```



## 테이블 삭제

> 문법
>
> ```mysql
> DROP TABLE 테이블이름
> ```

> 예시
>
> ```mysql
> DROP TABLE Reservation;
> ```

## 테이블의 데이터만을 삭제

> 문법
>
> ```mysql
> TRUNCATE TABLE 테이블이름
> ```

> 예시
>
> ```mysql
> TRUNCATE TABLE Reservation;
> ```