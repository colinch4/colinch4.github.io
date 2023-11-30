---
layout: post
title: "[java] Apache Commons Collections와 Java Collection Framework의 차이점"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

Java Collection Framework는 Java 프로그래밍 언어에 내장된 컬렉션 관련 클래스와 인터페이스의 모음입니다. 이 프레임워크를 사용하여 데이터를 보다 쉽고 효율적으로 관리할 수 있습니다. 반면, Apache Commons Collections는 Java Collection Framework의 기본 기능을 확장하고 보완하는 데 중점을 둔 외부 라이브러리입니다.

## 공통점

- 둘 다 데이터를 저장하고 관리하기위한 다양한 클래스와 인터페이스를 제공합니다.
- 둘 다 자바 언어로 작성되었으며 Java 프로젝트에서 사용할 수 있습니다.
- 둘 다 컬렉션과 관련된 작업을 수행하는 메서드와 유틸리티 클래스를 제공합니다.
- 둘 다 데이터 구조간의 변경이나 변환을 수행하는 유틸리티 메서드를 제공합니다.

## 차이점

### 기능의 다양성

Java Collection Framework는 List, Set, Queue 및 Map과 같은 간단한 데이터 구조 외에도 여러 구현과 유용한 메서드를 제공합니다. 컬렉션에 포함된 데이터를 검색, 정렬 및 필터링 할 수 있는 메서드도 지원합니다. 하지만 Apache Commons Collections는 Java Collection Framework의 기능을 확장하고, 더 다양한 기능을 제공합니다. 예를 들어, 다양한 유형의 배열, 확장된 정렬 및 필터링 기능을 제공합니다.

### 용도

Java Collection Framework는 기본적으로 JDK에 포함되어 있으므로 별도의 다운로드나 설치 작업이 필요하지 않습니다. Java 개발자는 JDK의 일부로 제공되는 Collection Framework를 자유롭게 사용할 수 있습니다. 반면에, Apache Commons Collections는 외부 라이브러리로 다른 프로젝트에서 사용되기 위해서는 별도의 다운로드 및 의존성 추가 작업이 필요합니다.

### 호환성

Java Collection Framework는 JDK의 일부로 제공되는 것이기 때문에 Java 버전과의 호환성이 보장됩니다. 그러나 Apache Commons Collections는 외부 라이브러리이므로 버전 호환성을 유지하기 위해 수동으로 의존성을 관리해야 합니다. 따라서 프로젝트에서 Apache Commons Collections를 사용하기 전에 라이브러리의 버전과 Java 버전의 호환성을 확인해야 합니다.

## 결론

Java Collection Framework는 Java 개발에 필수적인 컬렉션 관련 클래스와 인터페이스를 제공하며, 대부분의 Java 프로젝트에서 기본 구현체를 사용할 수 있습니다. 반면에 Apache Commons Collections는 Java Collection Framework를 보완하고 다양한 컬렉션 관련 기능을 제공하며, 특정한 요구사항을 충족시키기 위해 외부 라이브러리로 사용될 수 있습니다.