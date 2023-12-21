---
layout: post
title: "[android] 안드로이드 Content Provider와 URI (Uniform Resource Identifier)"
description: " "
date: 2023-12-22
tags: [android]
comments: true
share: true
---

안드로이드에서 데이터를 다른 애플리케이션과 공유하기 위해 `Content Provider`를 사용합니다. `Content Provider`는 응용 프로그램 간에 데이터를 제공하고 공유하기 위한 안드로이드 시스템 컴포넌트입니다. 

## Content Provider
안드로이드 애플리케이션은 자체 데이터베이스를 가지며, 이 데이터베이스에 접근하려면 Content Provider를 통해 데이터를 제공해야 합니다. Content Provider를 통해 제공되는 데이터는 URI를 통해 식별됩니다.

## URI (Uniform Resource Identifier)
URI는 특정 자원을 나타내는 유일한 주소입니다. 안드로이드에서는 Content Provider에 접근하기 위해 URI를 사용합니다. URI는 다음과 같은 형식을 가지고 있습니다.
- `content://authority/path` 

여기서, 
- `content://` : URI 스키마로 Content Provider를 가리킵니다.
- `authority` : Content Provider의 고유 식별자입니다.
- `path` : Content Provider 내부의 데이터를 가리킵니다.

예를 들어, 주소록 정보에 접근하기 위한 URI는 다음과 같을 수 있습니다.
- `content://contacts/people`

## Content Resolver
애플리케이션은 `Content Resolver`를 사용하여 Content Provider에 쿼리를 수행합니다. Content Resolver를 사용하여 URI를 사용하여 Content Provider에 액세스하고 데이터를 추가, 수정, 삭제 또는 조회할 수 있습니다.

안드로이드 시스템에서는 Content Provider, URI 및 Content Resolver를 사용하여 다른 애플리케이션 간에 데이터를 공유하고 상호 작용할 수 있습니다.

이처럼 안드로이드에서는 Content Provider와 URI를 통해 데이터를 안전하게 제공하고 공유할 수 있습니다. 안드로이드의 Content Provider와 URI는 데이터 관리 및 보안에 중요한 부분을 담당하고 있습니다.  

## 참고 자료
- 안드로이드 개발자 문서: [Content Provider](https://developer.android.com/guide/topics/providers/content-providers)
- 안드로이드 개발자 문서: [Content Resolver](https://developer.android.com/reference/android/content/ContentResolver)

Content Provider와 URI에 대한 자세한 내용은 안드로이드 개발자 문서를 참고하시기 바랍니다.