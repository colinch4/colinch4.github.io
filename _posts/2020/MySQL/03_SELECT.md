## 모든 데이터 출력

> `SELECT * FROM '테이블명';`

 

## 열 선택

- `SELECT 'column이름','column이름',... FROM '테이블명';`

- - FROM 생략 가능

- 예시

- - `SELECT id,title,created,author FROM topic;`

 

## 특정 이름을 가진 애들 선택

- `SELECT 'column이름' FROM '테이블명' WHERE '이름';`

- 예시

- - `SELECT id,title,created,author FROM topic WHERE author='kangmoo';`

 

## 정렬

- `SELECT 'column이름' FROM '테이블명' WHERE '이름' ORDER BY 'column이름' DESC;`

- - DESC : 역순정렬

- 예시

- - `SELECT id,title,created,author FROM topic WHERE author='kangmoo' ORDER BY id DESC;`

 

> ```mysql
> #정렬하지 않은 경우
> SELECT * FROM 테이블;
> 
> #오름차순 정렬
> SELECT * FROM 테이블 ORDER BY 컬럼1 ASC;
> 
> #오름차순 정렬 (ASC 생략)
> SELECT * FROM 테이블 ORDER BY 컬럼1;
> 
> #내림차순 정렬
> SELECT * FROM 테이블 ORDER BY 컬럼1 DESC;
> 
> #여러 컬럼으로 정렬
> SELECT * FROM 테이블 ORDER BY 컬럼1 [, 컬럼2, 컬럼3 ...];
> 
> #조건식이 있는 경우 정렬
> SELECT * FROM 테이블 WHERE 조건식 ORDER BY 컬럼1 [, 컬럼2, 컬럼3 ...];
> 
> #컬럼 번호로 정렬
> SELECT * FROM 테이블 WHERE 조건식 ORDER BY 컬럼 번호1 [, 컬럼 번호2, 컬럼 번호3 ...];
> ```

