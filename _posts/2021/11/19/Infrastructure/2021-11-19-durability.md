---
layout: post
title: "[Infrastructure] Durability"
description: " "
date: 2021-11-19
tags: [Infrastructure]
comments: true
share: true
---

# Durability 
**내구성 (Durability)**  
```내구성 != 용량```

### Table of Contents
- [Durability](#durability)
    - [Table of Contents](#table-of-contents)
  - [내구성이란](#내구성이란)
    - [99.999999999% 의 의미](#99999999999-의-의미)
  - [Cloud 와 내구성](#cloud-와-내구성)
    - [AWS S3 와 내구성](#aws-s3-와-내구성)
  - [DB 와 내구성](#db-와-내구성)


## 내구성이란
내구성이란 '스토리지가 안정적으로 데이터를 기억할 수 있는 성질'을 말한다.

### 99.999999999% 의 의미  
Amazon S3 의 내구성은 99.999999999% 로 표현된다.  
이는 S3에 1억개의 객체를 저장했을 때 10,000년 이란 시간 동안 S3 에 저장된 객체 하나가 손실될 확률을 의미한다.
하지만 이 내구성의 결과는 실험하에 나온 확실한 결과가 아니다. AWS가 S3 버킷에 객체를 넣어두고 1만년이란 기간동안 실험 해 본 것이 아니다(AWS 의 등장은 2006년).  

Amazon 외에도 Google사의 GCP Storage 의 내구성 또한 99.999999999% 로 표현되며 Microsoft 사의 Azure 또한 내구성을 99.999999999% 로 보장한다. 여러 클라우드사가 내구성을 9's 로 표현할 수 밖에 없는 이유는 애초에 정확한 측정 숫자를 제공하기가 어렵기 때문이다. 딱 떨어지는 정확한 숫자의 결과를 제공하는 대신 높은 내구성을 표현하기 위해 9's 를 사용한다.

[↑ return to TOC](#table-of-contents)

## Cloud 와 내구성
클라우드에서 내구성이란, 데이터가 어느정도로 안전하고 탄력성있게 변형없이 그 상태를 유지하는 것을 의미한다.

데이터가 온전치 못하게 되는데 영향을 주는 요소로는 **데이터 손실** 과 **데이터 손상** 의 경우가 있다.

### AWS S3 와 내구성
아마존이 내세우는 S3의 강점은 내구성과 [가용성](https://github.com/8luebottle/TIL/blob/master/Infrastructure/stability.md)이다.  
위에서도 언급 했듯이 99.999999999% 라는 강력한 가용성을 자랑하는데, 행여나 데이터가 손실 되더라도 빠르게 복원 되도록 설계 되어 있다. 그 이유는 저장된 객체(데이터)를 여러 시설에 동기식으로 중복하여 저장해 놓기 때문이다.  
* 동일한 region 내에 3개의 가용영역(AZ)에 데이터를 중복 저장.  

2006년 3월 14일 미국에서 처음 선보인 S3가 강한 내구성을 가질 수 있는데는 마이크로서비스 설계 기반이기 때문이다.

[↑ return to TOC](#table-of-contents)

## DB 와 내구성  
DB에서의 내구성은 DB 트랜잭션이 지닌 ACID 특성에서 맨 끝 글자 D 를 뜻한다. 이는 DB가 Crash 나더라도 트랜잭션이 손실되거나 지워지지 않는 성질을 의미한다.  

* ACID
  * **A**tomicity
  * **C**onsistency
  * **I**solation
  * **D**urability

[↑ return to TOC](#table-of-contents)
