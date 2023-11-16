---
layout: post
title: "[swift] - Swift Charts와 Core Graphics의 관계"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift Charts는 데이터 시각화를 위한 오픈 소스 라이브러리로, iOS 애플리케이션에서 그래프나 차트를 만들기 위해 사용됩니다. 이 라이브러리는 Core Graphics 프레임워크를 기반으로 구현되었으며, 그래프 그리기에 필요한 다양한 기능을 제공합니다.

### Core Graphics란?

Core Graphics는 iOS 및 macOS에서 2D 그래픽 렌더링에 사용되는 그래픽 프레임워크입니다. Core Graphics 프레임워크는 벡터 그래픽을 생성하고 표현하기 위해 사용되며, 라인, 원, 사각형 등 다양한 기본 도형을 그릴 수 있는 기능을 제공합니다.

### Swift Charts와 Core Graphics의 관계

Swift Charts는 Core Graphics를 기반으로 그래프를 그립니다. Swift Charts는 사용자가 차트의 유형, 스타일 및 데이터를 정의하면 Core Graphics를 사용하여 해당 정보를 바탕으로 그래프를 렌더링합니다.

예를 들어, Swift Charts를 사용하여 선 그래프를 그릴 때, Core Graphics를 사용하여 각 데이터 포인트를 선으로 연결하고, 축의 눈금을 그리고, 라벨을 추가하는 등의 작업을 수행합니다. Core Graphics의 다양한 그리기 함수와 속성을 활용하여 그래프를 자세하게 제어할 수 있습니다.

Core Graphics를 직접 사용하여 그래프를 그리는 것도 가능하지만, Swift Charts를 사용하면 보다 쉽고 편리하게 그래프를 구현할 수 있습니다. Swift Charts는 이미 다양한 그래프 유형과 사용자 정의 기능을 제공하므로, 그래프를 만들기 위한 기본적인 작업들을 극적으로 단순화합니다.

### 결론

Swift Charts는 Core Graphics를 기반으로 한 데이터 시각화 라이브러리입니다. Core Graphics는 iOS 및 macOS에서 2D 그래픽 렌더링을 위해 사용되는 프레임워크로, Swift Charts는 Core Graphics를 내부적으로 활용하여 그래프를 그립니다. Swift Charts를 사용하면 Core Graphics의 다양한 기능을 활용하여 손쉽게 그래프를 만들 수 있습니다.

**참고 자료:**
- [Swift Charts GitHub](https://github.com/i-schuetz/SwiftCharts)
- [Core Graphics Documentation](https://developer.apple.com/documentation/coregraphics)