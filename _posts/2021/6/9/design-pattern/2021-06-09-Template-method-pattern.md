---
layout: post
title: "[디자인패턴] Template method 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Template method 패턴
--------------------

-	상위 클래스에서 처리의 뼈대를 결정하고, 하위 클래스에서 그 구체적인 내용을 결정하는 디자인 패턴.
-	ConcreteClass1, ConcreteClass2, ConcreteClass3 모두 비슷하지만 다른 클래스이다. 그렇기 때문에 비슷한 기능 수정이 있을 때 모든 클래스 수정이 필요하다. 하지만 Template method 패턴으로 프로그래밍을 하면 템플릿 메소드만 수정을 하면 된다.
-	Template method 패턴 등장인물
	-	AbstractClass(추상 클래스)의 역할
		-	AbstractClass는 템플릿 메소드를 구현한다. 또한 그 템플릿 메소드에서 사용하고 있는 추상 메소드를 선언한다. 이 추상 메소드는 하위 클래스인 ConcreteClass 역할에 의해 구현된다.
	-	ConcreteClass(구현 클래스)의 역할
		-	AbstractClass 역할에서 정의되어 있는 추상 메소드를 구체적으로 구현한다. 여기서 구현한 메소드는 AbstractClass역의 템플릿 메소드에서 호출한다.

![Template method 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUEFJUWVPM3AzMWc)

-	예제

![Template method 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzeDkzU2xCT1RtbzA)

```java
public abstract class AbstractDisplay {
    public abstract void open();        
    public abstract void print();       
    public abstract void close();      
    public final void display() {       
        open();                             
        for (int i = 0; i < 5; i++) {  
            print();                    
        }
        close();
    }
}

public class CharDisplay extends AbstractDisplay {  
    private char ch;                               
    public CharDisplay(char ch) {            
        this.ch = ch;                               
    }
    @Override
    public void open() {                       
        System.out.print("<<");             
    }
    @Override
    public void print() {                        
        System.out.print(ch);                 
    }
    @Override
    public void close() {                       
        System.out.println(">>");           
    }
}

public class StringDisplay extends AbstractDisplay {   
    private String string;                            
    private int width;                                 
    public StringDisplay(String string) {       
        this.string = string;                           
        this.width = string.getBytes().length;   
    }
    @Override
    public void open() {                                
        printLine();                                    
    }
    @Override
    public void print() {                          
        System.out.println("|" + string + "|");  
    }
    @Override
    public void close() {                               
        printLine();                                    
    }
    private void printLine() {                  
        System.out.print("+");                  
        for (int i = 0; i < width; i++) {      
            System.out.print("-");               
        }
        System.out.println("+");                
    }
}

public class Main {
    public static void main(String[] args) {
        AbstractDisplay d1 = new CharDisplay('H');
        AbstractDisplay d2 = new StringDisplay("Hello, world.");
        AbstractDisplay d3 = new StringDisplay("안녕하세요.");
        d1.display();                                               
        d2.display();                                               
        d3.display();                                               
    }
}

```
