# INSERT

### INSERT

- 테이블에 새로운 레코드 추가

  > 문법
  >
  > ```mysql
  > 1. INSERT INTO 테이블이름(필드이름1, 필드이름2, 필드이름3, ...)
  >    VALUES (데이터값1, 데이터값2, 데이터값3, ...)
  > 2. INSERT INTO 테이블이름
  >    VALUES (데이터값1, 데이터값2, 데이터값3, ...)
  > ```

  > 예제
  >
  > ```mysql
  > INSERT INTO Reservation(ID, Name, ReserveDate, RoomNum)
  > VALUES(5, '이순신', '2016-02-16', 1108);
  > ```

  > 예제
  >
  > ```mysql
  > INSERT INTO Reservation(ID, Name)
  > VALUES (6, '김유신');
  > ```



#### 삽입

> ```mysql
> INSERT INTO '테이블명' (column1, column2,…)  VALUES(column1에 들어갈 데이터, column에 들어갈 데이터,...);
> ```

* 예제

  > ```mysql
  > INSERT INTO topic (title,description,created,Author,profile) VALUES('MySQL','Mysql is ...',NOW(),'kangmoo','developer');
  > ```



#### row확인

> ```mysql
> SELECT * FROM '테이블이름';
> ```
>
> 테이블 이름으로부터 전부 show