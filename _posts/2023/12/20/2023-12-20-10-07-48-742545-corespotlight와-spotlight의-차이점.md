---
layout: post
title: "[ios] CoreSpotlight와 Spotlight의 차이점"
description: " "
date: 2023-12-20
tags: [ios]
comments: true
share: true
---

iOS 애플리케이션을 개발할 때 사용되는 CoreSpotlight와 Spotlight은 모두 사용자가 콘텐츠를 검색하고 찾기 쉽도록 도와주는 기능이지만, 각각의 목적과 사용 방법에 차이가 있습니다.

## Spotlight

Spotlight는 iOS의 운영 체제 수준에서 제공되는 **전역 검색 기능**입니다. 사용자가 iOS 장치에서 검색할 때 애플리케이션의 콘텐츠 외에도 시스템 레벨의 결과를 표시하여 특정 애플리케이션 내의 콘텐츠 또는 데이터를 사용자가 손쉽게 찾을 수 있도록 도와줍니다.

## CoreSpotlight

반면에 CoreSpotlight은 iOS 애플리케이션에서 **사용자 지정 검색 데이터**를 추가하는 데 사용됩니다. 애플리케이션 내에서 사용자가 주로 사용하는 콘텐츠나 중요한 정보를 디바이스에 색인화하여, 사용자가 애플리케이션을 실행하지 않고도 해당 정보를 검색하고 싶을 때에도 해당 정보를 제공할 수 있도록 도와줍니다.

따라서, Spotlight는 iOS 장치의 운영 체제 수준에서 작동하는 반면, CoreSpotlight은 개발자가 직접 애플리케이션에 추가하는 커스텀 검색 데이터를 관리하고 활용하는 데 사용됩니다.

이러한 차이점으로 인해, 개발자는 애플리케이션의 콘텐츠를 사용자가 쉽게 검색하고 찾을 수 있도록 하기 위해 두 가지 기능을 함께 활용할 수 있습니다.

더 자세한 내용은 아래 참고 자료를 참고하시기 바랍니다.

## 참고 자료

- [Apple Developer Documentation - Core Spotlight](https://developer.apple.com/documentation/corespotlight)
- [Apple Developer Documentation - Spotlight](https://developer.apple.com/documentation/corespotlight)

이상으로 CoreSpotlight와 Spotlight의 차이점에 대한 내용을 정리해보았습니다.