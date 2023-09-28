---
layout: post
title: "Immer와 immer.setAutoFreeze의 차이점 이해하기"
description: " "
date: 2023-09-27
tags: [Immer]
comments: true
share: true
---

immer.setAutoFreeze를 사용하여 객체를 자동으로 동결할 수 있습니다. 동결된 객체는 수정이 불가능하며, 내부 속성의 추가, 수정 또는 삭제가 불가능합니다.

하지만 사용자는 immer.setAutoFreeze를 사용하여 동결 설정을 해제할 수도 있습니다. 동결 설정이 해제되면 객체가 자동으로 동결되지 않으므로, 객체를 수정하는 것이 가능해집니다. 이 경우에는 객체가 불변성을 유지하지 않을 수 있으므로 조심해야 합니다.

이러한 차이점을 이해하고 나면, immer.setAutoFreeze를 사용하여 객체를 자동으로 동결할지 여부를 설정하는 방법에 따라 애플리케이션의 요구사항에 맞게 Immer를 활용할 수 있습니다.

#Immer #자바스크립트