---
layout: post
title: "[go] 구조체(struct)를 XML 형식으로 직렬화(Serialization)"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

구조체(struct)를 XML 형식으로 직렬화(Serialization)하는 방법에 대해 알아보겠습니다. XML은 데이터를 계층 구조로 표현하는 인기있는 형식이며, 다양한 프로그래밍 언어에서 데이터를 저장하고 전송하는 데 사용됩니다. 

## 1. encoding/xml 패키지

Go 언어에서 XML 형식으로 직렬화하기 위해 `encoding/xml` 패키지를 사용합니다. 이 패키지는 XML 태그를 정의하는 구조체를 만들고, 해당 구조체를 XML 형식으로 변환할 수 있는 기능을 제공합니다.

```go
import (
    "encoding/xml"
    "fmt"
    "os"
)

type Person struct {
    XMLName xml.Name `xml:"person"`
    Name    string   `xml:"name"`
    Age     int      `xml:"age"`
    Email   string   `xml:"email"`
}

func main() {
    person := Person{
        Name:  "John Doe",
        Age:   30,
        Email: "johndoe@example.com",
    }

    file, err := os.Create("person.xml")
    if err != nil {
        fmt.Println("Error creating XML file:", err)
        return
    }
    defer file.Close()

    encoder := xml.NewEncoder(file)
    encoder.Indent("", "    ")
    err = encoder.Encode(person)
    if err != nil {
        fmt.Println("Error encoding XML:", err)
        return
    }

    fmt.Println("XML file created successfully.")
}
```

위의 예제에서는 `Person`이라는 구조체를 정의하고, `XMLName` 필드를 사용하여 루트 엘리먼트의 이름을 지정합니다. 그리고 `xml` 태그를 이용하여 필드와 XML 엘리먼트 간의 매핑을 정의합니다.

`main` 함수에서는 `Person` 구조체의 인스턴스를 생성하고, 이를 XML 파일로 직렬화합니다. `os.Create` 함수로 XML 파일을 생성하고, `xml.NewEncoder` 함수로 인코더를 생성합니다. 인코더의 `Encode` 함수를 사용하여 구조체를 XML 형식으로 변환 후 파일에 쓰여지게 됩니다.

## 2. XML 파일 결과

위 예제를 실행하면 "person.xml"이라는 이름의 XML 파일이 생성됩니다. 그리고 해당 파일을 열어보면 아래와 같은 XML 형식으로 변환된 것을 확인할 수 있습니다.

```xml
<person>
    <name>John Doe</name>
    <age>30</age>
    <email>johndoe@example.com</email>
</person>
```

## 3. 요약

이번 글에서는 Go 언어에서 구조체를 XML 형식으로 직렬화하는 방법을 소개했습니다. `encoding/xml` 패키지를 사용하여 구조체를 XML 형식으로 변환한 후 파일로 저장하거나 다른 시스템과 데이터를 교환하는 데 사용할 수 있습니다. Go 언어는 XML을 다루기 위한 기본 라이브러리와 강력한 기능을 제공하기 때문에, 이를 활용하여 복잡한 데이터 구조를 XML로 표현하는 작업을 할 수 있습니다. 

더 자세한 내용은 [Go 공식 문서](https://golang.org/pkg/encoding/xml/)를 참고하시기 바랍니다.