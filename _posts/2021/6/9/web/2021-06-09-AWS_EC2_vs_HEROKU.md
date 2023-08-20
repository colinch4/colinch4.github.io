---
layout: post
title: "[web] AWS EC2 vs HEROKU"
description: " "
date: 2021-06-09
tags: [web]
comments: true
share: true
---

## AWS EC2 vs HEROKU

> 서버 배포시 어떤것이 더 효율적일까?

* ### 2가지 컨셉

  * `HEROKU`
    * 플랫폼으로서의 서비스(Platform as a Service) = `PaaS`
    * EX
      1. 장고 백앤드 작업 끝냄
      2. HEROKU에 가서 계정 생성하고 설정 해줌
      3. 5분안에 HEROKU가 이해하고 다 설치함
      4. 도메인 이름을 줌
      5. 나는 코드만 업로드했음(플랫폼이 나의 코드를 다 이해해주고, 그 플랫폼에 접근하기 위한 비용을 지불)
  * `AWS EC2`
    * 인프라로서의 서비스(Infrastructure as Service) = `IaaS`
    * EX
      1. 나를 도와줄 플랫폼이 없음
      2. 인프라(서버)를 위한 비용을 결제하는 것
      3. 내가 알아서 설정(git을 설치하여 레포지토리를 pull 혹은 파일질라)



* ### 고려해야할 3가지 요소

  1. 가격
     * `HEROKU > AWS EC2` 
     * HEROKU는 AWS 위에서 작동함
  2. 시간
     * 시간이 얼마나 있어? 시간은 소중하잖아!
       * 우분투, 유닉스, 서버, 포트 .... 배울 시간이 없을 때 `HEROKU!`
       * 클라우드 올리는 시간이라 배워야함
  3. 컨트롤
     * `HEROKU`의 경우 
       * 이미 파이썬이 다 설치 되어있음
       * 선택권이 없음--> 예를 들면 appache, nginx
     *  `AWS EC2`인 경우
       * 내가 인프라 설정
       * 선택권이 있음 --> 예를 들면 포트오픈 등등...
       * 더 많은 컨트롤을 가짐 
     * 컨트롤을 원하면 `AWS EC2`
     
     

* ### 경쟁

  * `AWS EB(Elastic Beanstalk)` vs `HEROKU`
    * AWS EB 더 저렴
    * HEROKU가 더 쉬움, 더 빠름, 사용하기 쉬움







#### 참고

https://www.youtube.com/watch?v=NTDhBh1SdZ4