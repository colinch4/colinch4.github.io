---
layout: post
title: "[flutter] 플러터 cached_network_image 패키지와 flutter_cache_manager 패키지의 차이점은 무엇인가요?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

### cached_network_image 패키지
cached_network_image 패키지는 네트워크에서 이미지를 가져와 캐싱하는 데 특화된 패키지입니다. 이 패키지를 사용하면 이미지를 쉽게 캐싱하여 앱의 성능을 향상시킬 수 있습니다. 이 패키지는 이미지를 불러올 때 캐싱 옵션과 한계를 가지고 있습니다. 또한 캐싱된 이미지를 변경하거나 업데이트하는 기능이 상대적으로 제한적입니다.

### flutter_cache_manager 패키지
반면에 flutter_cache_manager 패키지는 다양한 형식의 파일(이미지 외에도 비디오, 오디오 등)을 관리하는 데 사용됩니다. 이 패키지를 통해 캐싱된 파일의 수명 주기, 업데이트 처리 및 추가적인 사용자 지정 기능을 쉽게 구현할 수 있습니다. 

### 요약
기본적으로, cached_network_image 패키지는 이미지 캐싱에 초점을 맞추고 좀 더 간단한 사용 사례에 적합합니다. 반면에 flutter_cache_manager 패키지는 다양한 종류의 파일에 대한 고급 캐싱 및 관리 기능이 필요한 경우에 유용합니다.

따라서 프로젝트의 요구 사항에 맞게 적합한 패키지를 선택하여 사용하는 것이 중요합니다.

마지막으로, 이러한 패키지의 사용법과 장단점에 대한 자세한 정보는 공식 문서를 참조하는 것이 좋습니다.