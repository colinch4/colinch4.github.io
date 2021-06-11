---
layout: post
title: "[java] String의 compareTo"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---

# String의 compareTo()

* String은 Comparable 인터페이스을 구현한 클래스이고 
따라서 compareTo()를 오버라이딩 하였고, String의 compareTo()는 
아래의 코드와 같다. 

```java
public int compareTo(String anotherString) {
        int len1 = value.length;
        int len2 = anotherString.value.length;
        int lim = Math.min(len1, len2);
        char v1[] = value;
        char v2[] = anotherString.value;

        int k = 0;
        while (k < lim) {
            char c1 = v1[k];
            char c2 = v2[k];
            if (c1 != c2) {
                return c1 - c2;
            }
            k++;
        }
        return len1 - len2;
    }
```

=> 위의 코드를 보면 String의 첫 글자부터 비교하고 첫글자가 서로 다르다면 유니코드값\[아스키코드값]의 차이(return c1 - c2;)를 리턴한다. 
<br>하지만 처음 글자가 서로 같고 그 이후의 글자도 모두 같다면(while문으로 비교한 글자들까지만) String의 길이값의 차이(return len1 - len2;)를 리턴함을 알 수 있다.  
<br> 또 유니코드값\[아스키코드값]은 사전순으로 앞에 나오면 작은 값이고, 뒤에 나오면 큰 값이다. 
예를 들어 a는 사전순으로 앞에 있어 c보다 작은 값이다. 따라서 "a".compareTo("c") 하면 리턴값은 음수가 나온다.\[-2]  
<br>
문자열 "Alex" 와 문자열 "Alexa" 비교하기. 
```java
public class StringExample {
    public static void main(String[] args) {
        String str1 = "Alex";
        String str2 = "Alexa";

        System.out.println(str1.compareTo(str2));

    }
}
// 실행 결과
// -1

/* Alex가 this, Alexa가 anotherString
public int compareTo(String anotherString) {
        int len1 = 4;
        int len2 = 5;
        int lim = 4;
        char v1[] = value; => 'A','l','e','x'
        char v2[] = anotherString.value; => 'A','l','e','x','a'

        int k = 0;
        while (k < lim) {
            char c1 = v1[k];
            char c2 = v2[k];
            if (c1 != c2) {
                return c1 - c2;
            }
            k++;
        }
        // case k = 0
        // 'A' == 'A'
        // case k = 1
        // 'l' == 'l'
        // case k = 2
        // 'x' == 'x'
        // case k = 3 
        // 'e' == 'e'
        // while 문 빠져나오고 return len1 - len2 ( 4 - 5 ) 
        // 이므로 -1을 리턴한다.
        
        return len1 - len2;
    }
*/

```
=> "Alex".compareTo("Alexa")가 -1 이고 따라서 정렬하면 Alex, Alexa 가 됨을 알 수 있다. 
또 이 경우는 비교한 문자들이 모두 같아 Alex의 문자열 길이에서 Alexa의 문자열 길이를 뺀 값(-1)을
리턴하였음을 알 수 있다. 


문자열 "Group" 와 문자열 "Grit" 비교하기. 

```java
public class StringExample {
    public static void main(String[] args) {
        String str1 = "Group";
        String str2 = "Grit";
        System.out.println(str1.compareTo(str2));
    }
}
// 실행 결과 
// 6 

/* Group이 this,  Grit이 anotherString
public int compareTo(String anotherString) {
        int len1 = 5;
        int len2 = 4;
        int lim = 4;
        char v1[] = value; => 'G','r','o','u','p'
        char v2[] = anotherString.value; => 'G','r','i','t'

        int k = 0;
        while (k < lim) {
            char c1 = v1[k];
            char c2 = v2[k];
            if (c1 != c2) {
                return c1 - c2;
            }
            k++;
        }
        // case k = 0;
        // 'G' == 'G'
        // case k = 1
        // 'r' == 'r'
        // case k = 2
        // 'o' != 'i'
        // 'o'의 아스키 코드값이 111, 'i'의 아스키 코드값이 105 이므로
        // return 111 - 105; ,즉 6을 리턴한다. 
    }
*/
```