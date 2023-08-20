---
layout: post
title: "[CS] Data Transmission"
description: " "
date: 2021-11-19
tags: [CS]
comments: true
share: true
---

## Data Transmission
데이터를 한 지점에서 다른 지점으로 보내는 방법에 대해 알아보자.  
> 데이터 전송에서 살펴볼 주제들은 아래와 같다.
  * Serial | Parallel
    * [직렬 | Serial](#Serial) 
    * [병렬 | Parallel](#Parallel)
  * Synchronous | Asynchronous | Isochronous
    * [동기 | Synchronous](#Synchronous)
    * [비동기 | Asynchronous](#Asynchronous)
    * [등시성 | Isochronous](#Isochronous)  

![data-transmission](https://user-images.githubusercontent.com/48475824/74103194-890ca280-4b8d-11ea-89dc-7e09b895a070.png)


## Serial | Parallel
Digital Data 즉, 0과 1의 데이터를 보낼때는 고려해야 할 점들이 많다. 예를들어 한번에 데이터를 몇 개씩 전송할 것인지? 데이터를 보낼때 묶어서 보낼 것인지? 배선의 형태는 어떤 것을 선택할 것인지 등이 있다. 

데이터 전송방식은 직렬전송 또는 병렬전송의 방법중 선택할 수 있다. 직렬 처리가 분기해서 병렬이 되거나 병렬이 다시 합류하여 직렬이 되기도 한다. 

직렬과 병렬, 각각의 장단점에 대해 알아보자.


### Serial
직렬 전송 : 1차선 도로  
데이터<small>(비트들)</small>가 하나의 통로로만 직렬로 줄지어진채 전송된다.  
![serial-data](https://user-images.githubusercontent.com/48475824/74102304-bd7c6080-4b85-11ea-8cad-81c2a944d419.png)

직렬 전송 방식은 3가지로 나눌 수 있다.  
<small>(각각에 대해서는 아래에서 자세히 알아보도록 하겠다.)</small>
  1. 동기식 Synchronous
  1. 비동기식 Asynchronous
  1. 등시식 Isochronous

#### 직렬 전송의 특징
* 하나의 채널만 이용
  * 한 비트 뒤로 다음 비트가 따라오므로 통신하는 두 장치간 하나의 채널만을 사용.
  * 병렬 전송에 비해 1/n 만큼 비용 절감 가능.

* 비동기 또는 동기식으로 구성

* 직렬 전송으로 속도를 올리는데는 한정적

* 장거리 연결에 좋다
  * LANs

* 구조가 간단하여 설계,구현 난이도가 낮다.

#### 직렬 전송의 예
* USB
* Bluetooth
* Ethernet
* IrDA


### Parallel
병렬 전송 : 2차선 이상의 도로  
데이터가 2개 이상의 병렬로 늘여놓아진 통로를 통해 전송된다. 
 * 한 번에 1개의 비트가 아닌 n개 그룹의 비트를 함께 전송한다.  
![parallel-data](https://user-images.githubusercontent.com/48475824/74102590-409eb600-4b88-11ea-94e5-7c5464951b2d.png)  

웹 서비스는 수많은 사용자들의 요청을 처리하기 위해 많은 서버를 배치하여 병렬로 처리한다. 병렬화만 한다고 성능이 향상되지는 않는다. CPU 코어나 서버를 병렬화 할 때는 '병렬화한 하드웨어들을 어떻게 효율적으로 활용하느냐'에 대해 관심을 가져야 한다. 

#### 병렬 전송의 특징
 * 비싼 가격
  * 여러개의 선을 써야 하기에 그 만큼 가격이 올라간다.

 * 거리가 길어지면 Delay가 발생

 * 병렬화시 단위 시간당 데이터 처리량이 늘어남
  * 처리 시간이 빨라지는 것이 아니라 처리량이 늘어나는 것.
  * 합류점, 직렬화 구간, 분기점으로 인해 병목현상이 발생
    * **병목** : 차선으로 비유를 하자면 다차선이 1차선으로 합류 될 때 혼잡해지게 되어 병목현상이 발생하게 된다. 그 지점은 전체 흐름을 느리게 만드는 부분이 된다.
    * 해결책 : CPU 코어를 늘려 처리를 분담시키기

* 오버헤드 발생
  * 병렬화를 통해 일을 분담해서 처리한후 다시 집약시에 오버헤드가 발생한다.
  * 오버헤드를 감안하더라도 효과를 볼 경우에만 병렬화를 진행하는 것이 좋다.
  * 오버헤드를 예상하여 어떤 부분을 병렬화 할지 파악해야 한다.

* 구조가 복잡하여 설계, 구현 난이도가 높다.

* 다수의 리소스를 유용하게 이용할 수 있다.
  * 일부가 문제가 발생하더라도 처리를 계속할 수 있다.


#### 병렬 전송의 예
* PCI bus
* PCMCIA
* SCSI-2


## Synchronous | Asynchronous | Isochronous
### Synchronous
동기
### Asynchronous
비동기
### Isochronous
등시성
