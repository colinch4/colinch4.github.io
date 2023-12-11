---
layout: post
title: "[go] Go 언어에서 ORM(Object-Relational Mapping) 라이브러리를 활용한 데이터베이스 연동 방법"
description: " "
date: 2023-12-11
tags: [go]
comments: true
share: true
---

개발자들이 데이터베이스와 상호 작용할 때 사용하는 ORM(Object-Relational Mapping)은 객체 지향 프로그래밍 언어와 관계형 데이터베이스 간의 호환성을 제공합니다. **Go** 언어의 ORM 라이브러리들은 데이터베이스와의 상호 작용을 단순화하고 생산성을 향상시킵니다.

이번 블로그에서는 **Go** 언어에서 ORM 라이브러리를 사용하여 데이터베이스를 연동하는 방법을 다룰 것입니다. 우리는 `gorm` 라이브러리를 사용하여 MySQL 데이터베이스에 연결하는 과정을 살펴볼 것입니다.

## 목차
1. [gorm 라이브러리 설치](#install-gorm)
2. [데이터베이스 모델 정의](#define-database-models)
3. [데이터베이스 연결 설정](#database-connection-setup)
4. [데이터베이스 연동 테스트](#test-database-connection)

## 1. gorm 라이브러리 설치 <a name="install-gorm"></a>
가장 먼저, gorm 라이브러리를 설치해야 합니다. 아래의 명령어를 사용하여 gorm 라이브러리를 설치합니다.

```sh
go get -u github.com/jinzhu/gorm
```

## 2. 데이터베이스 모델 정의 <a name="define-database-models"></a>
다음으로, 데이터베이스 모델을 정의해야 합니다. 예를 들어, 사용자 모델을 정의하는 방법은 다음과 같습니다.

```go
package models

import "github.com/jinzhu/gorm"

type User struct {
    gorm.Model
    Username  string
    Email     string
}
```

위의 코드에서, 우리는 `gorm.Model`을 임베드하여 각 모델에 대한 일반적인 필드들을 정의할 수 있습니다.

## 3. 데이터베이스 연결 설정 <a name="database-connection-setup"></a>
이제, 데이터베이스에 연결하는 설정을 해야 합니다. 아래의 예제는 **MySQL** 데이터베이스에 대한 연결 설정을 보여줍니다.

```go
package main

import (
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
    db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
    if err != nil {
        panic("failed to connect database")
    }
    defer db.Close()
}
```

위의 코드에서, `gorm.Open` 함수를 사용하여 MySQL 데이터베이스에 연결하고, 에러를 체크하여 연결 여부를 확인할 수 있습니다.

## 4. 데이터베이스 연동 테스트 <a name="test-database-connection"></a>
마지막으로, 연결이 제대로 설정되었는지 확인하기 위해 데이터베이스 연동 테스트를 수행합니다.

```go
package main

import (
    "fmt"
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
)

func main() {
    db, err := gorm.Open("mysql", "user:password@/dbname?charset=utf8&parseTime=True&loc=Local")
    if err != nil {
        panic("failed to connect database")
    }
    defer db.Close()

    if db.DB().Ping() != nil {
        panic("failed to ping database")
    }

    fmt.Println("Successfully connected to database")
}
```

위의 예제에서, `Ping` 메서드를 사용하여 데이터베이스와의 연결을 확인합니다.

이제, **Go** 언어에서 **gorm** 라이브러리를 사용하여 데이터베이스를 연동하는 방법에 대해 알아보았습니다. ORM 라이브러리를 활용하면, 데이터베이스와 상호 작용하는 것이 훨씬 간편해질 뿐만 아니라 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

끝.