---
layout: post
title: "[디자인패턴] Abstract Factory 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---


Abstract Factory 패턴
---------------------

-	추상적인 공장이 등장하고, 추상적인 부품을 조합해서 추상적인 제품을 만든다. 즉 부품의 구체적인 구현에는 주목하지 않고 인터페이스(API)만을 사용해서 부품을 조립하고 제품을 완성하는 패턴이 `Abstract Factory 패턴`이다.

-	Abstract Factory 패턴에 구체적인 공장을 새로 추가하는 것은 간단하다. '간단'하다는 것은 어떤 클래스를 만들고, 어떤 메소드를 구현하면 좋은지가 확실하다는 의미이다. 새로운 구체적인 공장을 추가한다고 가정할 때 Factory, Link, Tray, Page의 하위 클래스를 만들고 각각의 추상메소드를 구현한다. 즉, factory 패키지의 클래스가 가지고 있는 추상적인 부분을 구체화 해가는 일이다. 이때 아무리 구체적인 공장을 추가해도(또 구체적인 공장의 버그를 수정해도) 추상적인 공장이나 Main 부분을 수정할 필요는 전혀 없다.

-	Abstract Factory 패턴의 등장인물

	-	AbstractProduct(추상적인 제품)의 역할
		-	AbstractProduct는 AbstractFactory 역할에 의해 만들어지는 추상적인 부품이나 제품의 인터페이스(API)를 결정한다. Link 클래스, Tray 클래스, Page 클래스가 이 역할을 한다.
	-	AbstractFactory(추상적인 공장)의 역할
		-	AbstractFactory는 AbstractProduct 역할의 인스턴스를 만들어 내기 위한 인터페이스(API)를 결정한다. Factory클래스가 이 역할을 한다.
	-	Client(의뢰자)의 역할
		-	Client는 AbstractFactory역할과 AbstractProduct 역할의 인터페이스(API)만을 사용해서 주어진 역할을 실행한다. Client는 구체적인 부품이나 제품, 공장에 대해서는 모른다. Main 클래스가 이 역할을 한다.
	-	ConcreteProduct(구체적인 제품)의 역할
		-	ConcreteProduct는 AbstractProduct 역할의 인터페이스(API)를 구현한다.
		-	listfactory 패키지 : ListLink 클래스, ListTray 클래스, ListPage 클래스
		-	tablefactory 패키지 : TableLink 클래스, TableTray 클래스, TablePage 클래스
	-	ConcreteFactory(구체적인 공장)의 역할
		-	ConcreteFactory는 AbstractFactory 역할의 인터페이스(API)를 구현한다.
		-	listfactory 패키지 : ListFactory 클래스
		-	tablefactory 패키지 : TableFactory 클래스

![Abstract Factory 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzbl9uUl85WlhrQzA)

-	예제

![Abstract Factory 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzR2h2dFRMUHM0YlE)

![Abstract Factory 패턴-패키지](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzbDVUUll0VWVBQ0E)

-	package AbstractFactory

```java
public class Main {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java Main class.name.of.ConcreteFactory");
            System.out.println("Example 1: java Main listfactory.ListFactory");
            System.out.println("Example 2: java Main tablefactory.TableFactory");
            System.exit(0);
        }
        Factory factory = Factory.getFactory(args[0]);

        Link joins = factory.createLink("중앙일보", "http://www.joins.com");
        Link hani = factory.createLink("한계레 신문", "http://www.hani.co.kr/");

        Link us_yahoo = factory.createLink("Yahoo!", "http://www.yahoo.com/");
        Link kr_yahoo = factory.createLink("Yahoo!korea", "http://www.yahoo.co.kr/");
        Link excite = factory.createLink("Excite", "http://www.excite.com/");
        Link google = factory.createLink("Google", "http://www.google.com/");

        Tray traynews = factory.createTray("신문");
        traynews.add(joins);
        traynews.add(hani);

        Tray trayyahoo = factory.createTray("Yahoo!");
        trayyahoo.add(us_yahoo);
        trayyahoo.add(kr_yahoo);

        Tray traysearch = factory.createTray("서치엔진");
        traysearch.add(trayyahoo);
        traysearch.add(excite);
        traysearch.add(google);

        Page page = factory.createPage("LinkPage", "홍길동");
        page.add(traynews);
        page.add(traysearch);
        page.output();
    }
}
```

-	package AbstractFactory.factory;

