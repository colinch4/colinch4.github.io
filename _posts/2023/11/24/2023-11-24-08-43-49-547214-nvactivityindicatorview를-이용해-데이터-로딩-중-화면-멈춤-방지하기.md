---
layout: post
title: "[swift] NVActivityIndicatorView를 이용해 데이터 로딩 중 화면 멈춤 방지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 데이터를 로딩할 때, 사용자는 화면이 멈추는 것을 경험하고 싶지 않을 것입니다. 이를 방지하기 위해 NVActivityIndicatorView 라이브러리를 사용하여 데이터 로딩 중에 화면이 멈추지 않도록 할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 구현하는데 도움이 되는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상의 로딩 인디케이터를 제공합니다. 또한, 간단한 코드로 사용자화된 로딩 인디