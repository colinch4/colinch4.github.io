---
layout: post
title: "[go] go 언어의 source code formatting"
description: " "
date: 2023-12-15
tags: [go]
comments: true
share: true
---

Go 언어는 강력한 표준 라이브러리와 간결하고 가독성이 높은 문법으로 많은 개발자들에게 인기를 얻고 있습니다. Go 언어에서 코드를 작성할 때 코드 서식을 맞추는 것은 중요한 부분입니다. 코드 서식을 맞추면 코드의 가독성이 좋아지고 유지보수가 쉬워집니다. Go 언어에서 코드 서식을 맞추는 데 사용되는 도구에는 `gofmt`와 `goimports`가 있습니다.

## gofmt
`gofmt`는 Go 언어에서 코드를 서식에 맞게 자동으로 정렬해주는 도구입니다. 이를 통해 일관된 코드 형식을 유지할 수 있고, 들여쓰기, 공백, 중괄호의 위치 등을 일관되게 유지할 수 있습니다. `gofmt`를 사용하면 코드 리뷰와 협업에서 발생할 수 있는 서식 관련된 논쟁을 줄일 수 있습니다.

예시:

\```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
\```

위의 코드는 `gofmt`를 사용하여 다음과 같이 포맷팅될 수 있습니다.

\```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}
\```

## goimports
`goimports`는 `gofmt`와 비슷하지만 추가적으로 필요한 import 문을 자동으로 추가하거나 제거해줍니다. 이를 통해 필요한 패키지를 추가하거나 불필요한 패키지를 제거함으로써 코드를 간결하게 유지할 수 있습니다.

예시:

\```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
\```

위의 코드에서 `"time"` 패키지가 필요하다면 `goimports`를 사용하여 다음과 같이 import문이 추가될 수 있습니다.

\```go
package main

import "fmt"
import "time"

func main() {
    fmt.Println("Hello, World!")
}
\```

`gofmt`와 `goimports`를 사용하여 Go 언어의 코드를 일관된 서식으로 유지하고 필요한 import문을 관리함으로써 코드를 좀 더 깔끔하게 작성할 수 있습니다.

참고 문헌: [The Go Programming Language Specification - gofmt](https://golang.org/ref/spec#Formatting)