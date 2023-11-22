---
layout: post
title: "[springcore] Resource 추상화"
description: " "
date: 2021-06-18
tags: [spring]
comments: true
share: true
---

## Resource 추상화
- java.net.URL을 추상화한 것
- 추상화 이유
    - 클래스패스 기준으로 리소스 읽어오는 기능 없음
    - ServletContext 기준으로 상대 경로를 읽어오는 기능 없음
    - 새로운 핸들러를 등록하여 특별한 URL을 만들어 사용할 수 있지만 구현이 복잡하고 편의성 메소드가 부족

- 주요 메소드
    - getInputStream()
    - exist()
    - isOpen()
    - getDescription() : 전체 경로 포함한 파일 이름 또는 실제 URL

- 구현체
    - UrlResource : 기본으로 지원하는 프로토콜 http, https, ftp, file, jar
    - ClassPathResource : 접두어로 `classpath:`를 사용
    - FileSystemResource : 접두어로 `file://`을 사용
    - ServletContextResource : 웹 애플리케이션 루트에서 상대경로로 리소스 찾음

- 리소스 읽어오기
    - Resource 타입은 location값과 ApplicationContext 타입에 따라 결정
        - ClassPathXmlApplicationContext -> ClassPathResource
        - FileSystemXmlAppliationContext -> FileSystemResource
        - WebApplicationContext -> ServletContextResource
    - ApplicationContext의 타입에 상관없이 리소스 타입을 강제하려면 java.net.URL 접두어(`classpath:`같은) 중 하나 사용 가능
    