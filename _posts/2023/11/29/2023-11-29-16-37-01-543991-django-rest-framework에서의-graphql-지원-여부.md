---
layout: post
title: "[python] Django REST framework에서의 GraphQL 지원 여부"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Django REST framework (DRF)은 웹 API를 쉽게 개발할 수 있는 강력한 프레임워크입니다. 그러나 DRF는 기본적으로 RESTful 아키텍처를 지원하며 GraphQL을 직접적으로 지원하지는 않습니다.

하지만 DRF와 GraphQL을 함께 사용할 수 있는 여러 가지 옵션이 있습니다. 이러한 옵션은 GraphQL을 DRF 프로젝트에 통합하고 기존의 RESTful 엔드포인트와 함께 사용할 수 있도록 해줍니다.

가장 일반적인 방법은 `graphene-django` 라이브러리를 사용하는 것입니다. `graphene-django`는 Django와 GraphQL을 연동하는 용이한 방법을 제공하며, DRF와의 통합도 가능합니다. 

아래의 예시 코드는 `graphene-django`를 사용하여 DRF 프로젝트에 GraphQL 기능을 추가하는 방법을 보여줍니다:

```python
# myapp/schema.py
import graphene
from graphene_django import DjangoObjectType

from myapp.models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    my_model = graphene.Field(MyModelType, id=graphene.Int())

    def resolve_my_model(self, info, id):
        return MyModel.objects.get(id=id)

schema = graphene.Schema(query=Query)
```

위의 코드에서 `MyModel`은 DRF 모델입니다. `MyModelType`은 GraphQL에서 표현되는 모델의 타입을 정의하고, `resolve_my_model` 함수는 해당 모델의 데이터를 가져오는 로직을 구현합니다. 

그리고 DRF 프로젝트에서 GraphQL 엔드포인트를 추가하기 위해 다음과 같이 `urls.py` 파일을 수정해야 합니다:

```python
# myproject/urls.py
from django.urls import path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),
    # ...
]
```

위의 코드는 `GraphQLView`를 사용하여 `/graphql` 경로에 GraphQL 엔드포인트를 등록하는 방법을 보여줍니다. `graphiql=True`로 설정하면 GraphQL 쿼리를 테스트할 수 있는 인터페이스인 GraphiQL도 함께 제공됩니다.

이제 DRF 프로젝트에 GraphQL 기능이 추가되었습니다. 이를 통해 기존의 RESTful 아키텍처와 함께 사용하거나, RESTful API를 GraphQL로 완전히 대체하는 것도 가능합니다.

더 자세한 내용과 다른 방법들은 `graphene-django`의 공식 문서를 참고하시기 바랍니다.

**참고 문서:**
- [graphene-django 공식 문서](https://docs.graphene-python.org/projects/django/en/latest/)
- [Django REST framework 공식 문서](https://www.django-rest-framework.org/)
- [GraphQL 공식 문서](https://graphql.org/)