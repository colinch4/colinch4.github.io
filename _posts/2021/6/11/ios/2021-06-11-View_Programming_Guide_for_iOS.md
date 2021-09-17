---
layout: post
title: "[ios] View Programming Guide for iOS 번역"
description: " "
date: 2021-06-11
tags: [ios]
comments: true
share: true
---

# View Programming Guide for iOS 번역

출처 : <https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503-CH1-SW2>

## 뷰들은 당신의 앱의 시각적 내용을 담당합니다. 

뷰는 **UIView 클래스 ( 혹은 이것의 서브클래스 중 하나 ) 의 인스턴스**이고 그리고 당신의 앱 창(window) 안에서 **사각형 구역**을 담당한다. 뷰들은 내용을 그리고, 다수의 터치 이벤트를 다루고, 어떠한 서브 뷰의 레이아웃을 관리하는 것에 책임이 있습니다. 
드로잉에는 Core Graphics, OpenGL ES 또는 UIKit과 같은 그래픽 기술을 사용하여 뷰의 사각형 영역 안에 모양, 이미지 및 텍스트를 그리는 작업이 포함됩니다.
뷰는 제스처 인식기를 사용하거나 터치 이벤트를 직접 처리하여 **자신의 직사각형 영역의 터치 이벤트에 응답합니다.** 
뷰 계층에서 상위 뷰는 하위 뷰의 위치를 ​​지정하고 크기를 조정하는 역할을하며 동적으로 수행 할 수 있습니다. ( 동적이다 => 프로그램 돌아갈 때 )
하위 뷰를 동적으로 수정하는 기능을 통해 인터페이스 rotations 및 animations와 같은 변화하는 조건에 맞게 당신의 뷰를 조정할 수 있습니다.

뷰는 당신이 사용자 인터페이스를 구성하는 데 사용하는 빌딩 블록(building block)으로 생각할 수 있습니다. 
하나의 뷰를 사용하여 모든 컨텐츠를 표시하는 대신 여러 뷰를 사용하여 뷰 계층 구조(view hierarchy)를 작성하는 경우가 많습니다.  계층 구조의 각각의 뷰는 당신의 user interface의 특정한 부분을 나타내고 그리고 이것은 일반적으로 콘텐츠의 특정한 타입을 위해 최적화 되어 있습니다. (계층 구조라... 애매하다 다시 한번 확인해보자)
예를 들어, UIKit는 이미지, 또는 텍스트, 혹은 콘텐츠의 기타 타입을 나타내기 위한 뷰들을 가지고 있습니다.

## 창은 당신의 뷰들이 보여지는 것을 조정한다. 

**window는 UIWindow 클래스의 인스턴스이고** 그리고 당신의 앱의 유저 인터페이스의 전체적인 보여주기를 다룬다. window들은 뷰들과 함께 동작하며( 및 그들 자체의 뷰 컨트롤러와 ), 눈에 보이는 뷰 계층과의 상호작용 및 변경사항을 관리(담당)합니다. 
**대부분의 경우, 당신의 앱의 창들을 절대 변하지 않습니다.**
window가 생성된 이후에, 이것은 같음을 유지하고 그리고 오직 뷰들만이 변화됩니다.
모든 앱들은 적어도 하나의 window가 장치(핸드폰 or 아이패드) 에 대한 앱의 유저 인터페이스를 나타냅니다. 
외부 display가 장치에 연결된 경우 앱은 해당 화면에 내용을 표시하는 **두 번째 window**을 만들 수 있습니다. 

## 애니메이션들은 인터페이스의 변화에 대한 눈에 보이는 피드백을 사용자들에게 제공한다.  

애니메이션들은 당신의 뷰 계층에 대한 변화에 대해 눈에 보이는 피드백을 사용자들에게 제공합니다. 
시스템은 모달(modal) 뷰들을 나타내고 뷰들간 서로 다른 그룹 사이에 전환(transitioning)하는데 표준 애니메이션들을 정의한다. 
그러나, 뷰의 많은 속성들이 직접 애니메이션 될 수도 있다. 
예를 들어 애니메이션을 통해 뷰의 투명도, 화면에서의 위치, 크기, 배경색 또는 기타 특성을 변경할 수 있습니다. 
뷰의 기본 Core Animation 레이어 객체로 직접 작업하면 다른 많은 애니메이션도 수행 할 수 있습니다.

