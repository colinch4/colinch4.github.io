---
layout: post
title: "[Container] 2. K8S solution"
description: " "
date: 2021-09-03
tags: [Container]
comments: true
share: true
---


## # K8S solution

## 1. CCP (Cisco Container Platform)

### 1-1. 

시스코와 구글이 파트너 쉽을 통해 제공하는 하이브리드 클라우드 솔루션

### 1-2. 구조

### 1-3. 특징

- 네이티브 쿠버네티스
- HX 기반(VMware)
  - QoS 기반 SLA 보장
  - 분산 구조 자동 리밸런싱
- 컨테이너 네트워킹 최적화
- 보안 및 로드밸런싱 기술
- 통합 모니터링 및 로깅 적용
- 엔터프라이즈 Persistent storage 지원
- 3 Node 기반 가용성 구조
- 구글과의 협업으로 GCP와 통합 연동 가능
- 쿠버네티스와 ACI 정책 연계
- 다양한 컨테이너 서비스 연동 제공 (ex: k8s, Docker Swarm, OpenShift, CF)
- 패브릭 로드밸런싱 구현(OVS/PBR기반)



## 2. OpenShift

### 2-3. 특징

#### Infra

- 쿠버네티스를 사용하여 컨테이너 운용
- RESTful API 지원
- 다양한 공유 스토리지 적용 가능(Ceph, Cinder, NFS, iSCSI, Fiber Channel, EBS ...)
- OpenStack, RHEV, VMware, Amazon EC2, BareMetal 지원

#### Image

- Integration Image Registry를 통한 이미지 관리 : OpenShift 내부에 Image Registry를 통해 기본 이미지 및 S2I Builder에 의해 생성되는 애플리케이션 이미지 관리
- 다양한 미들웨어 및 DB 이미지 사용 가능 : Tomcat, Jboss, NodeJS, MySQL, MongoDB 등

#### DevOps

- Self-Service : Build, Application 생성, DEV / Staging 테스트 등을 Self-Service로 진행 가능
- Collaboration : Openshift Plugin for Eclipse IDE, Web Console, CLI 등의 툴을 통해 협업가능 
- S2I Build / 배포 
- Git과 Jenkins등을 통해 개발/스테이징에 빌드, 테스트, 배포를 자동화하는 CI / CD 구성 가능
- 배포 내역 관리 및 편리한 Rollback
- 모니터링 : 컨테이너별로 모니터링이 가능
- Auto-Scaling 기능 제공
- Openshift Plugin for Eclipse IDE : JBoss Tools 내에 JBoss Openshift Tools를 설치하면  IDE를 통해 Openshift를 연결하여 어플리케이션 빌드, 배포 등이 가능

