---
layout: post
title: "[android] 안드로이드 Continuous Integration의 멀티-모듈 프로젝트 빌드"
description: " "
date: 2023-12-20
tags: [android]
comments: true
share: true
---

안드로이드 애플리케이션을 개발하다 보면 여러 모듈로 구성된 프로젝트를 관리해야 할 때가 있습니다. 이런 경우 CI (Continuous Integration) 시스템을 설정하여 모든 모듈이 함께 테스트되고 빌드될 수 있도록 해야 합니다. 이번 포스팅에서는 **안드로이드 멀티-모듈 프로젝트를 CI 시스템에 통합**하는 방법에 대해 알아보겠습니다.

## 1. 멀티-모듈 프로젝트 구성

안드로이드 프로젝트를 멀티-모듈로 구성하려면 `settings.gradle`과 `build.gradle` 파일을 적절하게 구성해야 합니다. 각 모듈의 의존성과 빌드 설정을 올바르게 설정하는 것이 중요합니다.

예를 들어, 다음과 같이 `settings.gradle` 파일에 하위 모듈을 include할 수 있습니다.
```groovy
include ':app', ':library'
```

## 2. CI 시스템 설정

대표적인 CI 도구로는 Jenkins, CircleCI, GitLab CI 등이 있습니다. 이 예시에서는 Jenkins를 사용한다고 가정하겠습니다. 

Jenkins Job을 생성할 때는, 다음과 같이 해당 안드로이드 프로젝트의 **코드를 가져오는 빌드 스크립트를 작성**해야 합니다.
```shell
git clone https://github.com/your-repo-url.git
```

## 3. 안드로이드 빌드 및 테스트 실행

Jenkins Job 내에서 다음과 같이 안드로이드 빌드 및 테스트를 실행하는 스크립트를 작성해야 합니다.
```shell
./gradlew clean build connectedAndroidTest
```

## 4. 통합 테스트

멀티-모듈 프로젝트에서는 **모든 모듈의 통합 테스트**를 수행해야 합니다. 이를 위해 Jenkins Job에서 다음과 같이 하위 모듈 빌드를 추가해야 합니다.
```shell
./gradlew :app:connectedAndroidTest :library:test
```

이러한 설정을 통해 모든 모듈을 함께 테스트하고 빌드할 수 있게 됩니다.

안드로이드 프로젝트의 CI 설정은 전반적으로 이와 유사하지만, **멀티-모듈 프로젝트의 특징을 고려하여 설정해야** 합니다. 멀티-모듈 프로젝트에서의 CI 설정은 애플리케이션의 안정성과 품질을 유지하는 데 매우 중요합니다. 

CI를 통해 효율적인 모듈 간 협업 및 안정적인 릴리스를 보장할 수 있도록 노력해야 합니다.

## 참고 자료
- [Jenkins](https://www.jenkins.io/)
- [CircleCI](https://circleci.com/)
- [GitLab CI](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/)