---
layout: post
title: "[AWS] AWS Glossary"
description: " "
date: 2021-11-19
tags: [AWS]
comments: true
share: true
---

# AWS Glossary 
AWS 용어를 간략하게 알아보자.  
세부적인 내용은 각각의 개별적 Markdown file에서 참고 가능하다.  

> 링크를 클릭하여 이동 

| [A](#A) | [B](#B) | [C](#C) | [D](#D) | [E](#E) | [F](#F) | [G](#G) | [H](#H) | [I](#H) | [G](#G) | [K](#K) | [L](#L) | [M](#M) | [N](#N) | [O](#O) |
 [P](#P) | [Q](#Q) | [R](#R) | [S](#S) | [T](#T) | [U](#U) | [V](#V) | [W](#W) | [X, Y, Z](#XYZ) |[References](#References)|

 ---

## A
  * [**AMI**](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#AmazonMachineImage)  
  Amazon Machine Image  
  OS의 서버 이미지  
  Instance를 시작할 때 AMI를 지정해주어야 한다.

  * **AZ**  
  Available Zone | 가용 영역  
  데이터센터(IDC)를 말한다.  
  리전은 가용영역들의 집합이다.  
  동일 지역의 가용 영역은 전용선으로 연결되어 있다.  


## B
## C
  * [**CDN**](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#content-delivery-network)  
  Content Delivery Network  
  CloudFront로써 data, video, application 및 API를 안전하고 빠르게 전송한다.  


## D
  * [**Direct Connect**](https://aws.amazon.com/directconnect/)  
  전용선  
    * **Direct Connect 사용시의 장점**  
      1. 대역폭 비용 감소
      1. 일관된 네트워크 성능
      1. 모든 AWS Service와 호환 가능
      1. 간편성
      1. 탄력성
      1. Amazon VPC로 Private 연결
  
  * [**DNS**](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#domainnamesystem)  
  Domain Name System  
  문자로된 인터넷 주소를 Numeric IP Address<small>(숫자)</small>로 바꿔준다. 혹은 그 반대도 가능. 
    * 예)  
      <code>babytiger.netlify.com/</code> <--> <code>20X.189.105.112</code>   
      인간에겐 문자가 편리 | 컴퓨터에겐 숫자가 편리


## E
| [A](#A) | [B](#B) | [C](#C) | [D](#D) | [E](#E) | [F](#F) | [G](#G) | [H](#H) | [I](#H) | [G](#G) | [K](#K) | [L](#L) | [M](#M) | [N](#N) | [O](#O) |
 [P](#P) | [Q](#Q) | [R](#R) | [S](#S) | [T](#T) | [U](#U) | [V](#V) | [W](#W) | [X, Y, Z](#XYZ) |[References](#References)|
  * [**EBS**](https://aws.amazon.com/ebs/)  
  Amazon Elastic Block Store  
  하드디스크  
    * **Volume**  
    EBS로 생성한 디스크를 volume 이라고 일컫는다.
      * 4 Volume Types  
        1. Provisioned IOPS SSD (io1)
        1. General Purpose SSD (gp2)
        1. Throughput Optimized HDD (st1)
        1. Cold HDD (sc1)

  * **Elastic IP Address**  
  공인 IP 이지만 한번 할당되면 변하지 않는다.
  
  * [**EC2**](https://aws.amazon.com/ec2/)  
  Elastic Compute Cloud  
  서버  
  독립된 컴퓨터를 임대해주는 서비스.

  * **Edge Location**  
  CloudFront를 위한 캐시 서버  
    * Edge : CDN 서비스와 사용자가 직접 만난다는 의미

  * [**Elastic Load Balancing**](https://aws.amazon.com/elasticloadbalancing/)  
  들어오는 Traffic 분산시 사용 
      * **3 Types**
        1. **Application Load Balancer**  
          HTTP / HTTPS 트래픽에 적합
        1. **Network Load Balancer**  
          TCP / UDP / TLS 트래픽에 적합
        1. **Classic Load Balancer**  
          EC2 Instance에서 기본적인 로드 밸런싱을 제공


## F
  * **Firewall**  
  방화벽  
  인터넷에서 네트워크를 차단, 허용시 사용

## G
## H
## I
  * **Instance**  
  컴퓨터 한 대의 개념.  
  가상의 컴퓨팅 환경.  
  
  * [**IGW**](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)  
  Internet GateWay  
  IGW는 VPC의 Instance와 Internet 간에 통신할수 있도록 해준다.  
  IPv4, IPv6 를 지원.

## J 
## K
## L

## M
## N
## O
## P
  * **Public IP Address**  
  변경되는 공인 IP  
  AWS Instanc 시작할때 임의 IP로 할당된다.

## Q
## R
  * [**Region**](https://docs.aws.amazon.com/general/latest/gr/aws-general.pdf#rande-manage)  
  지역<small>(서비스 지역)</small>  
  나라 단위로 구분 된다. <small>(미국 리전, 한국 리전)</small>    
    * 각각의 리전은 독립적이다 == 서로 격리되어 있다.  
    * 지역별로 가격은 다름.
    * AWS Resource<small>(컴퓨터 etc)</small>가 어디에 놓이게 될 지 Region을 통해 선택 가능하다.  
    * 거리가 멀 수록 네트워크 경유지<small>(router)</small>가 많아지기에 속도가 느려지게 된다.  
    병목현상  
    지연시간<small>(latency)</small>을 줄이기 위해 적합한 리전을 선택하는 것이 중요하다.
    * [**Region Table**](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
    * [**Region Maps**](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)

## S
  * [**S3**](https://aws.amazon.com/s3/)  
  Amazon Simple Sroage Service  
  Image, Video, Mp3등의 콘텐츠 저장 서비스. 

## T
## U
## V
  * [**VPC**](https://aws.amazon.com/vpc/)  
  Virtual Private Cloud  
  네트워크 할당시 사용  
    * IP 주소 범위 선택
    * Subnets 생성    
    * Route table 및 Network Gateways 구성

## W
## X, Y, Z
## References
  * [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)
  * [AWS 전문가 되기](https://brunch.co.kr/@topasvga/76)
