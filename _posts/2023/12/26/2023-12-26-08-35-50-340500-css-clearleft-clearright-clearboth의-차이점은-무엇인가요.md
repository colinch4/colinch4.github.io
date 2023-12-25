---
layout: post
title: "[css] CSS clear:left, clear:right, clear:both의 차이점은 무엇인가요?"
description: " "
date: 2023-12-26
tags: [css]
comments: true
share: true
---

- `clear: left`는 요소가 왼쪽에 float된 요소들을 피하도록 합니다.
- `clear: right`는 요소가 오른쪽에 float된 요소들을 피하도록 합니다.
- `clear: both`는 요소가 양쪽에 float된 요소들을 피하도록 합니다.

예를 들어, 부모 요소 안에 두 개의 float된 자식 요소가 있을 때, `clear: left`를 가진 세 번째 요소는 왼쪽에 float된 자식 요소를 피하게 됩니다. 마찬가지로, `clear: right`나 `clear: both`는 오른쪽 또는 양쪽에 float된 요소들을 피하게 됩니다.

이 속성들을 사용하여 float된 요소와의 상호 작용을 제어할 수 있습니다.