## 인터페이스 빌더의 역할 

Interface Builder는 응용 프로그램의 window와 view를 그래픽적으로 구성하고 설정하는데 사용하는 편집기입니다.( configure : To set up or arrange something in such a way that it is ready for operation for a particular purpose, or to someone's particular liking) ( construct : Something constructed from parts.)
<br>Interface builder를 사용해서, 당신은 당신의 뷰들을 어셈블하고 nib 파일에 배치할 수 있습니다. nib 파일은 동결 건조된(freeze-dried) 뷰 및 기타 객체의 버전을 저장하는 리소스 파일입니다.
(nib 파일은 iOS 및 Mac 앱의 사용자 인터페이스를 저장하는 데 사용하는 특수 유형의 리소스 파일입니다. nib 파일은 Interface Builder 문서입니다 from apple document)
<br> 당신이 nib file을 런타임 시간에 로드할 때, nib file 안의 객체들은 코드로 프로그래밍적으로 조작할 수 있는 실제적인 객체로 재구성되어 집니다. 


interface builder는 당신이 당신의 앱의 user inferface을 만드는데 해야 하는 당신의 일들을 매우 단순화 합니다. 왜냐하면 interface Builder 편집기와 nib 파일을 위한 지원이 ios를 통틀어서 통합되어 있기 때문에, 당신의 앱 디자인 안에 nib file들을 통합하는데 적은 노력만이 요구되어 집니다.   


# View and Window Architecture
 
시스템 뷰를 사용하든 커스텀 뷰를 생성해서 작성하든, 당신은 **UIView 및 UIWindow 클래스가 제공하는 인프라를 이해해야합니다.이 클래스는 뷰의 보기 및 레이아웃을 관리하기위한 정교한 기능을 제공합니다.**
**이러한 기능이 작동하는 방식을 이해하는 것**은 애플리케이션에서 변경이 발생할 때 뷰가 올바르게 작동하도록 하는데 중요합니다.

## 뷰 아키텍쳐 기본들

시각적으로 할 수있는 대부분의 작업은 뷰 객체(UIView 클래스의 인스턴스 인)를 사용하여 수행됩니다. 
뷰 객체는 화면에서 **직사각형 영역을 정**의하고 해당 영역의 드로잉 및 터치 이벤트를 처리합니다.
뷰는 다른 뷰의 상위 뷰 역할(parent)을하고 해당 뷰(child view)의 배치 및 크기 조정을 조정할 수도 있습니다.
UIView 클래스는 뷰 간 이러한 관계를 관리하는 작업을 대부분 수행하지만 필요에 따라 기본 동작을 사용자 정의(customizing) 할 수도 있습니다.

뷰는 Core Animation layers와 함께 작동하여 뷰 컨텐츠의 렌더링 및 애니메이션을 처리합니다.
UIKit 안의 모든 뷰는 레이어 객체(일반적으로 CALayer 클래스의 인스턴스)에 의해 지원됩니다, 레이어 객체란 뷰의 백업 저장소를 관리하고 뷰와 관련된 애니메이션들을 처리하는(다루는) 녀석입니다.   
뷰와 관련되어 수행하는 대부분의 작업들은 UIView 인터페이스를 통해 수행되어야 합니다. 
하지만, 뷰의 애니메이션 또는 랜더링과 관련되어 더 많은 control이 필요한 상황에서, 당신은 뷰의 레이어를 대신 작업들을 수행할 수 있습니다. 

For simplicity, and because that view is usually hidden, it is not included in Figure 1-1.) Every view has a corresponding layer object that can be accessed from that view’s layer property. (Because a bar button item is not a view, you cannot access its layer directly.) Behind those layer objects are Core Animation rendering objects and ultimately the hardware buffers used to manage the actual bits on the screen.

