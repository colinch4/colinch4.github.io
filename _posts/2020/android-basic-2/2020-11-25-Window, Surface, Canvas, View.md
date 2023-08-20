---
layout: post
title: "[안드로이드] Window, Surface, Canvas, View"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---

## 안드로이드에서 뷰가 그려지는 과정
  
  
  안드로이드에서 UI를 렌더링하기 위한 여러 개념들이 있는데 window, surface, canvas, view 가 있다.
  
  각 요소들의 크기는 Window > Surface > Canvas > View 순이다.
  
  
  ## Window
  
  하나의 화면 안에서는 여러개의 Window를 가질 수 있고, 이러한 Window들은 WindowManager가 관리를 합니다.
  
  Window는 뭔가를 그릴 수 있는 창이며, 보통 하나의 Surface를 가지고 있습니다. 어플리케이션은 WindowManager와 상호작용하여
  
  Window를 만들어내고 각각의 Window 표면에 그리기 위해 Surface를 만듭니다.
  
  일반적으로 Activity가 window를 가지게 됩니다.
  
  
  ## Surface
  
  Surface는 화면에 합성되는 픽셀을 보유한 객체입니다. 화면에 표시되는 모든 Window는 자신만의 Surface가 포함되어 있으며,
  
  Surface Flinger가 여러 소스로부터 그래픽 데이터 버퍼를 받고, 그것들을 합성해서 Display로 보냅니다.
  
  개별 Surface는 이중 버퍼 렌더링을 위한 1개 이상 (보통 2개)의 버퍼를 가집니다.
  
  
  #### 이중 버퍼 렌더링?
  
  - 스크린에 출력될 화면 데이터는 **프레임 버퍼**에 저장되는데, 하나의 버퍼만 가지는 경우 이미지가 반복해서 그려지게 되거나, 이미지가 다 그려지지 않아도
    화면 주사율 때문에 렌더링을 해야할 때, 다 그려지지 않은 프레임 버퍼가 렌더링이 되어서 이미지가 깜빡이는 Flicker 현상이 나타날 수 있습니다.
    이를 해결하기 위해 프레임 버퍼에 바로 렌더링 하지 않고, 다른 버퍼를 만들어서 그 버퍼에 렌더링을 완료 하고, 다음 프레임 버퍼에 옮기는 방식을 사용하여 Flicker 현상을 해결할 수 있습니다.
  
  
  ## Canvas
  
  실제 UI를 그리기 위한 공간으로 비트맵이 그려지는 공간이다.
  
  
  ## View
  
  View는 Window 내부의 대화식 UI요소입니다. Window에는 단일 뷰 계층 구조가 연결되어 있으며 모든 Window의 동작을 제공합니다.
  
   Window가 다시 뭔가를 그려야할때마다 Window의 Surface에서 작업이 수행됩니다. 만약 Surface가 잠기면 그리는데 사용할 수 있는
   
   Canvas가 반환이 되니다. 그럼 Draw Traversal로 인해 각 뷰를 계층적으로 Canvas에 전달하여 UI를 그리기 시작합니다.
  
   완료가 되면 Surface가 잠기고 방금 그린 Buffer가 포그라운드 상태로 바뀌고 Surface Flinger에 의해서 화면에 합성됩니다.
   
   
  ## SurfaceView
  
  기존의 뷰를 상속받으며, 그래픽처리가 빠른 View 이다.
  
  일반적인 View는 Main Thread에서 캔버스를 그리기 때문에, 그리기를 하는 동안에는 사용자의 입력을 받을 수 없고 그로 인해 반응성이 좋지 못합니다.
  
  그렇다고 그리는 작업을 작업 스레드에서 하고 싶어도 안드로이드 정책상 main thread 이외에서는 할 수가 없습니다.
  
  이때 사용하는게 SurfaceView입니다.
  
  일반 view와 달리 그리기를 onDraw를 호출하는 것이 아닌 스레드를 이용해 강제로 화면에 그려버린다.
  
  SurfaceView는 Canvas가 아닌 Surface(= 가상 메모리 화면)에 그리고 그려진 Surface를 화면에 뿌리기 때문에 게임이나 카메라같은 
  
  높은 반응성이 필요한 UI 작업이 필요한 경우 사용할 수 있습니다.
  
  SurfaceView의 구조는 Surface와 SurfaceHolder 로 구성되며, SurfaceHolder가 Surface에 미리 그리고, 이 Surface가 SurfaceView에 반영하는 구조입니다.
  
  
  ## View와 ViewGroup
  
  안드로이드에서 UI요소들은 크게 View와 ViewGroup으로 이루어져 있으며, 아래와 같은 특징이 있습니다.
  
  - View 는 화면상의 UI를 구성합니다.
  - ViewGroup은 ViewGroup와 View를 포함합니다. (디렉토리처럼)
  - TextView 같은 기본적인 화면 구성요소들은 View에 상속되어 구현됩니다.
  - 개별적으로 속성을 가지며, 개별 속성은 Parent로부터 상속 받을 수 있습니다.
  - View는 Window의 Surface를 이용하여 화면을 그리고, 이벤트를 어떻게 처리할지에 대한 구현을 하는 객체입니다.
  
  
  ## Layout이 그려지는 과정
  
  안드로이드에서는 액티비티가 포커스를 얻게 되면 자신의 Layout을 그리게 됩니다.
  이때 그리고자 하는 Layout의 Root Node를 요청하게 되는데, 우리가 setContentView()를 호출할 때 Root Node가 정해집니다.
  
  ```
   override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(com.empo.android.empoapp.R.layout.activity_main) // 루트 노드가 정해진다.

    }
  ```
  
  Root Node가 결정이 되면 Root Node를 따라 Child Node를 찾아가면서 차례대로 View를 그리게 됩니다.
  
  Layout을 그리는건 아래 과정을 통해 **측정**과 **순서**란 과정을 거치게 됩니다.
  
  ```
  measure() -> onMeasure() -> layout() -> onLayout()
  ```
  
  1. measure(widthMeasureSpec: Int, heightMeasureSpec : Int): 뷰의 크기를 알아내기 위해 호출되며, 실제 크기 측정을 위해 onMeasure()를 호출합니다.
  각 부모들은 measure를 한번 이상 호출하여 자식들의 사이즈를 알아내거나 부모가 정합니다.
  
   - widthMeasureSpec : Parent가 부여한 필요한 가로공간
   - heightMeasureSpec : Parent가 부여한 필요한 세로공간
   
   
  2. onMeasure(widthMeasureSpec:Int, heightMeasureSpec: Int): 실제 뷰의 크기를 측정합니다.
  
   - 각 파라미터는 위와 동일
  
  
  3. layout(left: Int, top: Int, right: Int, botton: Int): 뷰의 위치를 할당하기위해 onLayout을 호출합니다.
  
   - left : Parent에 대한 왼쪽 포지션
   - top : Parent에 대한 위쪽 포지션
   - right : Parent에 대한 오른쪽 포지션
   - bottom : Parent에 대한 하단 포지션
   
   
  4. onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) : 실제 뷰의 할당을 합니다.
   
   - changed: 새로운 사이즈나 위치인지 맞으면 True, 아니면 False
   - 나머진 위와 동일
  
  
  ## Custom View LifeCycle
  
  뷰가 생성이 되면 다음 순서대로 메소드들이 호출이 됩니다. View의 라이프사이클은 여러가지 이유로 공식적으로
  
  제공이 되지 않습니다. 다음 라이프 사이클은 널리 퍼져있는 라이프 사이클입니다.
  
  ```
  Constructor -> onAttachedToWindow() -> measure() -> onMeasure() -> layout() -> onLayout()
  
  -> dispatchDraw() -> draw() -> onDraw()
  ```
  
  이때 onDraw이루 invalidate()가 호출되면 다시 dispatchDraw() 부터 다시 호출되며,
  requestLayout()가 호출되면 measure() 부터 다시 호출된다.
  
  1. Constructor
  
   - CustomView(context: Context) : 코드로 생성하면 호출
   - CustomView(context: Context, attributeSet:AttributeSet): xml로 생성하면 호출
    
  2. onAttachedToWindow: Parent View가 addView(view: View)를 호출하면 해당 View가 window에 연결됩니다.
    이 단계 부터 id를 통해 접근 할 수 있습니다.
    
  3. onMeasure : View의 사이즈 측정
  
     1. ViewGroup.MeasureSpec : 부모 뷰에서 자식 뷰로 요구사항을 보내기 위해 사용
      - MeasureSpec.EXACTLY : 직접적으로 width와 height에 대해 하드코딩할 때 사용
      - MeasureSpec.AT_MOST : 부모가 자식의 최대 사이즈를 설정하기 위해 사용
      - MeasureSpec.UNSPECIFIED: 부모에 의해 사용되며 제한이 없기 때문에 자식 View가 원하는 사이즈를 가질 수 있습니다.
        
        
     2. ViewGroup.LayoutParams : 자식 뷰가 부모 뷰에게 자신이 어떻게 측정되고 위치를 정할지 요청하는데 사용
      - 정확한 수치 (50dp, 100dp ...)
      - MATCH_PARENT : 자신의 부모만큼 크기를 원함
      - WRAP_CONTENT : 자신의 내용물을 담을 수 있을 만큼만 크기를 원함. padding 포함
      
  4. onLayout: 개별 자식 뷰들의 사이즈 및 위치 할당
  5. onDraw : 뷰를 그리기 시작한다. Canvas와 Paint를 사용하여 그리기 시작하며, Canvas는 모양을 그리고 Paint는 색을 칠합니다.
  
  
  ## View Update
  
  뷰의 업데이트는 두 함수를 통해서 이루어 집니다.
  
  invalidate() : View에 변화가 생겨서 다시 그려야 할때 (dispatchDraw 부터)
  requestLayout(): View를 처음부터 그려야 할때 (measure 부터)
  
  
  ## Animation
  
  View의 애니매이션은 frame 단위로 View에 애니메이션으로 변화가 있을때마다 invalidate를 호출하여 뷰를 그립니다. 대표적으로 애니매이션을 사용하는 클래스는 ValueAnimator 입니다.
  
  
  
  
  
