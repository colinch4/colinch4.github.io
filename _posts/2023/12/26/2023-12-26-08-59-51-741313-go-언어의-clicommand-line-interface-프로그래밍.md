---
layout: post
title: "[go] Go 언어의 CLI(Command Line Interface) 프로그래밍"
description: " "
date: 2023-12-26
tags: [go]
comments: true
share: true
---

CLI(Command Line Interface)는 사용자와 컴퓨터 사이의 상호작용을 위해 텍스트 명령을 사용하는 방법을 제공합니다. Go 언어는 이러한 CLI 프로그램을 개발하는 데 매우 적합한 언어입니다. Go 언어는 간결하고 효율적인 문법을 가지고 있으며, 병행성을 지원하여 대규모 CLI 프로그램을 쉽게 작성할 수 있도록 도와줍니다.

## CLI 프로그램 만들기

Go 언어를 사용하여 기본적인 CLI 프로그램을 만들어보겠습니다. 먼저, 프로그램의 진입점인 `main` 함수를 작성합니다. 

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("Hello, CLI!")
}
```

위의 예제는 가장 간단한 형태의 CLI 프로그램입니다. 프로그램을 실행하면 "Hello, CLI!"가 출력됩니다.

## CLI 플래그 사용하기

CLI 프로그램은 종종 명령행 인수(arguments)를 허용해야 합니다. `flag` 패키지를 사용하여 명령행 인수를 처리할 수 있습니다.

```go
package main

import (
	"flag"
	"fmt"
)

func main() {
	name := flag.String("name", "Guest", "사용자의 이름")
	flag.Parse()
	fmt.Printf("안녕하세요, %s님!\n", *name)
}
```

위의 예제는 `flag` 패키지를 사용하여 사용자의 이름을 인수로 받아 환영 메시지를 출력하는 CLI 프로그램입니다. 프로그램을 실행할 때 `-name` 플래그를 사용하여 사용자의 이름을 전달할 수 있습니다.

## 외부 라이브러리 활용

Go 언어는 다양한 외부 라이브러리를 활용하여 CLI 프로그램을 더욱 강력하게 만들 수 있습니다. 예를 들어, 테이블 형식의 출력을 위해 [`golang.org/x/tables`](https://pkg.go.dev/golang.org/x/tables) 라이브러리를 사용할 수 있습니다.

```go
package main

import (
	"fmt"
	"os"

	"golang.org/x/tables"
)

func main() {
	data := [][]string{
		{"이름", "나이"},
		{"철수", "30"},
		{"영희", "25"},
	}
	tables.Print(os.Stdout, data)
}
```

위의 예제는 `golang.org/x/tables` 라이브러리를 사용하여 테이블을 출력하는 기능을 갖춘 CLI 프로그램입니다.

CLI 프로그램을 개발할 때는 사용자 경험, 안정성, 처리 속도 등을 고려해야 합니다. Go 언어를 사용하면 이러한 측면을 고려하여 안정적이고 효율적인 CLI 프로그램을 쉽게 만들 수 있습니다.

Go 언어를 활용하여 CLI 프로그램을 개발해보세요. CLI 프로그래밍은 다양한 오픈소스 프로젝트에 기여하고, 자신만의 강력한 도구를 만들 수 있는 흥미로운 분야입니다.