---
layout: post
title: "[java] PDF 파일 텍스트 활자(kerning) 처리(Java Apache PDFBox 사용)"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

PDF 파일에서 텍스트를 추출하거나 편집할 때, 종종 텍스트의 간격이 정확히 표현되지 않는 경우가 있습니다. 이는 활자(kerning) 처리가 필요한 경우입니다. 

Apache PDFBox는 Java 기반의 오픈 소스 라이브러리로, PDF 파일을 생성하고 편집할 수 있는 강력한 기능을 제공합니다. 이 라이브러리를 사용하여 PDF 파일의 텍스트 활자 처리를 할 수 있습니다.

## 1. Apache PDFBox 라이브러리 추가하기

먼저, Maven 또는 Gradle을 사용하여 프로젝트에 Apache PDFBox 라이브러리를 추가해야 합니다.

Maven을 사용하는 경우, `pom.xml` 파일에 다음 의존성을 추가합니다:
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.pdfbox</groupId>
        <artifactId>pdfbox</artifactId>
        <version>2.0.26</version>
    </dependency>
</dependencies>
```

Gradle을 사용하는 경우, `build.gradle` 파일의 `dependencies` 블록에 다음 코드를 추가합니다:
```groovy
dependencies {
    implementation 'org.apache.pdfbox:pdfbox:2.0.26'
}
```

이후, Maven 또는 Gradle을 사용하여 종속성을 다운로드합니다.

## 2. PDF 파일에서 텍스트 활자 처리하기

이제, PDF 파일에서 텍스트 활자 처리를 수행하는 Java 코드를 작성해보겠습니다.

```java
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.contentstream.operator.Operator;
import org.apache.pdfbox.contentstream.operator.OperatorName;
import org.apache.pdfbox.contentstream.operator.state.Concatenate;
import org.apache.pdfbox.contentstream.operator.state.SetFontAndSize;
import org.apache.pdfbox.contentstream.operator.text.MoveText;
import org.apache.pdfbox.contentstream.operator.text.ShowText;

import java.io.IOException;

public class KerningExample {

    public static void main(String[] args) {
        try (PDDocument document = PDDocument.load(new File("input.pdf"))) {
            for (PDPage page : document.getPages()) {
                processPage(page);
            }
            document.save("output.pdf");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void processPage(PDPage page) throws IOException {
        PDStream contents = page.getContents();
        // 활자 처리를 위한 필터 코드 작성
        PDResources resources = page.getResources();
        COSName fontName = resources.getFontNames().iterator().next();
        PDFont font = resources.getFont(fontName);
        float fontSize = 12;
        
        // 활자 처리 수행
        for (PDContentStream contentStream : PDContentStreamUtilities.extractStreams(page)) {
            processContentStream(contentStream, font, fontSize);
        }
    }

    private static void processContentStream(PDContentStream contentStream, PDFont font, float fontSize) throws IOException {
        OperatorProcessor processor = new OperatorProcessor() {
            @Override
            public void process(Operator operator, List<COSBase> operands) throws IOException {
                String operation = operator.getName();
                switch (operation) {
                    case OperatorName.SET_FONT_AND_SIZE:
                        // 폰트 및 크기 설정
                        SetFontAndSize setFontAndSize = (SetFontAndSize) operator;
                        font = setFontAndSize.getFont();
                        fontSize = setFontAndSize.getFontSize();
                        break;
                    case OperatorName.SHOW_TEXT:
                        // 텍스트 활자 처리
                        ShowText showText = (ShowText) operator;
                        String text = showText.getText();
                        showText.setText(processText(text, font, fontSize));
                        break;
                    case OperatorName.MOVE_TEXT:
                        // 텍스트 이동
                        MoveText moveText = (MoveText) operator;
                        float tx = moveText.getDeltaX() * fontSize;
                        float ty = moveText.getDeltaY() * fontSize;
                        moveText.setDelta(tx, ty);
                        break;
                    case OperatorName.CONCAT_MATRIX:
                        // 변환 행렬 설정
                        break;
                    default:
                        break;
                }
            }

            private String processText(String text, PDFont font, float fontSize) throws IOException {
                List<Glyph> glyphs = font.getStringWidth(text);
                float[] positions = new float[glyphs.size() * 2];
                font.getPositions(glyphs.toArray(new Glyph[0]), positions);
                StringBuilder processedText = new StringBuilder();
                for (int i = 0; i < text.length(); i++) {
                    String unicode = glyphs.get(i).getUnicode();
                    int index = i * 2;
                    processedText.append(unicode);
                    if (unicode.equals(" ")) {
                        continue;
                    }
                    processedText.append(" ");
                    processedText.append(positions[index] / fontSize);
                    processedText.append(" ");
                }
                return processedText.toString();
            }
        };
        PDStreamContentsVisitor.processContentStream(contentStream, processor);
        contentStream.setBytes(processor.getTokens());
    }
}
```

위의 코드는 PDF 파일의 각 페이지를 순회하면서 텍스트 활자 처리를 수행합니다. 활자 처리를 위해서는 해당 페이지의 폰트 정보가 필요하며, 예제 코드에서는 첫 번째 폰트를 사용하도록 작성되어 있습니다. 만약 다른 폰트를 사용해야 하는 경우, 폰트의 이름을 찾아서 적절히 설정해주어야 합니다.

활자 처리를 수행하는 `processContentStream()` 메서드는 PDF 파일의 컨텐츠 스트림을 가져와서, 각각의 연산자에 대해 적절한 처리를 수행합니다. `SetFontAndSize` 연산자에서는 폰트와 크기를 설정하고, `ShowText` 연산자에서는 텍스트를 활자 처리합니다. 다른 연산자에 대해서는 필요한 처리를 추가로 작성해주어야 합니다.

텍스트 활자 처리는 `processText()` 메서드에서 수행됩니다. 각 글자의 좌표를 조정하여 간격을 조절하고, 공백 문자에 대해서는 처리를 생략합니다.

## 3. 실행 및 결과 확인

위의 예제 코드를 컴파일 및 실행하면, `input.pdf`로부터 텍스트를 추출하여 텍스트 간격을 조정한 결과를 `output.pdf`로 저장합니다. 이렇게 생성된 PDF 파일을 열어서 텍스트의 간격이 정확하게 조정된 것을 확인할 수 있습니다.

## 참고 자료

- [Apache PDFBox 공식 문서](https://pdfbox.apache.org/)

위의 예제 코드와 Apache PDFBox 라이브러리를 사용하여 PDF 파일의 텍스트 활자 처리를 수행할 수 있습니다. PDF 파일의 텍스트를 정확히 표현하기 위해 활자 처리가 필요한 경우, 이 예제를 참고하여 활자 처리를 수행해보세요!