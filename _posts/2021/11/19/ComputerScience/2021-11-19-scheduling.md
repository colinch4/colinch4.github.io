---
layout: post
title: "[CS] Scheduling"
description: " "
date: 2021-11-19
tags: [cs]
comments: true
share: true
---

## Scheduling
Scheduling 을 통해 CPU를 효율적으로 사용할 수 있다.  

### Table of Contents
* [About Scheduling](#about-scheduling)   
  * [Processs state](#process-state)
  * [PCB](#pcb)
  * [Preemtive & Non-Preemtive](#preemtive-&-Non-Preemtive)
* [Scheduling Algorithms](#scheduling-algoritms)
  * [Criteria for Scheduling](#criteria-for-scheduling)


## About Scheduling  
**예시) 유저가 프로그램을 실행하는 상황**  
OS는 유저의 요청대로 프로그램을 실행시키기 위해 보조기억장치(HDD, SSD)에 있던 프로그램을 주기억장치(RAM)에 올린다.  

하나의 CPU(Processor)는 하나의 프로세스만 실행 시킬 수 있다. CPU 상에서 실행(`running`) 상태에 놓여 있지 않은 다른 프로세스들은 준비(`ready`), 또는 대기(`waiting`)의 상태에 놓여 있다.  
- Dual-core 라면 동시 실행 가능한 프로세스는 두개, Quad-core 라면 동시 실행 가능한 프로세스는 네개 라는 것을 의미한다.  
  Apple 의 M1 칩 경우 8-core 로써 동시에 8개의 프로세스가 실행될 수 있다.  

  <img width="350" alt="m1-8-core" src="https://user-images.githubusercontent.com/48475824/124504953-65da3700-de03-11eb-8ed1-2f1a22d2692a.gif">

**Multiprogramming 다중 프로그래밍**  
> Multiprogramming != Multitasking  

유저는 다수의 프로그램을 함께 사용한다. 이러한 상황에서 각각의 프로세서는 여러 프로그램을 빠른 속도로 번갈아가며(마치 수십가지의 프로그램이 모두 동시에 실행되는 것 처럼) 실행한다.  

CPU가 효율적으로 사용되게 하기 위해 고안된 다중 프로그래밍은 [3세대 컴퓨터(1965-1980)](https://www.stitson.com/pub/book_html/node7.html)의 시점에 도입되었다. 다중 프로그래밍 방식의 탄생 이전 세대의 컴퓨터에서는 단일의 프로그램만 사용할 수 있었다. 이를 단일 프로그래밍(`Uniprogramming`) 이라 부른다.  

중앙처리장치는 끊임없이 논리 연산(ALU)의 작업만 수행하지 않는다. I/O 연산이 진행 될 때 CPU는 대기(`idle`)상태에 머무르게 된다. 기다림의 시간은 상대적으로 빠른 CPU 와 상대적으로 느린 I/O 기기의 속도 차이에서 비롯된다. CPU가 아무 일도 하지 않는 상태를 줄이고 효율적으로 더 많은 일을 할수 있도록 하기 위해 다중 프로그래밍 방식을 사용한다. 이때, 다른 프로그램을 CPU에 적재시켜 CPU가 다른 일을 하도록 돕는 역할을 스케줄러가 담당한다.  
- ALU(Arithmetic Logic Unit): 논리 연산을 담당하는 연산 논리 장치  


### Process state
> Process state: 프로세스의 생성부터 소멸되기 까지의 생명주기를 나타낸다.  

프로세스의 상태는 아래의 다섯가지로 나눌수 있다.  

1. **New**  
  **생성**: process가 생성되어진 상태  
1. **Ready**  
  **준비**: process가 CPU에서 실행 될 때 필요한 모든 리소스가 준비 완료 되어 있는 상태  
1. **Running**  
  **실행**: process가 CPU에서 실행되고 있는 상태  
1. **Waiting**  
  **대기**: process가 특정 이벤트를 기다리고 있는(실행되고 있지 않은) 상태  
1. **Terminated**  
  **완료**: process의 실행이 완료 또는 중단된 상태  

![process state](https://user-images.githubusercontent.com/48475824/124386488-aa87a480-dd15-11eb-824b-5809e797822e.png)  

CPU 는 `ready` 상태에 놓여있는 여러 프로세스중 하나의 프로세스를 선택한다.  

<details>
  <summary>Process Flags</summary>

  [Linux Kernel](https://github.com/torvalds/linux/tree/master/kernel)

  ```cpp
  #define PF_VCPU			0x00000001	/* I'm a virtual CPU */
  #define PF_IDLE			0x00000002	/* I am an IDLE thread */
  #define PF_EXITING		0x00000004	/* Getting shut down */
  #define PF_IO_WORKER		0x00000010	/* Task is an IO worker */
  #define PF_WQ_WORKER		0x00000020	/* I'm a workqueue worker */
  #define PF_FORKNOEXEC		0x00000040	/* Forked but didn't exec */
  #define PF_MCE_PROCESS		0x00000080      /* Process policy on mce errors */
  #define PF_SUPERPRIV		0x00000100	/* Used super-user privileges */
  #define PF_DUMPCORE		0x00000200	/* Dumped core */
  #define PF_SIGNALED		0x00000400	/* Killed by a signal */
  #define PF_MEMALLOC		0x00000800	/* Allocating memory */
  #define PF_NPROC_EXCEEDED	0x00001000	/* set_user() noticed that RLIMIT_NPROC was exceeded */
  #define PF_USED_MATH		0x00002000	/* If unset the fpu must be initialized before use */
  #define PF_USED_ASYNC		0x00004000	/* Used async_schedule*(), used by module init */
  #define PF_NOFREEZE		0x00008000	/* This thread should not be frozen */
  #define PF_FROZEN		0x00010000	/* Frozen for system suspend */
  #define PF_KSWAPD		0x00020000	/* I am kswapd */
  #define PF_MEMALLOC_NOFS	0x00040000	/* All allocation requests will inherit GFP_NOFS */
  #define PF_MEMALLOC_NOIO	0x00080000	/* All allocation requests will inherit GFP_NOIO */
  #define PF_LOCAL_THROTTLE	0x00100000	/* Throttle writes only against the bdi I write to, I am cleaning dirty pages from some other bdi. */
  #define PF_KTHREAD		0x00200000	/* I am a kernel thread */
  #define PF_RANDOMIZE		0x00400000	/* Randomize virtual address space */
  #define PF_SWAPWRITE		0x00800000	/* Allowed to write to swap */
  #define PF_NO_SETAFFINITY	0x04000000	/* Userland is not allowed to meddle with cpus_mask */
  #define PF_MCE_EARLY		0x08000000      /* Early kill for mce process policy */
  #define PF_MEMALLOC_PIN		0x10000000	/* Allocation context constrained to zones which allow long term pinning. */
  #define PF_FREEZER_SKIP		0x40000000	/* Freezer should not count it as freezable */
  #define PF_SUSPEND_TASK		0x80000000      /* This thread called freeze_processes() and should not be frozen */
  ```

</details>
<br>

### PCB 
> PCB: Process Control Block  
OS가 프로세스를 제어하기 위해 필요한 정보들은 `프로세스 제어 블록`(PCB) 에 저장되어 있다.  

![pcb](https://user-images.githubusercontent.com/48475824/124385633-8aee7d00-dd11-11eb-9f90-654179aab208.png)  

- Process state  
  프로세스 상태 관련 데이터가 담겨 있다.  
  (New, Ready, Waiting, Running, Terminated)
- Process number  
- Process counter  
  프로세스 카운터  
- Registers
- Memory Limits
- List of open files


### Preemtive & Non-Preemtive
스케줄링은 preemtive와 non-preemtive 방식이 존재한다.

- Preemtive Scheduling 선점 스케쥴링
- Non-Preemtive Scheduling 비선점 스케쥴링  



## Scheduling Algorithms  
앞서 언급했듯이 스케줄러는 CPU가 효율적으로 활용되도록 돕는 역할을 한다.  
그렇다면 스케줄러는 많고 많은 프로세스중에서 다음에 실행될 프로세스를 어느 방법(스케줄링 알고리즘)으로 골라야 할까?  


스케줄링 알고리즘은 아래와 같은 것들이 있다.  
- **FCFS**  
  First Come, First Served
- **RR**  
  Round Robin
- **SJF**  
  Shortest Job First
- **Multilevel Feedback Queues**  
- **Lottery Scheduling**  

<br>


**OS & Scheudling algorithm**  

OS|Type of Algorithms
:---:|:---
MacOS X|Multilevel Feedback Queeue, RR
Windows 10|Multilevel Feedback Queeue, RR

<br>

### Criteria for Scheduling
좋은 스케줄링 알고리즘을 판별하기 위한 기준  
- CPU Utilization
- Throughput
- Turnaround time
- Waiting time
- Response time
