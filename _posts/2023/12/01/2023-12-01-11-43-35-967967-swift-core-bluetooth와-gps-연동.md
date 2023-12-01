---
layout: post
title: "[swift] Swift Core Bluetooth와 GPS 연동"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift Core Bluetooth와 GPS를 연동하는 방법에 대해 알아보겠습니다.

## 1. Bluetooth 연동

Swift에서 Bluetooth를 사용하기 위해서는 Core Bluetooth 프레임워크를 import해야 합니다. 다음과 같은 코드로 Bluetooth를 활성화할 수 있습니다.

```swift
import CoreBluetooth

// Bluetooth Manager 생성
let centralManager = CBCentralManager()

// Bluetooth 활성화 상태 변경 이벤트 처리
centralManager.delegate = self

// Bluetooth 활성화 확인
if centralManager.state == .poweredOn {
    // Bluetooth 켜져 있음
    // 디바이스 스캔, 페어링 등의 작업 수행 가능
} else {
    // Bluetooth 꺼져 있음
    // 사용자에게 Bluetooth를 켜도록 안내
}

// Bluetooth 상태 변경 이벤트 수신
extension ViewController: CBCentralManagerDelegate {
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            // Bluetooth 활성화됨
        } else {
            // Bluetooth 비활성화됨
        }
    }
}
```

Bluetooth가 활성화된 상태이면 디바이스 스캔, 페어링 등의 작업을 수행할 수 있습니다. 

## 2. GPS 연동

GPS와의 연동을 위해서는 Core Location 프레임워크를 import해야 합니다. 다음과 같은 코드로 GPS를 사용할 수 있습니다.

```swift
import CoreLocation

// Location Manager 생성
let locationManager = CLLocationManager()

// GPS 권한 요청
locationManager.delegate = self
locationManager.requestWhenInUseAuthorization()

// GPS 권한 상태 확인
if CLLocationManager.authorizationStatus() == .authorizedWhenInUse {
    // GPS 권한 승인됨
    // 위치 정보 수집 및 사용 가능
} else {
    // GPS 권한 거절됨
    // 사용자에게 GPS 권한 부여를 요청
}

// GPS 권한 상태 변경 이벤트 수신
extension ViewController: CLLocationManagerDelegate {
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        if status == .authorizedWhenInUse {
            // GPS 권한 승인됨
        } else {
            // GPS 권한 거절됨
        }
    }
}
```

GPS 권한이 승인되면 위치 정보 수집 및 사용이 가능해집니다. 

## 3. Bluetooth와 GPS 연동

Bluetooth와 GPS를 연동하기 위해서는 해당 기능들을 동시에 사용할 수 있어야 합니다. 따라서 Bluetooth와 GPS 기능을 모두 활성화하고, 각각의 이벤트를 처리해야 합니다.

```swift
import CoreBluetooth
import CoreLocation

class ViewController: UIViewController, CBCentralManagerDelegate, CLLocationManagerDelegate {
    
    let centralManager = CBCentralManager()
    let locationManager = CLLocationManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        centralManager.delegate = self
        locationManager.delegate = self
        
        // Bluetooth 활성화 확인
        if centralManager.state == .poweredOn {
            // Bluetooth 켜져 있음
            // 디바이스 스캔, 페어링 등의 작업 수행 가능
        } else {
            // Bluetooth 꺼져 있음
            // 사용자에게 Bluetooth를 켜도록 안내
        }
        
        // GPS 권한 요청
        locationManager.requestWhenInUseAuthorization()
        
        // GPS 권한 상태 확인
        if CLLocationManager.authorizationStatus() == .authorizedWhenInUse {
            // GPS 권한 승인됨
            // 위치 정보 수집 및 사용 가능
        } else {
            // GPS 권한 거절됨
            // 사용자에게 GPS 권한 부여를 요청
        }

    }
    
    // Bluetooth 상태 변경 이벤트 수신
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        if central.state == .poweredOn {
            // Bluetooth 활성화됨
        } else {
            // Bluetooth 비활성화됨
        }
    }
    
    // GPS 권한 상태 변경 이벤트 수신
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        if status == .authorizedWhenInUse {
            // GPS 권한 승인됨
        } else {
            // GPS 권한 거절됨
        }
    }
}
```

위와 같이 Bluetooth와 GPS를 동시에 연동하여 사용할 수 있습니다. Bluetooth와 GPS 모두 활성화되어야만 원하는 작업들을 수행할 수 있습니다.

위의 예제 코드는 Swift에서 Core Bluetooth와 Core Location 프레임워크를 이용하여 Bluetooth와 GPS를 연동하는 방법을 알아보았습니다. Bluetooth와 GPS를 함께 사용하는 경우, 각각의 상태 및 이벤트를 처리하여 필요한 작업을 수행할 수 있습니다.