---
layout: post
title: "[android] Java Garbage Collection"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---

Java Garbage Collection

가비지 컬렉션 과정

GC에 대해 설명하기 전에 먼저 'stop-the-world'를 알아야한다. Stop-the-world란, GC을 실행하기 위해 JVM이 애플리케이션 실행을 멈추는 것이다. stop-the-world가 발생하면 GC를 실행하는 쓰레드를 제외한 나머지 쓰레드는 모두 작업을 멈춘다. GC작업을 완료한 이후에야 중단했던 작업을 다시 시작한다. 어떤 GC 알고리즘을 쓰던지 'stop-the-world'는 발생하기 때문에 GC튜닝이란 'stop-the-world' 시간을 줄이는 것이다.

 Java는 프로그램 코드에서 메모리를 명시적으로 지정하여 해제하지 않는다.가끔 명시적으로 해제하려고 해당 객체를 null로 지정하거나 System.gc() 메소드를 호출하는 개발자가 있다. null 로 지정하는 것은 큰 문제가 안 되지만, System.gc() 메소드를 호출하는 것은 시스템의 성능에 매우 큰 영향을 끼치므로 System.gc() 메서드는 절대로 사용하면 안된다.

 Java에서는 개발자가 프로그램 코드로 메모리를 명시적으로 해제하지 않기 때문에 가비지 컬렉터(Garbage Collector)가 더이상 필요없는 (쓰레기)객체를 찾아 지우는 작업을 한다. 이 가비지 컬렉터는 두가지 가설 하에 만들어졌다.(가설이라기보다는 전제 조건)

- 대부분의 객체는 금방 접근 불가능 상태(unreachable)가 된다.
- 오래된 객체에서 젊은 객체로의 참조는 아주 적게 존재한다.

이러한 가설을 'weak generational hypothesis'라 한다. 이 가설의 장점을 최대한 살리기 위해서 HotSpot VM에서는 크게 2개로 물리적 공간을 나누었다. 둘로 나눈 공간이 Young 영역과 Old 영역이다.

- Young 영역(Young Generation 영역) : 새롭게 생성한 객체의 대부분이 여기에 위치한다. 대부분의 객체가 금방 접근 불가능 상태가 되기 때문에 많은 객체가 Young 영역에 생성되었다가 사라진다. 이 영역에서 객체가 사라질 때 Minor  GC가 발생한다고 말한다.
- Old 영역(Old Generation 영역) : 접근 불가능 상태로 되지 않아 Young 영역에서 살아남은 객체가 여기로 복사된다. 대부분 Young 영역보다 크게 할당되며, 크기가 큰 만큼 Young영역보다 GC는 적게 발생한다. 이 영역에서 객체가 사라질 때 Major GC(혹은 Full GC)가 발생했다고 말한다.

![img](./images/gc1.png)

​				그림 1 GC 영역 및 데이터 흐름도

위 그림의 Permanent Generation 영역(이하 Perm 영역)은 Method Area라고도 한다. 객체나 억류(intern)된 문자열 정보를 저장하는 곳이며,Old 영역에서 살아남은 객체가 영원히 남아있는 곳은 절대 아니다. 이 영역에서 GC가 발생할 수도 있는데,여기서 GC가 발생해도 Major GC의 횟수에 포함된다.

그렇다면 "Old 영역에 있는 객체가 Young 영역에 있는 객체를 참조하는 경우는?"

Old 영역에는 512바이트의 덩어리(chunk)로 되어 있는 카드 테이블이 존재.

![img](./images/gc2.png)

​					그림 2 카드 테이블 구조

카드 테이블은 write barrier를 사용하여 관리한다. Write barrier는 Minor GC를 빠르게 할 수 있도록 하는 장치이다. Write barrier 때문에 약간의 오버헤드는 발생하지만 전반적인 GC시간은 줄어들게 된다.

## Young 영역의 구성

