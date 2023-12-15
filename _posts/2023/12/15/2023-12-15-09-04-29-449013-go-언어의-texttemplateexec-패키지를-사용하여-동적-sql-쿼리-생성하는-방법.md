---
layout: post
title: "[go] go 언어의 text/template/exec 패키지를 사용하여 동적 SQL 쿼리 생성하는 방법"
description: " "
date: 2023-12-15
tags: [go]
comments: true
share: true
---

고(Go) 언어를 사용하는 개발자들은 SQL 쿼리를 동적으로 생성하고자 할 때 종종 템플릿을 사용합니다. go 언어에서는 text/template 패키지를 통해 이를 간단하게 할 수 있습니다. 또한, 동적으로 생성한 SQL 쿼리를 실행하기 위해 exec 패키지를 사용할 수 있습니다. 이 블로그 포스트에서는 go 언어의 text/template와 exec 패키지를 사용하여 동적 SQL 쿼리를 생성하는 방법을 살펴보겠습니다.

## text/template 패키지를 이용한 동적 SQL 템플릿 생성

text/template 패키지를 사용하여 동적 SQL 쿼리를 생성하기 위해서는 먼저 다음과 같이 템플릿을 정의해야 합니다.

```go
package main

import (
	"os"
	"text/template"
)
{% raw %}
func main() {
	sqlTemplate := "SELECT * FROM users WHERE {{.Condition}};"

	tmpl, err := template.New("sqlTemplate").Parse(sqlTemplate)
	if err != nil {
		panic(err)
	}

	data := struct {
		Condition string
	}{
		Condition: "age > 30",
	}

	err = tmpl.Execute(os.Stdout, data)
	if err != nil {
		panic(err)
	}
}
{% endraw %}
```

위 예제에서는 `sqlTemplate` 문자열에 SQL 쿼리의 템플릿을 정의하고, text/template 패키지를 사용하여 데이터를 주입하여 최종 SQL 쿼리를 생성하고 출력합니다.

## exec 패키지를 이용한 동적 SQL 쿼리 실행

이제 동적으로 생성한 SQL 쿼리를 실행해보겠습니다. exec 패키지를 사용하여 데이터베이스와의 인터페이스를 생성하고, SQL 쿼리를 실행할 수 있습니다.

```go
package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql", "user:password@tcp(localhost:3306)/dbname")
	if err != nil {
		panic(err)
	}
	defer db.Close()

	rows, err := db.Query("SELECT * FROM users WHERE age > 30")
	if err != nil {
		panic(err)
	}
	defer rows.Close()

	for rows.Next() {
		var id int
		var name string
		err = rows.Scan(&id, &name)
		if err != nil {
			panic(err)
		}
		fmt.Println(id, name)
	}
	err = rows.Err()
	if err != nil {
		panic(err)
	}
}
```

위 예제에서는 `database/sql` 패키지를 사용하여 MySQL 데이터베이스에 연결하고, 생성한 동적 SQL 쿼리를 실행하는 방법을 보여줍니다.

이렇듯 text/template와 exec 패키지를 사용하면 go 언어에서 동적 SQL 쿼리를 쉽게 생성하고 실행할 수 있습니다. 
   
더 많은 go 언어 관련 정보는 [공식 Go 언어 웹사이트](https://golang.org/)에서 확인할 수 있습니다.