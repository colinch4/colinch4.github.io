---
layout: post
title: "브라우저 객체 모델(Browser Object Model, BOM)의 개요"
description: " "
date: 2023-10-13
tags: [bom]
comments: true
share: true
---

## 개요
브라우저 객체 모델(Browser Object Model, BOM)은 웹 브라우저 안에서 웹 페이지를 조작하고 제어하는 데 사용되는 객체의 계층 구조를 나타냅니다. BOM은 웹 브라우저의 창, 프레임, 히스토리, 쿠키, 위치 등과 같은 다양한 요소에 접근하고 조작할 수 있는 메서드와 속성을 제공합니다.

## 주요 객체
BOM은 다음과 같은 주요 객체를 포함합니다.

### Window
`Window` 객체는 브라우저 창을 나타냅니다. 전역 객체로서 웹 페이지의 최상위에 위치하며, 브라우저 창과 관련된 작업을 수행할 수 있는 많은 메서드와 속성을 제공합니다. `Window` 객체를 통해 브라우저 창의 크기, URL, 문서 요소에 접근하고 조작할 수 있습니다.

### Navigator
`Navigator` 객체는 웹 브라우저의 정보를 제공합니다. 웹 브라우저의 유형, 버전, 플러그인 정보 등을 알 수 있습니다. `Navigator` 객체는 사용자 에이전트 정보와 관련한 속성을 제공하여 웹 페이지가 브라우저의 기능에 따라 동작할 수 있도록 합니다.

### Location
`Location` 객체는 현재 웹 페이지의 URL 정보를 제공합니다. URL의 프로토콜, 호스트, 경로 등의 정보에 접근할 수 있으며, URL을 변경하여 페이지를 다시 로드할 수도 있습니다.

### History
`History` 객체는 브라우저의 방문 기록에 접근할 수 있는 메서드와 속성을 제공합니다. `History` 객체를 사용하여 이전 페이지로 이동하거나 앞으로 이동하면서 페이지의 방문 기록을 조작할 수 있습니다.

### Document
`Document` 객체는 현재 로드된 웹 페이지의 문서를 나타냅니다. HTML 요소에 접근하고 조작할 수 있는 메서드와 속성을 제공하여 웹 페이지의 내용을 변경하거나 이벤트를 처리할 수 있습니다.

## 마무리
브라우저 객체 모델(Browser Object Model)은 웹 브라우저의 다양한 요소에 접근하고 조작할 수 있는 객체의 계층 구조를 제공합니다. BOM을 이용하여 브라우저 창, URL 정보, 방문 기록 등을 다룰 수 있으며, 웹 페이지를 동적으로 제어할 수 있습니다. BOM은 웹 개발에서 필수적인 개념이므로, 이를 잘 이해하고 활용할 수 있어야 합니다.

> 해시태그: #브라우저객체모델 #BOM