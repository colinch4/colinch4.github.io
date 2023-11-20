---
layout: post
title: "[Cloud Computing] Cloud Computing"
description: " "
date: 2021-11-19
tags: [개발]
comments: true
share: true
---

## Cloud Computing
WIP : 틈틈이 지속적으로 작성중인 글 입니다.

### Table of Content

- [Cloud Computing](#cloud-computing)
    - [Table of Content](#table-of-content)
  - [Cloud](#cloud)
    - [클라우드 이름의 유래와 등장 배경](#클라우드-이름의-유래와-등장-배경)
    - [클라우드 중요성](#클라우드-중요성)
    - [클라우드 특징](#클라우드-특징)
      - [장점 | 유지관리](#장점--유지관리)
      - [장점 | 유연성 증가](#장점--유연성-증가)
      - [장점 | 글로벌 서비스](#장점--글로벌-서비스)
      - [장점 | 비용](#장점--비용)
      - [단점 | 의존도](#단점--의존도)
      - [단점 | 중요 데이터 외부 보관](#단점--중요-데이터-외부-보관)
      - [단점 | 비용](#단점--비용)
  - [Cloud Services](#cloud-services)
    - [Type of Services](#type-of-services)
      - [Public Cloud](#public-cloud)
      - [Private Cloud](#private-cloud)
      - [Hybrid Cloud](#hybrid-cloud)
      - [IaaS](#iaas)
      - [PaaS](#paas)
      - [SaaS](#saas)
  - [Key Technologies](#key-technologies)
    - [Virtualization](#virtualization)
    - [Parallel Programming](#parallel-programming)
    - [Mass Distributed Storage](#mass-distributed-storage)
    - [Data Management](#data-management)
  - [Cloud Computing Value Chain](#cloud-computing-value-chain)
  - [Top Cloud Computing Platform](#top-cloud-computing-platform)
    - [Amazon](#amazon)
    - [Google](#google)
    - [Microsoft](#microsoft)
    - [Huawei](#huawei)

## Cloud

클라우드 사업자가 제공하는


### 클라우드 이름의 유래와 등장 배경

**클라우드 이전 : On-premise**  
클라우드 서비스가 등장하기 전 모든 회사는 온프레미스 환경에서 고객들에게 서비스를 제공하였다. 

<img width="550" alt="on-premise" src="https://user-images.githubusercontent.com/48475824/78931900-97b9fc00-7ae1-11ea-9c33-409e0902d28e.png">

On-premise는 시스템 운용시 필요한 설비들이 자체 회사 내에(on the  premises) 있는 것을 말한다. 

클라우드 컴퓨팅이 등장하기 전부터 사용 되어진 전통적인 방식이다. 서버와 네트워크 기기등을 모두 자사에서 관리하기에 기업이 원하는 방식대로 커스터마이징을 할 수 있다. 라이선스와 버전업도 직접 관리한다.

**AWS**  
아마존 클라우드의 등장은 '어떻게 하면 엔지니어의 생산성을 올릴 수 있을까?' 라는 질문에서 부터 시작했다.  
개발자가 실질적 개발을 시작하기 까지 인프라를 설정하고 관리하는 부분에서 걸리는 시간과 노력의 비용을 절감하고자 하였다.

### 클라우드 중요성

### 클라우드 특징
장점과 단점을 통해 클라우드가 지닌 특징이 무엇인지 알아보자.  

* **장점** : 유지관리, 유연성, 탄력성, 글로벌 서비스, 비용  
* **단점** : 의존도, 중요 데이터 외부 보관, 비용

#### 장점 | 유지관리

간단한 유지관리.  
Virtualization, Hardware, Storage, Server등 많은 부분을 관리할 필요가 없다. 최소한의 작업만으로 편리하게 시스템을 관리 할 수 있게 된다.  
클라우드를 이용함으로써 개발자는 이전에 인프라에 썻던 시간들을 집중적으로 프로젝트에 사용 할 수 있게 된다.

#### 장점 | 유연성 증가

인프라를 조정하는데 유연성이 확장되었다. 트래픽이 급변하거나 예측할 수 없는 환경에서도 유연성을 자랑한다.  
오토스케일링(Auto Scaling)을 통해 용량을 동적으로 확장시키거나 축소시킬 수 있다.

#### 장점 | 글로벌 서비스

세계 각지에 위치한 클라우드사의 데이터센터를 통해 보다 빠른 서비스를 제공할 수 있게된다.

#### 장점 | 비용

시간과 금전적 비용을 절약할 수 있다. 초기 자본 비용이 적게 들어간다.  
복잡한 인프라를 몇번의 클릭을 통해 짧은 시간 내에 구축가능하다.  
월별 클라우드 사용량에 대한 비용만 지불하면 되기에 비용 절감의 효과를 볼 수 있다.

#### 단점 | 의존도

#### 단점 | 중요 데이터 외부 보관

기업의 핵심 자산인 데이터를 기업 외부에서 보관하는데에 따른 불안함이 존재한다.  
민감한 데이터를 다루는 기업이라면 public cloud 대신 private 이나 hybrid cloud 를 사용하는 것이 권장된다.

#### 단점 | 비용  

비용적인 면에서는 클라우드 서비스를 어떻게 이용하느냐에 따라 장점이 될 수도 단점이 될 수 도 있다.

[↑ return to TOC](#table-of-contents)

## Cloud Services

### Type of Services

클라우드 서비스를 구축 유형 또는 서비스에 따라 나눌 수 있다.  

* 구축 유형에 따른 분류
  * Public Cloud
  * Private Cloud
  * Hybrid Cloud
* 서비스 유형에 따른 분류
  * IaaS
  * PaaS
  * SaaS

<img width="550" alt="cloud-example" src="https://user-images.githubusercontent.com/48475824/78933059-9c7faf80-7ae3-11ea-8c65-69ca78d46e03.png">

피라미드 아래로 내려갈 수록 복잡성이 증가하는데 클라우드 이용자가 관리해야 하는 항목들이 많아지기 때문이다.  
피라미드 위로 올라갈수록 직접 관리할 항목이 줄어들기에 컨트롤하기는 편하지만 그만큼 유연성이 떨어지게 된다.  

![cloud-pyramid](https://user-images.githubusercontent.com/48475824/78932281-2c245e80-7ae2-11ea-86b5-9a065a96f317.png)  
* **복잡성 :** IaaS > PaaS > SaaS  
* **유연성 :** IaaS < PaaS < SaaS  
  
#### Public Cloud

불특정 다수에게 제공되는 클라우드 서비스.

#### Private Cloud

특정한 이용자에게만 제공되는 클라우드 서비스.

#### Hybrid Cloud
 
[↑ return to TOC](#table-of-contents)
 
 #### IaaS
 **I**nfrastructure **a**s **a** **S**ervice
 
 #### PaaS
 **P**latform **a**s **a** **S**ervice
 
 #### SaaS
 **S**oftware **a**s **a** **S**ervice  
구독 기반으로 제공되는 서비스

[↑ return to TOC](#table-of-contents)

## Key Technologies

클라우드 핵심 기술

### Virtualization

**가상화**는 클라우드를 지탱하는 주요 기술중 하나이다.  
가상화는 하나의 물리적인 '시스템을 마치 여러 물리적 시스템이 존재하는 것'(가상) 처럼 독립적으로 분리시키는 것을 말한다. 같은 시스템을 잘개 쪼개어 사용함으로써 제한된 자원을 효율적으로 사용할 수 있게 된다. 가상화 기술을 통해 단일의 서버 자원을 다수로 쪼개어 여러 유저들이 사용할 수 있도록 만들어준다.

가상화를 실현시키기 위해서 필요한 기술은 분산처리와 컨테이너이다.

### Parallel Programming

병렬 프로그래밍

### Mass Distributed Storage

### Data Management

데이터 관리 

[↑ return to TOC](#table-of-contents)
 
 
## Cloud Computing Value Chain 

[↑ return to TOC](#table-of-contents) 
 
 
## Top Cloud Computing Platform
클라우드 시장에서의 경쟁력을 크게 좌우하는 것중 하나는 규모의 경제다.

### Amazon
AWS  
아마존의 가격 인하 정책  

### Google
GCP

### Microsoft
Azure

### Huawei
Huawei Cloud

[↑ return to TOC](#table-of-contents)
