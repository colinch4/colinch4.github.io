---
layout: post
title: "[Docker] 4. Docker Swarm"
description: " "
date: 2020-01-04
tags: [docker]
comments: true
share: true
---

## Docker Swarm

* 오케스트레이션
* 여러 docker host를 클러스트로 묶어주는 컨테이너 오케스트레이션



| 이름    | 역할                                                         | 대응하는 명령어 |
| ------- | ------------------------------------------------------------ | --------------- |
| compose | 여러 컨테이너로 구성된 도커 어플리케이션을 관리 (주로 단일 호스트) | docker-compose  |
| Swarm   | 클러스트 구축 및 관리(주로 멀티 호스트)                      | docker swarm    |
| Service | 스웜에서 클러스트 안의 서비스(컨테이너 하나 이상의 집합)을 관리 | docker service  |
| Stack   | 스웜에서 여러 개의 서비스를 합한 전체 어플리케이션을 관리    | docker stack    |



Dockerfile -> Compose -> Service -> Stack



#### Swarm vs 쿠버네티스

* 적은 호스트 : Swarm이 유리
* 많은 호스트 : 쿠버네티스가 유리



**Swarm을 경험하기 위해서 dind(Docker in Docker)사용**



#### Manager에 Swarm설정

* Manager container에 docker swarm init 설정 -> Swarm 모드 활성화
* worker 컨테이너 등록 with join token



#### 레지스트리에 등록 방법

* 이미지 태그를 변경

  > 예시
  >
  > `docker tag busybox:latest localhost:5000/busybox:latest`

* 이미지를 로컬 호스트로 추가

  > 예시
  >
  > `docker push localhost:5000/busybox:latest`

#### 레지스트리에서 사용 방법

* 레지스트리로부터 이미지 pull

  > 예시
  >
  > `docker pull registry:5000/busybox:latest`
  >
  > registry 대신 ip주소 사용해도 됨.
  >
  > registry는 컨테이너명




#### 명령어

> ```shell
> $ docker swarm init	# 스웜 초기화
> $ docker swarm join ... # ...에 참여
> ```



#### Docker Service

* Service
  * 어플리케이션을 구성하는 일부 컨테이너 (단일 또는 복수)를 제어하기 위한 단위

> ```shell
> $ docker exec -it manager \
> 	docker service create --replicas 1 --publish 8000:8080 --name echo\
> 	registry:5000/example/echo:latest
> $ docker exec -it manager service ls
> $ docker exec -it manager sclae echo=6
> $ docker exec -it manager service ps [ServiceName]
> $ docker exec -it manager service rm [ServiceName or ServiceID]
> ```
>



## Docker Stack

#### Docker Stack

* 하나 이상의 서비스를 그룹으로 묶은 단위, 어플리케이션 전체 구성 정의
  * 서비스는 어플리케이션 이미지를 하나 밖에 다루지 못함
* 여러 서비스를 함께 다룰 수 있음
* 스택을 사용해 배포된 서비스 그룹은 overlay 네트워크에 속함

####  명령어

> ```shell
> $ docker stack ls
> $ docker stack services [Service Name]
> ```

#### overlay

> 오버레이 생성
>
> `$ docker network create --driver=overlay --attachable [name]`

> `$ docker stack deploy -c [filePath] [stack name]`
>
> > `docker stack deploy -c /stack/my-webapi.yml echo`



