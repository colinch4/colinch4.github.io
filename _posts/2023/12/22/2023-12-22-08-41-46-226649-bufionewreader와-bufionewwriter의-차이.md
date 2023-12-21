---
layout: post
title: "[go] bufio.NewReader와 bufio.NewWriter의 차이"
description: " "
date: 2023-12-22
tags: [go]
comments: true
share: true
---

Go 언어의 `bufio` 패키지는 I/O 작업을 보다 효율적으로 수행하기 위한 기능을 제공합니다. 이 패키지는 버퍼링된 I/O 를 지원하며, `bufio.Reader` 와 `bufio.Writer` 는 이에 대한 기반을 제공합니다.

### bufio.NewReader와 bufio.NewWriter의 차이

`bufio.NewReader` 와 `bufio.NewWriter` 함수는 각각 읽기와 쓰기 작업을 위한 버퍼링된 리더와 라이터를 생성합니다. **차이점**은 다음과 같습니다:

- `bufio.NewReader` 는 주어진 리더로부터 데이터를 읽어오는 데 사용되며, 읽기 작업을 위해 버퍼를 생성합니다.
- `bufio.NewWriter` 는 주어진 라이터에 데이터를 쓰는 데 사용되며, 쓰기 작업을 위해 버퍼를 생성합니다.

### 예시

아래는 `bufio.NewReader` 와 `bufio.NewWriter` 의 사용 예시입니다.

```go
package main

import (
	"bufio"
	"os"
)

func main() {
	file, err := os.Open("example.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	reader := bufio.NewReader(file)
	writer := bufio.NewWriter(file)
	
	// bufio.Reader를 사용한 읽기 작업
	// bufio.Writer를 사용한 쓰기 작업
}
```

이 예시에서 `bufio.NewReader` 와 `bufio.NewWriter` 는 각각 파일에서 데이터를 읽고 쓰기 위한 기능을 제공하는 것을 볼 수 있습니다.

### 참고 자료

- [Go 언어 bufio 패키지 공식 문서](https://golang.org/pkg/bufio/)

이제 파일을 읽거나 쓸 때 어떤 상황에서 어떻게 사용해야 하는지에 대해 더 잘 이해할 수 있을 것입니다.