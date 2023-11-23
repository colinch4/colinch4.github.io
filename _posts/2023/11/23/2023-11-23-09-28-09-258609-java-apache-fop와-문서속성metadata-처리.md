---
layout: post
title: "[java] Java Apache FOP와 문서속성(metadata) 처리"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

Apache FOP는 XML 기반의 XSL-FO(Formatting Objects) 문서를 처리하여 PDF, PNG, SVG 등 다양한 형식의 문서로 변환하는 도구입니다. 이번에는 Java에서 Apache FOP를 사용하여 문서속성(metadata)을 처리하는 방법에 대해 알아보겠습니다.

## 문서속성(metadata)이란?

문서속성이란 문서에 대한 추가적인 정보를 제공하는 속성들을 말합니다. 일반적으로 문서의 제목, 작성자, 생성일 등의 정보가 문서속성에 포함됩니다. 이러한 문서속성은 문서 관리 및 검색에 유용하게 사용될 수 있습니다.

## Apache FOP에서 문서속성 처리하기

Apache FOP를 사용하여 문서속성을 처리하기 위해서는 다음과 같은 단계를 거칩니다:

1. XSL-FO 문서에 문서속성을 추가합니다.
2. FOP 설정 파일에 문서속성 처리를 위한 설정을 추가합니다.
3. Java 코드에서 FOP를 사용하여 문서를 생성할 때 문서속성을 설정합니다.

### XSL-FO 문서에 문서속성 추가하기

XSL-FO 문서에 문서속성을 추가하기 위해서는 다음과 같은 방법을 사용할 수 있습니다:

```xml
<fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
  <fo:layout-master-set>
    <fo:simple-page-master master-name="my-page">
      <fo:region-body />
    </fo:simple-page-master>
  </fo:layout-master-set>
  
  <fo:page-sequence master-reference="my-page">
    <fo:static-content flow-name="xsl-region-before">
      <fo:block>
        <fo:basic-link external-destination="http://www.example.com">
          <fo:retrieve-marker retrieve-class-name="doc-info"/>
        </fo:basic-link>
      </fo:block>
    </fo:static-content>
   
    <fo:flow flow-name="xsl-region-body">
      <fo:block>
        내용이 여기에 들어갑니다.
      </fo:block>
    </fo:flow>
  </fo:page-sequence>
  
  <fo:declarations>
    <fo:page-sequence-master master-name="doc-info">
      <fo:repeatable-page-master-alternatives>
        <fo:conditional-page-master-reference page-position="last">
          <fo:marker retrieve-class-name="doc-info">
            <fo:retrieve-position-within-page retrieve-class-name="doc-info" retrieve-boundary="page-sequence"/>
          </fo:marker>
        </fo:conditional-page-master-reference>
      </fo:repeatable-page-master-alternatives>
    </fo:page-sequence-master>
  </fo:declarations>
</fo:root>
```

위의 예제에서는 `<fo:block>` 요소 안에 `<fo:basic-link>` 요소를 사용하여 문서속성을 추가했습니다. `external-destination` 속성에 문서속성의 값을 지정하고, `<fo:retrieve-marker>` 요소를 사용하여 문서속성 값을 나타내도록 설정합니다.

### FOP 설정 파일에 문서속성 처리 설정 추가하기

FOP 설정 파일에 문서속성 처리를 위한 설정을 추가해야 합니다. 다음은 FOP 설정 파일의 예시입니다:

```xml
<fop version="1.1">
  <renderer mime="application/pdf">
    <fonts>
      <!-- 폰트 설정 -->
    </fonts>
    <extensions>
	  <!-- 기타 확장 설정 -->
    </extensions>
    <document-properties>
      <meta>
        <!-- 문서속성 설정 -->
      </meta>
    </document-properties>
  </renderer>
</fop>
```

위의 예제에서는 `<document-properties>` 요소 안에 `<meta>` 요소를 사용하여 문서속성을 설정합니다. `<meta>` 요소 안에는 `<property>` 요소를 사용하여 각각의 문서속성을 지정합니다.

### Java 코드에서 문서속성 설정하기

Java 코드에서 Apache FOP를 사용하여 문서를 생성할 때, 문서속성 값을 설정해야 합니다. 다음은 Java 코드에서 문서속성을 설정하는 예시입니다:

```java
import org.apache.fop.apps.*;
import java.util.HashMap;
 
public class FOPExample {
  public static void main(String[] args) {
    try {
      // FOP 설정 파일 로드
      FopFactoryBuilder fopFactoryBuilder = new FopConfParser(getClass().getResourceAsStream("fop.xconf")).getFopFactoryBuilder();
      FopFactory fopFactory = fopFactoryBuilder.build();
      
      // FO 파일 로드
      StreamSource xmlSource = new StreamSource(new File("input.fo"));
      
      // FOP 기본 설정 생성
      FOUserAgent userAgent = fopFactory.newFOUserAgent();
      
      // 문서속성 설정
      HashMap<String, String> metadata = new HashMap<>();
      metadata.put("Title", "제목");
      metadata.put("Author", "작성자");
      userAgent.setMetadata(metadata);
      
      // PDF 파일 생성
      Fop fop = fopFactory.newFop(MimeConstants.MIME_PDF, userAgent, new FileOutputStream("output.pdf"));
      TransformerFactory factory = TransformerFactory.newInstance();
      Transformer transformer = factory.newTransformer();
      
      Result result = new SAXResult(fop.getDefaultHandler());
      transformer.transform(xmlSource, result);
      
      System.out.println("PDF 파일 생성 완료.");
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

위의 예제에서는 `FOUserAgent` 객체를 사용하여 문서속성 값을 설정하고, `setMetadata()` 메서드를 호출하여 값을 지정합니다. 문서속성과 값을 추가하기 위해서는 `HashMap`을 사용할 수 있습니다.

## 결론

Java에서 Apache FOP를 사용하여 문서속성(metadata)을 처리하는 방법을 알아보았습니다. 문서속성은 문서에 대한 추가적인 정보를 제공하므로, 문서 관리 및 검색에 유용하게 활용될 수 있습니다. Apache FOP를 사용하여 다양한 형식의 문서로 변환할 때, 문서속성을 적절히 설정하여 보다 유연하고 효율적인 문서 처리를 할 수 있습니다.

## 참고 자료

- [Apache FOP 공식 웹사이트](https://xmlgraphics.apache.org/fop/)
- [Apache FOP 문서속성 설정 가이드](https://xmlgraphics.apache.org/fop/1.1/MetaData.html)