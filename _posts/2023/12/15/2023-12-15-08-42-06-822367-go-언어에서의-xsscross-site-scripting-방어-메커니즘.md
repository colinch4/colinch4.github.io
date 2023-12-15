---
layout: post
title: "[go] go 언어에서의 XSS(Cross-Site Scripting) 방어 메커니즘"
description: " "
date: 2023-12-15
tags: [go]
comments: true
share: true
---

웹 어플리케이션을 개발하다 보면 XSS(Cross-Site Scripting) 공격을 방어할 필요가 있습니다. Go 언어에서는 이를 방어하기 위해 내장된 기능을 제공합니다. 이 기능을 사용하여 웹 어플리케이션을 안전하게 개발할 수 있습니다. 

## 1. text/template 패키지를 사용한 HTML 출력

Go 언어에서는 텍스트를 HTML로 출력하는 경우에 `text/template` 패키지를 사용하여 자동적으로 이스케이핑(escaping)을 수행합니다. 이를 통해 사용자가 입력한 스크립트를 그대로 출력함으로써 발생할 수 있는 XSS 공격을 방어할 수 있습니다.

```go
package main

import (
	"html/template"
	"os"
)
{% raw %}
func main() {
	t := template.New("example")
	t, err := t.Parse("Hello, {{.}}!")
	if err != nil {
		panic(err)
	}
	err = t.Execute(os.Stdout, "<script>alert('XSS 공격')</script>")
	if err != nil {
		panic(err)
	}
}
{% endraw %}
```

## 2. html/template 패키지 사용

`html/template` 패키지는 `text/template` 패키지와 유사하지만, HTML 문서를 렌더링할 때 보다 안전하게 자동 이스케이핑을 수행합니다. 이를 통해 어플리케이션에서 사용자 입력을 안전하게 렌더링할 수 있습니다.

```go
package main

import (
	"html/template"
	"os"
)
{% raw %}
func main() {
	t := template.New("example")
	t, err := t.Parse("Hello, {{.}}!")
	if err != nil {
		panic(err)
	}
	err = t.Execute(os.Stdout, "<script>alert('XSS 공격')</script>")
	if err != nil {
		panic(err)
	}
}
{% endraw %}
```

Go 언어는 이러한 방어 메커니즘을 통해 프로그래머가 웹 어플리케이션을 개발할 때 XSS 공격을 방어할 수 있도록 도와줍니다.  만약 필요하다면 자체적인 보안 미들웨어를 개발하여 추가 보안을 적용할 수도 있습니다.

## 참고 자료
1. [Go 언어 - text/template 패키지](https://pkg.go.dev/text/template)
2. [Go 언어 - html/template 패키지](https://pkg.go.dev/html/template)