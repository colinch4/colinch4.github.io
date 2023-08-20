---
layout: post
title: "[CS] Program Counter "
description: " "
date: 2021-11-19
tags: [CS]
comments: true
share: true
---

## Program Counter 
**PC** : **P**rogram **C**ounter  
PC 는 레지스터의 일종으로써 CPU 가 다음에 실행시켜야 할 명령의 주소를 담고 있다.  
* IP (Instrcuton Pointer) 또는 IAR (Instruction Address Register) 라 불리기도 한다.  

![diagram of processor](https://user-images.githubusercontent.com/48475824/78616857-7a521b80-78b0-11ea-97d2-3eb60a7bb25e.png)
Image credit : thinglink.com

### Table of Contents
- [Program Counter](#program-counter)
    - [Table of Contents](#table-of-contents)
  - [Register](#register)
  - [Stack](#stack)
    - [Fetch Instruction 명령어 읽어오기](#fetch-instruction-명령어-읽어오기)
  - [32 bits](#32-bits)
    - [3 Fields](#3-fields)
  - [Control Signals](#control-signals)


## Register  
명령어들은 Main Memory 에 저장되어 있다.   
PC 는 Main Memory 가 다음으로 실행해야 하는 명령어의 주소를 포인터로 가리킨다.  
* 첫 번째 명령어의 주소는 늘 0 번지부터 시작한다.  

[Return to TOC](#table-of-contents)


## Stack
LIFO(Last In First Out) 의 특성을 지닌 Stack 에 주소를 차곡 차곡 쌓아둔다. 

### Fetch Instruction 명령어 읽어오기
현재의 명령어를 실행시킨 CPU 는 포인터가 가리키는 주소로 찾아가 다음에 진행 시켜야하는 명령들을 순차적으로 실행시켜나간다.  

하나의 instruction을 실행 시킨 이후에 PC 값이 증가된다.

[Return to TOC](#table-of-contents)


## 32 bits  
PC 는 32 bits 의 길이를 가진다.  
32 bits == 4 bytes.  

모든 명령은 32 비트이다. 이는 ALU가 32 비트 이기 때문이다.  
32 비트 길이로 규격화 해 놓음으로써 fetch 및 decode 하기가 수월해 진다.
* ALU (Arithmetic and Logic Unit) 연산장치 : CPU의 명령에 따라 연산을 수행하는 장치.
  * 연산의 종류는 산술연산, 논리 연산, 관계 연산, 이동(Shift) 등이 있다.

### 3 Fields
32 비트는 3개의 필드로 나뉜다.  
* 1 operation code (8 bits)
* 2 operands (8 bits + 16 bits)

![program counter](https://user-images.githubusercontent.com/48475824/78615771-53461a80-78ad-11ea-9bf4-1adc8d491afe.png)

[Return to TOC](#table-of-contents)


## Control Signals
PC 는 세 개의 컨트롤 시그널을 가진다.  
* **CE**  
  Program **C**ounter **E**nable
* **CO**  
  Program **C**ounter **O**utput **E**nable
* **J**   
  Program counter **J**ump

[Return to TOC](#table-of-contents)