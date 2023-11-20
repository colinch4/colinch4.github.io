---
layout: post
title: "[java] TestNG와 CI/CD 도구의 통합(GitLab CI, Travis CI)"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

TestNG는 자바 기반의 테스트 프레임워크로, 단위 테스트와 기능 테스트를 지원합니다. 이 테스트 프레임워크를 사용하여 자동화된 테스트를 구축하는 경우, 테스트의 지속적인 통합 및 배포를 위해 CI/CD 도구와의 통합이 필요합니다. 

이 글에서는 TestNG를 GitLab CI와 Travis CI와 통합하는 방법에 대해 알아보겠습니다.

## GitLab CI와의 통합

### 1. `.gitlab-ci.yml` 파일 생성

GitLab CI를 사용하기 위해 우선 프로젝트 루트 디렉토리에 `.gitlab-ci.yml` 파일을 생성해야 합니다. 이 파일은 GitLab CI/CD 파이프라인의 설정을 담당합니다.

```yaml
image: maven:latest

stages:
  - build
  - test

build:
  stage: build
  script:
    - mvn clean install

test:
  stage: test
  script:
    - mvn test
```

위의 예시는 간단한 `.gitlab-ci.yml` 파일로, 두 개의 스테이지(build와 test)로 구성되어 있습니다. 먼저 `image` 키를 사용하여 컨테이너의 이미지를 지정하고, `stages` 키를 사용하여 파이프라인의 스테이지를 정의합니다. 스크립트 부분에서는 Maven 명령어를 사용하여 프로젝트를 빌드(build)하고 테스트(test)합니다.

### 2. GitLab 저장소와 연동

GitLab 저장소에 `.gitlab-ci.yml` 파일을 커밋하고 푸시하여 연동을 설정합니다. 이후, GitLab CI/CD 파이프라인이 자동으로 실행됩니다.

## Travis CI와의 통합

### 1. `.travis.yml` 파일 생성

Trvis CI를 사용하기 위해 프로젝트 루트 디렉토리에 `.travis.yml` 파일을 생성해야 합니다. 이 파일은 Travis CI의 설정을 담당합니다.

```yaml
language: java
jdk:
  - openjdk8

script:
  - mvn clean install
  - mvn test
```

위의 예시는 간단한 `.travis.yml` 파일로, 자바 언어를 사용하고 JDK 8을 사용하여 빌드 및 테스트를 실행합니다.

### 2. Travis CI와 GitHub 계정 연동

Travis CI 웹사이트에서 GitHub 계정으로 로그인하여 프로젝트를 활성화합니다. 이후, `.travis.yml` 파일을 GitHub 저장소에 커밋하고 푸시하면 Travis CI가 자동으로 파이프라인을 실행합니다.

## 결론

TestNG는 강력한 자바 테스트 프레임워크이며, CI/CD 도구인 GitLab CI와 Travis CI와의 통합을 통해 자동화된 테스트 과정을 구축할 수 있습니다. 이러한 통합은 개발 생산성을 향상시키고 품질 관리를 강화하는데 도움이 됩니다.

## 참고 자료

- [TestNG 공식 웹사이트](https://testng.org/)
- [GitLab CI/CD 문서](https://docs.gitlab.com/ee/ci/)
- [Travis CI 문서](https://docs.travis-ci.com/)