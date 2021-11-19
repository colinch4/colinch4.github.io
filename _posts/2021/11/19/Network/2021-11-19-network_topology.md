---
layout: post
title: "[Network] Network Topology"
description: " "
date: 2021-11-19
tags: [Network]
comments: true
share: true
---


# Network Topology

다양한 통신망의 구성 형태에 대해 알아보도록 하자.

### Table of Contents
- [Network Topology](#network-topology)
    - [Table of Contents](#table-of-contents)
  - [About Network Topology](#about-network-topology)
    - [Bus](#bus)
      - [장점](#장점)
      - [단점](#단점)
    - [Hybrid](#hybrid)
      - [장점](#장점-1)
      - [단점](#단점-1)
    - [Mesh](#mesh)
      - [장점](#장점-2)
      - [단점](#단점-2)
    - [Ring](#ring)
      - [Token Passing](#token-passing)
      - [Data Flows](#data-flows)
      - [장점](#장점-3)
      - [단점](#단점-3)
    - [Star](#star)
      - [장점](#장점-4)
      - [단점](#단점-4)

## About Network Topology

통신망의 구성형태(이하 '네트워크 토폴로지'라 한다) 는 물리적 구성형태와 논리적 구성형태로 나뉜다.  
- 물리적 토폴로지  
  구성 요소(노드, 링크)의 배치 형태에 따라 구분  
  - 노드 : 파일 서버, 워크 스테이션, 주변 장치
- 논리적 토폴로지  
  데이터의 흐름에 따라 구분

네트워크가 논리적으로 물리적으로 연결되는 방식에 따라 각기 다른 장단점을 지니게 된다. 대표적으로 사용되는 네트워크 토폴로지는 버스(bus)형, 하이브리드(hybrid)형, 망(mesh)형, 링(ring)형, 성(star)형이 있다.  

|Types|Protocol|Cable|
|-----|--------|-----|
|BUS|LAN|Coaxial, Fiber, Twisted Pair|
|HYBRID|||
|MESH|WAN||
|RING|LAN||
|STAR|LAN, Ethernet|Fiber, Twisted Pair|

용도에 맞는 네트워크 토폴로지를 선택하기 위해서 고려해야 할 사항은 아래와 같다.  
- 비용  
- 내결함성
- 회선의 종류  
- 확장의 필요성


### Bus
> Backbone Topology 또는 Line Topology 라고도 불린다.  

한개의 통신 회선(cable)에 여러 노드들이 연결된 형태. 회선의 양쪽 끝부분에 Terminator 가 필요하다. 각각의 노드들은 Adapter 로 연결되어 있다.

보통 버스형은 LAN 과 같이 작은 규모의 네트워크에 사용된다.

<img src="https://user-images.githubusercontent.com/48475824/118780328-e4682d00-b8c6-11eb-8d1b-6240cffcbce3.png" alt="topology diagram info" title="topology diagram info" width="180" />

![bus topology](https://user-images.githubusercontent.com/48475824/118779638-35c3ec80-b8c6-11eb-9ff0-7e1f46e49e2f.gif)


#### 장점
- **간편한 설치**  
  간단한 구조로 인해 설치가 어렵지 않음
- **저렴한 비용**  
  다른 토폴로지에 비해서 적은 길이의 케이블이 사용됨
- **특정 노드가 실패 했을 시 다른 노드에 영향을 주지 않음**
- **쉬운 노드의 추가 및 삭제**

#### 단점
- **메인 회선이 고장났을시 네트워크 전체에 영향을 줌**
- **병목 현상**  
  한 회선에서 단일한 방향으로 데이터가 흐른다.  
  대용량의 트래픽에 적합하지 않으며 그로인해 버스형은 작은 규모의 네트워크에 사용된다.  
  - 예) LAN  

  각각의 노드들이 한가지 회선의 대역폭을 공유하기 때문에 연결된 노드의 수가 늘어나면 늘어날 수록 성능은 저하된다.
- **연결 가능한 노드수가 한정적임**  
  버스의 길이가 한정적이기 때문에 연결 가능한 노드도 한정적
- **낮은 보안성**  

[↑ return to TOC](#table-of-contents)


### Hybrid  
두가지 이상의 통신망의 구성 형태가 함께 사용되는 토폴로지.  
- 예)  
  - Star + Bus Topology
  - Star + Ring Topology


#### 장점
- 높은 신뢰성 

#### 단점

[↑ return to TOC](#table-of-contents)


### Mesh
각각의 노드는 다수의 노드들과 연결되어 그물망의 형태를 지니게 된다.  
망형은 두 가지 타입으로 구분된다.  
- Full Mesh
- Partial Mesh

#### 장점

#### 단점
- 비싼 비용  
- 어려운 설치  
  복잡한 구조로 인해 설치하기가 쉽지 않다.  
- MSAL 필요  
  Multi-Station Access Unit 이 요구된다.

[↑ return to TOC](#table-of-contents)


### Ring
각각의 노드들은 두 개의 이웃(근접한) 노드들과 연결돼 있다. 연결된 노드들은 고리의 형태를 이룬다.  

링형은 대체적으로 LAN에서 많이 사용된다. 그럴수 밖에 없는 것이 토큰 패싱을 사용하는 링형은 IBM에서 1980년대에 LAN을 위해 만들어 졌기 때문이다.  
- 80-90 년대는 어떤 기술을 LAN에 접목시켜야 하는지 활발하게 토론이 오갔던 시기.  

#### Token Passing
링형은 토큰 패싱(token passing)을 통해 데이터를 전송한다.  
  - **토큰 구조**  
    <img src="https://user-images.githubusercontent.com/48475824/119010605-34321b80-b9cf-11eb-9dc7-12644c279f46.png" alt="token" title="ring topology token" width="400" />

    토큰은 세개의 필드로 구성되어 있다.  
    1. Start Delimiter (1 byte)
    1. Access Control (1 byte)  
      우선순위에 관한 정보가 담겨 있다.  
      높은 우선순위를 가진 노드가 프리 토큰을 먼저 사용하게 된다.  
    1. End Delimiter (1 byte)
  - **토큰에 데이터 담아 보내기**  
    X-노드 에서 Y-노드로 보내야 할 데이터가 있다면 그전까지 비어있던 토큰(free token)에는 보내야할 데이터가 담긴다.  
    이 데이터는 `Access Control` 과 `End Delimiter` 사이에 담겨 보내지게 된다. `End Delimiter`의 뒷부분 꼬리에는 `Frame Status`가 붙는다. 토큰의 데이터는 `Destination Address`에 담긴 노드로 전송된다. Y-노드(목적지 노드)에 토큰이 도착하면 프레임을 복사하여 목적지 노드에게 전달한 후 `Frame Status` 를 성공으로 바꾼다. 원본 프레임은 회선을 따라 `Source Address`를 기준으로 X-노드(송신 노드)로 되돌려진다. 프레임이 송신노드에 성공적으로 도달하면 해당 노드는 토큰에 적재되어 있는 데이터를 제거한후 빈 토큰(free token)으로 만들어 준다.

    ![token with data](https://user-images.githubusercontent.com/48475824/119012104-b111c500-b9d0-11eb-8812-f85330f028ee.png)
    - **Frame Control** (1 byte)  
      데이터 프레임(data frame) 또는 제어 프레임(control frame) 정보가 담겨 있다.  
      - `00` : data frame
      - `11` : control frame
    - **Destination Address** (6 bytes)  
      데이터가 전송될 목적지 주소가 담겨있다.  
      - 고유하게 구별되는 MAC 주소가 사용된다.  
        - 2 bytes : local address
        - 6 bytes : global address
    - **Source Addres** (6 bytes)  
      데이터를 보낸 송신지의 주소가 담겨 있다.  
    - **Data** (0~8,182 bytes)  
      IP Packet : 실질적으로 전송해야 하는 데이터  
    - **Frame Check Sequence** (4 bytes)  
      CRC 에러 관련 정보가 담겨 있다.  
    - **Frame Status** (1 byte)  
      데이터의 전송 상태의 정보가 담겨 있다.  
      데이터가 성공적으로 전송 됬다는 것은 프레임 복사본이 도착지에 성공적으로 전송되었다는 것을 의미한다.  

      A와 C 두 비트가 존재한다.  
      - `A` = 1  
        Address-Recognized Bits : 이는 데이터가 목적지에 거쳤음(도착함) 을 의미  
      - `C` = 1  
        Frame-Copied Bits : 전송할 데이터의 복사본이 목적지에 전송됨을 의미  

#### Data Flows
링형은 단일링형과 이중링형이 있다.
- **단일링형**  
  단방향(Unidirectional) : 한 회선에서 데이터 트래픽이 한 방향으로만 흐름.  
   Half-duplex 네트워크라고 불리기도 한다.  
  - Clockwise
  - Counterclockwise  
 
  ![Unirectional ring topology](https://user-images.githubusercontent.com/48475824/119003542-c4b92d80-b9c8-11eb-9f9d-00ff23b09c6b.gif)

- **이중링형**  
  양방향(Bidirectional) : 두 회선에서 데이터 트래픽이 각각 반대 방향으로 흐름.  

  ![Bidirectional ring topology](https://user-images.githubusercontent.com/48475824/119005010-072f3a00-b9ca-11eb-9939-b89d905814b4.gif)


#### 장점
- **간편한 설치**  
  어렵지 않은 레이아웃으로 인해 설치가 간단하다.
- **저렴한 비용**  
  버스형과 마찬가지로 적은 길이의 케이블이 사용됨.
- **낮은 데이터 충돌 가능성**  
  단일링형이든 이중링형이든 데이터는 회선에서 동일한 방향으로 흐르기 때문에 데이터 충돌이 거의 발생하지 않는다.  
  그에 반해 `CSMA/CD` 방식을 사용하는 Ethernet 에서는 데이터 충돌이 발생한다.
- **수월한 에러 대처**  
  토큰은 각각의 노드를 순차적으로 통과한다. 만약 특정 노드에서 문제가 발생했다면 토큰은 문제가 생긴 노드를 통과하지 못하며 이전 노드로 되돌아 가게 된다. 이는 에러가 발생한 노드를 발견하기가 쉽게 해준다.  
- **동일한 데이터 전송 속도**  
  

#### 단점
- **낮은 보안성**  
- **느린 전송 속도**  
  고리모양의 회선을 모두 돌아야 함(데이터가 전송 된 후 송신 노드로 되돌아 와야 끝남).
- **어려운 노드 추가 및 삭제**  
  확장성이 용이하지 않다. 새로운 노드를 추가하기 위해 회선을 끊고 연결 시켜야 한다. 회선이 끊어져 있는 동안 네트워크는 동작하지 않는다.
- **한 노드의 장애는 전체 네트워크의 장애를 유발**  
  노드 하나에서 장애가 발생하게 됬을시 네트워크 전체에 영향을 주게 된다.  

[↑ return to TOC](#table-of-contents)

### Star

각각의 노드들은 중앙에 위치한 허브와 연결되어 있다. 허브를 중심으로 여러 기기가 연결된 모습이 별과 같다고 하여 스타 토폴로지라 불리운다. 성형은 큰 규모, 작은 규모 네트워크 가릴것 없이 가장 많이 사용되는 토폴로지 중 하나이다.  

스타 토폴로지에서 중앙 장치(허브 또는 스위치)는 링크를 통해 각각의 노드(기기) 들과 데이터를 주고받는다.

<img src="https://user-images.githubusercontent.com/48475824/122074915-964a3900-ce34-11eb-9b1f-18a4877cbf99.png" alt="star-topology" title="star topology" width="450" />

#### 장점
- **수월한 에러 대처**  
  특정 노드에서 장애가 발생했을 때 해당 노드는 응답을 하지 않기 때문에 장애 노드를 쉽게 발견 가능하다.
- **유연한 확장성**  
  노드를 추가 및 제거하기가 쉽다.

#### 단점
- **허브의 장애시 전체 네트워크의 장애를 유발**  
  허브에서 장애가 발생했을 시 이에 의존하는 노드들도 함께 영향을 받게 된다.  

[↑ return to TOC](#table-of-contents)
