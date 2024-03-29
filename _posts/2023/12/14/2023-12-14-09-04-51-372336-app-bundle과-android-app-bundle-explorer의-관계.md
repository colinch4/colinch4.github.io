---
layout: post
title: "[android] App Bundle과 Android App Bundle Explorer의 관계"
description: " "
date: 2023-12-14
tags: [android]
comments: true
share: true
---

안드로이드 앱을 개발하다 보면 앱 번들(App Bundle) 및 안드로이드 앱 번들 익스플러(Explorer)와 같은 용어를 자주 듣게 됩니다. 이번 글에서는 이 두 용어에 대해 알아보고 그 관계에 대해 살펴보겠습니다.

## 앱 번들(App Bundle)

`앱 번들`은 구글 플레이 스토어용으로 앱을 빌드할 때 사용되는 바이너리 파일의 형식입니다. 이 형식은 앱을 최적화된 형태로 묶어 사용자의 디바이스에 최적화된 앱을 제공하는 데 도움을 줍니다. 또한, 앱 번들은 앱 번들 동적 모듈과 원하는 언어 및 화면 크기에 대한 리소스를 분리하여 제공합니다.

## 안드로이드 앱 번들 익스플러(Android App Bundle Explorer)

`안드로이드 앱 번들 익스플러`는 구글이 제공하는 온라인 도구로, 앱 번들을 업로드하고 해당 번들의 콘텐츠를 시각적으로 살펴볼 수 있는 도구입니다. 이 도구를 사용하면 앱 번들에 포함된 다양한 리소스 및 파일을 살펴볼 수 있으며, 개발자는 이를 통해 번들의 구성을 확인하고 문제를 해결할 수 있습니다.

## 관계

`앱 번들`은 앱을 빌드하는 데 사용되는 형식이며, `안드로이드 앱 번들 익스플러`는 해당 번들의 내부 구조를 시각적으로 표시해주는 도구입니다. 따라서, 이 두 용어는 앱을 개발하고 릴리스하는 과정에서 밀접하게 연관되어 있습니다.

앱 번들을 생성하고 관리하기 위해서는 앱 번들 도구나 플러그인을 사용해야 하며, 번들에 포함된 리소스나 파일을 살펴보기 위해서는 안드로이드 앱 번들 익스플러를 활용할 수 있습니다.

그러므로, `앱 번들`은 안드로이드 개발자가 앱을 최적화된 형태로 제공하는 데 사용되는 형식이며, `안드로이드 앱 번들 익스플러`는 해당 앱 번들의 내부 구조를 시각적으로 표시해주는 도구로, 두 용어는 개발 및 릴리스 프로세스에서 중요한 요소로 작용합니다.

앱 번들과 안드로이드 앱 번들 익스플러에 대해 더 알아보려면 다음 문서를 참고하세요: [공식 안드로이드 개발자 사이트](https://developer.android.com/guide/app-bundle)