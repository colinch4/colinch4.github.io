## ALTER

- 이미 존재하는 데이터베이스나 테이블의 구조나 형식등을 바꾸기 위해 사용

- - 칼럼의 구조나 형식을 변경하기 위해 사용

 

## 데이터베이스 수정

- ALTER DATABASE문은 데이터베이스의 전체적인 특성을 수정할 수 있게 해줌



> 문법
>
> ```mysql
> ALTER DATABASE 데이터베이스이름 CHARACTER SET=문자집합이름 #1
> ALTER DATABASE 데이터베이스이름 COLLATE=콜레이션이름 #2
> ```

> 예시
>
> ```mysql
> ALTER DATABASE Hotel CHARACTER SET=euckr_bin COLLATE=euckr_korean_ci;
> ```



## 자주 사용되는 CHRACTER SET

1. utf8 : UTF-8 유니코드를 지원하는 문자셋 (1~3바이트)
2. euckr : 한글을 지원하는 문자셋 (1~2바이트)

 

## 자주 사용되는 대표적인 COLLATE

1. utf8_bin
2. utf8_general_ci (기본설정)
3. euckr_bin
4. euckr_korean_ci

 

## 테이블 수정

- ALTER TALBE 문은 테이블에 필드를 추가, 삭제하거나 필드의 타입을 변경할 수 있게 해줌

1. ADD
2. DROP
3. MODIFY COLUMN

 

# 새로운 필드 추가

- ALTER TABLE 문과 함꼐 ADD 문을 사용하면, 테이블에 필드를 추가할 수 있음

> 문법
>
> ```mysql
> ALTER TABLE 테이블이름 ADD 필드이름 필드타입
> ```

> 예시
>
> ```mysql
> ALTER TABLE Reservation
> ADD Phone INT;
> ```



## 기존 필드의 삭제

- ALTER TABLE 문과 함께 DROP 문을 사용하면, 테이블의 필드를 삭제할 수 있음

> 문법
>
> ```mysql
> ALTER TABLE 테이블이름 DROP 필드이름
> ```

> 예시
>
> ```mysql
> ALTER TABLE Reservation
> DROP RoomNum;
> ```



## 필드 타입 변경

- ALTER TABLE 문과 함꼐 MODIFY COLUMN문을 사용하면, 테이블의 필드 타입 변경 가능

> 문법
>
> ```mysql
> ALTER TABLE 테이블이름 MODIFY COLUMN 필드이름 필드타입
> ```

> 예시
>
> ```mysql
> ALTER TABLE Reservation
> MODIFY COLUMN ReserveDate VARCHAR(20);
> ```