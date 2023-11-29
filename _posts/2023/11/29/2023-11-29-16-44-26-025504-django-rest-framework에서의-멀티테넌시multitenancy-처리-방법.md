---
layout: post
title: "[python] Django REST framework에서의 멀티테넌시(Multitenancy) 처리 방법"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

## 목차
- [멀티테넌시란?](#멀티테넌시란)
- [Django 멀티테넌시 처리](#Django-멀티테넌시-처리)
- [Django REST framework 멀티테넌시 처리](#Django-REST-framework-멀티테넌시-처리)
- [참고자료](#참고자료)

## 멀티테넌시란?
멀티테넌시는 소프트웨어 시스템에서 여러 명의 사용자(테넌트)가 동시에 독립된 데이터 테넌트에 접근하고 조작하는 것을 의미합니다. 대표적으로 SaaS(Software as a Service) 서비스에서 각 고객이 독립된 데이터베이스를 가짐으로써 테넌트 간의 데이터 분리를 가능하게 합니다.

## Django 멀티테넌시 처리
Django는 멀티테넌시를 처리하기 위한 여러 가지 방법을 제공합니다. 가장 일반적인 방법은 다음과 같습니다:

1. **Schema-based Multi-tenancy**: 각 테넌트 별로 독립된 스키마(데이터베이스)를 사용하여 데이터 분리를 달성합니다.
2. **Shared-schema Multi-tenancy**: 동일한 스키마를 사용하되, 테넌트 식별자를 사용하여 데이터를 구분합니다.
3. **Row-based Multi-tenancy**: 하나의 테이블에서 테넌트 식별자를 사용하여 데이터를 필터링하여 분리합니다.

이 중에서도 대부분의 경우 Schema-based Multitenancy가 가장 일반적으로 사용됩니다. 단일 코드베이스를 유지하면서 테넌트 간의 데이터 분리를 달성할 수 있습니다.

## Django REST framework 멀티테넌시 처리
Django REST framework는 Django에서 제공하는 멀티테넌시 처리 방법을 그대로 사용할 수 있습니다. Django의 Schema-based Multitenancy를 사용하여 테넌트 간의 데이터 분리를 달성한 후, Django REST framework를 사용하여 RESTful API를 개발할 수 있습니다.

Django REST framework의 주요 구성요소 중 하나인 `APIView`를 사용하여 테넌트 간의 데이터 접근 및 조작을 처리할 수 있습니다. 각 APIView에서 테넌트 식별자를 확인하고 해당 테넌트의 데이터에만 접근할 수 있도록 필터링하면 됩니다.

```python
from rest_framework.views import APIView

class TenantAPIView(APIView):
    def get(self, request, tenant_id):
        # 테넌트 식별자를 확인하고 해당 테넌트의 데이터에만 접근
        queryset = MyModel.objects.filter(tenant_id=tenant_id)
        serializer = MySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, tenant_id):
        # 테넌트 식별자를 확인하고 해당 테넌트의 데이터에만 쓰기
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tenant_id=tenant_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

이와 같이 Django REST framework를 사용하면 멀티테넌시 처리를 간편하게 구현할 수 있습니다.

## 참고자료
- Django 공식 문서: [Supporting multiple databases](https://docs.djangoproject.com/en/3.2/topics/db/multi-db/)
- Django REST framework 공식 문서: [Authentication and Permissions](https://www.django-rest-framework.org/api-guide/authentication/)