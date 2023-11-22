---
layout: post
title: "[AWS] CloudFront"
description: " "
date: 2021-11-19
tags: [aws]
comments: true
share: true
---


## CloudFront
> Reference : [CloudFront](https://aws.amazon.com/ko/cloudfront/features)

<img width="150" alt="CloudFront" src="https://user-images.githubusercontent.com/48475824/89286048-7da5ba00-d68c-11ea-9977-505ca988cd88.png">


### Table of Contents
- [CloudFront](#cloudfront)
    - [Table of Contents](#table-of-contents)
  - [About CloudFront](#about-cloudfront)
    - [Edge Location](#edge-location)
  - [CloudFront Log](#cloudfront-log)
    - [CloudFront Pricing](#cloudfront-pricing)
      - [1. S3 Bucket Storage 요금](#1-s3-bucket-storage-요금)
      - [2. Edge Location 객체 서비스 요금](#2-edge-location-객체-서비스-요금)
      - [3. 오리진에 데이터 제출에 대한 요금](#3-오리진에-데이터-제출에-대한-요금)
      - [4. HTTPS 요청에 대한 요금](#4-https-요청에-대한-요금)

## About CloudFront  
CloudFront는 웹 콘텐츠를 유저에게 더 빨리 배포할 수 있도록 지원해주는 아마존 서비스이다.  
* 웹 콘텐츠 : html, css, js, image, video ...etc  

사용자에게 빠르게 콘텐츠를 전달하기 위해 엣지(Edge) 로케이션을 이용한다. 

### Edge Location  
![CloudFront Network Map 13May2020 c3b10a8bfd4203333c1ef6878211a8366ff4d1f5](https://user-images.githubusercontent.com/48475824/89286490-44ba1500-d68d-11ea-87e8-515c5b72a4a8.png)
> 이미지 출처 : [AWS CloudFront](https://aws.amazon.com/ko/cloudfront/features/)

현재(08.04.2020) 전 세계 42개국 94개 도시에 216개의 엣지 로케이션이 존재한다.  

CloudFront는 콘텐츠를 요청한 유저와 제일 가까운 엣지 로케이션에서 콘텐츠를 제공해 줌으로써 지연시간을 줄일 수 있도록 해준다.
  * 서울에 거주하는 유저가 다른 국가에 있는 콘텐츠를 요청 했을 시, AWS는 서울 엣지 로케이션에서 해당 컨텐츠를 제공해준다.  

유저가 요청한 콘텐츠가 물리적으로 멀리 떨어진 곳에 있을 때 해당 콘텐츠는 여러 네트워크의 경로를 거쳐야 한다. 그로인해 지연시간이 발생하게 되는데 CloudFront는 이러한 병목현상을 줄이기 위해 가까운 엣지 로케이션에서 컨텐츠를 보내주는 역할을 하는 것이다.  

<!-- ### 엣지 로케이션에 콘텐츠가 존재할 시 
  CloudFront는 존재하는 콘텐츠를 즉각 유저에게 제공해 준다.  

### 엔지 로케이션에 콘텐츠가 존재하지 않을 시  
  CloudFront는 해당 콘텐츠가 위치한 오리진  -->


[↑ return to TOC](#table-of-contents)


## CloudFront Log  

[↑ return to TOC](#table-of-contents)


### CloudFront Pricing  
CloudFront와 관련하여 청구되는 비용으로 아래의 4가지가 있다.  

#### 1. S3 Bucket Storage 요금
S3 버킷에 객체를 보관하는 비용.
* 이 요금은 AWS 청구서의 Amazon S3 부분에서 확인 가능.

#### 2. Edge Location 객체 서비스 요금
CloudFront가 객체 요청에 응답할 때 발생하는 비용.  
* WebSocket 데이터의 서버에서 클라이언트로의 전송에 따른 금액이 포함.  
* 이 요금은 AWS 청구서의 CloudFront 부분에 리전 -DataTransfer-Out-Bytes로 표시.

#### 3. 오리진에 데이터 제출에 대한 요금 
사용자가 HTTP Methods ```(DELETE, OPTIONS, PATCH, POST,and PUT)``` 를 포함하는 데이터 요청을 Origin에 전송하는 비용.  
* 이 요금은 AWS 청구서의 CloudFront 부분에 리전 -DataTransfer-Out-OBytes로 표시.

#### 4. HTTPS 요청에 대한 요금  
HTTPS 관련 요청에 대한 추가적인 비용이 발생할 수 있다.  

[↑ return to TOC](#table-of-contents)
