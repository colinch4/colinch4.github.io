---
layout: post
title: "[sketch] 스케치 작업 환경 설정하기"
description: " "
date: 2021-09-09
tags: [개발]
comments: true
share: true
---


## 스케치 작업 환경 설정하기

[원문보기](https://uxdesign.cc/workplace-hygiene-in-sketch-dc8184c0dc8f)

### 1. 파일의 이름을 일관되게 지정하라

- “VisualDesign_v4.2_final_final2 Copy”와 같은 악명 높은 파일명에서 벗어나 하나의 명명규칙을 선택하고 팀원이 함께 협의해라
- “file naming convention”으로 예제를 구글링해라 
- 하위 구성요소, 주 및 부 버전뿐만 아니라 여러 팀 구성원과 같이 작업 파일의 특성을 고려한 네이밍 컨벤션이다
- 하나의 디바이스만 디자인할 때는 가능한 간단하게 이름을 유지하기 위해 Device 속성을 버린다 
- 어떤 컨벤션을 사용하든 중요한것은 프로젝트 전체에서 일관성을 유지하는것이다. 이 간단한 규칙을 어떻게 활용하는지 알게된다면 모든사람의 시간을 줄여줄 강력한 도구가 될 것이다 
- [abstract](https://www.abstract.com/)나 [plant](https://plantapp.io/ )와 같은 버전관리 도구를 찾아볼 가치가 있다

### 2. 아트보드를 조직적인 형태로 만들어라

- 아트보드는 인터페이스의 페이지, 뷰 또는 콤포넌트를 편집하는 영역 또는 캔버스이다 
- 스케치는 아트보드를 파일로 내보내거나 InVision과 같은 프로토타이핑 플랫폼에 직접 사용되기에 명명규칙을 투명하고 순차적으로 유지하는것이 좋다 
- 초기 컨셉설정이 끝나면 정보구조(IA)에 대한 아이디어가 있다면 모든 스크린/뷰에 ID와 네임 태그를 지정한다. 이 ID는 앱 또는 웹 사이트의 계층 구조에 대한 힌트를 제공하는 식별자가 된다
- 스케치의 drawing area에서 각 뷰의 아트보드는 수직 방향으로 배치되는 반면, 동일한 뷰의 여러가지 상태(비활성화, 비어있는 상태)는 수평으로 정렬된다. 동일한 뷰의 여러 상태를 구별하기 위해 각 대지는 1에서 부터 시작하는 번호를 가진다
- 이 컨벤션은 특히 큰 스케치파일에서 더 나은 방향성을 제공하고 모든 내보낸 파일 또는 인비전 화면이 순차적으로 표시되도록하여 단일화면을 쉽게 찾거나 변경할 수 있다. 프로젝트가 크고 정교해질수록 유익할것이다

### 3. 의미 있는 방식으로 레이어 라벨링하기

* 의미 있는 이름으로 해당 요소를 쉽게 찾을수있도록 하는것은 디자인 파일을 깔끔하게 유지하는데에 가장 기본적이고 소홀한 연습 중 하나이다

  > [Rename It](https://github.com/rodi01/RenameIt) 참조

### 4. Page를 사용하여 작업물을 배포하라

* 스케치는 프로젝트를 여러 페이지에 걸쳐 배포할 수 있는 기능을 제공한다. 프로젝트가 커지고 아트보드가 많아지면 페이지 기능을 이용하라

* 일반적으로 앱/웹 사이트에 관계없이 하나 이상의 주요 섹션을 만들고, 다른 주요 ID를 반영할 때마다 페이지를 사용한다. 각 주요 ID는 고유한 페이지를 가지므로 동시에 처리해야하는 아트보드의 수가 상대적으로 적게 유지된다

### 5. 스스로 반복하지 말아라 - 심볼을 사용하라

- 스케치가 제공하는 가장 강력한 기능 중 하나다. 심볼은 그래픽 객체의 블루프린트라고 볼수있다 (벡터 쉐입에서 비트맵, 텍스트 엘리먼트 그 중 하나일 수 있음)  
- Symbols라는 별도의 페이지에 저장된다 
- 아트보드에서 심볼을 사용하려면 원본 심볼이 꾸준히 연결되어있는 복사본을 만들어라 
- 이 복사본은 심볼의 instance라 부른다 
- 심볼의 아름다운점은 한번 편집하면 모든 인스턴스가 이러한 변경 사항을 상속받고 자동으로 업데이트된다는 점이다 
- 심볼 인스턴트는 크기는 조정 가능하고 텍스트 레이블을 개별적으로 재정의(override)하여 스케치에서 매우 유연하고 강력하게 사용할 수 있다 
- 심볼 이름 앞에 슬래시 기호를 입력하면 서브카테고리를 생성해준다. 프로젝트 및 심볼라이브러리가 매우 커지면 유용해진다 
- 일반적으로 동일한 유형의 요소(버튼 또는 텍스트 필드)를 한번 이상 사용할 때마다 심볼을 만들어 인스턴스를 사용해야한다 
- 스케치는 심볼을 [중첩](https://www.sketch.com/docs/symbols/nested-symbols/)시킬 수 있도록 했다
- 다른 심볼을 상휘 심볼에 그룹화할 수 있다 
- 심볼을 중첩하고 크기 조정 동작을 제어하는 기능은 스케치에서 정교한 디자인 시스템을 구축하기 위한 토대가 된다 
- Bradn Frost의 [Atomic Design](http://bradfrost.com/blog/post/atomic-web-design/) 과 같은 개념을 구현할 수 있다 

### 6. 스타일로 텍스트 및 쉐입 레이어 제어

- 심볼, [공유된 레이어와 텍스트 스타일](https://www.sketch.com/docs/styling/shared-styles/)과 매우 유사하여 스케치 파일을 정리할 필요가 없다
- HTML과 CSS에 익숙하다면 당신은 그 개념을 생각해낼 필요가 없다: 도형이나 텍스트 엘리먼트를 생성해 그들에게 미리 정의된 스타일을 지정하면 fill, stroke, color, opacity와 같은 시각적 속성을 변환하거나 텍스트 요소의 경우 font family, font size, weight등을 수정할 수 있다
- 심볼과 마찬가지로 텍스트와 레이어 스타일은 이름에 슬래시를 사용하여 중첩할 수 있으므로 계층 구조로 스타일을 멋지게 정리할 수 있다

### 7. 여러 파일에서 공유 라이브러리 사용

- 팀원들이 최신 버전을 찾을 때 혼란에 빠지지 않도록 파일 이름을 멋지게 지정하고, 심볼과 텍스트 스타일을 사용하여 파일의 모든 요소를 일관되게 유지했다. 엘리먼트 스타일이나 다른 파일에도 전파하려는 심볼에 변경사항을 적용하기로 한경우에는 [공유 라이브러리](https://medium.com/ux-power-tools/sketch-libraries-how-they-work-and-the-crazy-stuff-you-can-do-with-them-fc10f142ac80) 를 사용할 수 있다 
- 공유 라이브러리는 여러 스케치 파일간 공유되는 라이브러리(일명 심볼 모음)이다 
- 원래는 서드파티앱을 사용해야했지만 47버전부터 이 기능을 내장하고 있다 
- 작동 방법: 라이브러리가 될 별도의 스케치 파일에 모든 종류의 심볼을 정의한다. 새 스케치 파일을 만들거나 기존 스케치 파일을 열어 스케치 파일에 링크하여 라이브러리의 심볼을 가져온다. 완료되면 로컬 심볼에 액세스하는것과 동일한 방법으로 라이브러리 파일의 모든 심볼에 액세스할 수 있다.
- 라이브러리의 심볼을 편집하고 변경 사항을 저장하기로 결정한 경우 링크된 파일을 열때마다 공유 라이브러리의 변경 사항에 대한 알림이 표시된다. 각각 하나씩 가져와서 변경하도록 결정할 수 있다 



 알다시피, 여기에 설명한 방법과 기능은 매우 간단하며 다음 프로젝트에서 약간의 노력으로 구현할 수 있다 - 당신과 당신의 팀을 위한 약간의 훈련이 필요하다.  

 프로젝트 초기에는 파일이 작고 프로젝트가 관리하기 쉬워운것 처럼 보이지만 디자인 단계 끝무렵에는 크고 서로 엉킨 카오스를 발견할 수 있다. 아트보드 카오스에 대해 전혀 이해할 수 없거나, 최신 버전을 찾을 수 없는 경우 조정을 위해 지난 반년간 얼마나 자주 아카이브된 프로젝트를 파고들어야 했는지 돌이켜보라.  