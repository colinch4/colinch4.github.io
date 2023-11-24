---
layout: post
title: "[swift] Swift 퍼미션(Permission) 관련 코딩 팁과 Best Practice."
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 개발을 하다 보면 사용자의 권한(permission)을 요청해야 할 때가 많습니다. 예를 들어, 위치 정보에 접근하기 위해 위치 권한을 요청하거나 카메라를 사용하기 위해 카메라 권한을 요청하는 경우가 있습니다. Swift 언어를 사용하여 퍼미션을 관리하는데 유용한 팁과 Best Practice를 알아보겠습니다.

## 1. Info.plist 파일 수정

iOS에서 권한을 요청할 때는 앱의 Info.plist 파일에 해당 권한에 대한 설명을 추가해야 합니다. 예를 들어, 위치 권한을 요청할 경우 다음과 같이 `NSLocationWhenInUseUsageDescription` 또는 `NSLocationAlwaysAndWhenInUseUsageDescription` 키를 Info.plist 파일에 추가해야 합니다.

```xml
<key>NSLocationWhenInUseUsageDescription</key>
<string>우리 앱이 위치 정보에 접근할 수 있도록 허용해주세요.</string>
```

## 2. 권한 요청 코드 작성

권한 요청 코드는 `CLLocationManager` 클래스를 사용하여 작성할 수 있습니다. 위치 권한을 요청하는 경우 다음과 같이 코드를 작성할 수 있습니다.

```swift
import CoreLocation

let locationManager = CLLocationManager()

func requestLocationPermission() {
    locationManager.delegate = self
    locationManager.requestWhenInUseAuthorization()
}

extension ViewController: CLLocationManagerDelegate {
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        switch status {
        case .notDetermined:
            // 사용자에게 권한 요청 팝업 표시
            break
        case .restricted:
            // 권한 제한 상태 처리
            break
        case .denied:
            // 권한 거부 상태 처리
            break
        case .authorizedWhenInUse, .authorizedAlways:
            // 권한 허용 상태 처리
            break
        @unknown default:
            break
        }
    }
}
```

위의 코드에서 `requestLocationPermission()` 메서드를 호출하여 위치 권한을 요청할 수 있습니다. 이때 `CLLocationManagerDelegate` 프로토콜을 구현하고 `didChangeAuthorization` 메서드를 사용하여 권한 상태를 처리할 수 있습니다.

## 3. 권한 상태 확인

앱에서는 사용자가 권한을 허용했는지 여부를 확인해야 합니다. 이를 위해 `CLLocationManager` 클래스의 `authorizationStatus` 속성을 사용할 수 있습니다.

```swift
if CLLocationManager.authorizationStatus() == .authorizedWhenInUse {
    // 위치 권한이 허용된 경우
} else {
    // 위치 권한이 허용되지 않은 경우
}
```

위의 코드에서는 `authorizationStatus` 속성의 값이 `.authorizedWhenInUse` 일 경우 위치 권한이 허용된 상태임을 확인할 수 있습니다.

## 4. 권한 변경 감지

사용자가 앱 내에서 권한을 변경하는 경우를 감지하고 처리해야 할 수도 있습니다. 이를 위해 `CLLocationManagerDelegate` 프로토콜의 `didChangeAuthorization` 메서드를 사용할 수 있습니다. 위에서 소개한 코드에 이미 해당 메서드가 구현되어 있으므로, 해당 메서드 내에서 권한 변경에 따른 필요한 로직을 추가하면 됩니다.

## 5. 에러 처리

권한 요청 중에 발생하는 에러에 대한 처리를 해야 합니다. 위치 권한 요청 중에 에러가 발생할 경우 다음과 같이 처리할 수 있습니다.

```swift
func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
    // 에러 처리 로직 작성
}
```

위의 코드에서는 `locationManager(_:didFailWithError:)` 메서드를 사용하여 위치 권한 요청 중에 발생한 에러를 처리할 수 있습니다.

위의 팁과 Best Practice를 참고하여 Swift 언어로 퍼미션(permission)을 관리하는 코드를 작성할 수 있습니다. 이를 통해 사용자에게 권한 요청과 권한 상태 확인, 권한 변경 처리 등을 원활하게 할 수 있습니다.

더 자세한 내용은 [Apple 개발자 문서](https://developer.apple.com/documentation/corelocation/requesting_authorization_for_location_services)를 참고하시기 바랍니다.