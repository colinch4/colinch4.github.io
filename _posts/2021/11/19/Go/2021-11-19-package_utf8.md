---
layout: post
title: "[Go] Package UTF8"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

# Package UTF8  
UTF8 은 인코딩 방식중 하나로써 세상의 문자들을 1-4 byte 를 사용하여 표현한다.

### Table of Contents
- [Package UTF8](#package-utf8)
    - [Table of Contents](#table-of-contents)
  - [UTF8 코드 열어보기](#utf8-코드-열어보기)
    - [utf8.RuneCountInString](#utf8runecountinstring)


## UTF8 코드 열어보기

### utf8.RuneCountInString
글자 수를 int 타입으로 리턴한다.
```go
func RuneCountInString(s string) (n int) {
  ns := len(s)
  for i := 0; i < ns; n++ {
     c := s[i]
     if c < RuneSelf {
        i++
        continue
     }
     x := first[c]
     if x == xx {
        i++ 
        continue
     }
     size := int(x & 7)
     if i+size > ns {
        i++ 
        continue
     }
     accept := acceptRanges[x>>4]
     if c := s[i+1]; c < accept.lo || accept.hi < c {
        size = 1
     } else if size == 2 {
     } else if c := s[i+2]; c < locb || hicb < c {
        size = 1
     } else if size == 3 {
     } else if c := s[i+3]; c < locb || hicb < c {
        size = 1
     }
     i += size
  }
  return n
}
```
* RuneCountInString 은 RuneCount 와 비슷하지만 입력 받는 Parameter 타입이 문자열 이다. 

* 글자수(문자열의 길이)를 얻기 위해서 ```len(str)``` 대신 ```RuneCountInString``` 을 사용하도록 한다.
    * ```len(str)``` 의 경우 '바이트의 길이' 를 리턴하지만, ```RuneCountInString``` 은 '글자의 길이' 를 리턴하기 때문이다.  
   문자당 1 바이트인 영문자를 사용하는 것은 문제가 없지만 그 외의 언어(예를 들어 한국어, 중국어, 아랍어 등)는 1 바이트 크기로 표현 불가하기 때문에 multi-byte 를 사용한다.  
   아래의 예를 보면 확연한 차이를 느낄 수 있다.
    ```go
    // Example 
    package main

    import (
        "fmt"
        "unicode/utf8"
    )

    func main() {
        enWords := "Backend"   // English Words
        chWords := "喜欢"       // Chinese Words
        jpWords := "緒にいたい"  // Japanese Words

        compare(enWords)      // len :  7 RuneCountInString :  7
        compare(chWords)      // len :  6 RuneCountInString :  2
        compare(jpWords)      // len : 15 RuneCountInString :  5
    }

    func compare(str string) {
        fmt.Println()
        fmt.Println("len : ", len(str), "RuneCountInString : ", utf8.RuneCountInString(str))
    }
    ```

[↑ return to TOC](#table-of-contents)