=> 그냥 레이어 객체라는 것이 있고 **뷰 컨텐츠의 렌더링과 애니메이션**과 관련되어 뷰들과 연결되어 있다는 정도만 알고 있자. 
<br>렌더링 == 처리

**Core Animation 레이어 객체를 사용하면 성능에 중요한 영향**을 미칩니다. 
뷰 객체의 실제 드로잉 코드는 가능한 한 적게 호출되며(called), **코드가 호출되면 결과는 Core Animation에 의해 캐시되어 나중에 최대한 많이 재사용됩니다.**
이미 렌더링된 컨텐츠를 재사용하는 것은 뷰를 업데이트 하는데 보통 필요한 값 비싼 드로잉 주기를 제거합니다. => (뷰의 변화를 표현하는 데 많은 비용을 줄일 수 있다.)
<br>콘텐츠의 재사용은 기존의 콘텐츠를 조작할 수 있는 애니메이션 활동 동안에 특히 중요합니다.
**이러한 재사용은 새로운 컨텐츠를 생성하는 것보다 훨씬 저렴합니다!**

## View Hierarchies and Subview Management

자체 컨텐츠를 제공하는 것 외에도 뷰는 다른 뷰의 컨테이너 역할을 할 수 있습니다. 한 뷰에 다른 뷰가 포함 된 경우 두 뷰 사이에 부모-자식 관계가 생성됩니다.
이 관계에서 자식 뷰를 subview라고 부르고 그리고 부모 뷰를 superview라고 부릅니다. 이 관계 유형의 생성은 앱의 시각적 모양과 앱의 동작 둘 다에 영향을 끼칩니다.

시각적으로, 한 subview 의 콘텐츠는 부모 뷰의 콘텐츠의 일부이거나 전부를 가립니다. 만약에 subview가 100% 불투명하다면, subview에 의해 차지하는 영역은 그에 해당하는 부모 뷰의 영역을 가립니다. 

If the subview is partially transparent, the content from the two views is blended together prior to being displayed on the screen. Each superview stores its subviews in an ordered array and the order in that array also affects the visibility of each subview.

하위 뷰가 부분적으로 투명하면 두 뷰의 내용이 화면에 표시되기 전에 함께 혼합됩니다. 
각각의 superview는 자신의 subview를 정렬된 배열에 저장하고 그리고 배열의 순서 역시 각각 subview의 비주얼에 영향을 미칩니다. 

만약 두 개의 형제(sibling) subview가 서로 겹치는 경우, 마지막에 추가된 (또는 subview 배열의 끝으로 이동 한) 하나가 다른 것 위에 나타납니다. => 마지막에 있는 놈이 제일 위에 나타난다는 뜻.
<br>super view-subview 관계는 또한 여러개의 뷰 동작에 영향을 줍니다. 
상위 뷰의 크기를 변경하면 잔물결 효과(a ripple effect)가 있어 하위 뷰의 크기와 위치도 변경 될 수 있습니다.
상위 뷰의 크기를 변경할 때, 각 하위 뷰를 상위 뷰에서 적절히 설정(configure)하여 각 하위 뷰의 크기를 조정하는 동작을 제어 할 수 있습니다. => autolayout 등등.
<br>subview에 영향을주는 다른 변경으로는 superview 숨기기, superview의 알파 (투명도) 변경 또는 superview의 좌표계에 수학적 변환 적용이 있습니다.

