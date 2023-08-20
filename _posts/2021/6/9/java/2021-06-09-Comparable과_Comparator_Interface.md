---
layout: post
title: "[java] Comparable과 Comparator Interface"
description: " "
date: 2021-06-09
tags: [java]
comments: true
share: true
---

## Comparable과 Comparator Interface

> 배열이나 리스트의 정렬을 돕기 위한 Comparable과 Comparator, 두가지 Interface를 제공



### Comparable

> 기본 정렬기준을 구현하는데 사용	

* Java에서 제공되는 정렬이 가능한 클래스들은 모두 Comparable 인터페이스로 구현되어있음
* 정렬기준
  * Integer, Double 클래스 : 오름차순 정렬
  * String 클래스 : 사전적 정렬
* 구현 방법
  * 정렬한 객체에 Comparable interface를 implements 후, comparaTo() 메서드를 오버라이딩
  * 객체 안의 여러가지 변수들 중 기준을 잡는 것이라 생각하자

```java
// x좌표가 증가하는 순, x좌표가 같으면 y좌표가 감소하는 순으로 정렬하라.
class Point implements Comparable<Point> {
    int x, y;

    @Override
    public int compareTo(Point p) {
        if(this.x > p.x) {
            return 1; // x에 대해서는 오름차순
        }
        else if(this.x == p.x) {
            if(this.y < p.y) { // y에 대해서는 내림차순
                return 1;
            }
        }
        return -1;
    }
}

// main에서 사용법
List<Point> pointList = new ArrayList<>();
pointList.add(new Point(x, y));
Collections.sort(pointList);
```



### Comparator

> 기본 정렬기준 외에 다른 기준으로 정렬하고자할 때 사용

* 주로 익명 클래스로 사용된다.
* 기본적인 정렬 방법인 오름차순 정렬을 내림차순으로 정렬할 때 많이 사용한다.
* 구현 방법
  * Comparator interface를 implements 후 compare() 메서드를 오버라이드한다
  * Integer.compare(x,y) 오르차순 정렬
    * = return (x<y) ? -1 : (( x == y ) ? 0 : 1 );
  * Integer.compare(y,x) 내림차순 정렬
* 사용법
  * Arrays.sort(array, myComprator)
  * Collections.sort(list, myComparator) 
  * 위처럼 메서드들의 두번째 인자로 Comparator interface를 받을 수 있다.



1. 두 번째 인자로 Comparator interface를 받는 경우

   * 우선 순위큐 (PriorityQueue) 생성자의 두번째 인자로 Comprator interface를 받을 수 있다.

   ```java
   // x좌표가 증가하는 순, x좌표가 같으면 y좌표가 감소하는 순으로 정렬하라.
   class MyComparator implements Comparator<Point> {
     @Override
     public int compare(Point p1, Point p2) {
       if (p1.x > p2.x) {
         return 1; // x에 대해서는 오름차순
       }
       else if (p1.x == p2.x) {
         if (p1.y < p2.y) { // y에 대해서는 내림차순
           return 1;
         }
       }
       return -1;
     }
   }
   
   // main에서 사용법
   List<Point> pointList = new ArrayList<>();
   pointList.add(new Point(x, y));
   MyComparator myComparator = new MyComparator();
   Collections.sort(pointList, myComparator);
   ```

2. Comprator 익명클래스 이용

   1. 

   ```java
   Comparator<Point> myComparator = new Comparator<Point>() {
     @Override
     public int compare(Point p1, Point p2) {
       if (p1.x > p2.x) {
         return 1; // x에 대해서는 오름차순
       }
       else if (p1.x == p2.x) {
         if (p1.y < p2.y) { // y에 대해서는 내림차순
           return 1;
         }
       }
       return -1;
     }
   };
   
   List<Point> pointList = new ArrayList<>();
   pointList.add(new Point(x, y));
   Collections.sort(pointList, myComparator);
   ```

   2.

   ```java
   Arrays.sort(student, new Comparator<Student>(){
   		public int compare(Point p1, Point p2) {
      				if (p1.x > p2.x) {
         				return 1; // x에 대해서는 오름차순
       			}
       			else if (p1.x == p2.x) {
                     if (p1.y < p2.y) { // y에 대해서는 내림차순
                       return 1;
                     }
                   }
                   return -1;
                 }
   		});
   ```

   

#### 참고

1. Arrays.sort()
   1. 배열 정렬
   2. Object Array 새로 정의한 클래스에 대한 배열
      1. Time Sort(Merge Sort + Insertion Sort)
   3. Primitive Array 기본 자료형에 대한 배열
      1. Dual Pivot QuickSort(Quick Sort + Insertion Sort)  
2. Collections.sort()
   1. 리스트 정렬
   2.  내부적으로 Arrays.sort()사용



##### References

https://gmlwjd9405.github.io/2018/09/06/java-comparable-and-comparator.html