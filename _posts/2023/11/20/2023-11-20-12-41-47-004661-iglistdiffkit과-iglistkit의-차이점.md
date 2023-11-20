---
layout: post
title: "[swift] IGListDiffKit과 IGListKit의 차이점"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

IGListDiffKit과 IGListKit은 모두 Instagram에서 개발한 iOS용 데이터 주도 UI 라이브러리입니다. 이들은 유사한 목적을 가지고 있지만 몇 가지 차이점이 있습니다.

## IGListDiffKit

IGListDiffKit은 데이터 변경 사항을 감지하여 효율적으로 UI 업데이트를 수행하는데 중점을 둔 라이브러리입니다. 데이터 변경을 추적하기 위해 유용한 알고리즘과 기능을 제공합니다.

IGListDiffKit의 주요 기능:

1. 데이터 변경 감지: IGListDiffKit은 두 데이터 집합 간의 변경을 자동으로 감지합니다. 이를 통해 변경된 항목만 업데이트되고, 불필요한 UI 업데이트를 방지할 수 있습니다.
2. 전체 리스트 업데이트: IGListDiffKit은 변경된 항목이 아닌 전체 리스트를 업데이트하는 기능을 제공합니다. 이를 통해 더 효율적인 UI 업데이트를 수행할 수 있습니다.
3. 세그먼트 업데이트: IGListDiffKit은 세그먼트별로 데이터 변경을 추적할 수 있습니다. 이를 통해 세그먼트 간의 변경이 발생할 때 효율적인 업데이트를 수행할 수 있습니다.

## IGListKit

IGListKit은 IGListDiffKit 위에 구축된 확장된 라이브러리입니다. IGListDiffKit의 기능을 포함하면서 데이터 주도 UI 개발을 더욱 쉽게 만들어줍니다.

IGListKit의 주요 기능:

1. 데이터 소스: IGListKit은 데이터를 제공하는 데 사용되는 데이터 소스 프로토콜을 제공합니다. 이를 사용하여 셀 및 섹션 구성을 수행할 수 있습니다.
2. 스크롤 이벤트 처리: IGListKit은 스크롤 이벤트를 처리하는 기능을 제공합니다. 이를 통해 스크롤에 따라 동적으로 UI를 업데이트할 수 있습니다.
3. 컨테이너 뷰 컨트롤러: IGListKit은 컨테이너 뷰 컨트롤러를 사용하여 다양한 컨텐츠를 표시하는 기능을 제공합니다. 이를 통해 다중 컨텐츠 뷰를 구성할 수 있습니다.

## 결론

IGListDiffKit은 데이터 변경 감지와 효율적인 UI 업데이트에 중점을 둔 라이브러리입니다. IGListKit은 IGListDiffKit을 확장하여 데이터 주도 UI 개발을 더욱 쉽게 만들어줍니다. 선택은 개발자의 필요와 선호도에 따라 달라질 수 있습니다.

- [IGListDiffKit 공식 문서](https://github.com/Instagram/IGListKit)
- [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)