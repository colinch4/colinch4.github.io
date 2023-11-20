---
layout: post
title: "[java] Java Apache Jena를 사용하여 Turtle 형식의 RDF 데이터를 읽는 방법은?"
description: " "
date: 2023-11-20
tags: [java]
comments: true
share: true
---

Apache Jena는 Java로 구현된 Semantic Web 프레임워크로, RDF(Resoucre Description Framework) 데이터를 다루는 데 사용됩니다. 이 프레임워크를 사용하여 Turtle 형식의 RDF 데이터를 읽는 방법에 대해 알아보겠습니다.

먼저, Apache Jena 라이브러리를 프로젝트에 추가해야 합니다. Maven을 사용하는 경우, pom.xml 파일에 다음 종속성을 추가합니다:

```xml
<dependency>
    <groupId>org.apache.jena</groupId>
    <artifactId>apache-jena-libs</artifactId>
    <version>3.16.0</version>
</dependency>
```

그런 다음, 다음과 같이 Turtle 형식의 RDF 파일을 읽는 예제 코드를 작성할 수 있습니다:

```java
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.rdf.model.Statement;
import org.apache.jena.rdf.model.StmtIterator;
import org.apache.jena.util.FileManager;

public class RDFReaderExample {
    public static void main(String[] args) {
        // Turtle 형식의 RDF 데이터 파일 경로
        String rdfFile = "path/to/data.ttl";

        // 모델 생성
        Model model = ModelFactory.createDefaultModel();

        // 파일 매니저를 사용하여 RDF 파일 읽기
        FileManager fileManager = FileManager.get();
        model = fileManager.readModel(model, rdfFile, "TURTLE");

        // 모델에서 모든 문장(statement)을 반복하여 출력
        StmtIterator iterator = model.listStatements();
        while (iterator.hasNext()) {
            Statement statement = iterator.nextStatement();
            Resource subject = statement.getSubject();
            Resource predicate = statement.getPredicate();
            Resource object = statement.getObject();

            System.out.println(subject + " " + predicate + " " + object);
        }

        // 모델 사용 후에는 리소스 해제하기
        model.close();
    }
}
```

위의 코드에서는 Apache Jena의 FileManager를 사용하여 Turtle 형식의 RDF 파일을 읽는 방법을 보여줍니다. Model 객체를 생성한 후 FileManager의 readModel 메서드를 사용하여 해당 파일을 모델에 로드합니다. 이후 모델의 모든 문장을 반복하여 출력하고, 모델을 사용한 후에는 리소스를 해제합니다.

이를 실행하면 Turtle 형식의 RDF 데이터 파일의 내용이 출력됩니다.

참고문헌:
- Apache Jena 공식 문서: https://jena.apache.org/documentation/rdf_io.html
- Apache Jena Github 저장소: https://github.com/apache/jena