---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 앱의 백그라운드 작업 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 긴 작업을 수행하는 동안 사용자에게 작업이 진행 중임을 시각적으로 표시하는 것은 중요합니다. 이를 통해 사용자는 앱이 정상적으로 작업 중임을 인지할 수 있습니다. NVActivityIndicatorView는 Swift에서 작업 상태 표시를 위한 라이브러리 중 하나입니다. 이 블로그 포스트에서는 NVActivityIndicatorView를 활용하여 앱의 백그라운드 작업 상태를 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 라이브러리 추가하기

[NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 NVActivityIndicatorView 라이브러리를 다운로드하거나 CocoaPods로 추가할 수 있습니다. 이 예제에서는 CocoaPods를 사용하여 라이브러리를 추가하는 방법을 설명하겠습니다.

1. `Podfile` 파일을 열고 다음 줄을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널에서 프로젝트 폴더로 이동한 후 다음 명령어를 실행하여 Cocoapods를 설치합니다.

```bash
pod install
```

3. 프로젝트를 열고 `import NVActivityIndicatorView`를 추가하여 라이브러리를 사용할 준비를 합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 초기화하고 화면에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballRotateChase, color: UIColor.red)
view.addSubview(activityIndicatorView)
```

2. 작업이 시작되면 액티비티 인디케이터를 시작합니다.

```swift
activityIndicatorView.startAnimating()
```

3. 작업이 완료되면 액티비티 인디케이터를 중지합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 예제 코드

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballRotateChase, color: UIColor.red)

    override func viewDidLoad() {
        super.viewDidLoad()
        // 액티비티 인디케이터를 화면에 추가
        view.addSubview(activityIndicatorView)

        // 작업 시작
        startLongRunningTask()
    }

    func startLongRunningTask() {
        // 액티비티 인디케이터 시작
        activityIndicatorView.startAnimating()

        // 긴 작업 수행
        DispatchQueue.global().async {
            // 긴 작업 수행 로직
            Thread.sleep(forTimeInterval: 5)

            // 작업 완료 후 액티비티 인디케이터 중지
            DispatchQueue.main.async {
                self.activityIndicatorView.stopAnimating()
            }
        }
    }
}
```

위 예제 코드에서는 `ViewController` 클래스에서 `NVActivityIndicatorView`를 초기화하고 화면에 추가한 다음, `startLongRunningTask()` 메소드를 호출하여 액티비티 인디케이터를 시작합니다. `startLongRunningTask()` 메소드에서는 백그라운드에서 5초 동안 긴 작업을 수행한 후 액티비티 인디케이터를 중지합니다.

---

이렇게 NVActivityIndicatorView를 활용하여 앱의 백그라운드 작업 상태를 표시할 수 있습니다. 사용자에게 앱이 작업 중임을 알려줌으로써 사용자 경험을 향상시킬 수 있습니다.