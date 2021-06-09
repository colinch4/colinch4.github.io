---
layout: post
title: "[디자인패턴] Decorator 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Decorator 패턴
--------------

-	스펀지 케이크와 같이 중심이 되는 오프젝트가 있을 때 이 오브젝트에 장식이 되는 기능을 하나씩 추가하면서 좀더 목적에 맞는 오브젝트를가 완성된다. 이와 같이 오브젝트에 장식을 해 나가는 디자인 패턴을 `Decorator 패턴`이라고 한다.
-	Decorator 패턴에서는 장식도 내용물도 공통의 인터페이스(API)를 가진다. 인터페이스(API)는 공통이지만, 장식하면 장식할수록 기능이 추가된다. 즉, 내용물은 변경하지 않고 기능을 추가할 수 있다.
-	Decorator 패턴에서는 위임을 사용한다. '장식'에 대한 요구(메소드 호출)는 그 '내용물'에 떠넘겨(위임)진다.
-	Decorator 패턴과 Composite 패턴은 재귀적인 구조를 취하는 점에서는 유사하지만 목적이 다르다. Decorator 패턴은 테두리 장식을 중복해서 기능을 추가해가는 것에 중안점은 둔다.

-	Decorator 패턴의 등장인물

	-	Component의 역할
		-	기능을 추가할 때 핵심이 되는 역할이다. 서두의 케이크에 비교하면 장식하기 전의 스펀지 케이크에 해당한다. Component 역할은 스펀지 케이크의 인터페이스만을 결정한다.
	-	ConcreteComponent의 역할
		-	Component 역할의 인터페이스를 구현하고 있는 구체적인 스펀지 케이크이다. 예제 프로그램에서는 StringDisplay 클래스가 이 역할을 한다.
	-	Decorator(장식자)의 역할
		-	Component 역할과 동일한 인터페이스를 가지며, 또한 이 Decorator 역할이 장식할 대상이 되는 Component 역할도 가진다. 이 역할은 자신이 장식하고 있는 대상을 알고 있다. 예제 프로그램에서는 Border 클래스가 이 역할을 한다.
	-	ConcreteDecorator(구체적인 장식자)의 역할
		-	구체적인 Decorator의 역할이다. 예제 프로그램에서는 SideBorder 클래스와 Fullborder 클래스가 이 역할을 한다.

![Decorator 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzSWJ4Rm93aml2NEk)

-	예제

![Decorator 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzSFMzUnFfVXJOdTg)

```java
public class Main {
    public static void main(String[] args) {
        Display b1 = new StringDisplay("Hello, world.");
        Display b2 = new SideBorder(b1, '#');
        Display b3 = new FullBorder(b2);
        b1.show();
        b2.show();
        b3.show();
        Display b4 =
                    new SideBorder(
                        new FullBorder(
                            new FullBorder(
                                new SideBorder(
                                    new FullBorder(
                                        new StringDisplay("안녕하세요")
                                    ),
                                    '*'
                                )
                            )
                        ),
                        '/'
                    );
        b4.show();
    }
}

public abstract class Display {
    public abstract int getColumns();               // 가로의 문자수를 얻는다.
    public abstract int getRows();                  // 세로의 줄수를 얻는다.
    public abstract String getRowText(int row);     // row번째의 문자열을 얻는다.
    public final void show() {                      // 전부 표시한다.
        for (int i = 0; i < getRows(); i++) {
            System.out.println(getRowText(i));
        }
    }
}

public abstract class Border extends Display {
    protected Display display;          // 장식이 감싸고 있는 "내용물"을 가리킨다.
    protected Border(Display display) { // 인스턴스 생성시에 "내용물"을 인수로 지정
        this.display = display;
    }
}

public class StringDisplay extends Display {
    private String string;                          // 표시문자열
    public StringDisplay(String string) {           // 인수로 표시문자열을 지정
        this.string = string;
    }
    public int getColumns() {                       // 문자수
        return string.getBytes().length;
    }
    public int getRows() {                          // 줄수는 1
        return 1;
    }
    public String getRowText(int row) {             // row가 0일때만 반환한다.
        if (row == 0) {
            return string;
        } else {
            return null;
        }
    }
}

public class FullBorder extends Border {
    public FullBorder(Display display) {
        super(display);
    }
    public int getColumns() {                   // 문자수는 내용물의 양쪽에 좌우의 장식 문자분을 더한 것
        return 1 + display.getColumns() + 1;
    }
    public int getRows() {                      // 줄수는 내용물의 줄수에 상하의 장식문자분을 더한 것
        return 1 + display.getRows() + 1;
    }
    public String getRowText(int row) {         // 지정한 줄의 내용
        if (row == 0) {                                                 // 장식의 상단
            return "+" + makeLine('-', display.getColumns()) + "+";
        } else if (row == display.getRows() + 1) {                      // 장식의 하단
            return "+" + makeLine('-', display.getColumns()) + "+";
        } else {                                                        // 그 밖에
            return "|" + display.getRowText(row - 1) + "|";
        }
    }
    private String makeLine(char ch, int count) {         // 문자ch를 count개 연속시킨 문자열을 만든다.
        StringBuffer buf = new StringBuffer();
        for (int i = 0; i < count; i++) {
            buf.append(ch);
        }
        return buf.toString();
    }
}

public class SideBorder extends Border {
    private char borderChar;                        // 장식이 되는 문자
    public SideBorder(Display display, char ch) {   // 생성자에서 Display와 장식문자
        super(display);
        this.borderChar = ch;
    }
    public int getColumns() {                       // 문자수는 내용물의 양쪽에 장식 문자분을 더한 것
        return 1 + display.getColumns() + 1;
    }
    public int getRows() {                          // 줄수는 내용물의 줄수와 같음
        return display.getRows();
    }
    public String getRowText(int row) {             // 지정한 줄의 내용은 내용물의 지정 줄의 양쪽에 장식문자를 붙인 것
        return borderChar + display.getRowText(row) + borderChar;
    }
}

```
