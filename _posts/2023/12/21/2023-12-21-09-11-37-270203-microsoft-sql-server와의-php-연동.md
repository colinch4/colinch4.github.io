---
layout: post
title: "[php] Microsoft SQL Server와의 PHP 연동"
description: " "
date: 2023-12-21
tags: [php]
comments: true
share: true
---

이 기술 블로그에서는 PHP 어플리케이션에서 Microsoft SQL Server와의 연동에 대해 알아보겠습니다.

## 필요한 도구

PHP 어플리케이션에서 SQL Server와의 연동을 위해 [**SQLSRV 확장 프로그램**](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)이 필요합니다. 이 확장 프로그램을 사용하면 PHP에서 SQL Server에 접속하여 쿼리를 실행할 수 있습니다.

## 연결 설정

먼저, SQL Server와의 연결을 설정해야 합니다. `sqlsrv_connect()` 함수를 사용하여 SQL Server 데이터베이스에 연결할 수 있습니다.

예를 들어, 다음과 같이 연결 설정을 할 수 있습니다:

```php
<?php
$serverName = "localhost";
$connectionOptions = array(
    "Database" => "myDatabase",
    "Uid" => "myUsername",
    "PWD" => "myPassword"
);
$conn = sqlsrv_connect($serverName, $connectionOptions);
if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}
?>
```

위의 예제에서는 `localhost` 서버에 `myDatabase` 데이터베이스에 `myUsername`으로 연결하고 있습니다.

## 쿼리 실행

연결을 설정한 후에는 `sqlsrv_query()` 함수를 사용하여 SQL Server에 쿼리를 실행할 수 있습니다.

예를 들어, 다음과 같이 쿼리를 실행할 수 있습니다:

```php
<?php
$query = "SELECT * FROM myTable";
$result = sqlsrv_query($conn, $query);
if ($result === false) {
    die(print_r(sqlsrv_errors(), true));
}
?>
```

위의 예제에서는 `myTable` 테이블에서 모든 데이터를 가져오는 쿼리를 실행하고 있습니다.

## 결론

PHP 어플리케이션에서 Microsoft SQL Server와의 연동은 SQLSRV 확장 프로그램을 사용하여 간단하게 설정할 수 있습니다. 필요한 연결 설정과 쿼리 실행 방법을 이해하면 SQL Server와의 원활한 통합이 가능해집니다.

더 많은 정보를 원하시면 [**PHP 공식 문서**](https://www.php.net/manual/en/book.sqlsrv.php)를 참고하시기 바랍니다.