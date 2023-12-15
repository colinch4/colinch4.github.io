---
layout: post
title: "[go] go 언어의 text/template/exec 패키지를 활용하여 JSON 결과 처리 방법"
description: " "
date: 2023-12-15
tags: [go]
comments: true
share: true
---

Go 언어의 `text/template`과 `exec` 패키지는 텍스트 템플릿을 사용하여 동적 데이터를 처리할 수 있는 강력한 기능을 제공합니다. 이 패키지를 사용하여 JSON 결과를 처리하는 방법에 대해 알아보겠습니다.

## 1. text/template과 exec 패키지 소개

`text/template`은 텍스트 기반의 템플릿을 만들고 해석하는 기능을 제공하는 패키지입니다. `exec` 패키지는 `text/template`을 사용하여 코드를 실행하고 결과를 생성하는 기능을 제공합니다.

## 2. JSON 결과 처리 방법

다음은 `text/template`과 `exec` 패키지를 사용하여 JSON 결과를 처리하는 간단한 예제 코드입니다.

```go
package main

import (
	"os"
	"text/template"
)
{% raw %}
func main() {
	data := map[string]interface{}{
		"Name": "John Doe",
		"Age":  30,
	}

	tmpl, err := template.New("test").Parse(`{"name": "{{.Name}}", "age": {{.Age}}}`)
	if err != nil {
		panic(err)
	}

	err = tmpl.Execute(os.Stdout, data)
	if err != nil {
		panic(err)
	}
}
{% endraw %}
```

이 예제에서는 `text/template`을 사용하여 JSON 형식의 템플릿을 정의하고, `Execute` 함수를 통해 데이터를 적용하여 결과를 생성합니다.

## 3. 결론

`text/template`과 `exec` 패키지를 사용하면 간단한 JSON 결과를 처리하는 것은 물론, 복잡한 동적 데이터를 포함한 JSON 결과도 쉽게 처리할 수 있습니다. 이를 통해 Go 언어로 다양한 형식의 데이터를 처리하는 데 유용하게 활용할 수 있습니다.