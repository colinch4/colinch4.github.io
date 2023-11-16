---
layout: post
title: "[java] TestContainers를 사용하여 AWS Lambda 흉내내기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

AWS Lambda는 서버리스 아키텍처를 구현할 수 있는 플랫폼으로, 개발자들은 운영에 신경 쓰지 않고 코드를 작성할 수 있습니다. 하지만 로컬 환경에서 Lambda 함수를 테스트하려면 어려움이 있습니다. 이때 TestContainers를 활용하여 로컬에서 AWS Lambda를 흉내내는 방법을 알아보겠습니다.

## 1. TestContainers란?

TestContainers는 테스트 환경에서 외부 시스템과의 통합 테스트를 위한 도구입니다. 우리가 테스트하려는 시스템의 컨테이너를 프로그래밍 방식으로 관리하고 제어할 수 있습니다. AWS Lambda를 흉내내기 위해 TestContainers를 사용할 것입니다.

## 2. AWS Lambda 테스트용 컨테이너 생성하기

AWS Lambda를 테스트하기 위해 TestContainers에서 제공하는 `GenericContainer`를 사용해보겠습니다. 다음은 간단한 예제 코드입니다.

```java
import org.testcontainers.containers.GenericContainer;
import org.testcontainers.containers.Network;

public class LambdaContainer extends GenericContainer<LambdaContainer> {

    private static final int LAMBDA_PORT = 9000;
    private static final int LAMBDA_CONTAINER_TIMEOUT_SECONDS = 60;
    private static final String LAMBDA_IMAGE_NAME = "amazon/aws-lambda-java:latest";

    public LambdaContainer(Network network) {
        super(LAMBDA_IMAGE_NAME);
        this.setPortBindings(Arrays.asList(LAMBDA_PORT));
        this.withNetwork(network);
        this.withStartupTimeout(Duration.ofSeconds(LAMBDA_CONTAINER_TIMEOUT_SECONDS));
    }

    @Override
    public Integer getMappedPort(int originalPort) {
        return super.getExternalPort(LAMBDA_PORT);
    }
}
```

위 코드에서는 `LambdaContainer`라는 클래스를 정의하고, `GenericContainer`를 상속받아 AWS Lambda용 컨테이너를 생성합니다. `LAMBDA_IMAGE_NAME`은 AWS Lambda의 컨테이너 이미지 이름입니다. 생성된 컨테이너는 테스트용 네트워크에 연결하고, 포트 바인딩을 통해 로컬 포트로 사용할 수 있게 설정합니다.

## 3. AWS Lambda 함수 실행하기

테스트용 컨테이너가 정상적으로 생성되었다면, 이제 AWS Lambda 함수를 실행해보겠습니다. 다음은 예제 코드입니다.

```java
import software.amazon.awssdk.core.SdkBytes;
import software.amazon.awssdk.services.lambda.LambdaClient;
import software.amazon.awssdk.services.lambda.model.InvokeRequest;
import software.amazon.awssdk.services.lambda.model.InvokeResponse;

public class LambdaClientWrapper {

    private static final String LAMBDA_FUNCTION_NAME = "my-lambda-function";
    private static final String AWS_REGION = "us-east-1";
    private static final String LAMBDA_HANDLER = "MyLambdaHandler";

    public String invokeLambda(String payload) {
        try (LambdaClient lambdaClient = LambdaClient.builder().region(Region.of(AWS_REGION)).build()) {
            InvokeRequest request = InvokeRequest.builder()
                .functionName(LAMBDA_FUNCTION_NAME)
                .invocationType(InvocationType.REQUEST_RESPONSE)
                .payload(SdkBytes.fromUtf8String(payload))
                .build();

            InvokeResponse response = lambdaClient.invoke(request);
            return response.payload().asString(StandardCharsets.UTF_8);
        }
    }
}
```

위 코드에서는 `LambdaClientWrapper`라는 클래스를 정의하고, `invokeLambda` 메소드를 통해 AWS Lambda 함수를 실행합니다. `LAMBDA_FUNCTION_NAME`은 실행할 함수의 이름, `AWS_REGION`은 AWS 리전, `LAMBDA_HANDLER`는 AWS Lambda 핸들러 이름입니다.

테스트 코드에서는 생성한 테스트용 컨테이너를 사용하여 `LambdaClientWrapper`를 초기화한 후, `invokeLambda` 메소드로 AWS Lambda 함수를 호출합니다. 반환된 결과를 확인할 수 있습니다.

## 4. 테스트 코드 작성하기

이제 모든 준비가 끝났으므로 TestContainers와 AWS Lambda를 사용하는 테스트 코드를 작성해볼 수 있습니다. 다음은 예제 코드입니다.

```java
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.Network;
import org.testcontainers.junit.jupiter.Testcontainers;

import static org.junit.jupiter.api.Assertions.assertEquals;

@Testcontainers
class LambdaTest {

    private static final Network network = Network.newNetwork();

    private static final LambdaContainer lambdaContainer = new LambdaContainer(network);

    @Test
    void testLambdaFunction() {
        lambdaContainer.start();

        String response = new LambdaClientWrapper().invokeLambda("{ \"key\": \"value\" }");
        assertEquals("Hello, value!", response);

        lambdaContainer.stop();
    }
}
```

위 코드에서는 `Testcontainers` 애노테이션을 사용하여 TestContainers를 실행환경으로 설정합니다. `LambdaContainer` 객체를 생성하여 테스트용 컨테이너를 실행하고, `LambdaClientWrapper`를 이용해 AWS Lambda 함수를 호출합니다. 기대되는 결과와 실제 결과를 비교하여 테스트를 수행합니다. 테스트가 완료된 후에는 컨테이너를 중지시킵니다.

## 5. 결론

TestContainers를 사용하여 AWS Lambda를 흉내내는 방법에 대해 알아보았습니다. 이를 통해 로컬에서 AWS Lambda 함수를 테스트하고 디버깅하는 일이 더욱 쉬워질 것입니다. TestContainers의 다양한 기능과 AWS Lambda의 유연함을 활용하여 원활한 테스트를 진행해보세요.

## 참고 자료

- [TestContainers 공식 문서](https://www.testcontainers.org/)
- [AWS Lambda 공식 문서](https://aws.amazon.com/lambda/)