뷰 계층 안에서의 뷰들의 정렬은 어떻게 너의 어플리케이션이 이벤트들에 반응해야 하는지도 결정합니다. 
터치가 특정한 뷰 안에서 일어날 때, 시스템은 해당 터치를 처리하기 위해 터치 정보가 있는 이벤트 객체(event object)를 해당 뷰로 직접(directly) 보냅니다(sends).
그러나, 만약 뷰가 특정한 터치 이벤트를 처리하지 않으면, 이벤트 객체를 superview로 전달 할 수 있습니다. 
만약 superview도 그 이벤트를 처리하지 않으면, superview의 superview에게 이벤트 객체를 전달하는 방식으로 응답자 체인이 위로 올라갑니다. 
특정 뷰는 이벤트 객체를 뷰 컨트롤러와 같은 중간 응답자 객체로 전달할 수도 있습니다. 
객체가 이벤트를 처리하지 않으면 결국 어플리케이션 객체에 도달하여 **일반적으로 삭제**(최종적으로 처리 안되면 맨 위의 앱 객체가 결국 삭제한다)합니다.

## The View Drawing Cycle

The UIView class uses an **on-demand drawing model(주문형 드로잉 모델)** for presenting content. When a view first appears on the screen, the system asks it to draw its content.(=> system이 demand 하는 것) The system captures a snapshot of this content and uses that snapshot as the view’s visual representation. If you never change the view’s content, the view’s drawing code may never be called again. The snapshot image is reused for most operations involving the view.(core animation layer 가 캐싱하겠지) If you do change the content, you **notify** the system that the view has changed. The view then repeats the process of drawing the view and capturing a snapshot of the new results.

When the contents of your view change, you do not redraw those changes directly. Instead, you invalidate the view using either the setNeedsDisplay or setNeedsDisplayInRect: method. These methods tell the system(시스템이 controller를 말하는 것인가?) that the contents of the view changed and need to be redrawn at the next opportunity. The system waits until the end of the current run loop before initiating any drawing operations. This delay gives you a chance to invalidate multiple views, add or remove views from your hierarchy, hide views, resize views, and reposition views all at once.(=> 마치 버퍼링과 같다. 오버헤드를 줄여준다.) All of the changes you make are then reflected at the same time.

Note: Changing a view’s geometry does not automatically cause the system to redraw the view’s content. The view’s contentMode property determines how changes to the view’s geometry are interpreted. Most content modes stretch or reposition the existing snapshot within the view’s boundaries and do not create a new one. For more information about how content modes affect the drawing cycle of your view, see Content Modes.

뷰의 컨텐츠를 렌더링 할 때가되면 실제 드로잉 프로세스는 뷰와 뷰의 설정에 따라 다릅니다.
System views typically implement private drawing methods to render their content. Those same system views often expose interfaces that you can use to configure the view’s actual appearance. For custom UIView subclasses, you typically override the drawRect: method of your view and use that method to draw your view’s content. There are also other ways to provide a view’s content, such as setting the contents of the underlying layer directly, but overriding the drawRect: method is the most common technique.

For more information about how to draw content for custom views, see Implementing Your Drawing Code.

## Windows (UIWindow는 UIView의 sub class 이다.)

Every iOS application needs at least one window—an instance of the UIWindow class—and some may include more than one window. 

A window object has several responsibilities:

* It contains your application’s visible content.
* It plays a **key role** in the delivery of touch events to your views and other application objects.
* It works with your application’s view controllers to facilitate orientation changes.

In iOS, windows do not have title bars, close boxes, or any other visual adornments. A window is always just a blank container for one or more views. Also, applications do not change their content by showing new windows. When you want to change the displayed content, you change the frontmost views of your window instead.

Most iOS applications create and use only one window during their lifetime. This window spans the entire main screen of the device and is loaded from the application’s main nib file (or created programmatically) early in the life of the application. However, if an application supports the use of an external display for video out, it can create an additional window to display content on that external display. All other windows are typically created by the system, and are usually created in response to specific events, such as an incoming phone call.

## Tasks That Involve Windows
## 윈도우와 관련된 일들 

많은 응용 프로그램의 경우 응용 프로그램이 창과 상호 작용하는 유일한 시간은 시작시 창을 만드는 것입니다.
그러나 응용 프로그램의 창 객체를 사용하여 몇 가지 응용 프로그램 관련 작업을 수행 할 수 있습니다.

