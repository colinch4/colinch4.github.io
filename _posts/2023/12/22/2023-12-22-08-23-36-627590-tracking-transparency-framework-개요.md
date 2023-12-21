---
layout: post
title: "[ios] Tracking Transparency Framework 개요"
description: " "
date: 2023-12-22
tags: [ios]
comments: true
share: true
---

iOS 14에서 도입된 **Tracking Transparency Framework**는 사용자의 데이터를 수집하고 추적하는 앱들이 사용자에게 권한을 요청할 수 있도록 하는 기능을 제공합니다. 이 기능은 개인정보 보호 및 사용자 프라이버시 강화를 위해 중요한 역할을 합니다.

## Tracking Transparency Framework란?

**Tracking Transparency Framework**는 앱 내에서 사용자의 권한을 요청하고 권한 상태를 확인하는 데 사용됩니다. 앱이 사용자의 데이터를 추적하거나 광고 및 데이터 수집 목적으로 정보를 공유하는 경우, 해당 앱은 사용자에게 관련된 설정을 통해 권한을 요청해야 합니다.

이 프레임워크를 사용하면 앱은 App Tracking Transparency 권한 요청 대화상자를 표시하고, 사용자의 선택에 따라 앱 추적에 대한 권한을 요청할 수 있습니다.

## Tracking Transparency Framework 사용하기

Tracking Transparency Framework를 사용하려면 개발자는 Info.plist 파일에서 **NSUserTrackingUsageDescription** 키를 추가하여 앱이 사용자의 데이터를 추적하거나 광고 및 데이터 수집을 위해 정보를 공유하는 이유를 설명해야 합니다. 

또한 코드에서는 **ATTrackingManager** 클래스를 사용하여 권한 상태를 확인하고, 필요한 경우 권한을 요청할 수 있습니다. 

```swift
import AppTrackingTransparency

if #available(iOS 14, *) {
    ATTrackingManager.requestTrackingAuthorization(completion: { status in
        if status == .authorized {
            // 사용자가 권한을 허용한 경우의 처리
        } else {
            // 사용자가 권한을 거부한 경우의 처리
        }
    })
} else {
    // iOS 14 미만의 버전에서의 처리
}
```

앱이 Tracking Transparency Framework를 사용하도록 업데이트될 경우, 앱의 개인정보 처리 방침을 업데이트하고 관련된 규정을 준수하여야 합니다.

Tracking Transparency Framework를 사용하여 앱의 광고 및 데이터 수집에 대한 권한을 사용자에게 요청함으로써, 개인정보 보호 및 사용자 프라이버시 측면에서 보다 투명하고 책임감 있는 서비스를 제공할 수 있습니다.

Tracking Transparency Framework에 대한 자세한 내용은 [Apple 개발자 사이트](https://developer.apple.com/documentation/apptrackingtransparency)에서 확인할 수 있습니다.