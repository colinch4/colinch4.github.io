---
layout: post
title: "[java] Java Cucumber에서 Page Object 패턴 사용하기"
description: " "
date: 2023-11-15
tags: [java]
comments: true
share: true
---

## 소개
Java Cucumber는 BDD(Behavior Driven Development)를 위한 자바 테스트 프레임워크입니다. Cucumber를 통해 BDD 스타일로 테스트 코드를 작성하고 실행할 수 있습니다. Page Object 패턴은 테스트 코드를 보다 모듈화하고 재사용성을 높이기 위해 사용되는 디자인 패턴입니다. 이 패턴을 사용하면 테스트 코드를 유지보수하기 쉽고 가독성을 높일 수 있습니다.

## Page Object 패턴이란?
Page Object 패턴은 웹 애플리케이션의 각 페이지를 객체로 추상화하는 방법입니다. 예를 들어, 로그인 페이지를 나타내는 LoginPage 객체, 회원가입 페이지를 나타내는 SignUpPage 객체 등을 만들 수 있습니다. 각 페이지 객체는 그 페이지와 관련된 동작과 상태를 캡슐화하고, 테스트 코드에서 해당 페이지 객체를 사용하여 테스트를 진행할 수 있습니다.

## Page Object 패턴의 장점
1. **재사용성 증가**: 각 페이지 객체를 모듈화하여 필요한 곳에서 호출하므로 코드 재사용성이 높아집니다.
2. **유지보수 용이**: 페이지 변경이 필요한 경우 해당 페이지 객체만 수정하면 되므로 유지보수가 용이합니다.
3. **가독성 향상**: 테스트 코드가 페이지 구조를 반영하므로 가독성이 높아집니다.
4. **테스트 코드 분리**: 테스트 로직과 페이지 동작 및 상태가 분리되어 테스트 코드가 더욱 깔끔해집니다.

## Page Object 패턴 예제 코드
다음은 Java Cucumber에서 Page Object 패턴을 사용하는 예제 코드입니다.

```java
public class LoginPage {
    private final WebDriver driver;
    
    @FindBy(id = "username")
    private WebElement usernameField;
    
    @FindBy(id = "password")
    private WebElement passwordField;
    
    @FindBy(id = "submit-button")
    private WebElement submitButton;
    
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    
    public void enterUsername(String username) {
        usernameField.sendKeys(username);
    }
    
    public void enterPassword(String password) {
        passwordField.sendKeys(password);
    }
    
    public void clickSubmitButton() {
        submitButton.click();
    }
}

public class LoginTest {
    private final WebDriver driver;
    private final LoginPage loginPage;
    
    public LoginTest() {
        driver = new ChromeDriver();
        loginPage = new LoginPage(driver);
    }
    
    @Given("I am on the login page")
    public void iAmOnTheLoginPage() {
        driver.get("https://example.com/login");
    }
    
    @When("I enter the username {string}")
    public void iEnterTheUsername(String username) {
        loginPage.enterUsername(username);
    }
    
    @When("I enter the password {string}")
    public void iEnterThePassword(String password) {
        loginPage.enterPassword(password);
    }
    
    @When("I click the submit button")
    public void iClickTheSubmitButton() {
        loginPage.clickSubmitButton();
    }
    
    @Then("I should be logged in")
    public void iShouldBeLoggedIn() {
        // Verify login logic
    }
}
```

위 예제 코드에서 LoginPage 클래스는 로그인 페이지를 나타내는 Page Object 입니다. WebDriver 기반으로 동작하며, 페이지의 요소들을 WebElement로 정의하고 필요한 동작 메서드를 구현합니다. LoginTest 클래스에서는 LoginPage 객체를 통해 로그인 테스트를 진행합니다. 각각의 스텝에 해당하는 메서드를 호출하여 테스트를 구현합니다.

## 결론
Java Cucumber에서 Page Object 패턴을 사용하면 테스트 코드의 가독성과 유지보수성을 향상시킬 수 있습니다. Page Object 패턴을 적용하여 테스트 코드를 작성해보세요.