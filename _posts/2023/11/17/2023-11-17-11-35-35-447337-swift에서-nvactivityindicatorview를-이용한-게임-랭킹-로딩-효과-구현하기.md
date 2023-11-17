---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 게임 랭킹 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

게임 어플리케이션에서 사용자의 게임 랭킹을 로딩하는 동안에는 로딩 화면을 제공하는 것이 좋습니다. 이를 위해 `NVActivityIndicatorView`를 사용하여 로딩 효과를 구현할 수 있습니다. 이번 블로그 포스트에서는 Swift에서 `NVActivityIndicatorView`를 이용해 게임 랭킹 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치

`NVActivityIndicatorView`는 간단하게 CocoaPods 또는 Carthage를 통해 설치할 수 있습니다. 여기서는 CocoaPods를 사용한다고 가정하고 설치 방법을 안내하겠습니다. 먼저 `Podfile`에 다음과 같은 내용을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 CocoaPods를 이용하여 `NVActivityIndicatorView`를 설치합니다.

```bash
$ pod install
```

## 2. NVActivityIndicatorView 사용하기

### 2.1 NVActivityIndicatorView 뷰 추가하기

`NVActivityIndicatorView`는 로딩 효과를 나타내는 뷰입니다. 이 뷰를 사용하기 위해 해당 뷰를 추가해야 합니다. 아래 코드를 참고하여 로딩 뷰를 추가해주세요.

```swift
import NVActivityIndicatorView

class RankingViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 뷰 설정
        let activityIndicatorSize: CGFloat = 50
        let activityIndicatorFrame = CGRect(x: (view.frame.width - activityIndicatorSize) / 2,
                                            y: (view.frame.height - activityIndicatorSize) / 2,
                                            width: activityIndicatorSize,
                                            height: activityIndicatorSize)
        activityIndicatorView = NVActivityIndicatorView(frame: activityIndicatorFrame,
                                                        type: .ballSpinFadeLoader,
                                                        color: .white,
                                                        padding: nil)
        view.addSubview(activityIndicatorView)
    }
}
```

### 2.2 로딩 효과 제어하기

이제 `NVActivityIndicatorView`를 제어하여 로딩 효과를 나타내고 숨길 수 있는 기능을 추가해보겠습니다. 아래 코드를 참고하여 로딩 효과를 제어하는 함수를 추가해주세요.

```swift
extension RankingViewController {
    // 로딩 효과 시작
    func startLoading() {
        view.isUserInteractionEnabled = false
        activityIndicatorView.startAnimating()
    }

    // 로딩 효과 종료
    func stopLoading() {
        view.isUserInteractionEnabled = true
        activityIndicatorView.stopAnimating()
    }
}
```

이제 `startLoading` 함수를 호출하여 로딩 효과를 시작하고, `stopLoading` 함수를 호출하여 로딩 효과를 종료할 수 있습니다.

## 3. 로딩 효과 사용하기

로딩 효과를 게임 랭킹 로딩에 사용하기 위해서는 해당 기능을 호출하는 시점에 로딩 효과를 보여주면 됩니다. 예를 들어, 게임 랭킹을 로딩하는 API 요청이 시작되면 `startLoading` 함수를 호출하여 로딩 효과를 시작하고, API 요청이 완료되면 `stopLoading` 함수를 호출하여 로딩 효과를 종료하는 방식으로 사용할 수 있습니다.

```swift
class RankingViewController: UIViewController {
    //...

    override func viewDidLoad() {
        super.viewDidLoad()

        //...

        // 게임 랭킹 로딩 예시
        startLoading()
        apiService.fetchGameRanking { [weak self] result in
            // 게임 랭킹 로딩 완료 후 처리
            self?.stopLoading()
            
            switch result {
            case .success(let ranking):
                // 게임 랭킹 데이터 처리
                self?.handleRankingData(ranking)
            case .failure(let error):
                // 에러 처리
                self?.handleError(error)
            }
        }
    }
}
```

위 예시는 게임 랭킹을 가져오는 API 요청 시작 시점에 `startLoading` 함수를 호출하여 로딩 효과를 시작하고, API 요청이 완료되면 `stopLoading` 함수를 호출하여 로딩 효과를 종료하는 방식입니다.

## 4. 결론

이번 튜토리얼에서는 Swift에서 `NVActivityIndicatorView`를 이용하여 게임 랭킹 로딩 효과를 구현하는 방법에 대해 알아보았습니다. `NVActivityIndicatorView`를 사용하면 사용자에게 더 나은 사용 경험을 제공할 수 있으며, 코드 구현도 간단하게 할 수 있습니다. 이를 참고하여 여러분의 게임 어플리케이션에 로딩 효과를 추가해보세요.

## 참고 자료

- [NVActivityIndicatorView - GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)