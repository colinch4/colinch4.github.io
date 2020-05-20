---
layout: post
title: "Context Switch(컨텍스트 스위치)가 무엇인가?"
date: 2020-05-19 13:47
category: 
author: kskim2
tags: [os]
summary: 
description: 
comments: true
share: true
---


> **Context Switching이 무엇인가?**  

멀티프로세스 환경에서 CPU가 어떤  하나의 프로세스를 실행하고 있는 상태에서 인터럽트 요청에 의해  다음 우선 순위의 프로세스가 실행되어야 할 때 기존의 프로세스의 상태 또는 레지스터 값(Context)을 저장하고 CPU가 다음 프로세스를 수행하도록 새로운 프로세스의  상태 또는 레지스터 값(Context)를 **교체하는 작업**을 Context Switch(Context Switching)라고 한다.

질문에 대한 답변은 이정도로 하고 좀 더 명확하게 이해해본다.

* Context Switching을 문맥 교환으로 번역하지 말자.  

> **Context는 무엇인가?**  

사용자와 다른 사용자, 사용자와 시스템 또는 디바이스간의 상호작용에 영향을 미치는 사람, 장소, 개체등의 현재 상황(상태)을 규정하는 정보들을 말한다.

android나 servlet등에서도 context가 있지만 OS에서  **Context는 CPU가 해당 프로세스를 실행하기 위한 해당 프로세스의 정보들이다.**

이  **Context는 프로세스의 PCB(Process Control Block)에 저장**된다.

그래서 Context Switching 때 PCB의 정보를 읽어(적재) CPU가 전에 프로세스가 일을 하던거에 이어서 수행이 가능한 것이다.

PCB의 저장정보

- 프로세스 상태 : 생성, 준비, 수행, 대기, 중지

- 프로그램 카운터 : 프로세스가 다음에 실행할 명령어 주소

- 레지스터 : 누산기, 스택, 색인 레지스터

- 프로세스 번호

*  참고로 Context Switching 때 해당 CPU는 아무런 일을 하지 못한다. 따라서 컨텍스트 스위칭이 잦아지면 오히려 오버헤드가 발생해 효율(성능)이 떨어진다.

Context가 뭔지 알았고 멀티프로세싱하기 위해 CPU를 나눠서 사용하기 위해 Context를 교체하는 것이 Context Switching임을 알았다. 그리고 PCB에 Context가 저장됨도 알았다.

남은 것은 인터럽트 요청이 뭐고 어떤 종류가 있는지 + 서브로 우선 순위에 대한 이야기다.

> **Context Switching - 인터럽트(Interrupt)**  

인터럽트는 CPU가 프로그램을 실행하고 있을 때 실행중인 프로그램 밖에서 예외 상황이 발생하여 처리가 필요한 경우 CPU에게 알려 예외 상황을 처리할 수 있도록 하는 것을 말한다.

어떤 인터럽트 요청이 와야 Context Switching이 일어날까?

1. I/O request (입출력 요청할 때)

2. time slice expired (CPU 사용시간이 만료 되었을 때)

3. fork a child (자식 프로세스를 만들 때)

4. wait for an interrupt (인터럽트 처리를 기다릴 때)

+ 더 있겠지만 자세한 것은 생략.

* 우선 순위는 해당 OS의 스케줄러가 우선 순위 알고리즘에 의해 정해지고 수행하게 되어있다.

라운드로빈 스케줄링(Round Robin Scheduling)은 시분할 시스템을 위해 설계된 선점형 스케줄링의 하나다.

쉽게 설명하면 순서대로 시간단위(Time Quantum)을 CPU에 할당하는 방식이다.

꽤 효율적인 스케줄링 알고리즘이지만 이 시간단위를 작게 설정하면 CPU가 조금 일하고 Context Switching을 반복하므로 아까 말했듯이 효율이 떨어진다.

* Context Switch를 하는 주체 = OS 스케줄러
