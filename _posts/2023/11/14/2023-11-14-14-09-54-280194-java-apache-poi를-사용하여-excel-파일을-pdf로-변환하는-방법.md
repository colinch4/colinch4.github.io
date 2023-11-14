---
layout: post
title: "[java] Java Apache POI를 사용하여 Excel 파일을 PDF로 변환하는 방법"
description: " "
date: 2023-11-14
tags: [java]
comments: true
share: true
---

Apache POI는 자바로 Microsoft Office 포맷인 Excel 파일을 조작할 수 있는 라이브러리입니다. 이번에는 Apache POI를 사용하여 Excel 파일을 PDF로 변환하는 방법에 대해 알아보겠습니다.

## 1. Apache POI와 Apache PDFBox 의존성 추가

먼저, Maven 또는 Gradle을 사용하여 프로젝트에 Apache POI와 Apache PDFBox의존성을 추가해야 합니다. 프로젝트의 build 파일에서 아래 의존성을 추가해주세요.

```xml
<!-- Apache POI -->
<dependency>
    <groupId>org.apache.poi</groupId>
    <artifactId>poi</artifactId>
    <version>4.1.2</version>
</dependency>

<!-- Apache PDFBox -->
<dependency>
    <groupId>org.apache.pdfbox</groupId>
    <artifactId>pdfbox</artifactId>
    <version>2.0.21</version>
</dependency>
```

## 2. Excel 파일을 PDF로 변환하는 코드 작성

Excel 파일을 PDF로 변환하기 위해 다음과 같은 단계를 따라야 합니다:

1. Excel 파일을 읽어들입니다.
2. PDF 문서를 생성합니다.
3. Excel 파일의 내용을 PDF로 복사합니다.
4. PDF 문서를 저장합니다.

아래는 Java 코드로 구현된 Excel 파일을 PDF로 변환하는 예제입니다:

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.apache.pdfbox.pdmodel.*;
import org.apache.pdfbox.util.*;

import java.io.*;

public class ExcelToPdfConverter {

    public static void main(String[] args) {
        try {
            // 1. Excel 파일 읽기
            FileInputStream excelFile = new FileInputStream("input.xlsx");
            Workbook workbook = new XSSFWorkbook(excelFile);
            Sheet sheet = workbook.getSheetAt(0);

            // 2. PDF 문서 생성
            PDDocument document = new PDDocument();
            PDPage page = new PDPage();
            document.addPage(page);

            // 3. Excel 파일 내용을 PDF로 복사
            PDFGraphics2D graphics2D = new PDFGraphics2D(document, page);
            for (Row row : sheet) {
                for (Cell cell : row) {
                    graphics2D.drawString(cell.getStringCellValue(), cell.getColumnIndex() * 100, cell.getRowIndex() * 20);
                }
            }

            // 4. PDF 문서 저장
            document.save("output.pdf");
            document.close();

            System.out.println("Excel 파일이 성공적으로 PDF로 변환되었습니다.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

이 예제에서는 `input.xlsx` 파일을 읽어들여서 첫 번째 시트의 내용을 PDF로 생성하고, `output.pdf` 파일로 저장합니다.

## 3. 실행 결과 확인

위 예제를 실행하면, `input.xlsx` 파일의 내용이 `output.pdf` 파일로 성공적으로 변환됩니다. `output.pdf` 파일을 열어서 변환된 내용을 확인해보세요.

## 참고 자료

- [Apache POI 공식 문서](https://poi.apache.org/)
- [Apache PDFBox 공식 문서](https://pdfbox.apache.org/)