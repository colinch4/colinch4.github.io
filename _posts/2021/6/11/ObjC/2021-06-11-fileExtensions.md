---
layout: post
title: "[Objective-C++] Objective-C++ 은 무엇일까? "
description: " "
date: 2021-06-11
tags: [c++]
comments: true
share: true
---


| 확장자 | 의미  |
|--------|-------|
| .c| C 언어 소스 파일|
| .cc, .cpp|C++ 언어 소스 파일 |
| .h| 헤더 파일|
| .m| Objective-C 소스 파일 |
| .mm| Objective-C++ 소스 파일|
| .pl| Perl 소스 파일|
| .o| (컴파일된) 오브젝트 파일|


### Objective-C++ 은 무엇일까? 

[애플 문서]를 살펴보면, Objective-C++ 는 Objective-c 와 c++을 혼합해 사용할 수 있는 언어를 말한다. 애플의 Objective-C 컴파일러가 한 소스 파일(.mm)에 C++과 Objective-C 를 혼합해 쓸 수 있는 걸 허락하고, 따라서 Objective-C 프로그램에 C++ 라이브러리를 사용하는 것도 가능하다.

**주의**: Xcode에서 Objective-C++ 을 사용하려면 .mm 확장자 파일을 사용해야 합니다. 

[애플 문서]: https://web.archive.org/web/20101203170217/http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ObjectiveC/Articles/ocCPlusPlus.html

### .o file

오브젝트 파일. 컴파일하면 기계어(0,1)로 이루어진 오브젝트 파일로 변환된다. 
