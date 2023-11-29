---
layout: post
title: "[python] Django와 Django REST framework의 차이점"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

## 목차
- [개요](#개요)
- [Django](#Django)
- [Django REST framework](#Django-REST-framework)
- [차이점](#차이점)
- [요약](#요약)

## 개요
Django와 Django REST framework는 Python 웹 애플리케이션 개발에 널리 사용되는 프레임워크입니다. 하지만 이 두 프레임워크의 목적과 특징은 다른 부분도 있습니다. 이 글에서는 Django와 Django REST framework 사이의 주요 차이점에 대해 알아보겠습니다.

## Django

Django는 Python 웹 애플리케이션을 개발하기 위한 고성능 웹 프레임워크입니다. Django는 MVC (Model-View-Controller) 아키텍처 패턴을 따르며, 데이터베이스 관리, URL 라우팅, 세션 관리, 보안 등 다양한 기능을 제공합니다. Django는 전체적인 웹 애플리케이션의 개발을 위한 완전한 기능세트를 제공하고 있습니다.

## Django REST framework

Django REST framework는 Django 프레임워크를 기반으로한 Web API 개발을 위한 확장이라고 볼 수 있습니다. Django REST framework는 RESTful API를 쉽게 개발할 수 있도록 도와주는 다양한 기능과 유틸리티를 제공합니다. 이 프레임워크는 CRUD (Create, Read, Update, Delete) 작업에 대한 일반적인 기능을 지원하며, 인증, 권한 관리, 시리얼라이저 등 다양한 추가 기능을 제공합니다.

## 차이점

Django와 Django REST framework 사이의 주요 차이점은 다음과 같습니다:

1. 목적: Django는 전체적인 웹 애플리케이션 개발을 위한 프레임워크입니다. 반면에 Django REST framework는 RESTful API 개발을 위해 Django를 확장한 것입니다.

2. 기능: Django는 웹 애플리케이션의 전반적인 기능을 제공하며, 데이터베이스 관리, URL 라우팅, 보안 등을 포함합니다. Django REST framework는 RESTful API 개발을 위한 다양한 기능과 유틸리티를 제공합니다.

3. 설계: Django ORM을 기본으로 사용하여 데이터베이스 관리를 처리합니다. Django REST framework는 Django의 모델과 시리얼라이저를 기반으로 한 RESTful API 개발에 특화된 설계를 제공합니다.

4. 인증과 권한: Django는 사용자 인증과 권한 관리에 강력한 기능을 제공합니다. Django REST framework는 이러한 기능을 추가로 제공하여 API 엔드포인트에 대한 인증과 권한 제어를 쉽게 구현할 수 있습니다.

## 요약

Django와 Django REST framework는 Python 웹 애플리케이션 개발에 많이 사용되는 프레임워크입니다. Django는 전체적인 웹 애플리케이션 개발에 특화되어 있으며, Django REST framework는 RESTful API 개발을 위해 Django를 확장한 것입니다. 이 두 프레임워크의 차이점은 목적, 기능, 설계, 인증과 권한 관리에서 나타납니다. 따라서 프로젝트의 목적과 요구사항에 따라 적절한 프레임워크를 선택해야 합니다.