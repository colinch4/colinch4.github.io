---
layout: post
title: "[java] JHipster와 Azure App Service"
description: " "
date: 2023-11-29
tags: [java]
comments: true
share: true
---

[JHipster](https://www.jhipster.tech/)는 모노리포지터리 아키텍처로 구축된 자바 스프링부트 기반의 웹 어플리케이션을 빠르게 개발할 수 있는 도구입니다. [Azure App Service](https://azure.microsoft.com/ko-kr/services/app-service/)는 Microsoft Azure에서 호스팅되는 매우 유연하고 확장 가능한 웹 어플리케이션 호스팅 서비스입니다.

여기서는 JHipster를 사용하여 개발한 웹 어플리케이션을 Azure App Service에 배포하는 방법에 대해 알아보겠습니다.

## 1. Azure 계정 생성 및 App Service 생성

Azure에 계정이 없다면 [Azure 포털](https://portal.azure.com)에서 계정을 생성하세요. 그리고 Azure App Service를 생성하여 호스팅할 웹 어플리케이션의 환경을 구성해야 합니다.

## 2. JHipster 프로젝트 생성

JHipster를 설치하고 새로운 프로젝트를 생성합니다. 옵션에 맞게 설정하면 됩니다.

```
$ npm install -g generator-jhipster
$ jhipster
```

## 3. Azure CLI 설치

Azure App Service를 관리하기 위해서는 Azure CLI를 설치해야 합니다. 다음 명령어를 사용하여 설치할 수 있습니다.

```
$ curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## 4. Azure에 로그인

Azure CLI를 사용하기 위해 Azure에 로그인해야 합니다. 다음 명령어를 실행하고 Azure 계정 인증 절차를 수행하세요.

```
$ az login
```

## 5. 배포 스크립트 작성

Azure App Service에 배포하기 위한 스크립트를 작성합니다. `deploy.sh` 파일을 생성하고 아래 내용을 추가하세요.

```shell
#!/bin/bash

# Azure App Service에 배포하기 위한 정보
resourceGroup="my-resource-group"
appName="my-app-name"

# JHipster 프로젝트 폴더로 이동
cd /path/to/your/jhipster/project

# JHipster 프로젝트 빌드
./mvnw clean install -DskipTests

# 배포 패키지 생성
jhipster azureapp

# Azure에 배포
az webapp up --name $appName --resource-group $resourceGroup --sku F1
```

## 6. 웹 어플리케이션 배포

`deploy.sh` 스크립트를 실행하여 JHipster 프로젝트를 Azure App Service에 배포합니다.

```
$ bash deploy.sh
```

## 7. 웹 어플리케이션 확인

웹 브라우저에서 배포한 Azure App Service의 URL로 접속하여 웹 어플리케이션을 확인합니다.

이제 JHipster로 개발한 웹 어플리케이션이 Azure App Service에 성공적으로 배포되었습니다. Azure App Service를 사용하면 웹 어플리케이션을 쉽게 호스팅하고 관리할 수 있습니다.