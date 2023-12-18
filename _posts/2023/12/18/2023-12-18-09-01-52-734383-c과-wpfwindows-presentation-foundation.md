---
layout: post
title: "[c#] C#과 WPF(Windows Presentation Foundation)"
description: " "
date: 2023-12-18
tags: [c#]
comments: true
share: true
---

## 소개

C#은 Microsoft에서 개발한 객체지향 프로그래밍 언어로, .NET Framework의 일부로 제공됩니다. WPF는 윈도우 응용프로그램의 사용자 인터페이스를 개발하기 위한 Microsoft의 플랫폼입니다. 이 문서에서는 C#으로 WPF를 사용하는 방법에 대해 살펴보겠습니다.

## WPF에서 UI 구성하기

WPF를 사용하면 XAML(Extensible Application Markup Language)을 사용하여 사용자 인터페이스를 디자인할 수 있습니다. XAML은 XML 기반의 마크업 언어로, UI 요소를 정의하고 배치하는 데 사용됩니다. 예를 들어, 다음은 간단한 버튼을 포함하는 XAML 예시입니다:

```xml
<Button Content="Click me" />
```

## C#에서 WPF 제어하기

C# 코드를 사용하여 WPF의 UI 요소를 제어할 수 있습니다. 예를 들어, 버튼을 클릭했을 때 메시지를 표시하는 이벤트 핸들러를 추가하는 방법은 다음과 같습니다:

```csharp
private void Button_Click(object sender, RoutedEventArgs e)
{
    MessageBox.Show("버튼이 클릭되었습니다.");
}
```

## 데이터 바인딩

WPF에서는 UI 요소와 데이터를 쉽게 바인딩할 수 있습니다. 이를 통해 데이터의 변경에 따라 UI가 자동으로 업데이트될 수 있습니다. 예를 들어, 다음은 데이터바인딩을 이용하여 텍스트 상자에 입력된 데이터를 보여주는 방법입니다:

```xml
<TextBox Text="{Binding Path=UserName, UpdateSourceTrigger=PropertyChanged}" />
```

```csharp
public string UserName { get; set; }
```

## 요약

C#을 사용하여 WPF를 개발하면 강력한 사용자 인터페이스를 구축할 수 있습니다. XAML을 사용하여 UI를 디자인하고, C# 코드를 사용하여 UI를 제어하고 데이터를 바인딩할 수 있습니다.

참고문헌:
- https://docs.microsoft.com/en-us/dotnet/desktop/wpf/getting-started/getting-started-with-wpf
- https://docs.microsoft.com/en-us/dotnet/csharp/