GC를 이해하기 위해서 객체가 제일 먼저 생성되는 Young 영역부터 알아보자. Young 영역은 3개의 영역으로 나뉜다.

- Eden 영역
- Survivor 영역(2개)

Survivor영역이 2개이기 때문에 총 3개의 영역으로 나뉘는 것이다. 각 영역의 처리 절차를 순서에 따라서 기술하면 다음과 같다.

- 새로 생성된 대부분의 객체는 Eden 영역에 위치합니다.
- Eden 영역에서 GC가 한 번 발생한 후 살아남은 객체는 Survivor 영역중 하나로 이동됩니다.
- 나의 Survivor 영역이 가득 차게 되면 그 중에서 살아남은 객체를 다른 Survivor 영역으로 이동한다. 그리고 가득 찬 Survivor 영역은 아무 데이터도 없는 상태로 된다.
- 이 과정을 반복하다가 계속해서 살아남아 있는 객체는 Old 영역으로 이동하게 된다.

![img](./images/gc3.png)

### Old 영역에 대한 GC

Old 영역은 기본적으로 데이터가 다 차면 GC가 발생한다. GC방식에 따라서 처리 절차가 달라지므로, 어떤 GC방식이 있는지 살펴보면 이해가 쉬울 것이다. 

- Serial GC
- Parallel GC
- Paralled Old GC
- Concurrent Mark & Sweep GC
- G1(Garbage First) GC

### Serial GC (-XX:+UseSerialGC)

Young 영역에서의 GC는 앞 절에서 설명한 방식을 사용한다. Old 영역의 GC는 mark-sweep-compact이라는 알고리즘을 사용한다. 이 알고리즘의 첫 단계는 Old 영역에 살아 있는 객체를 식별(Mark)하는 것이다. 그 다음에는 힙(heap)의 앞 부분부터 확인하여 살아 있는 것만 남긴다(Sweep). 마지막 단계에서는 각 객체들이 연속되게 쌓이도록 힙의 가장 앞 부분부터 채워서 객체가 존재하는 부분과 객체가 없는 부분으로 나눈다(Compaction).

Serial GC는 적은 메모리와 CPU 코어 개수가 적을 때 적합한 방식이다.

### Parallel GC (-XX:+UseParallelGC)

Parallel GC는 Serial GC와 기본적인 알고리즘은 같지다. 그러나 Serial GC는 GC를 처리하는 스레드가 하나인 것에 비해, Parallel GC는 GC를 처리하는 쓰레드가 여러 개이다. 그렇기 때문에 Serial GC보다 빠른게 객체를 처리할 수 있다. Parallel GC는 메모리가 충분하고 코어의 개수가 많을 때 유리하다. Parallel GC는 Throughput GC라고도 부른다.

### G1 GC

마지막으로 G1(Garbage First) GC에 대해서 알아보자. G1 GC를 이해하려면 지금까지의 Young 영역과 Old 영역에 대해서는 잊는 것이 좋다.

다음 그림에서 보다시피, G1 GC는 바둑판의 각 영역에 객체를 할당하고 GC를 실행한다. 그러다가, 해당 영역이 꽉 차면 다른 영역에서 객체를 할당하고 GC를 실행한다. 즉, 지금까지 설명한 Young의 세가지 영역에서 데이터가 Old 영역으로 이동하는 단계가 사라진 GC 방식이라고 이해하면 된다. G1 GC는 장기적으로 말도 많고 탈도 많은 CMS GC를 대체하기 위해서 만들어 졌다.

G1 GC의 가장 큰 장점은 성능이다. 지금까지 설명한 어떤 GC 방식보다도 빠르다. 하지만, JDK 6에서는 G1 GC를 early access라고 부르며 그냥 시험삼아 사용할 수만 있도록 한다. 그리고 JDK 7에서 정식으로 G1 GC를 포함하여 제공한다.

참조 : <https://d2.naver.com/helloworld/1329>

