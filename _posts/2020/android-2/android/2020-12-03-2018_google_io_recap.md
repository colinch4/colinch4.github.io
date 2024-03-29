---
layout: post
title: "[안드로이드] google io recap"
description: " "
date: 2020-12-03
tags: [android]
comments: true
share: true
---


## 2018 google io recap with android (in kakao)

구글 IO를 정리하자면 크게 5가지 꼭지로 볼 수 있다. 새로운 안드로이드의 기능과 안드로이드 스튜디오, 머터리얼 디자인, 플레이 콘솔의 새로운 기능, 인스턴트앱, Chrome OS를 위한 Android App이다. 


 Quick Links:
 
 *  [What's New in Android](#android)
 *  [Material Design](#material)
 *  [Play console New Feature](#playconsole)
 *  [Android App Bundle](#bundle)
 *  [Android for ChormeOS](#chrome)


## <a name="android"></a> What's New in Android

##### Key Word : bettery, slices View, actions with google accistant, notification, Notch Design, compatibility, pre profile tools, androidx

dapte bettery
remoteView -> slices - (특정 뷰만 사용할 수 있도록)
actions- 머신러닝에서 실행 시켜딜 수 있음(슬라이스를 제공기능)

notification - 
이미지를 바로 추가
애니메이션 추가
특정 노티피케이션에 대해 서제스트 추가
블로킹 기능 - 같은 노티에 대해 여러 차례블록한다면 추천 해줌 차단할까라고 물어봄

컷아웃( 노치) 
스테이터스바 사이즈 하드코딩만 안하면 되!!! 
노치는 스테이터스바 높이가 달라질 수 있음
풀스크린 - 스테이터스 바크기만 큼 짤라서 전체 크기가 달라짐 (노치사이즈만 큼 줄어듬) 그러므로 사이즈 하드코딩을 조심해야함

호환성 - 프라이빗 api사용 불가 - 리플렉션 금지
퍼블릭으로 모두 사용 가능해야한다
타겟sdk 26이상으로
에뮬레터 빨라짐
크롬 os 도 실행 가능!!

파이어베이스에서 머신러닝 기능 중에 몇 거지를 클라에서도 쓸 수 있게 추가되어짐.

빠르고 쉽게 android 개발하기

개선된 사항들 정리
1. 이전Profile your code 성능 평가 툴
    1. 측정에 걸리는 시간이 많아서 실제 시간보다 부풀려 보이는 시간이 있음.
    2. 개선 -> 안드로이드 스튜디오 내부에 완전히 통합. 시간도 축소

2. Layout design
    1. constraintLayout이 나오기 시작해서 툴로 작업하는게 좀 편하게 되었다.
3. Runtime & langeue
    1. 새로운 runtime ART 가 나옴
    2. 메모리가 부족해서 gc를 돌려하는 그런 작업을 최소화
    3. 기존 언어는 자바로 선정했고 1.8까지만 지원
    4. 코틀린으로 공식언어로 지원
4. Lib & api
    1. layout
        1. Abs , linear, frame, grid, relative 등등을 썼는데.
        2. Abs 쓰지말고 절대!!!
        3. Linear 간단한 구조에만
        4. Frame okay
        5. Grid 비추!
        6. Relative 쓰지말고 -> constratint
    2. Adapter views
        1. listView/ gridView / Gallery 
        2. -> recycler view 
    3. fragment
        1. 복잡해.. 업데이트 불가능..?
        2. Frmagnet는 support에서 사용!!
    4. activitiy
        1. 이제는 하나의 액티비티에서 여러 프래그먼트를 사용하는 방식으로
        2. context를 유지하는 방향으로
    5. achitecture
        1. 이제는 지원!
        2. Architecture component를 추천 반드시 사용하진 앙ㅎ아도도
    6. lifeCycle
        1. 아키텍쳐 컴포넌트의 라이프사이클 라이브러리를ㄹ 사용한느 방법으로
        2. Implements 해서 사용
        3. activity와 lifecycle을 분리할 수 있음
    7. data
        1. Room!
5. Android jetpack
    1. 안드로이드 앱에 좋은앱을 만드는데 필요한 가이드 와 라이브러리
    2. androidx
        1. Support lib의 새로운 장!
        2. 컴포넌트 별로 분리해서 사용!
        3. 28.0.0 -> 1.0.0으로 다시 내려서 필요한 부분만 하는
    3. 마이그레이션 툴을 지원해주고 있음. 
    4. Refactor 메뉴에서 리소스, 그래이들, 소스 까지 전부 커버
    5. Sql 코드를 짤 때 지원
https://developer.android.com/jetpack/

## <a name="material"></a> Material Design


1. 내가 알고 있는 종이, 질감, 지우개 등등을 익숙한 아날로그를 그냥 디지털로 옮기자해서 만들어짐
2. 크로스 플랫폼을 할 수 있도록 지향
3. 머터리얼 디자인이라하면 컴포넌트라 할 수 있다.
4. 엠티 스페이스나 로그인 액션에 대한 가이드 까지. 지원 자세하게!
5. Https://material.io/ 
6. 릴리즈가 빈번해서 번역이 크게 의미가 없기 때문!
7. 새로운 툴 런칭! - 시안에 소스도 지원!
8. 크.. 예쁘다 조아조아
9. Workflow ->product -> components
10. 뭐가 새로워 졌냐!
    1. 홈페이지가 좋아졌어 ㅋㅋㅋㅋ귀엽..
    2. Design, develop, tools 3가지메뉴
    3. 디자인!
        1. 각 회사에 대한 브랜드에 맞춰 하는 부분!
        2. 머터리얼 파운데이션
            1. 테마 , 왜 나왔는지 등등을 학술적으로 설명
            2. 계층구조
            3. 머터리얼 한글, 한문 등을 지원할 수 있도록!
        3. 머터리얼 가이드
            1. 에셋에 대한 길이 부터 소스코드까지!
            2. 와.. 개예뻐.. 
    4. 디벨롭!
        1. Github - > material components
        2. 전부 공개!
    5. tools
        1. 가장 직관적인 아이콘만! 애매한건 다뻄
        2. 컬러를 선택하면 가장 잘 어울리는 색을 골라줌ㅋㅋㅋ 미쳤다
        3. 에디터
        4. 디자인 -> 개발자 소스 sketch의 플러그인 형태!
        5. 갤러리는 협업하는 스튜디오
        6. 앱바가 아래로 내려와써.....! 오른손으로 하는데 위에는 불편!
        7. 백드롭!
        8. Relevant immediate
        9. Youtube.com/googledevelopers

## <a name="playconsole"></a> Play console New Feature

1. Release
    1. Prelaunch report 
        1. 실제 디바이스로 미리 테스트를 할 수 있도록
        2. 아 이거구나!
        3. 지금은 디자인 관련한 부분도 테스트가 가능
        4. 사이닝에 대한 기능이 필요한 부분ㅇ ㅣ많은데, 정보를 주면 이것도 테스트 가능
        5. 딥링크 - 딥하게 들어가있는 기능을 바로 테스트 가능하도록 
        6. 자바스크립트 부터 시작해서 로봇 크롤러가의 일을 지정해줌
    2. Testing
        1. 인터널하게 테스트할 수 있게 하는 트랙이 필요해서 만들어짐
        2. 최대 100명까지 테스트를 할 수 있도록 할 수 있고, 좀더 빠르고 쉽게 공유 가 가능
        3. 알파 혹은 배타테스트는 배포하고 대기가 필요함
        4. 인터널은 api의 지원을 받고 있다
    3. Play features
    4. Closed testing
        1. Create closed track
        2. 이제는 무한대로 가질 수 있다!
    5. usage
        1. 국가의 특정적인 부분을 활용 가능
    6. Open TEsting
        1. 클로즈 한 후에 오픈하게 되는데, 더 많은 피드백을 받고 있겠죠.
        2. 오픈테스팅을 통해서 특정 커뮤니티 안에 있는 사람들..?
        3. 테스트 사용자 수 조절
        4. 특정 나라에서 테스트 가능
    7. rollout
        1. 프로덕션단계
        2. 프로새스 간소화
    8. Staged rollout
        1. 점진적으로 진행해서 진행
        2. 퍼센테이지 별로 진행
    9. Release 
        1. 크래시나 이러
    10. 퍼블리싱 api
        1. 새로운 테스트 트랙이 포함되어 있고
        2. 릴리즈를 멈출 수 있다.
        3. Draft releases 가능
2. Craft better
    1. 안드러ㅗ이드 마이트
    2. 배터리, 안정성, 랜더링
        1. 새로운 기능 셋업타임과 퍼미션
    3. 배터리
        1. 여러 기능이 있음
    4. stability
        1. Crash reate
    5. rendering
        1. 싱글 프레임에서 얼마나 시간이 걸리는지 !
    6. App start time
    7. 퍼미션
        1. 유저들이 퍼미션 허락을 해줬는지 안했는지.
    8. 카테고리 밴치마크
        1. 같은 카테고리에서 다른 앱에 비해 어느정도 인지 확인가능
        2. 전체적으로 어떻게 perform을 볼 수 있다.
    9. Core vitals
        1. 중요한 정보들을 모아서 볼 수 있는 정보
        2. 무언가 문제가 생긴다면 맨위에 강조해서 보여줄거임
        3. 나쁜 기능이 생기기 전에 감지해서 할
        4. 이슈 감지와 같은 부분은 이메일로 날려줌.
3. Make better decisions
    1. 더 나은 비즈니스 결정
    2. 유저 라이프 사이클에서 결정을 내리는 것이 중요하다.
    3. Awesome acquisition
        1. 수익. 창출하는 유저와 그냥 유저가 있음
        2. 그래서 고객을 확보하거나 수익을 내기 우,ㅣ해서 어떻게 해야하는지
        3. 유저의 진입점부터 어떻게 유지가 되는지 볼 수 있음.
        4. 어떻게 플레이스토어에서 접근하게 되었는지 알 수 있음. (브라우징, 검색 등)
        5. 유입 전략을 세울 수 있음
        6. 30일 유지
    4. Revenue optio
        1. 수익 최적화!!!
        2. 서브스크립션 레포틀르 만듦
        3. 리텐션이나 취소 삭제등을 알 수 있도록 업데이트 함
        4. 집단에서 테스트를 해보고 2개의 그룹을 만들어서 무료 체험 / 유료 체험 테스트하고 결과를 확인가능
        5. 어떤 고객들이 이탈이 되는지 알 수 있음.
        6. 유저로부터의 인사이트 제공
        7. 윙백 유저
    5. 뉴앱 대시보드
        1. 라이브로 반영되고 있는 정보드를 확인할 수 있다.
        2. 대시보드 커스텀 가능
4. 결론
    1. 프리런치를 통해 안정적
    2. 크래프트 배터를 통해서 유저에게 나은 유엑스르 할 숭 ㅣㅆ고
    3. 메이ㅏ커 배터를 통해서 회사에 더 나은 수익을 낼 수 있도록. 할 수 있었다 감사!


## <a name="bundle"></a> Android app bundle

1. 이걸 통해 안드로이드 앱을 줄일 수 있는
2. 퍼플리싱 방법과 이를 통해 어떻게 서빙할 수 있는지도 확인해보자
3. App bundle format
    1. 앱번들은 퍼블리싱 용도고 설치가 안됨. 
    2. 최종 apk에 들어가지 않음.
    3. 버퍼 포맷으로 바뀜.
    4. 바이너리로 바꾸기 전에 그런 방법이 있음.
    5. 파일 타겟팅이 잘 할 수 있음.
    6. File tartgeting
        1. 어떤 유저한테 어떤 파일이 가야 하는지가 결정
        2. 그들이 필요한 파일만을 제공 그러므로 용량이 줄어듦.
        3. Fr - French 불어 사용자에게
    7. Asset targeting
        1. 언어와 같이 필요한 assets만 제공.
4. Serving
    1. Split apks
        1. 여러 개 apk가 나뉘어져 있음.
        2. 하나하나가 apk포맷임
        3. 설치가 되고 나면 하나의 앱으로 동작.
        4. 동일한 키로 사인이 되어야 함
    2. 만드는 방법
        1. 커먼한 것은 base에 들어감
        2. 그리고 필요한 부분을 split으로 나눔
        3. Dpi / x86 / fr,en ...
    3. 어떻게 유저에게 활용하나
        1. 전부 서빙하는게 아니라 필요한 부분만 날리다
        2. 이럴 때 플레이 스토어는 포트 기술이 있다.
        3. 추가로 필요한 부분은알아서 네트워크 사황일 때 깔아줌
        4. 롤리팝이상일 때 가능
        5. 그 이전엔 앱번들은 pre l device라 함
        6. 앱번들을 만들고 스플릿을 만들고 하는 부분은 알아서 적용됨.
5. Size savings
    1. 멀티 apk를 만들 필요가 없고
    2. 앱의 사이즈를 세이브 할 수 있음
6. Building the android app bundle
    1. 안드로이드 스튜디오 
    2. 빌드메뉴 들어가서 create bundle을 ㅁ나들면됨
$./gradlew modulename : ***
    3. Budle block에서 disable가능
7. ㅇㅇㅇ
    1. 구글플레이에서 릴리즈 키를 가지고 있어야한다.
    2. 이를 릴리즈 키를 가지고 여러 스플릿으로 사이닝을 하게 되고 배포가 된다.
    3. 테스트를 하고 싶다면 resigning하지 않아도돔
    4. 작은 유저와 테스트를 할 수 있게 지원
    5. 에전처럼 릴리즈 하고, 
    6. apk와 번들읆 모두 드래그 가능
    7. 플레이가 다시 해줌
8. Publishing api
    1. 퍼블리싱 pai는 모두 지원
9. 어떻게 app bundle을 테스팅하는지
    1. 인터널 테스트 트랙
        1. 어떤 지연이 없고 바로 테스팅 가능.
    2. Bundle tools
        1. 워크 플로우에 통합하기 쉽다
        2. Universe apk 을 만들기쉽다. 모든 디바이스를 지원할 수 있도록
        3. GitHub/google/bundletool
10. modularzation
    1. 피처에 따라서 모듈화 할 수 있는기능 제공
    2. 피처에 따라서 빨간색으로 표기해주고 바로 설치가 되지 않도록
    3. 이를 나누는데 많은 사람이 사용? 많은 용량을 차지? 이걸 기다릴 수 있는?
    4. base는 항상 있고
    5. app_recipe모듈 
    6. vr_viewer모듈이 있다
    7. 각각은 모두 같은 구조로 배이스와 각각 hdpi와 같은 것들ㅇ ㅣ별도로 존재
11. creating a dynamic feature
    1. onDemand feature
    2. 메니페스트에서 ondemand= true로 사용 피처 모듈로 빼낸 후에
    3. 새로운 라이브러리를 만듦(playCoreLibrary -java)
    4. 스플릿인스톨 매니저를 통해서 리퀘스트를 만들 수 있고 삭제도 가능
    5. 일부 큰 모듈과 같은 부분은 유저의 확인이 필요!
    6. Deferred install이라는 기능이 있는데 추가적인 모듈이 설치가 될 수 있다.
    7. 여러가지 모드가 있다.
    8. 모듈은 앱버전과 동기화가 된다.
12. 결론
    1. 다 만들었고 가이드는 만들고 있다.


## <a name="chrome"></a> Android for ChormeOS


1. 크롬북 os의 특징
    1. 스크린이 넓고
    2. 가로모드
    3. 멀티 윈도우가 가능
    4. 입력방식이 키보드 마우스 터치팬으로 기능
2. 크롬 os의 새로운 기능
    1. 태블릿 모드가 개선되었음 
    2. 제목 푷시줄이 숨겨지고 
    3. 화면 분할모드가 추가
    4. 9월부터 안드로이드 vitural 키보드도 지원가능
    5. 노티도 많이 정리가 되어서 안드와 비슷한 제공
3. 어떤 것들을 하면 될까?
    1. 데스크탑을 위한 앱같은 느낌을 줘야한다
    2. 그러기 위해서 제공해줘야하는 단축키와 화면 디자인
        1. Layout xml항목에 지정해야한다.
    3. 작업표시줄에 대한 정리
        1. Shelf integration 폴더로 만들
    4. 앱 숏컷(바로가기
    5. 뒤로가기 버튼은 생성하지 않아도 됨. 크롬이 기본적으로 생산
    6. Lifetime management
        1. 카카오톡이 돌고 있는데 게임하고 있다면
        2. 중지된 상태에서도 메시지가 올라와야 맞는다.
        3. 근데 오히려 이것 떄문에 다운의 위험ㅇ ㅣ있다면 권고 하지 않겠다.
    7. Shared data
        1. 드래그앤 드롭해서 데이터를 세ㅜ어할 수 있다
        2. 정상적인 데이터읹 ㅣ체크해야한다 받을때
    8. 리사이징
        1. 반응형 디자인과 동일한 구조넹ㅋㅋ크크ㅡ
        2. 특정 사이즈에 맞춰서 구조를 바꾸는건가
        3. constratintLayout state 파일을 만들어야한다.
        4. 모든 레이아웃이 다 포함되어야 한다.
        5. oncreat에서 어떤걸 전환할 건지에 대해 설정해야한다.
        6. 자세하게 알려주면 GitHub,co
    9. 멀티 디스플레이
        1. 최대 7개 화면까지도 지원이 가느
        2. Android 5 이후의 버전으로 display default를 설정하지 말아야한다.
        3. 하지말아아ㅑ함
4. 베스트 케이스
    1. 안드로이드 스튜디오에서 크롬 os애뮬레이터 테스트 가능--------
    2. usb를 통해 adb 디버깅이 가능.
    3. 리눅스가 크롬북에서 돌아감
    4. Chrome안에 android . linux가 돌아갈 수 있다.
    5. 리눅스와 Android 를 연결할 수 있다.