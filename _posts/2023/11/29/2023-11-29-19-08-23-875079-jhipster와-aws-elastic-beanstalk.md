---
layout: post
title: "[java] JHipster와 AWS Elastic Beanstalk"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

## 소개

[JHipster](https://www.jhipster.tech/)는 자바 기반의 웹 애플리케이션 및 마이크로서비스를 생성하기 위한 오픈 소스 개발 플랫폼입니다. [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)는 애플리케이션을 간편하게 배포하고 관리하기 위한 서비스입니다. 이 두 가지 기술을 함께 사용하면 JHipster 애플리케이션을 Elastic Beanstalk에 배포할 수 있습니다.

## Elastic Beanstalk 설정

Elastic Beanstalk를 사용하기 위해 AWS 계정에서 환경을 설정해야 합니다. 다음은 설정하는 방법입니다.

1. Elastic Beanstalk 콘솔에 로그인합니다.
2. "새로운 애플리케이션 생성"을 클릭합니다.
3. 애플리케이션 이름을 입력하고 플랫폼을 선택합니다. JHipster는 Java 기반의 애플리케이션이므로 Java 플랫폼을 선택합니다.
4. 필요한 경우 환경 옵션을 구성합니다. 예를 들어, 로드 밸런서를 사용하려면 "로드 밸런서 구성" 단계에서 옵션을 선택합니다.
5. 환경 이름을 입력하고 "새로운 환경 생성"을 클릭합니다.

## JHipster 애플리케이션 배포

JHipster 애플리케이션을 Elastic Beanstalk에 배포하기 위해 다음 단계를 수행합니다.

1. 프로젝트 루트 디렉토리에서 `./mvnw package` 명령어를 실행하여 애플리케이션을 빌드합니다.
2. `target` 디렉토리에 생성된 JAR 파일을 `aws-cli`를 사용하여 Elastic Beanstalk 환경에 업로드합니다. 다음은 업로드하는 방법입니다.

```shell
$ aws elasticbeanstalk create-application-version \
    --application-name <application-name> \
    --version-label <version-label> \
    --source-bundle S3Bucket=<s3-bucket-name>,S3Key=<s3-key>
```

3. `aws-cli`를 사용하여 Elastic Beanstalk 환경을 업데이트하고 배포합니다. 다음은 업데이트하는 방법입니다.

```shell
$ aws elasticbeanstalk update-environment \
    --environment-name <environment-name> \
    --version-label <version-label>
```

4. 배포가 완료되면 Elastic Beanstalk 콘솔에서 애플리케이션의 URL을 확인할 수 있습니다.

## 결론

JHipster와 AWS Elastic Beanstalk를 함께 사용하면 JHipster 애플리케이션을 쉽게 배포하고 관리할 수 있습니다. Elastic Beanstalk를 사용하면 환경 설정도 간단하게 처리할 수 있으므로 개발자는 애플리케이션 개발에 집중할 수 있습니다.