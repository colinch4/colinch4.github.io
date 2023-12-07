---
layout: post
title: "[go] 구조체(struct)를 JSON 형식으로 직렬화(Serialization)"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

구조체(struct)를 JSON 형식으로 직렬화(Serialization)하는 것은 많은 프로그래밍 언어에서 자주 사용되는 작업입니다. JSON은 데이터를 저장하고 교환하기 위한 가벼운 형식으로 널리 사용되고 있습니다. Go 언어에서는 encoding/json 패키지를 사용하여 구조체를 JSON으로 직렬화할 수 있습니다.

## encoding/json 패키지

Go 언어에서 제공하는 encoding/json 패키지는 JSON 형식으로 데이터를 인코딩하고 디코딩할 수 있는 기능을 제공합니다. 이 패키지를 사용하여 구조체를 JSON으로 직렬화할 수 있습니다.

## 예제 코드

아래는 구조체를 JSON으로 직렬화하는 예제 코드입니다.

```go
package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name    string `json:"name"`
	Age     int    `json:"age"`
	Address string `json:"address"`
}

func main() {
	person := Person{
		Name:    "John",
		Age:     30,
		Address: "123 Main St",
	}

	jsonData, err := json.Marshal(person)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}

	fmt.Println(string(jsonData))
}
```

위의 코드에서는 Person이라는 구조체를 정의하고, Name, Age, Address라는 필드를 가지고 있습니다. 구조체를 JSON으로 직렬화하기 위해 encoding/json 패키지의 Marshal 함수를 사용하였습니다.

## 실행 결과

위의 예제 코드를 실행하면 다음과 같은 결과가 출력됩니다.

```shell
{"name":"John","age":30,"address":"123 Main St"}
```

위 결과는 구조체가 JSON 형식으로 직렬화된 결과입니다.

## 결론

Go 언어에서는 encoding/json 패키지를 사용하여 구조체를 JSON 형식으로 직렬화할 수 있습니다. 이를 통해 구조체를 다른 시스템과 데이터를 교환할 때 유용하게 사용할 수 있습니다.

더 자세한 내용은 [Go 공식 문서](https://golang.org/pkg/encoding/json/)를 참조하시기 바랍니다.