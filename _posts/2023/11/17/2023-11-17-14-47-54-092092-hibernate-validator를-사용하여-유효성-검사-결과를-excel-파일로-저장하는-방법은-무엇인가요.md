---
layout: post
title: "[java] Hibernate Validator를 사용하여 유효성 검사 결과를 Excel 파일로 저장하는 방법은 무엇인가요?"
description: " "
date: 2023-11-17
tags: [java]
comments: true
share: true
---

- [은행번호 유효성 검사](#은행번호-유효성-검사)
- [Excel 파일 생성](#excel-파일-생성)
- [결론](#결론)

---

## 은행번호 유효성 검사

Hibernate Validator는 Java에서 객체의 유효성 검사를 쉽게 수행할 수 있는 라이브러리입니다. 은행번호의 유효성을 검사하고, 검사 결과를 Excel 파일로 저장하는 예제를 작성해보겠습니다.

먼저, 은행번호를 나타내는 `BankAccount` 클래스를 생성합니다.

```java
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Pattern;

public class BankAccount {

    @NotBlank(message = "은행번호는 필수 입력 항목입니다.")
    @Pattern(regexp = "\\d{3}-\\d{3}-\\d{6}", message = "올바른 은행번호 형식이 아닙니다. (예: 123-456-789012)")
    private String accountNumber;

    // 생성자, getter, setter 등 생략
}
```

여기서 `@NotBlank`는 은행번호가 비어 있을 수 없음을, `@Pattern`은 지정된 정규식에 부합해야 함을 나타냅니다.

다음으로, 유효성 검사를 수행하고 검사 결과를 Excel 파일로 저장하는 `BankAccountValidator` 클래스를 작성합니다.

```java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Set;

public class BankAccountValidator {

    public static void main(String[] args) {
        // Hibernate Validator 초기화
        Validator validator = Validation.buildDefaultValidatorFactory().getValidator();

        // 유효성 검사를 수행할 객체 생성
        BankAccount bankAccount = new BankAccount();
        bankAccount.setAccountNumber("123-456-789012");

        // 유효성 검사 수행
        Set<ConstraintViolation<BankAccount>> violations = validator.validate(bankAccount);

        // 검사 결과를 Excel 파일에 저장
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("BankAccountValidation");
            int rowNum = 0;
            for (ConstraintViolation<BankAccount> violation : violations) {
                Row row = sheet.createRow(rowNum++);
                row.createCell(0).setCellValue(violation.getPropertyPath().toString());
                row.createCell(1).setCellValue(violation.getMessage());
            }
            // Excel 파일 저장
            FileOutputStream fileOut = new FileOutputStream("validation_result.xlsx");
            workbook.write(fileOut);
            fileOut.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

위 예제에서는 Hibernate Validator를 사용하여 `BankAccount` 객체의 유효성을 검사합니다. 유효성 검사 결과는 `ConstraintViolation` 객체의 형태로 반환됩니다. 이 결과를 Apache POI 라이브러리를 사용하여 Excel 파일에 저장합니다.

## Excel 파일 생성

위 예제 코드를 실행하면, 유효성 검사 결과가 `validation_result.xlsx` 파일에 저장됩니다. 이 파일을 열어보면, 은행번호에 대한 유효성 검사 결과가 엑셀 시트에 표시됩니다.

## 결론

Hibernate Validator를 사용하여 Java 객체의 유효성을 검사하고, 검사 결과를 Excel 파일로 저장하는 방법을 살펴보았습니다. 이를 응용하여 다양한 유효성 검사와 결과 저장 기능을 구현할 수 있습니다. Hibernate Validator와 Apache POI 라이브러리에 대한 자세한 내용은 공식 문서를 참조하시기 바랍니다.