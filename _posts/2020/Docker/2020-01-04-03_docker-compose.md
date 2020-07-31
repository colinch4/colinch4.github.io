---
layout: post
title: "[Docker] 3. docker-compose"
description: " "
date: 2020-01-04
tags: [Docker]
comments: true
share: true
---

# docker-compose

* 도커 어플리케이션을 정의하고 실행하는 도구

  * 도커 명령어를 손 쉽게 관리하게 해줌
    * docker명령어가 아니다!
  * 각 컨테이너별로 별도의 Docker 명령어 실행
  * 한 번에 여러 개의 컨테이너 동시 실행

* yml파일의 내용을 해석하여 실행

  * 들여쓰기 딱딱 맞아야됨

* yml파일 구성

  > ```yml
  > version: '3.1'
  > services:
  >  servicename:
  >      image: #optional
  >      ports: #optional
  >      environment: #optional
  >      volumes: #optional
  >  servicename2:
  > volumes: #optional
  > network: #optional
  > ```
  >
  > 들여쓰기 딱딱 맞아야됨.
  >
  > services의 내용만 바꿀 수 있음

  > 예시
  >
  > ```yml
  > version: "3"
  > services:
  >  mysql:
  >      image: example/echo:latest
  >      ports:
  >             - 9000:8080
  > ```

  > docker-composer를 통한 실행
  >
  > `$docker compose up`
  >
  > * -d 를 이용하여 백그라운드로 실행 가능
  >
  > docker-compose를 통한 종료
  >
  > `$ docker -compose down`

* 장점

  * 서비스를 여러개 만들 수 있음
    * 그러면서 속성값도 변경해줄 수 있음

