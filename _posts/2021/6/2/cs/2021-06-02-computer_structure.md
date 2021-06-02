---
layout: post
title: "[cs] 컴퓨터의 주요 구조"
description: " "
date: 2021-06-02
tags: [cs]
comments: true
share: true
---

## 목차

1. [폰 노이만 구조](#1-폰-노이만-구조)
2. [CPU와 단위](#2-cpu와-단위)
3. [메모리](#3-메모리)
4. [숫자와 입출력](#4-숫자와-입출력)

# 1. 폰 노이만 구조

![폰노이만 아키텍처](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c187daa5-6a7f-4370-8960-d9ad2c756752/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210222T011800Z&X-Amz-Expires=86400&X-Amz-Signature=a6cbfdc2aebdeb418187c3b776d59f20e218f9ff36d0561a0a1898e47daa0b94&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 컴퓨터의 주요 구조

- CPU
- 입출력 (I / O)
- 메모리

<br/>
<br>

# 2. CPU와 단위

<br>

## 2. 1 CPU는 뭘까?

**전기신호를 이용하여 1과0을 이용하여 정보를 처리하는 장치**

- CPU(Central Processing Unit) : 중앙 처리 장치
- 1과 0으로 정보처리
- Core, Thread, Ghz
  - Core : 칩
  - Thread : 멀티태스킹
  - Ghz(클럭) : 1번의 전기신호 사이클
- 4 Core 4 Thread 3.3Ghz
  - 1초에 $3.3$ x $10^9$개의 명령어를 처리하는 칩이 4개 탑재되었고, 각 칩은 4개의 Thread로 구성(한번에 16개의 작업을 동시 처리 = 멀티태스킹)

### 참조

[CPU에 대한 기본적인 것! 클럭(Clock), 코어(Core), 스레드(Thread), 캐시 메모리에 대해서 알아보자! 싱글코어? 멀티 코어?](https://m.blog.naver.com/PostView.nhn?blogId=wrtoa&logNo=221559511358&proxyReferer=https:%2F%2Fwww.google.com%2F)

### CPU 아키텍처

- 32비트 & 64비트
  - 비트의 크기에 따라 CPU의 성능이 다르다.
- 서버 & 데스크톱 & 모바일
  - 기기마다 CPU종류가 다르다

<br>

## 2. 2 컴퓨터의 숫자 단위

컴퓨터가 생각하는 기본 단위는 스위치의 2가지 경우인 off / on `0과 1` 이다.

- 1 bit = 1 or 0 = $2^0$ bit
- 1 Byte = 8 bit = $2^3$ bit

- 1000 Byte = 1KB = $10^3$ ~ 1,024 = $2^{10}$
- 1000 KB = 1MB = $10^6$ ~ 1,024 = $2^{20}$
- 1000 MB = 1GB = $10^9$ ~ 1,024 = $2^{30}$

10진수 표현은 근사치이고 2진수표현이 근사치이다.

<br>

## 2. 3 CPU 더 살펴보기

### 32비트 CPU = 한 번에 전송 가능한 데이터 크기 : 32bit

- 32bit = $2^{32}$ = 4,294967,296 = 1,07,741,824 \* 4 = 4GB
- 32비트 컴퓨터는 최대 4GB 메모리만 인식할 수 있다.
- 64비트는? $2^{64}$ 어마무시하다

### 32비트 vs 64비트

- 개발자가 알아야 할 것 : 자료형의 크기 (특정 언어에서만)
- 몰라도 되는 것 : 메모리 구조, 레지스터 활용 방법등

### 서버 vs 데스크탑 vs 모바일

- 서버 > 데스크탑 > 모바일 순으로 CPU성능이 높다

<br></br>

# 3. 메모리

<br>

## 3. 1 메모리의 역활

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/60c6ca4d-b58a-454a-afab-d3505e925499/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/60c6ca4d-b58a-454a-afab-d3505e925499/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210222T012713Z&X-Amz-Expires=86400&X-Amz-Signature=de218119010c2ed9e41677546bb53ade7042d1571197d6ea4235378b71433659&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 용량은 크지만 처리속도가 느려서 메모리를 거쳐 CPU와 통신하게 된다.
- 실질적으로 통신하는 주체는 CPU와 메모리
- CPU보다는 처리속도는 늦으나 저장공간이 크고, 디스크보다는 저장공간이 작으나 처리속도가 빠르다.
- 결국에는 효율 적인 구조와 성능을 위해 메모리를 사용한다.
- **메모리는 휘발성, 디스크는 비휘발성**
  - 메모리는 중재자 역활이기 때문에, 컴퓨터가 꺼지면 CPU와 디스크 간의 통신이 끊겨서 그전에 임시저장했던 데이터를 가질 필요가 없다.

<br>

## 3. 2 어셈블리 언어

메모리에 올라가는 모든 코드는 어셈블리 언어로 변환되어야 CPU에게 작업의뢰를 할 수 있다.

- 결국 모든 코드는 메모리를 거쳐 CPU에서 처리되어야된다.
- CPU는 0과 1밖에 모르기때문에 소통하기 위한 언어가 필요하다
- 그래서 필요한 것이 **어셈블리 언어**

### 어셈블리 명령어

- CPU 세계의 문법(e.g 인텔, ARM, MIPS 등)
- 하나의 명령어 = 하나의 사이클(클럭)
- 그 아무리 복잡한 문법도 **이동, 복사, 논리, 산술, 제어 이동** 으로 표현이 가능하다

### '빌드' 버튼을 누를 떄 일어나는 일

- 전처리 → 컴파일 → 어셈블리 → 링크 → 로드
- 편집을 하고, 조립을 한 다음 모든 조각을 연결 시킨다.

| Name     | Explain                                                                   |
| -------- | ------------------------------------------------------------------------- |
| 전처리   | 조건부 컴파일 명령어, 매크로, include 파일 처리                           |
| 컴파일   | 소스코드에서 어셈블리 소스 코드를 생성                                    |
| 어셈블리 | 어셈블리 소스 코드에서 어셈블리 목록을 추출(오프셋 포함)                  |
| 링크     | 컴파일의 마지막 단계로 오브젝트 파일과 라이브러리를 결합해 실행 파일 생성 |
| 로드     | 프로그램 실행 후 메모리 로드                                              |

### 컴파일 vs 인터프리터

- **컴파일러**

  - 프로그램으로 만들어 놓고 번역
  - 코드 수정할 경우 다시 컴파일 해야 한다.
  - 제품 환경에 적합
  - 특정 운영체제와 CPU에서만 사용 가능하다.

- **인터프리터**

  - 한 줄씩 번역 - line by line
  - 실행과 동시에 프로그램을 처리
  - 프로그램 개발 환경에 적합
  - 여러 환경에 이식 가능하다

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/94935254-8811-43d9-91e3-f8539efa1e1e/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/94935254-8811-43d9-91e3-f8539efa1e1e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210222T013005Z&X-Amz-Expires=86400&X-Amz-Signature=10ef185578ea77beb51dfa76c511477c68866df202561bf42823bb9793916771&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

| Name            | Compiler                                                     | Interpreter                                               |
| --------------- | ------------------------------------------------------------ | --------------------------------------------------------- |
| 개발 편의성     | 코드를 수정하고 실행하려면 컴파일을 다시 해야 한다. 👎       | 코드를 수정하고 즉시 실행할 수 있다. 👍                   |
| 실행 속도       | 빠르다. 👍                                                   | 느리다. 👎                                                |
| 보안            | 프로그램의 코드가 유출되지 않는다. 👍                        | 프로그램의 코드가 유출될 수 있다. 👎                      |
| 파일 용량       | 프로그램의 실행 파일 전체를 전송해야 하므로, 용량이 크다. 👎 | 프로그램의 코드만 전송하면 실행이 되므로, 용량이 작다. 👍 |
| 프로그래밍 언어 | C, C++처럼 비교적 저수준에 가까운 언어                       | Python, Ruby처럼 비교적 고수준에 가까운 언어              |

## 3. 3 가상 메모리

- 운영체제와 모든 프로그램이 나눠쓰기엔 메모리의 용량이 턱없이 부족하여 사용하는 메모리 방식
- 메인 메모리보다 훨씬 큰 기억공간인 디스크를 가상의 메모리 공간으로 이용하는 기법
- **한정된 메모리로 개발을 해야되는 Software 개발자로서 메모리는 꼭 이해하고 넘어가야된다**
- 메모리 정리를 알아서 해주는 언어로는 `가비지 컬렉션 옵션` 이 있다.

### 참조

[https://velog.io/@gimtommang11/가상메모리](https://velog.io/@gimtommang11/%EA%B0%80%EC%83%81%EB%A9%94%EB%AA%A8%EB%A6%AC)

<br></br>

# 4. 숫자와 입출력

<br>

## 4. 1 진법과 숫자

[숫자](https://www.notion.so/913712e1adea4daf90875b3b03573e5d)

### N 진법

- 10진법 : 사람들이 편하게 쓰는 숫자
- 16진법 : 컴퓨터가 좋아하는 숫자(e.g 0x8F, 10h)
  - 개발하면서 가장 많이 보는 진법
  - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F
  - Ascii 코드, 유니코드
  - 자릿수가 $2^4$ 으로 표현이 가능하고 훈련이 된 상황이라면 16진법의 숫자만 보고도 2진법 수로 변환이 가능하기 때문에 컴퓨터 분야에서 많이 쓰인다.
- 2진법 : 컴퓨터의 언어 (1과 0으로 이루어진 코드 e.g 1001010)

**사용자와 컴퓨터간에 소통하기 위해 좋은 언어는 어셈블리어가 좋고**

**진법으로는 16진법이 좋다.**

<br>

## 4. 2 입출력 이해

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/07dcdf51-9d05-4627-b8b3-5ed9dfc6eb0f/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/07dcdf51-9d05-4627-b8b3-5ed9dfc6eb0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210222T013201Z&X-Amz-Expires=86400&X-Amz-Signature=712ac5036e18d2673c79539921e39f5ddc066d25f3bc09a4b74d126dbb497d95&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

DMA

### 입력과 출력 : 하드웨어의 기본 기능

- 프로그램과 문서를 저장하는 하드디스크
- 마우스와 키보드 입력 결과를 출력하는 모니터
- 네트워크도 입출력, 카메라도 입출력, 지운식기도 입출력
- 입출력(I/O) 처리가 CPU속도에 비해 너무 느리기 떄문에 DMA(Direct Memory Access)를 이용하여 CPU의 개입없이 I/O 장치와 기억장치의 데이터 전송을 처리한다.

  **프로그래밍을 한다는 것은 외부로부터의 요청을 받아서 응답을 해주는 것이라고 할 수 있다.**

**그래서 모든 입출력은 프로그램 입장에서 외부와의 상호작용이다.**
