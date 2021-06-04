---
layout: post
title: "[android] 배열과 문자열 해법"
description: " "
date: 2021-06-04
tags: [android]
comments: true
share: true
---

# 배열과 문자열 해법

1.1 문자열에 포함된 문자열이 전부 유일한지를 검사하는 알고리즘을 구현하라. 다른 자료구조를 사용할 수 없는 상황이면 어떻게 하겠는가?

-  ASCII 문자열인지 유니코드 문자열인지 질문하라
- 간단히 하기위해서는 ASCII 문자열이지만 그렇지 않다면 필요한 공간의 크기를 늘려야 한다.

```java
public boolean isUniqueChars2(String str){
  if(str.length() > 256) return false;
  //becasue acscii has 256 items
  boolean[] char_set = new boolean[256];
  for(int i = 0;i<str.length();i++){
    int val = str.charAt(i);
    if(char_set[val]){
      return false;
    }
    char_set[val] = true;
   
  }
  return true;
}
```

- 시간복잡도 O(n), 공간복잡도 O(1)

```kotlin
fun isUniqueChars(val str : String) : Boolean {
  if(str.length > 26) return false;
  
  val checker : Int = 0;
  for(i in 0 .. str.length){
    val int = str.charAt(i) - 'a';
    if((checker & (1 << val)) > 0){
      return false;
    }
    checker |= (1 << val);
  }
  return true;
}
```

- 비트벡터를 사용하면 공간ㅇ르 1/8로 줄일 수 있다. 소문자 a to z 까지라  가정

1.2 널 문자로 끝나는 문자열을 뒤집는 reverser(char* str) 함수를 c++로 구현

```c++
void reverse(char *str){
  char* end = str;
  char temp;
  if(str){
    while(*end) ++end;
    
  --end;
  while(str < end){
    tmp = *str;
    *str++ = *end;
    *end-- = tmp;
  	}
  }
}
```

1.3 문자열 두개를 입력으로 바다 그중 하나가 다른 하나의 순열인지 판별하는 메서드를 작성하라

1. 정렬하라
2. 문자열에 포함된 문자의 출현 횟수가 같은지 검사하라

1.4 문자열에서 주어진 공백을 '%20'으로 바꾸는 메서들르 작성하라. 문자열 끝에 추가로 필요한 문자들을 더할 수 있는 충분한 공간이 있으며, 공백을 포함한 문자열의 길이도 함께 주어진다.

```java
public void replaceSpaces(char[] str,int length){
  int spaceCount = 0,newLenth, i =0;
  for(i = 0;i<length;i++) {
    if(str[i] == ' '){
      spaceCount++;
    }
  }
  newLength = lenth + spaceCount * 2;
  str[newLength] = '\0';
  
  for(i = length -1;i >=0 ;i--){
    if(str[i] == ' '){
      str[newLength - 1] = '0';
      str[newLength - 2] = '2';
      str[newLegnth = 3] = '%';
    }
  }
}
```

```java
public void rotate(int[][] matrix,int n){
  for(int layer = 0;layer < n /2;++layer){
    int first = layer;
    int last = n -1 - layer;
    for(int i = first;i < last;++i){
      int offset = i - first;
      int top = matrix[first][i];
      
      matrix[first][i] = matrix[last - offset][first];
      matrix[last-offset][fist] = matrix[last][last - offset];
      
      matrix[last][last - offset] = matrix[i][last];
      
      matrix[i][last] = top;
    }
  }
}
```

2.2 Stack pop push 두가지 연산 뿐만 아니라 최소값을 갖는 원소를 반환하는 min 연산을 갖춘 스택은 어떻게 구현할 수 있겠는가? Push, pop 그리고 in은 공히 O(1) 시간에 처리되어야한다.

- min 이라는 변수를 두고 pop push 마다 추적되게 할 수있지만 만약 최솟값이 지워진다면 O(1) 이 아닌 O(n) 이 되버린다.

```kotlin

import java.util.*

class StackWithMin : Stack<Int>() {
    var s2: Stack<Int> = Stack()
    override fun push(value: Int): Int? {
        if (value <= min()) {
            s2.push(value)
        }
        super.push(value)
        return value
    }

    override fun pop(): Int {
        val value = super.pop()
        if (value == min()) {
            s2.pop()
        }
        return value
    }

    private fun min(): Int {
        return if (s2.isEmpty()) {
            Int.MAX_VALUE
        } else {
            s2.peek()
        }
    }

}
```

- 스택을 하나 더만들어서 최소값을 추적하게 한다.  최적

```kotlin
class ReactiveCalculator(a:Int, b:Int) {
    val subjectCalc: Subject<ReactiveCalculator> = PublishSubject.create()

    var nums:Pair<Int,Int> = Pair(0,0)

    init{
        nums = Pair(a,b)

        subjectCalc.subscribe {
            with(it) {
                calculateAddition()
                calculateSubstraction()
                calculateMultiplication()
                calculateDivision()
            }
        }

        subjectCalc.onNext(this)
    }

    inline fun calculateAddition():Int {
        val result = nums.first + nums.second
        println("Add = $result")
        return result
    }

    inline fun calculateSubstraction():Int {
        val result = nums.first - nums.second
        println("Substract = $result")
        return result
    }

    inline fun calculateMultiplication():Int {
        val result = nums.first * nums.second
        println("Multiply = $result")
        return result
    }

    inline fun calculateDivision():Double {
        val result = (nums.first*1.0) / (nums.second*1.0)
        println("Division = $result")
        return result
    }


    inline fun modifyNumbers (a:Int = nums.first, b: Int = nums.second) {
        nums = Pair(a,b)
        subjectCalc.onNext(this)

    }

    suspend fun handleInput(inputLine:String?) {//(1)
        if(!inputLine.equals("exit")) {
            val pattern: java.util.regex.Pattern = java.util.regex.Pattern.compile("([a|b])(?:\\s)?=(?:\\s)?(\\d*)");

            var a: Int? = null
            var b: Int? = null

            val matcher: java.util.regex.Matcher = pattern.matcher(inputLine)

            if (matcher.matches() && matcher.group(1) != null && matcher.group(2) != null) {
                if(matcher.group(1).toLowerCase().equals("a")){
                    a = matcher.group(2).toInt()
                } else if(matcher.group(1).toLowerCase().equals("b")){
                    b = matcher.group(2).toInt()
                }
            }

            when {
                a != null && b != null -> modifyNumbers(a, b)
                a != null -> modifyNumbers(a = a)
                b != null -> modifyNumbers(b = b)
                else -> println("Invalid Input")
            }
        }
    }

}

fun main(args: Array<String>) {
    println("Initial Out put with a = 15, b = 10")
    val calculator: ReactiveCalculator = ReactiveCalculator(15, 10)

    println("Enter a = <number> or b = <number> in separate lines\nexit to exit the program")
    var line:String?
    do {
        line = readLine()
        async(CommonPool) {//(2)
            calculator.handleInput(line)
        }
    } while (line!= null && !line.toLowerCase().contains("exit"))
}
```

