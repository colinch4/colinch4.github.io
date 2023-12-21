---
layout: post
title: "[go] bufio.Writer와 bufio.Reader의 차이점"
description: " "
date: 2023-12-22
tags: [go]
comments: true
share: true
---

Go 언어에서는 I/O 성능을 향상시키기 위해 `bufio` 패키지를 제공합니다. 이 패키지에는 데이터를 버퍼링하고 읽고 쓰는 기능을 제공하는 `bufio.Writer`와 `bufio.Reader`가 있습니다. 이 두 개체의 주요 차이점을 알아보겠습니다.

## bufio.Writer

`bufio.Writer`는 데이터를 버퍼에 씁니다. 데이터를 작은 조각으로 나누어 버퍼에 저장한 다음, 특정 조건이 충족되면 실제로 작성됩니다. 이는 작은 크기의 데이터를 여러 번 작성하는 경우에 I/O 작업을 줄여 성능을 향상시킬 수 있습니다.

아래는 `bufio.Writer`의 간단한 예제 코드입니다.

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Create("output.txt")
	defer file.Close()
	writer := bufio.NewWriter(file)
	writer.WriteString("Hello, ")
	writer.WriteString("bufio.Writer!")
	writer.Flush()
}
```

## bufio.Reader

한편, `bufio.Reader`는 스트림에서 데이터를 읽어 버퍼에 저장합니다. 이를 통해 읽기 작업이 빨라지며, 내부적으로 I/O를 줄일 수 있습니다. 또한, 읽은 데이터를 버퍼에서 특정 단위로 읽어오거나 한 번에 전체 데이터를 읽을 수 있습니다.

아래는 `bufio.Reader`의 예제 코드입니다.

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	file, _ := os.Open("input.txt")
	defer file.Close()
	reader := bufio.NewReader(file)
	data, _ := reader.Peek(5)
	fmt.Printf("First 5 bytes: %s", data)
}
```

`bufio.Writer`와 `bufio.Reader`는 각각 데이터를 쓰고 읽는 작업에 최적화되어 있으며, 적절하게 사용함으로써 Go 언어의 성능을 향상시킬 수 있습니다.

더 자세한 정보는 [Go 언어 공식 문서](https://pkg.go.dev/bufio)를 참고하십시오.

성능 향상을 위한 다양한 기술 및 라이브러리는 [Go 성능 최적화 방법](https://dave.cheney.net/high-performance-go-workshop/dotgo-paris.html)을 참고하십시오.