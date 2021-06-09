---
layout: post
title: "[디자인패턴] Strategy 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Strategy 패턴
-------------

-	문제를 해결해 갈 때의 방법인 알고리즘을 빈틈없이 교체해서 같은 문제를 다른 방법으로도 쉽게 해결할 수 있도록 도와주는 패턴이 Strategy 패턴이다.
-	Strategy 패턴에서는 알고리즘의 부분을 다른 부분과 의식적으로 분리해서 알고리즘의 인터페이스(API) 부분만을 규정한다. 그리고 프로그램에서 위임에 의해 알고리즘을 이용한다. 위임이라는 느슨한 연결을 사용하고 있으므로 알고리즘을 용이하게 교환할 수 있다. 원래의 알고리즘과 개량한 알고리즘의 속도를 비교하고 싶은 경우에도 간단하게 교체해서 비교할 수 있다. Strategy 패턴을 사용하면 장기 게임을 하는 프로그램에서 사용자의 선택에 맞추어서 사고 루틴의 레벨을 간단하게 교체할 수 있다.

-	Strategy 패턴의 등장인물

	-	Strategy(전략)의 역할
		-	Strategy는 전략을 이용하기 위한 인터페이스(API)를 결정한다.
	-	ConcreteStrategy(구체적인 전략)의 역할
		-	ConcreteStrategy는 Strategy의 인터페이스(API)를 실제로 구현한다. 여기서 구체적인 전략(작전,방책,알고리즘)을 실제로 프로그래밍한다.
	-	Context(문맥)
		-	Context는 Strategy을 이용하는 역할이다. ConcreteStrategy의 인스턴스를 가지고 있으며 필요에 따라 그것을 이용한다.  

![Strategy 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzVm5zLXdNZmU1UzA)

-	예제

![Strategy 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzOEpFTWJUaE9keTQ)

```java
public class Main {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java Main randomseed1 randomseed2");
            System.out.println("Example: java Main 314 15");
            System.exit(0);
        }
        int seed1 = Integer.parseInt(args[0]);
        int seed2 = Integer.parseInt(args[1]);
        Player player1 = new Player("홍길동", new WinningStrategy(seed1));
        Player player2 = new Player("임꺽정", new ProbStrategy(seed2));
        for (int i = 0; i < 10000; i++) {
            Hand nextHand1 = player1.nextHand();
            Hand nextHand2 = player2.nextHand();
            if (nextHand1.isStrongerThan(nextHand2)) {
                System.out.println("Winner:" + player1);
                player1.win();
                player2.lose();
            } else if (nextHand2.isStrongerThan(nextHand1)) {
                System.out.println("Winner:" + player2);
                player1.lose();
                player2.win();
            } else {
                System.out.println("Even...");
                player1.even();
                player2.even();
            }
        }
        System.out.println("Total result:");
        System.out.println("" + player1);
        System.out.println("" + player2);
    }
}

public class Player {
    private String name;
    private Strategy strategy;
    private int wincount;
    private int losecount;
    private int gamecount;
    public Player(String name, Strategy strategy) {         // 이름과 전략을 전수 받는다.
        this.name = name;
        this.strategy = strategy;
    }
    public Hand nextHand() {                                // 전략의 지시를 받는다.
        return strategy.nextHand();
    }
    public void win() {                 // 이겼다.
        strategy.study(true);
        wincount++;
        gamecount++;
    }
    public void lose() {                // 졌다.
        strategy.study(false);
        losecount++;
        gamecount++;
    }
    public void even() {                // 무승부
        gamecount++;
    }
    public String toString() {
        return "[" + name + ":" + gamecount + " games, " + wincount + " win, " + losecount + " lose" + "]";
    }
}

public interface Strategy {
    public abstract Hand nextHand();
    public abstract void study(boolean win);
}

public class Hand {
    public static final int HANDVALUE_GUU = 0;  // 주먹을 나타내는 값
    public static final int HANDVALUE_CHO = 1;  // 가위를 나타내는 값
    public static final int HANDVALUE_PAA = 2;  // 보를 나타내는 값
    public static final Hand[] hand = {         // 가위바위보의 손을 나타내는 3개의 인스턴스
        new Hand(HANDVALUE_GUU),
        new Hand(HANDVALUE_CHO),
        new Hand(HANDVALUE_PAA),
    };
    private static final String[] name = {      // 가위바위보의 손의 문자열 표현
        "주먹", "가위", "보",
    };
    private int handvalue;                      // 가위바위보의 손의 값
    private Hand(int handvalue) {
        this.handvalue = handvalue;
    }
    public static Hand getHand(int handvalue) { // 값으로부터 인스턴스를 얻는다.
        return hand[handvalue];
    }
    public boolean isStrongerThan(Hand h) {     // this가 h보다 강할 때true
        return fight(h) == 1;
    }
    public boolean isWeakerThan(Hand h) {       // this가h보다 약할 때true
        return fight(h) == -1;
    }
    private int fight(Hand h) {                 // 무승부는 0, this가 이기면1, h가 이기면-1
        if (this == h) {
            return 0;
        } else if ((this.handvalue + 1) % 3 == h.handvalue) {
            return 1;
        } else {
            return -1;
        }
    }
    public String toString() {                  // 문자열 표현으로 변환
        return name[handvalue];
    }
}

public class ProbStrategy implements Strategy {
    private Random random;
    private int prevHandValue = 0;
    private int currentHandValue = 0;
    private int[][] history = {
        { 1, 1, 1, },
        { 1, 1, 1, },
        { 1, 1, 1, },
    };
    public ProbStrategy(int seed) {
        random = new Random(seed);
    }
    public Hand nextHand() {
        int bet = random.nextInt(getSum(currentHandValue));
        int handvalue = 0;
        if (bet < history[currentHandValue][0]) {
            handvalue = 0;
        } else if (bet < history[currentHandValue][0] + history[currentHandValue][1]) {
            handvalue = 1;
        } else {
            handvalue = 2;
        }
        prevHandValue = currentHandValue;
        currentHandValue = handvalue;
        return Hand.getHand(handvalue);
    }
    private int getSum(int hv) {
        int sum = 0;
        for (int i = 0; i < 3; i++) {
            sum += history[hv][i];
        }
        return sum;
    }
    public void study(boolean win) {
        if (win) {
            history[prevHandValue][currentHandValue]++;
        } else {
            history[prevHandValue][(currentHandValue + 1) % 3]++;
            history[prevHandValue][(currentHandValue + 2) % 3]++;
        }
    }
}

public class WinningStrategy implements Strategy {
    private Random random;
    private boolean won = false;
    private Hand prevHand;
    public WinningStrategy(int seed) {
        random = new Random(seed);
    }
    public Hand nextHand() {
        if (!won) {
            prevHand = Hand.getHand(random.nextInt(3));
        }
        return prevHand;
    }
    public void study(boolean win) {
        won = win;
    }
}

```
