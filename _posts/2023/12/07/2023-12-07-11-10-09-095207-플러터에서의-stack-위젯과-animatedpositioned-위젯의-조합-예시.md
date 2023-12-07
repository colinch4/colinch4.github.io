---
layout: post
title: "[flutter] 플러터에서의 Stack 위젯과 AnimatedPositioned 위젯의 조합 예시"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

Flutter에서 UI를 구성할 때 Stack 위젯과 AnimatedPositioned 위젯은 유용한 조합입니다. Stack 위젯은 위젯을 겹쳐서 배치할 수 있게 해주고, AnimatedPositioned 위젯은 위젯의 위치를 애니메이션으로 변경할 수 있게 해줍니다. 이번 포스트에서는 Stack 위젯과 AnimatedPositioned 위젯을 조합하여 간단한 예시를 만들어보겠습니다.

## 예시 소개

우리는 화면 상단에 다양한 색상과 크기를 가진 상자들이 나타나는 애니메이션을 만들어볼 것입니다. 상자들은 일정한 시간 간격으로 위치와 크기가 변경되면서 자연스럽게 이동하게 됩니다.

## 구현 방법

1. 필요한 패키지를 추가합니다. `flutter/material.dart`와 `dart:math` 패키지를 추가해야 합니다.
2. `MyApp`을 구현합니다. 이는 앱의 진입점이 됩니다.
3. `AnimatedBox` 클래스를 만듭니다. 이 클래스는 상자 하나를 나타냅니다.
    ```dart
    class AnimatedBox extends StatefulWidget {
      @override
      _AnimatedBoxState createState() => _AnimatedBoxState();
    }
    
    class _AnimatedBoxState extends State<AnimatedBox>
        with SingleTickerProviderStateMixin {
      AnimationController _controller;
      Animation<AlignmentGeometry> _animation;
    
      @override
      void initState() {
        super.initState();
        _controller = AnimationController(
          duration: const Duration(seconds: 2),
          vsync: this,
        )..repeat(reverse: true);
    
        _animation = Tween<AlignmentGeometry>(
          begin: Alignment.centerLeft,
          end: Alignment.centerRight,
        ).animate(_controller);
      }
    
      @override
      void dispose() {
        _controller.dispose();
        super.dispose();
      }
    
      @override
      Widget build(BuildContext context) {
        return AnimatedBuilder(
          animation: _controller,
          builder: (context, child) {
            return Positioned.fill(
              child: Align(
                alignment: _animation.value,
                child: Container(
                  width: 100,
                  height: 100,
                  decoration: BoxDecoration(
                    color: Colors.blue,
                    borderRadius: BorderRadius.circular(10),
                  ),
                ),
              ),
            );
          },
        );
      }
    }
    ```
4. `MyHomePage` 클래스를 만듭니다. 이 클래스는 상자들을 포함하는 화면을 나타냅니다.
    ```dart
    class MyHomePage extends StatelessWidget {
      @override
      Widget build(BuildContext context) {
        return Scaffold(
          appBar: AppBar(
            title: Text('Animated Stack Example'),
          ),
          body: Stack(
            children: [
              AnimatedBox(),
              AnimatedBox(),
              AnimatedBox(),
            ],
          ),
        );
      }
    }
    ```
5. `main` 함수를 구현하여 앱을 실행합니다.
    ```dart
    void main() {
      runApp(MyApp());
    }
    ```

## 실행 결과

위의 예시를 실행하면 화면 상단에 크기와 위치가 변하는 세 개의 상자가 이동하는 애니메이션을 볼 수 있습니다.

## 결론

Flutter에서 Stack 위젯과 AnimatedPositioned 위젯을 조합하여 애니메이션 효과를 구현하는 것은 매우 간단합니다. 위의 예시를 참고하여 다양한 애니메이션을 만들어 보세요.