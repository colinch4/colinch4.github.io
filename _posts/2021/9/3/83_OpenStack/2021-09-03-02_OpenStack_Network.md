---
layout: post
title: "[OpenStack] OpenStack Network"
description: " "
date: 2021-09-03
tags: [OpenStack]
comments: true
share: true
---


1. 종류

management network : 관리용 네트워크 / 각 컴포넌트가 서로 API를 호출하는 데 사용

Tunnel Network : VM instance 간 네트워크 구축하는데 사용 / GRE, VXLAN 기술 사용 / Overlay Network

External Network : VM instance 가 인터넷과 통신하기 위한 네트워크



2. Provider / Self-service network

Provider Network : 오픈스택을 서비스하는 관리자가 구축한 네트워크가 VM instance에 할당되는 네트워크

Self-Service Network : 

