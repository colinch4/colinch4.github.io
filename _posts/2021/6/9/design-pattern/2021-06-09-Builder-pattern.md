---
layout: post
title: "[디자인패턴] Builder 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Builder 패턴
------------

-	구조를 가진 인스턴스를 쌓아 올리는 패턴
-	Main 클래스는 Builder 클래스의 메소드를 모른다. Main 클래스는 Director 클래스의 construct 메소드만을 호출한다. Director 클래스는 자신이 실제로 이용하고 있는 클래스가 사실은 무엇인지 모른다. 모르기 때문에 교체할 수 있다. 모르기 때문에 교환이 가능하고, 교체가 가능하기 때문에 부품으로서 가치가 높다.
-	Builder 클래스는 문서를 구축할 때(목적을 달성하기 위해) 필요 충분한 메소드군을 선언해야 한다. Director 클래스에 주어진 도구는 Buillder 클래스가 제공하는 도구이기 때문에 Builder 클래스의 메소드로서 무엇을 준비해야 할지는 중요하다.

-	Builder 패턴의 등장인물

	-	Builder(건축자)의 역할
		-	Builder 역할은 인스턴스를 생성하기 위한 인터페이스(API)를 결정한다.
	-	ConcreteBuilder(구체적인 건축자)의 역할
		-	ConcreteBuilder역할은 Builder 역할의 인터페이스를(API)를 구현하고 있는 클래스이다. 실제의 인스턴스가 작성으로 호출되는 메소드가 여기에 정의된다.  
	-	Director(감독자)의 역할
		-	Director 역할은 Builder 역할의 인터페이스(API)를 사용해서 인스턴스를 생성한다. ConcreteBuilder 역할에 의존한 프로그래밍을 수행하지 않는다.
	-	Client(의뢰인)의 역할
		-	Builder 패턴을 이용하는 역할.

![Builder 패턴-1](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzUWZibmJPWFFYVjQ)

![Builder 패턴-2](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzWlhLUGZSVVppek0)

-	예제

![Builder 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzMGo1bVVmWVdIRUU)

```java
public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            usage();
            System.exit(0);
        }
        if (args[0].equals("plain")) {
            Director director = new Director(new TextBuilder());
            String result = (String)director.construct();
            System.out.println(result);
        } else if (args[0].equals("html")) {
            Director director = new Director(new HTMLBuilder());
            String filename = (String)director.construct();
            System.out.println(filename + "이 작성되었습니다.");
        } else {
            usage();
            System.exit(0);
        }
    }
    public static void usage() {
        System.out.println("Usage: java Main plain      일반 텍스트에서 문서작성");
        System.out.println("Usage: java Main html       HTML 파일에서 문서작성");
    }
}

public class Director {
    private Builder builder;
    public Director(Builder builder) {      // Builder의 하위 클래스의 인스턴스가 제공되기 때문에
        this.builder = builder;             // builder 필드에 보관해 둔다.
    }
    public Object construct() {             // 문서 구축
        builder.makeTitle("Greeting");              // 타이틀
        builder.makeString("아침과 낮에");     // 문자열
        builder.makeItems(new String[]{             // 항목
            "좋은 아침입니다.",
            "안녕하세요",
        });
        builder.makeString("밤에");                 // 다른 문자열
        builder.makeItems(new String[]{             // 다른 항목
            "안녕하세요",
            "안녕히 주무세요",
            "안녕히 계세요",
        });
        return builder.getResult();                 // 완성된 문서가 반환 값이 된다.
    }
}

public abstract class Builder {
    public abstract void makeTitle(String title);
    public abstract void makeString(String str);
    public abstract void makeItems(String[] items);
    public abstract Object getResult();
}

public class HTMLBuilder extends Builder {
    private String filename;                                    // 작성할 파일명
    private PrintWriter writer;                                 // 파일에 기술할 PrintWriter
    public void makeTitle(String title) {                       // HTML 파일에서의 타이틀
        filename = title + ".html";                                 // 타이틀을 토대로 파일명을 결정
        try {
            writer = new PrintWriter(new FileWriter(filename));     // PrintWriter만든다.
        } catch (IOException e) {
            e.printStackTrace();
        }
        writer.println("<html><head><title>" + title + "</title></head><body>");    // 타이틀을 출력
        writer.println("<h1>" + title + "</h1>");
    }
    public void makeString(String str) {                        // HTML 파일에서의 문자열
        writer.println("<p>" + str + "</p>");                       // <p>태그에서 출력
    }
    public void makeItems(String[] items) {                     // HTML 파일에서의 항목
        writer.println("<ul>");                                     // <ul>과<li>에서 출력
        for (int i = 0; i < items.length; i++) {
            writer.println("<li>" + items[i] + "</li>");
        }
        writer.println("</ul>");
    }
    public Object getResult() {                                 // 완성된 문서
        writer.println("</body></html>");                           // 태그를 만든다.
        writer.close();                                             // 파일을 클로즈
        return filename;                                            // 파일명을 반환한다.
    }
}

public class TextBuilder extends Builder {
    private StringBuffer buffer = new StringBuffer();           // 이 필드에 문서를 구축한다.
    public void makeTitle(String title) {                       // 일반 텍스트에서의 타이틀
        buffer.append("==============================\n");          // 장식선
        buffer.append("『" + title + "』\n");                       // 『』가 붙은 타이틀
        buffer.append("\n");                                        // 공란
    }
    public void makeString(String str) {                        // 일반 텍스트에서의 문자열
        buffer.append('■' + str + "\n");                           // ■이 붙은 문자열
        buffer.append("\n");                                        // 공란
    }
    public void makeItems(String[] items) {                     // 일반 텍스트에서의 항목
        for (int i = 0; i < items.length; i++) {
            buffer.append("●" + items[i] + "\n");                // ●이 붙은 항목
        }
        buffer.append("\n");                                        // 공란
    }
    public Object getResult() {                                 // 완성된 문서
        buffer.append("==============================\n");          // 장식선
        return buffer.toString();                                   // StringBuffer를String을 변환
    }
}

```

-	TextBuilder와 HTMLBuilder는 Builder의 하위 클래스이고 Director는 Builder의 메소드만을 사용해서 문서를 작성한다. Builder의 메소드만을 사용한다는 것은 Director는 실제로 동작하는 것이 TextBuilder인지, HTMLBuilder인지 모른다는 의미이다. 일반 텍스트나 HTML파일에 고유의 메소드까지 Builder가 제공해서는 안된다.
