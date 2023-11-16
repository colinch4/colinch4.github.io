---
layout: post
title: "[java] Apache Commons Codec의 HTML 인코딩과 디코딩"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---
Apache Commons Codec은 인코딩 및 디코딩 작업을 위한 다양한 유틸리티 기능을 제공하는 Java 라이브러리입니다. 이 라이브러리는 다양한 인코딩 형식과 디코딩 알고리즘을 지원하여 데이터를 변환하고 보호하는 데 도움이 됩니다.

## HTML 인코딩
HTML 인코딩은 특수 문자를 HTML 엔티티로 변환하는 작업입니다. 이 작업은 웹 애플리케이션에서 사용자로부터 입력된 데이터의 안전한 표시를 보장하기 위해 중요합니다. Apache Commons Codec을 사용하여 HTML 인코딩을 간편하게 수행할 수 있습니다.

```java
import org.apache.commons.codec.StringEscapeUtils;

public class HtmlEncodingExample {
    public static void main(String[] args) {
        String input = "<script>alert(\"XSS!\");</script>";
        String encoded = StringEscapeUtils.escapeHtml(input);
        System.out.println("Encoded Result: " + encoded);
    }
}
```

위의 예제에서는 `StringEscapeUtils.escapeHtml()` 메서드를 사용하여 입력된 문자열을 HTML 엔티티로 인코딩합니다. 출력 결과는 다음과 같습니다:

```
Encoded Result: &lt;script&gt;alert(&quot;XSS!&quot;);&lt;/script&gt;
```

인코딩된 결과를 출력하면 특수문자 `<`, `>`, `"`이 각각 `&lt;`, `&gt;`, `&quot;`로 변환되는 것을 확인할 수 있습니다.

## HTML 디코딩
HTML 디코딩은 HTML 엔티티를 원래 문자로 변환하는 작업입니다. 이 작업은 웹 애플리케이션에서 HTML 인코딩된 데이터를 다시 원래 상태로 복원하기 위해 필요합니다. Apache Commons Codec을 사용하여 HTML 디코딩을 간단하게 수행할 수 있습니다.

```java
import org.apache.commons.codec.StringEscapeUtils;

public class HtmlDecodingExample {
    public static void main(String[] args) {
        String input = "&lt;script&gt;alert(&quot;XSS!&quot;);&lt;/script&gt;";
        String decoded = StringEscapeUtils.unescapeHtml(input);
        System.out.println("Decoded Result: " + decoded);
    }
}
```

위의 예제에서는 `StringEscapeUtils.unescapeHtml()` 메서드를 사용하여 HTML 엔티티로 인코딩된 문자열을 디코딩합니다. 출력 결과는 다음과 같습니다:

```
Decoded Result: <script>alert("XSS!");</script>
```

디코딩된 결과를 출력하면 HTML 엔티티로 변환된 문자열이 다시 원래의 `<script>alert("XSS!");</script>` 문자열로 복원된 것을 확인할 수 있습니다.

Apache Commons Codec을 사용하면 HTML 인코딩 및 디코딩을 손쉽게 수행할 수 있으며, 웹 애플리케이션에서 데이터의 안전한 처리를 위해 꼭 필요한 기능입니다.

더 자세한 정보는 [공식 Apache Commons Codec 문서](https://commons.apache.org/proper/commons-codec/userguide.html)를 참조하세요.