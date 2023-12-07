---
layout: post
title: "[swift] Swift와 Elastic Animation을 이용한 탄성 애니메이션 구현하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

탄성 애니메이션은 화면 요소가 충돌하거나 움직일 때 나타나는 특별한 효과를 의미합니다. 이번 블로그 포스트에서는 Swift와 Elastic Animation 프레임워크를 사용하여 탄성 애니메이션을 구현하는 방법을 알아보겠습니다.

## 필수 사항

이 튜토리얼을 진행하기 위해서는 다음 사항들이 필요합니다.

- Swift 프로그래밍 언어의 기본 지식
- Xcode IDE
- Elastic Animation 프레임워크 설치

## Elastic Animation 프레임워크란?

Elastic Animation은 애니메이션을 더 재미있고 유연하게 만들어주는 Swift 기반의 오픈 소스 프레임워크입니다. 이 프레임워크는 오브젝트 간 충돌과 물리 역학을 시뮬레이션하는 것에 중점을 두고 있습니다. 이를 사용하면 간단한 코드로 다양한 탄성 애니메이션 효과를 추가할 수 있습니다.

## 설치 및 설정

Elastic Animation을 사용하기 위해서는 먼저 프로젝트에 프레임워크를 추가해야 합니다. 다음 단계를 따라서 Elastic Animation을 설치하고 설정해보세요.

1. Elastic Animation 프레임워크를 다운로드하고 압축을 해제합니다.
2. Xcode에서 프로젝트를 엽니다.
3. 프로젝트 네비게이터에서 프로젝트 파일을 선택하고, Targets 리스트에서 Build Phases 탭을 선택합니다.
4. 'Link Binary With Libraries' 섹션을 찾고, '+' 버튼을 클릭합니다.
5. ElasticAnimation.framework 파일을 선택하고 'Add' 버튼을 클릭합니다.

이로써 Elastic Animation 프레임워크의 설치와 설정이 완료되었습니다.

## 탄성 애니메이션 구현하기

이제 탄성 애니메이션을 구현해보겠습니다. 탄성 애니메이션을 적용할 뷰의 구성은 다음과 같습니다.

```swift
import ElasticAnimation

class ElasticView: UIView {

    private var animator: ElasticAnimator?

    override init(frame: CGRect) {
        super.init(frame: frame)
        setupGestureRecognizer()
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        setupGestureRecognizer()
    }

    private func setupGestureRecognizer() {
        let gestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan))
        self.addGestureRecognizer(gestureRecognizer)
    }

    @objc private func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
        switch gestureRecognizer.state {
        case .began:
            animator = ElasticAnimator(view: self)
            animator?.addTopBound(100)
            animator?.addBottomBound(self.superview?.frame.height ?? 0 - 100)
        case .changed:
            let translation = gestureRecognizer.translation(in: self)
            animator?.moveTopBound(to: translation.y + 100)
            animator?.moveBottomBound(to: self.superview?.frame.height ?? 0 - translation.y - 100)
        case .ended:
            animator?.startAnimation()
        default:
            break
        }
    }

}
```

위의 코드는 ElasticView라는 커스텀 뷰를 정의하는 예시입니다. 이 뷰는 UIPanGestureRecognizer를 사용하여 드래그 동작을 감지하고, 해당 동작에 따라 애니메이션을 적용합니다. 탄성 애니메이션을 구현하기 위해 ElasticAnimator를 사용하며, 상/하단 바운드 값을 추가하고 변경합니다. 드래그 동작이 종료되면 애니메이션을 시작합니다.

이제 ElasticView를 사용하여 탄성 애니메이션을 추가할 뷰를 생성하고, 화면에 추가하는 코드를 작성하면 됩니다.

```swift
let elasticView = ElasticView(frame: CGRect(x: 100, y: 100, width: 200, height: 200))
self.view.addSubview(elasticView)
```

## 결론

이번 포스트에서는 Swift와 Elastic Animation을 사용하여 탄성 애니메이션을 구현하는 방법을 알아보았습니다. Elastic Animation 프레임워크를 사용하면 간단한 코드로 다양한 탄성 애니메이션 효과를 적용할 수 있습니다. 추가적인 정보나 더 많은 예제 코드는 Elastic Animation의 공식 문서를 참고하시기 바랍니다. Happy coding! 

## 참고 자료

- [Elastic Animation 공식 GitHub 페이지](https://github.com/roberthein/Elastic)
- [Elastic Animation 문서](https://roberthein.com/blog/introducing-elastic-swiftui-animations)