---
layout: post
title: "[go] go 언어의 text/template/exec 패키지를 활용하여 HTML 템플릿 생성하기"
description: " "
date: 2023-12-15
tags: [go]
comments: true
share: true
---

go 언어의 `text/template`와 `html/template` 패키지는 텍스트나 HTML을 동적으로 생성하기 위한 강력한 기능을 제공합니다. 특히 `text/template` 패키지의 `Execute` 함수를 사용하여 HTML 템플릿을 생성하는 방법을 알아보겠습니다.

## 템플릿 작성하기
{% raw %}
먼저, HTML 템플릿을 작성합니다. 템플릿은 텍스트 파일에 작성하고, 동적으로 변하는 부분은 `{{}}` 안에 작성합니다. 예를 들어, 다음과 같은 간단한 템플릿을 작성해보겠습니다.
{% endraw %}
```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>{{.Title}}</title>
</head>
<body>
    <h1>Hello, {{.Name}}!</h1>
</body>
</html>
{% endraw %}
```

위의 템플릿은 `Title`과 `Name`이라는 두 가지 동적인 값을 가지고 있습니다.

## 템플릿 실행하기

이제 작성한 템플릿을 go 코드에서 실행해보겠습니다. 먼저, 필요한 패키지를 임포트합니다.

```go
package main

import (
	"os"
	"text/template"
)
```

다음으로, 템플릿을 `Parse` 함수를 사용하여 파싱합니다.

```go
tmpl, err := template.New("example").ParseFiles("template.html")
if err != nil {
    panic(err)
}
```

그리고 템플릿에 전달할 데이터를 정의합니다.

```go
type Data struct {
	Title string
	Name  string
}

data := Data{
    Title: "Welcome",
    Name:  "John",
}
```

마지막으로, 파싱한 템플릿을 실행하여 출력 결과를 확인합니다.

```go
err = tmpl.Execute(os.Stdout, data)
if err != nil {
    panic(err)
}
```

## 결론

위의 예제를 통해 go 언어의 `text/template` 패키지를 사용하여 HTML 템플릿을 동적으로 생성하는 방법을 알아보았습니다. 이러한 방법을 활용하여 웹 애플리케이션 개발 시 동적인 HTML 페이지를 손쉽게 생성할 수 있습니다.

참고문헌:
- [text/template package - Golang](https://golang.org/pkg/text/template/)
- [html/template package - Golang](https://golang.org/pkg/html/template/)