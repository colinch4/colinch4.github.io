---
layout: post
title: "[iOS] Localization"
description: " "
date: 2021-05-14
tags: [iOS]
comments: true
share: true
---

# Localization
- 현지화, 해당 나라의 문화, 특색에 맞게 언어 및 디자인을 변경하는것 

[Localizing Your App](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LocalizingYourApp/LocalizingYourApp.html)
<img width="606" alt="스크린샷 2021-04-24 오후 6 14 13" src="https://user-images.githubusercontent.com/45002556/115953860-e8539a00-a528-11eb-9a61-977d5069c10a.png">

1. App의 사용자 인터페이스와 코드를 국제화(internationalizing)한 후에는 현지화(localization) 프로세스를 시작하세요.
2. 사용자 지향 텍스트를 포함하는 모든 개발 언어 문자열 파일을 표준 XML지역화 교환 파일 형식(XLIFF)으로 내보냅니다.
3. XLIFF파일을 여러 언어로 번역하려면, 현지화팀에 제출합니다. 번역을 기다리는 동안, 계속해서 앱을 개발하세요.
4. XLIFF변환을 프로젝트로 가져와 추가 한 각 언어로 App을 테스트하십시오. 

문자열 파일을 만들면 위와 같은 과정을 거치면서 언어를 바꿔준다(자동번역 x)   

<img width="803" alt="스크린샷 2021-04-24 오후 6 18 45" src="https://user-images.githubusercontent.com/45002556/115954008-83e50a80-a529-11eb-9171-cd38a8081dee.png">

- String 파일 만들기      
- 파일 이름은 "Localizable.strings"           

<img width="1388" alt="스크린샷 2021-04-24 오후 6 36 48" src="https://user-images.githubusercontent.com/45002556/115954442-0b337d80-a52c-11eb-95da-8f5bdaae8b67.png">

- 파일 생성 후 오른쪽에 Localize 버튼 클릭

<img width="794" alt="스크린샷 2021-04-24 오후 6 39 50" src="https://user-images.githubusercontent.com/45002556/115954511-75e4b900-a52c-11eb-8875-585960977604.png">

- 프로젝트 설정 -> info -> Localization 에서 원하는 국가 추가

<img width="721" alt="스크린샷 2021-04-24 오후 6 41 50" src="https://user-images.githubusercontent.com/45002556/115954568-bd6b4500-a52c-11eb-88b8-1515d3ef981e.png">

- 아까 생성해둔 Localizable.strings 파일이 체크된걸 확인

<img width="262" alt="스크린샷 2021-04-24 오후 6 44 26" src="https://user-images.githubusercontent.com/45002556/115954663-1aff9180-a52d-11eb-9d7b-d2ef728f3853.png">

- 이후 Localizable.strings 파일 하위에 베이스가되는 파일가 추가한 국가가 생긴걸 확인할 수 있다.

<img width="360" alt="스크린샷 2021-04-24 오후 6 48 05" src="https://user-images.githubusercontent.com/45002556/115954742-9cefba80-a52d-11eb-99ee-af87fba4a3e1.png">

- 위와 같이 해당하는 단어나 문장을 지정해두면된다. (key - value 형식)

<img width="769" alt="스크린샷 2021-04-24 오후 6 52 55" src="https://user-images.githubusercontent.com/45002556/115954874-49ca3780-a52e-11eb-8ca4-401df54106f3.png">

- 위와 같이 String을 extension하여 다음과 같이 편리하게 사용할 수 있다.

```swift
testLabel.text = "안녕".localized
```

## Stroyboard 또는 xib에서 적용
<img width="220" alt="스크린샷 2021-04-24 오후 6 59 32" src="https://user-images.githubusercontent.com/45002556/115955050-513e1080-a52f-11eb-9538-5482c904cc68.png">

- 프로젝트 설정 info에서 localization을 추가하는 과정에서 위와 같이 Storyboard에도 하위에 파일이 생긴걸 확인

<img width="276" alt="스크린샷 2021-04-24 오후 7 03 03" src="https://user-images.githubusercontent.com/45002556/115955112-b42fa780-a52f-11eb-8586-93b34672f413.png">

- 오른쪽 inspector에서 원하는 국가의 stroyboard 파일을 Localizable Strings로 변경

<img width="548" alt="스크린샷 2021-04-24 오후 9 07 22" src="https://user-images.githubusercontent.com/45002556/115958129-12b15180-a541-11eb-99f6-a7de65c1481b.png">

- 위 사진과 같이 수정하면된다.
