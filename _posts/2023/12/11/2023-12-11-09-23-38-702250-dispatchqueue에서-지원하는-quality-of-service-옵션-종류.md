---
layout: post
title: "[swift] DispatchQueue에서 지원하는 Quality of Service 옵션 종류"
description: " "
date: 2023-12-11
tags: [swift]
comments: true
share: true
---

DispatchQueue는 GCD(Grand Central Dispatch)를 통해 비동기적으로 작업을 수행할 수 있는데, Quality of Service(QoS) 옵션을 통해 작업의 중요도와 우선순위를 설정할 수 있습니다. 이번 글에서는 DispatchQueue에서 지원하는 QoS 옵션 종류에 대해 알아보겠습니다.

## QoS 옵션 종류

DispatchQueue는 다음과 같은 다섯 가지의 QoS 옵션을 제공합니다.

### 1. User-Interactive

사용자와 직접적으로 상호작용하는 작업에 대한 QoS 레벨로, 매우 높은 우선순위를 가지고 있습니다. 예를 들어 사용자의 입력에 반응하는 UI 업데이트나 애니메이션 처리 등에 사용됩니다.

### 2. User-Initiated

사용자가 시작한 작업에 대한 QoS 레벨로, 상호작용을 기다리는 동안 기다리는 대신 즉시 수행되어야 하는 작업에 사용됩니다. 예를 들어 사용자가 웹페이지를 로딩하거나 문서를 열 때 사용될 수 있습니다.

### 3. Utility

백그라운드에서 수행되는 유틸리티 태스크에 대한 QoS 레벨로, 사용자의 입력이나 상호작용을 기다리지 않고 빠른 완료가 필요한 작업에 사용됩니다.

### 4. Background

백그라운드에서 수행되는 일반적인 태스크에 대한 QoS 레벨로, 사용자에게 바로 보여지지 않아도 되는 작업에 사용됩니다. 예를 들어 주기적으로 데이터를 업데이트하는 작업이 있을 때 사용될 수 있습니다.

### 5. Unspecified

QoS를 명시적으로 지정하지 않은 경우, Unspecified QoS가 사용됩니다. 이 레벨은 시스템에 의해 자동으로 결정되는 기본값으로, 특별한 경우가 아닌 이상 직접 사용되지 않습니다.

## 결론

DispatchQueue에서는 다양한 종류의 QoS 옵션을 통해 작업의 중요도와 우선순위를 지정할 수 있습니다. 이를 통해 애플리케이션의 성능을 최적화하고 사용자 경험을 향상시킬 수 있습니다.

자세한 내용은 [Apple 공식 문서](https://developer.apple.com/documentation/dispatch/dispatchqos)를 참고하세요.