---
layout: post
title: "[PHP] PHP"
description: " "
date: 2021-11-19
tags: [PHP]
comments: true
share: true
---

# A

## array_merge

둘 이상의 배열을 병합해 준다.

`function array_merge (array $array1, array $array2 = null, array $_ = null) array`

```php
$toms_pet = '{"cat": 5, "dog": 3}';
$johns_pet = '{"cat": 10, "dog": 1, "parrot": 1}';

$pets = array_merge(json_decode($toms_pet),json_decode($johns_pet));
```

- **Return values**
  - array ⇒ 병합된 배열이 리턴된다.  
    - Key 가 string 일 시  
      배열에 동일한 Key 가 존재한다면 해당 Key 의 값은 제일 마지막으로 덧붙여진 배열의 값으로 대체된다.
    - Key 가 Numeric 일 시  
      key 가 numeric 형태라면 해당 키값에 덮어쓰기가 진행되는 것이 아니라, 기존 array 에 다른 array 가 덧붙여진다. Key 는 1씩 증가된다.

      ```php
      $numeric_array1 = array(1=>'Last Year', 3=>2020);
      $numeric_array2 = array(1=>'Current Year', 3=>2021);
      print_r(array_merge($numeric_array1, $numeric_array2));
      ```
      ```php
      // RESULT
      Array
      (
          [0] => Last Year
          [1] => 2020
          [2] => Current Year
          [3] => 2021
      )
      ```

# D

## define

Constant 를 정의해준다(runtime 시 정해짐).

`define ( string $name , mixed $value , bool $case_insensitive = false ) : bool`

```php
define('ICECREAM', $icecream)
```

- **Parameters**
  - `name` : 상수명

    예약어와 겹치는 이름 조차 define 으로 정의 가능.  
    - 해당 상수(예약어와 겹치는 이름을 지닌) 값을 가져오려 할 때에는 `constant()` 를 사용해야 한다. → 비록 가능하더라도 지양할 것

  - `value` : 상수 값

    값은 scalar value(a single value) 또는 array
    - int
    - float
    - string
    - bool
    - null
    - array
  - `case_insensitive`
    - default: false ⇒ case sensitive

- **Return values**
  - Success ⇒ `true`
  - Failure ⇒ `false`


# E

## end

Array 에 사용한다. 배열의 내부 포인터가 마지막 요소를 가리키도록 한다.

`end ( array|object &$array ) : mixed`
```php
$moods = array('confident', 'enlightened', 'hopeful', 'amused');
echo end($moods); // amused
```

- **Parameters**
  - array

- **Return values**
  - Success → `마지막 요소의 값`
  - Empty Array → `false`

## explode

문자열을 split 해준다.

`explode ( string $separator , string $string , int $limit = PHP_INT_MAX ) : array`

```php
$finance = "account bank credit debit EBT";
$result = explode(" ", $finance, -1);

echo $result[0]; // account
echo $result[3]; // debit
echo $result[4]; // Undefined array key
```

- **Parameters**
  - `separator`
    - `""` : seperator 를 빈 스트링으로 설정했다면 `false` 가 리턴된다.
  - `string`
    - split 할  문자열
  - `limit`
    - 양수 : maximum
    - 음수 : -limit 만큼 제외
    - `0` : 1 로 취급 (1번만 split 함)

- **Return Values**
  - string array
    나뉜 문자열들이 배열에 담겨 리턴된다.


# H

## http_build_query

URL-encoded 된 문자열로 만들어준다.

`http_build_query( mixed $data, string $numeric_prefix = ?, string $arg_separator = ?,int $encoding_type = PHP_QUERY_RFC1738): string`

```php
$data = array(
  'limit' => 10,
  'keyword' => "prime",
  'is_deleted' => false
);

echo http_build_query($data) . "\n"; // limit=10&keyword=prime&is_deleted=0
```

- **Parameters**
  - `data`  
    배열 또는 객체
    - **배열**: 일차원 배열, 또는 다른 배열을 포함한 배열
    - **객체**: Public 속성들만 결과에 나타남

  - `numeric_prefix`  
    주어진 `data`가 배열인 경우 Key 값이 0, 1, 2 ... n+1 형태로 주어진다.  
    `numeric_prefix`를 통해 Key 에 prefix 를 더해줄 수 있다.  
    ```php
    $data = array( 'zero', 'one');

    echo http_build_query($data, 'number'); // number_0=zero&number_1=one 
    ```

  - `arg_separator`  
    구분자를 통해 요소들을 나누어 줄 수 있다.  
    만약 `arg_separator`를 지정해 주지 않으면, [`arg_separator.output`](http://new.lug.or.kr/files/docs/PHP/ini.core.html#ini.arg-separator.output) 이 사용된다.  

  - `encoding_type`  
    기본 인코딩 유형은 **PHP_QUERY_RFC1738**  
    - **PHP_QUERY_RFC1738**  
      [RFC 1738](http://www.faqs.org/rfcs/rfc1738.html)
      - 공백: `+` 로 인코딩 됨.
    - **PHP_QUERY_RFC3986**  
      [RFC 3986](http://www.faqs.org/rfcs/rfc3986.html)
      - 공백: `%20` 로 인코딩 됨.

- **Return Value**  
  URL-encoded 된 문자열


# I

## isset

변수가 선언이 되었는지 확인해준다.

- different than `null`
- 만약 변수가 `unset()` 을 함수를 거쳤다면, 해당 변수는 set 되었다고 취급되지 X.

`isset ( mixed $var , mixed ...$vars ) : bool`

```php
$you = array ('💩' => 1, '🍠' => NULL);

var_dump(isset($you['💩']));  // TRUE
var_dump(isset($you['🍠']));  // FALSE
```

- **Parameters**
  - `var` : 체크할 변수
  - `vars` : 그외에 더 체크하고픈 변수들  
    왼쪽부터 차례대로 검증하며 `unset`된 변수를 맞딱들이는 순간 검증을 멈추고 `false`를 리턴.

- **Return Values**
  - `true` : value 가 존재 할 시
  - `false` : value 가 `null` 인 경우
    - null character 인 `\0` 는 `null`로 취급되지 않기에 `true` 가 리턴되니 주의!


# S

## strpos
String 에 담겨 있는 substring 의 position 을 찾아준다.

`strpos ( string $haystack , string $needle , int $offset = 0 ) : int|false`

```php
$tasty = 'vanilla-icecream'; 
$findme = 'cream';
$pos = strpos($tasty, $findme); // 11
```

- **Parameters**
  - `haystack` : whole 문자열
  - `needle` : 찾고자 하는 문자열
    - 문자열이 아니면 integer 로 형변환됨.
      - 8.0.0 부터 integer passing 은 더이상 지원 안됨.
  - `offset`
    - 문자열의 시작점 부터 카운트 됨.
    - `-` : 음수일 시 문자열 끝지점 부터 카운트 됨.

- **Return Value**
  - `integer`: 찾음  
    (whole 문자열에서) 찾은 문자열의 시작 위치

  - `boolean` : 못찾음  
    못찾은 경우 `false` 를 리턴.

  **`%주의%`**
  - return 된 결과를 boolean 으로 비교연산 하고자 한다면 반드시 `===` 를 사용해야 한다.
    → 그 이유는 needle 이 haystack 의 첫번째 위치에 와 있을 경우 `0` 이 리턴되는데 `==`로 비교할 경우 0 은 falsy 값으로서 비교되기 때문.

    - 부정형은 `!==`
