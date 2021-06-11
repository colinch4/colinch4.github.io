---
layout: post
title: "[java] Immutable Object(불변 객체)"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---


## Immutable Object(불변 객체)

### 장점

1. 생성자의 방어 복사 및 접근 메소드의 방어 복사가 필요없다. (방어 복사: clone())
2. 병렬 프로그래밍을 작성할 때, 동기화 없이 객체를 공유 가능하다.

"특별한 이유가 없다면 객체를 불변 객체로 설계해야 한다."<br>

Effective Java, Effective Objective-C<br>

## 단점

1. 객체가 가지는 값마다 새로운 객체가 필요하다. 
2. String s += "xxx";   ⇒ "Helloxxx"

   : 내용이 동일한 객체는 공유되는 메커니즘을 제공해야 한다. (Flyweight)

   - static factory method

## 불변 클래스를 만드는 방법

- 객체를 변경하는 setter 를 제공하지 않습니다. JavaBeans Pattern- (x)
- 모든 필드는 final
- 가변 객체 참조 필드를 사용자가 얻을 수 없도록 해야 한다. (private 접근 제한자 사용)
- 상속 금지 ( final class, final method, 생성자를 private으로 정의하고 **public static factory method**를 제공한다.)

- **불변 객체가 아닌 경우**
```
    // 불변 객체가 아닌 경우
    public class MutableExample {
        public static void main(String[] args) {
            Point pos = new Point(10,20);
    
            Rect r = new Rect(pos);
            r.setPosition(new Point(10,100));
    
            pos = r.getPosition();
            pos.setX(-9999);
    
            String s = r.getName();
            s = "xxx"; // 새로운 객체를 참조한다.
        
            System.out.println(r);
            System.out.println(pos);
    
        }
    
    }
    
    class Rect{
      //캡슐화, 정보 은닉
        private Point position;
        private String name;
    
        Rect(Point position){
            this.position = position.clone();
            this.name = "Tom";
        }
    
        public String getName() {
            return name;
        }
    
        public Point getPosition() {
            return position.clone();
        }
    
        @Override
        public String toString() {
            return "Rect{" +
                    "position= " + position +
                    ",name= " + name + '\'' + '}';
        }
    
        public void setPosition(Point position) {
            this.position = position;
        }
    }
    
    class Point implements Cloneable{
    
        private int x;
        private int y;
    
        @Override
        public Point clone() {
            try {
                return (Point)super.clone();
            } catch (CloneNotSupportedException e) {
                e.printStackTrace();
            }
            return null;
        }
    
        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }
    
        public int getX() {
            return x;
        }
    
        public int getY() {
            return y;
        }
    
        public void setX(int x) {
            this.x = x;
        }
    
        public void setY(int y) {
            this.y = y;
        }
    
        @Override
        public String toString() {
            return  "Poiny{" + "x=" + x + ", y=" + y + "}";
        }
    }
```
- 필드의 접근 제한자에 final이 붙지 않고, 클래스마다 setter 메서드가 있기 때문에 객체의 값이 바뀔 가능성이 있다.
- 또 새로운 변수를 만드는 경우, 변수에 객체를 대입할때나 생성자에 인자 값을 전달할때 **인자나 객체를 그대로 참조해버리면 외부에 의해 값이 바뀔 위험이 있으므로**  생성자의 방어복사 및 접근 메소드(getter)의 방어 복사를 반드시 해야 하는 번거로움이 있다. ( 방어 복사 : clone())

- **불변 객체인 경우**
```java
    // 불변 객체인 경우
    public class ImmutableExample {
        public static void main(String[] args) {
            Point2 pos = new Point2(10,20);
            Point2 pos2 = new Point2(20,30);
            
            Rect2 r = new Rect2(pos);
            //r.setPosition(new Point(10,100));
                    
            pos = r.getPosition();
            //pos.setX(-9999);
    
            String s = r.getName();
            s = "xxx"; // 새로운 객체를 참조한다.
    
            System.out.println(r);
            System.out.println(pos);
    
        }
    
    }
    
    class Rect2{
        //캡슐화, 정보 은닉
        private final Point2 position;
        private final String name;
    
        Rect2(Point2 position) {
            this.position = position;
            this.name = "Bob";
        }
    
        public String getName() {
            return name;
        }
    
        Point2 getPosition() {
            return position;
        }
    
        @Override
        public String toString() {
            return "Rect{" +
                    "position= " + position +
                    ",name= " + name + '\'' + '}';
        }
    
    }
    
    class Point2 implements Cloneable{
    
        private final int x;
        private final int y;
    
        Point2(int x, int y){
            this.x = x;
            this.y = y;
        }
    
        public int getX() {
            return x;
        }
    
        public int getY() {
            return y;
        }
    
        @Override
        public String toString() {
            return  "Poiny{" + "x=" + x + ", y=" + y + "}";
        }
    }
```
- 불변 객체는 객체 생성 이후 값이 바뀔 수 없는 객체이므로 따로 생성자의 매개변수나 접근 메소드에 대해서 방어 복제를 취해주지 않았다.
- clone()과 관련하여 코드가 없으므로 한결 코드가 깔끔해졌다.