* 창 객체를 사용하여 점과 사각형을 **창의 로컬 좌표계와 변환**합니다.
<br>예를 들어, 창 좌표에 값이 제공되면 사용하기 전에 특정 뷰의 좌표 시스템으로 변환 할 수 있습니다. 좌표를 변환하는 방법에 대한 자세한 내용은 뷰 계층 구조에서 좌표 변환을 참조하십시오.
<br>=> window는 해당 위치의 점이나 사각형을 좌표 값으로 변환하는 기능을 한다. 

* 창 알림(notification)을 사용하여 창 관련 변경 사항을 추적하십시오.

Windows는 표시되거나 숨겨지거나() 키 상태를 수락(accept)하거나 사임할(resign) 때 **알림(notification)** 을 생성합니다. 
이 **알림(notification)**을 사용하여 응용 프로그램의 다른 부분에서 작업을 수행 할 수 있습니다. 자세한 내용은 창 변경 모니터링을 참조하십시오. => 알림이 뭐야... ㅡㅡ

## Creating and Configuring a Window
## Window 를 만들고 설정하기

프로그래밍 방식으로 또는 Interface Builder를 사용하여 응용 프로그램의 기본 창을 만들고 설정(configure)할 수 있습니다.
두 경우 모두 시작 시(at launch time) Window을 작성하고 이를 유지하고 **애플리케이션 Delegate 객체에게 창에 대한 참조를 저장해야합니다.** => Window가 구체적으로 무엇인지 물어보자... 힌트 : 창은 눈에 보이지 않는다. 
앱이 추가 창을 만드는 경우 추가 창이 필요할 때 느리게(lazily) 창을 만들도록 합니다. 
<br>예를 들어, 응용 프로그램이 외부 디스플레이에 내용 표시를 지원하는 경우 해당 창을 만들기 전에 디스플레이가 연결될 때까지 기다려야합니다.

## Creating Windows in Interface Builder
## Interface Builder 에서 Window 만들기 

Xcode 프로젝트 템플릿이 기본 Window를 직접 작성하기 때문에 Interface Builder를 사용하여 애플리케이션의 기본 Window을 만드는 것은 간단합니다.

In addition, these templates also define an outlet for that window in the application delegate object. You use this outlet to access the window object in your code.

게다가, Xcode 템플릿은 앱의 delegate 객체 안에서 이 창에 대한 outlet을 정의합니다. 당신은 이 outlet을 이용하여 당신의 코드에서 window 객체에 접근할 수 있습니다. 

중요 사항 : Interface Builder에서 창을 작성할 때 속성 관리자에서 시작시 전체 화면 옵션을 사용하는 것이 좋습니다.
이 옵션을 사용하지 않고 창이 대상 장치의 화면보다 작은 경우 일부보기에서 터치 이벤트가 수신되지 않습니다. 모든 뷰와 같이 창은 경계 사각형 외부에서 터치 이벤트를 수신하지 않기 때문입니다. (=> 뷰들의 터치 이벤트를 담당하는 것이 window이다.)

## Content modes

Each view has a content mode that controls how the view recycles its content in response to changes in the view’s geometry and whether it recycles its content at all.(콘텐츠의 재활용 여부를 판단함) When a view is first displayed, it renders its content as usual and the results are captured in an underlying bitmap. After that, changes to the view’s geometry do not always cause the bitmap to be recreated. Instead, the value in the contentMode property determines whether the bitmap should be scaled to fit the new bounds or simply pinned to one corner or edge of the view.

The content mode of a view is applied whenever you do the following:

* Change the width or height of the view’s frame or bounds rectangles.
* Assign a transform that includes a scaling factor to the view’s transform property.

**By default, the contentMode property for most views is set to UIViewContentModeScaleToFill**, which causes the view’s contents to be scaled to fit the new frame size. Figure 1-2 shows the results that occur for some content modes that are available. As you can see from the figure, not all content modes result in the view’s bounds being filled entirely, and those that do might distort the view’s content.

Content modes are good for recycling the contents of your view, but you can also set the content mode to the UIViewContentModeRedraw value when you specifically want your custom views to redraw themselves during scaling and resizing operations. Setting your view’s content mode to this value forces the system to call your view’s drawRect: method in response to geometry changes. In general, you should avoid using this value whenever possible, and you should certainly not use it with the standard system views.

