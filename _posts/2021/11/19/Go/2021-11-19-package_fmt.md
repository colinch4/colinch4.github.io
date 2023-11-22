---
layout: post
title: "[Go] Package fmt"
description: " "
date: 2021-11-19
tags: [go]
comments: true
share: true
---

## Package fmt

서식화된 문자열의 입출력 패키지 fmt.

### Table of Contents

- [Package fmt](#package-fmt)
    - [Table of Contents](#table-of-contents)
  - [fmt Basic](#fmt-basic)
    - [Print](#print)
    - [Scan](#scan)
  - [fmt 코드 열어보기](#fmt-코드-열어보기)
    - [pp 구조체](#pp-구조체)
    - [ss 구조체](#ss-구조체)
    - [fmt.Print](#fmtprint)
    - [fmt.Println](#fmtprintln)
    - [fmt.Printf](#fmtprintf)
    - [fmt.Fprintln](#fmtfprintln)
    - [fmt.Sprint](#fmtsprint)
    - [fmt.Sprintf](#fmtsprintf)
    - [fmt.Sprintln](#fmtsprintln)
    - [fmt.Sscan](#fmtsscan)

## fmt Basic

### Print

fmt 패키지내의 Print 관련 함수(또는 메서드)는 아래와 같다.

- 바이트 수(int)와 에러(error)를 반환하는 함수

  - Print
  - Printf
  - Println
  - Fprint
  - Fprintf
  - Fprintln

  `Print` 와 `Println` 은 raw string 을 프린팅한다.

- 문자열을 반환하는 함수
  - Sprint
  - Sprintf
  - Sprintln

[↑ return to TOC](#table-of-contents)

### Scan

fmt 패키지내의 Scan 관련 함수(또는 메서드)는 아래와 같다.

- Fscanf
- Fscanln
- Sscan
- Sscanf

[↑ return to TOC](#table-of-contents)

## fmt 코드 열어보기

### pp 구조체

pp 구조체는 프린터의 상태를 담아 둔다.  

```go
type pp struct {
    buf        buffer
    arg        interface{}
    value      reflect.Value
    fmt        fmt
    reordered  bool
    goodArgNum bool
    panicking  bool
    erroring   bool
    wrapErrs   bool
    wrappedErr error
}
```

- buf  
  데이터를 임시로 저장.
- arg  
  현재의 item 을 지님.
  - item은 integers, strings 등을 말한다.
- fmt  
  기본적인 item을 서식화 하기 위해 쓰임.

[↑ return to TOC](#table-of-contents)

### ss 구조체

```go
type ss struct {
    rs     io.RuneScanner
    buf    buffer
    count  int
    atEOF  bool
    ssave
}
```

- buf  
  데이터를 임시로 저장.

[↑ return to TOC](#table-of-contents)

### fmt.Print

```go
func Print(a ...interface{})(n int, err error) {
    return Fprint(os.Stdout, a...)
}
```

[↑ return to TOC](#table-of-contents)

### fmt.Println

**Println** == **Print** **l**i**n**e

`Println` 은 `Print`와 비슷하지만 마지막으로 전달된 argument의 마지막에 new line(`\n`)을 추가시킨다.

```go
func Println(a ...interface{}) (n int, err error) {
    return Fprintln(os.Stdout, a…)
}
```

[↑ return to TOC](#table-of-contents)

### fmt.Printf

**Printf** == **Print** **f**ormatter  
서식 지정자(format specifier)와 함께 쓰인다.

```go
func Printf(format string, a ...interface{}) (n int, err error) {
    return Fpintf(os.Stout, format, a …)
}
```

[↑ return to TOC](#table-of-contents)

### fmt.Fprintln

```go
func Fprintln(w io.Writer, a...interface{}) (n int, err error) {
    p := newPrinter()
    p.doPrintln(a)
    n, err = w.Write(p.buf)
    p.free()
    return
}
```

- `doPrintln` 의 코드는 아래와 같다.
  ```go
  func (p *pp) doPrintln(a []interface{}){
    for argNum, arg := range a {
        if argNum > 0 {
            p.buf.wrtieByte(‘ ’)
        }
        p.printArg(arg, ‘v’)
    }
    p.buf.writeByte(‘\n’)
  }
  ```
  `doPrintln` 은 `doPrint` 와 비슷하다. 다른점이라면 스페이스와, new line 을 추가해 준다는 것.
  - argument 사이에 스페이스 추가 → `p.buf.WriteByte(' ')`
  - new line 추가 → `p.buf.writeByte('\n')`

[↑ return to TOC](#table-of-contents)

### fmt.Sprint

**Sprint** == **S**tring **print**

```go
func Sprint(a ...interface{}) string {
    p := newPrinter()
    p.doPrint(a)
    s := string(p.buf)
    p.free()
    return s
}
```
* ```newPrinter()``` 는 새 pp 구조체를 할당.

[↑ return to TOC](#table-of-contents)

### fmt.Sprintf

**Sprintf** == **S**tring **print** **f**ormat

```Sprintf``` 는 전달받은 서식지정자의 형태로 문자열을 프린트해준다.

```go
func Sprintf(format string, a ...interface{}) string {
    p := newPrinter()
    p.doPrintf(format, a)
    s := string(p.buf)
    p.free()
    return s
}
```

[↑ return to TOC](#table-of-contents)

### fmt.Sprintln

**Sprintln** == **S**tring **print** **li**ne

여러 argument 를 받은 후 마지막 argument 뒤에 new line 을 추가해준다.

```go
func Sprintln(a ...interface{}) string {
    p := newPrinter()
    p.doPrintln(a)
    s := string(p.buf)
    p.free()
    return s
}
```

[↑ return to TOC](#table-of-contents)

### fmt.Sscan

```go
func Sscan(str string, a ...interface{}) (n int, err error) {
    return Fascan((*stringReader)(&str), a...)
}
```

- 전달 받은 argument 를 스캔.
- Newline 은 space 로 계산.

[↑ return to TOC](#table-of-contents)
