---
layout: post
title: "[go] big endian 인코딩 방식과 little endian 인코딩 방식에 대한 이해"
description: " "
date: 2023-12-18
tags: [go]
comments: true
share: true
---

컴퓨터에서는 메모리와 데이터를 다루는 방식에 따라 **big endian**과 **little endian**이라는 두 가지 주요 인코딩 방식이 있습니다. 두 방식은 데이터를 메모리에 저장하거나 전송할 때 해당 데이터의 바이트 순서를 나타냅니다. 

## Big Endian
**Big endian**은 가장 높은(맨 앞에 위치하는) 유효 데이터 바이트부터 낮은(맨 뒤에 위치하는) 순서대로 데이터를 저장하는 방식입니다. 이러한 형식은 네트워크 프로토콜에서 자주 사용됩니다. 예를 들어, 16진수로 표현된 값 `0x12345678`은 big endian으로 저장되면 다음과 같습니다.

```
0x12 0x34 0x56 0x78
```

## Little Endian
**Little endian**은 big endian과 정반대로, 가장 낮은(맨 뒤에 위치하는) 유효 데이터 바이트부터 높은(맨 앞에 위치하는) 순서대로 데이터를 저장하는 방식입니다. 이 방식은 x86 아키텍처에서 주로 사용됩니다. 예를 들어, 16진수로 표현된 값 `0x12345678`은 little endian으로 저장되면 다음과 같습니다.

```
0x78 0x56 0x34 0x12
```

## 사용 사례
이러한 인코딩 방식은 주로 네트워크 통신, 데이터 파일 형식, 프로세서 아키텍처 등과 관련이 있습니다. 때로는 이러한 차이로 인해 데이터 교환 시 문제가 발생할 수 있으므로 주의가 필요합니다.

메모리의 바이트 순서에 대한 이해는 특히 하드웨어와 네트워크 시스템과 작업하는 프로그래머들에게 중요합니다.

더 많은 정보를 원하시거나 추가적인 질문이 있으시면 아래의 참고 자료들을 참조하세요.

## 참고 자료
- [Big-endian and little-endian](https://en.wikipedia.org/wiki/Endianness), 위키피디아
- [Understanding Big and Little Endian Byte Order](https://www.geeksforgeeks.org/little-and-big-endian-mystery/), GeeksforGeeks