---
layout: post
title: "[c++] VTK (Visualization Toolkit) 설명"
description: " "
date: 2023-12-20
tags: [c++]
comments: true
share: true
---

VTK는 과학 및 공학 분야에서 사용되는 3차원 시각화 및 이미지 처리 소프트웨어 개발을 가능하게 하는 **오픈 소스 라이브러리**입니다. VTK는 데이터 시각화, 이미지 분석, 그리드 및 체적 계산, 그리고 가시화 관련 작업들을 위해 널리 사용됩니다.

## VTK의 기능

VTK는 다음과 같은 기능을 포함합니다:

- **다양한 데이터 유형 지원**: VTK는 구조화된 그리드, 비구조화된 그리드, 2D 및 3D 데이터, 이미지, 그리고 다른 유형의 과학 및 공학 데이터를 다루는 데 필요한 다양한 데이터 유형을 지원합니다.

- **시각화**: VTK는 복잡한 데이터를 시각적으로 이해하기 쉽도록 도와주는 강력한 시각화 도구를 제공합니다. 변형, 자르기, 색상 매핑, 및 그림자 효과 등 다양한 시각화 기능을 제공합니다.

- **이미지 처리**: VTK는 2D 및 3D 이미지 데이터를 처리 및 조작할 수 있는 다양한 도구와 알고리즘을 제공하여, 이미지 분석 및 처리 작업을 지원합니다. 

- **다양한 플랫폼 지원**: VTK는 Windows, macOS, Linux 등 다양한 운영 체제에서 동작하며, C++, Python, Java, 및 Tcl/Tk 등 다양한 프로그래밍 언어로 사용할 수 있습니다.

## VTK 사용 예시

다음은 VTK를 사용하여 간단한 3D 시각화를 수행하는 C++ 코드의 예시입니다.

```c++
#include <vtkSmartPointer.h>
#include <vtkXMLPolyDataReader.h>
#include <vtkPolyDataMapper.h>
#include <vtkActor.h>
#include <vtkRenderWindow.h>
#include <vtkRenderer.h>
#include <vtkRenderWindowInteractor.h>

int main() {
    // 파일에서 PolyData를 읽어옴
    vtkSmartPointer<vtkXMLPolyDataReader> reader =
        vtkSmartPointer<vtkXMLPolyDataReader>::New();
    reader->SetFileName("input.vtp");
    reader->Update();

    // Mapper 및 Actor 생성
    vtkSmartPointer<vtkPolyDataMapper> mapper =
        vtkSmartPointer<vtkPolyDataMapper>::New();
    mapper->SetInputConnection(reader->GetOutputPort());
    vtkSmartPointer<vtkActor> actor = vtkSmartPointer<vtkActor>::New();
    actor->SetMapper(mapper);

    // Renderer, RenderWindow, 및 Interactor 생성
    vtkSmartPointer<vtkRenderer> renderer = vtkSmartPointer<vtkRenderer>::New();
    vtkSmartPointer<vtkRenderWindow> renderWindow = vtkSmartPointer<vtkRenderWindow>::New();
    renderWindow->AddRenderer(renderer);
    vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor =
        vtkSmartPointer<vtkRenderWindowInteractor>::New();
    renderWindowInteractor->SetRenderWindow(renderWindow);

    // Actor를 Renderer에 추가하고 시각화
    renderer->AddActor(actor);
    renderer->SetBackground(0, 0, 0);  // 배경 색상 설정
    renderWindow->Render();
    renderWindowInteractor->Start();

    return 0;
}
```

## 마치며

VTK는 다양한 과학 및 공학 분야에서 3차원 시각화 및 이미지 처리 작업을 수행하는 데 매우 유용한 도구입니다. 사용자는 VTK를 통해 복잡한 데이터를 시각적으로 표현하고 분석하는 일에 활용할 수 있습니다.

[참조: VTK 공식 홈페이지](https://vtk.org/)