## Stretchable Views

You can designate a portion of a view as stretchable so that when the size of the view changes only the content in the stretchable portion is affected. You typically use stretchable areas for buttons or other views where part of the view defines a repeatable pattern. The stretchable area you specify can allow for stretching along one or both axes of the view. Of course, when stretching a view along two axes, the edges of the view must also define a repeatable pattern to avoid any distortion. Figure 1-3 shows how this distortion manifests itself in a view. The color from each of the view’s original pixels is replicated to fill the corresponding area in the larger view.

You specify the stretchable area of a view using the contentStretch property. This property accepts a rectangle whose values are normalized to the range 0.0 to 1.0. When stretching the view, the system multiplies these normalized values by the view’s current bounds and scale factor to determine which pixel or pixels need to be stretched. The use of normalized values alleviates the need for you to update the contentStretch property every time the bounds of your view change.

The view’s content mode also plays a role in determining how the view’s stretchable area is used. Stretchable areas are only used when the content mode would cause the view’s content to be scaled. This means that stretchable views are supported only with the UIViewContentModeScaleToFill, UIViewContentModeScaleAspectFit, and UIViewContentModeScaleAspectFill content modes. If you specify a content mode that pins the content to an edge or corner (and thus does not actually scale the content), the view ignores the stretchable area.

## View Geometry and Coordinate Systems

The default coordinate system in UIKit has its origin in the top-left corner and has axes that extend down and to the right from the origin point. Coordinate values are represented using floating-point numbers, which allow for precise layout and positioning of content regardless of the underlying screen resolution. Figure 1-4 shows this coordinate system relative to the screen. In addition to the screen coordinate system, **windows and views define their own local coordinate systems that allow you to specify coordinates relative to the view or window origin instead of relative to the screen.** (뷰와 윈도우도 각각의 로컬 좌표계를 가지고 았다고 한다. )

Because every view and window defines its own local coordinate system, you need to be aware of which coordinate system is in effect at any given time. Every time you draw into a view or change its geometry, you do so relative to some coordinate system. **In the case of drawing, you specify coordinates relative to the view’s own coordinate system. In the case of geometry changes, you specify coordinates relative to the superview’s coordinate system.**( 드로잉 할때랑, 위치 혹은 모양 잡을 때의 기준 좌표계가 다르다.) The UIWindow and UIView classes both include methods to help you convert from one coordinate system to another.

Important: Some iOS technologies define default coordinate systems whose origin point and orientation differ from those used by UIKit. 
For example, Core Graphics and OpenGLES use a coordinate system whose origin lies in the lower-left corner of the view or window and whose y-axis points upward relative to the screen. Your code must take such differences into account when drawing or creating content and adjust coordinate values (or the default orientation of the coordinate system) as needed.

## frame

The frame rectangle, which describes the view’s location and size **in its superview’s coordinate system.**

## bounds

The bounds rectangle, which describes the view’s location and size **in its own coordinate system.**

## Center 

The center property contains the known center point of the view in the superview’s coordinate system.

Although you can change the frame, bounds, and center properties independent of the others, changes to one property affect the others in the following ways:

* When you set the frame property, the size value in the bounds property changes to match the new size of the frame rectangle. The value in the center property similarly changes to match the new center point of the frame rectangle.

* When you set the center property, the origin value in the frame changes accordingly.

* When you set the size of the bounds property, the size value in the frame property changes to match the new size of the bounds rectangle.

By default, a view’s frame is not clipped to its superview’s frame. Thus, any subviews that lie outside of their superview’s frame are rendered in their entirety. You can change this behavior, though, by setting the superview’s clipsToBounds property to YES. Regardless of whether or not subviews are clipped visually, touch events always respect the bounds rectangle of the target view’s superview. In other words, touch events occurring in a part of a view that lies outside of its superview’s bounds rectangle are not delivered to that view.