```java
public abstract class Factory {
    public static Factory getFactory(String classname) {
        Factory factory = null;
        try {
            factory = (Factory)Class.forName(classname).newInstance();
        } catch (ClassNotFoundException e) {
            System.err.println("클래스 " + classname + " 발견되지 않았습니다.");
        } catch (Exception e) {
            e.printStackTrace();
        }
        return factory;
    }
    public abstract Link createLink(String caption, String url);
    public abstract Tray createTray(String caption);
    public abstract Page createPage(String title, String author);
}

public abstract class Item {
    protected String caption;
    public Item(String caption) {
        this.caption = caption;
    }
    public abstract String makeHTML();
}

public abstract class Link extends Item {
    protected String url;
    public Link(String caption, String url) {
        super(caption);
        this.url = url;
    }
}

public abstract class Tray extends Item {
    protected Vector tray = new Vector();
    public Tray(String caption) {
        super(caption);
    }
    public void add(Item item) {
        tray.add(item);
    }
}

public abstract class Page {
    protected String title;
    protected String author;
    protected Vector content = new Vector();
    public Page(String title, String author) {
        this.title = title;
        this.author = author;
    }
    public void add(Item item) {
        content.add(item);
    }
    public void output() {
        try {
            String filename = title + ".html";
            Writer writer = new FileWriter(filename);
            writer.write(this.makeHTML());
            writer.close();
            System.out.println(filename + "을 작성했습니다.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public abstract String makeHTML();
}
```

-	package AbstractFactory.listfactory;

```java
public class ListFactory extends Factory {
    public Link createLink(String caption, String url) {
        return new ListLink(caption, url);
    }
    public Tray createTray(String caption) {
        return new ListTray(caption);
    }
    public Page createPage(String title, String author) {
        return new ListPage(title, author);
    }
}

public class ListLink extends Link {
    public ListLink(String caption, String url) {
        super(caption, url);
    }
    public String makeHTML() {
        return "  <li><a href=\"" + url + "\">" + caption + "</a></li>\n";
    }
}


public class ListTray extends Tray {
    public ListTray(String caption) {
        super(caption);
    }
    public String makeHTML() {
        StringBuffer buffer = new StringBuffer();
        buffer.append("<li>\n");
        buffer.append(caption + "\n");
        buffer.append("<ul>\n");
        Iterator it = tray.iterator();
        while (it.hasNext()) {
            Item item = (Item)it.next();
            buffer.append(item.makeHTML());
        }
        buffer.append("</ul>\n");
        buffer.append("</li>\n");
        return buffer.toString();
    }
}

public class ListPage extends Page {
    public ListPage(String title, String author) {
        super(title, author);
    }
    public String makeHTML() {
        StringBuffer buffer = new StringBuffer();
        buffer.append("<html><head><title>" + title + "</title></head>\n");
        buffer.append("<body>\n");
        buffer.append("<h1>" + title + "</h1>\n");
        buffer.append("<ul>\n");
        Iterator it = content.iterator();
        while (it.hasNext()) {
            Item item = (Item)it.next();
            buffer.append(item.makeHTML());
        }
        buffer.append("</ul>\n");
        buffer.append("<hr><address>" + author + "</address>");
        buffer.append("</body></html>\n");
        return buffer.toString();
    }
}

```

-	package AbstractFactory.tablefactory;

```java
public class TableFactory extends Factory {
    public Link createLink(String caption, String url) {
        return new TableLink(caption, url);
    }
    public Tray createTray(String caption) {
        return new TableTray(caption);
    }
    public Page createPage(String title, String author) {
        return new TablePage(title, author);
    }
}

public class TableLink extends Link {
    public TableLink(String caption, String url) {
        super(caption, url);
    }
    public String makeHTML() {
        return "<td><a href=\"" + url + "\">" + caption + "</a></td>\n";
    }
}

public class TableTray extends Tray {
    public TableTray(String caption) {
        super(caption);
    }
    public String makeHTML() {
        StringBuffer buffer = new StringBuffer();
        buffer.append("<td>");
        buffer.append("<table width=\"100%\" border=\"1\"><tr>");
        buffer.append("<td bgcolor=\"#cccccc\" align=\"center\" colspan=\""+ tray.size() + "\"><b>" + caption + "</b></td>");
        buffer.append("</tr>\n");
        buffer.append("<tr>\n");
        Iterator it = tray.iterator();
        while (it.hasNext()) {
            Item item = (Item)it.next();
            buffer.append(item.makeHTML());
        }
        buffer.append("</tr></table>");
        buffer.append("</td>");
        return buffer.toString();
    }
}

public class TablePage extends Page {
    public TablePage(String title, String author) {
        super(title, author);
    }
    public String makeHTML() {
        StringBuffer buffer = new StringBuffer();
        buffer.append("<html><head><title>" + title + "</title></head>\n");
        buffer.append("<body>\n");
        buffer.append("<h1>" + title + "</h1>\n");
        buffer.append("<table width=\"80%\" border=\"3\">\n");
        Iterator it = content.iterator();
        while (it.hasNext()) {
            Item item = (Item)it.next();
            buffer.append("<tr>" + item.makeHTML() + "</tr>");
        }
        buffer.append("</table>\n");
        buffer.append("<hr><address>" + author + "</address>");
        buffer.append("</body></html>\n");
        return buffer.toString();
    }
}
```
