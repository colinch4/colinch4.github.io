---
layout: post
title: "[java] Java Play Framework에서의 OAuth 인증 방법은 어떻게 되나요?"
description: " "
date: 2023-11-23
tags: [java]
comments: true
share: true
---

OAuth는 외부 서비스로부터 인증을 받아 액세스 토큰을 얻어 Play Framework 애플리케이션 내에서 사용할 수 있는 인증 방식입니다. 다음은 Java Play Framework에서 OAuth 인증을 구현하는 방법입니다.

1. 의존성 추가
Play Framework 애플리케이션의 `build.sbt` 파일에 다음과 같이 의존성을 추가하세요.

```scala
libraryDependencies += "com.typesafe.play" %% "play-oauth2-provider" % "2.1.0"
```

2. `oauth.conf` 파일 설정
Play Framework 애플리케이션의 `conf` 폴더 내에 `oauth.conf` 파일을 생성하고 다음과 같이 OAuth 제공자에 대한 설정을 작성하세요.

```conf
myoauthprovider {
  authorizationUrl = "https://myoauthprovider.com/auth"
  tokenUrl = "https://myoauthprovider.com/token"
  clientId = "your_client_id"
  clientSecret = "your_client_secret"
  scope = "read write"
  callbackUrl = "/oauth/callback"
}
```

3. OAuth 제공자 플러그인 등록
Play Framework 애플리케이션의 `conf/application.conf` 파일을 열고 다음과 같이 OAuth 제공자 플러그인을 등록하세요.

```
play.modules.enabled += "play.api.libs.oauth.MyOAuthProviderModule"
```

4. 컨트롤러 작성
OAuth 인증 흐름을 처리하기 위한 컨트롤러를 작성하세요. 예를 들어, `OAuthController`라는 컨트롤러를 생성하고 다음과 같이 작성할 수 있습니다.

```java
import play.api.libs.oauth.{ ConsumerKey, ServiceInfo }
import play.api.libs.ws.WSRequest
import play.api.mvc.{ AbstractController, ControllerComponents }
import play.api.Configuration
import javax.inject.Inject

class OAuthController @Inject()(cc: ControllerComponents, config: Configuration) 
  extends AbstractController(cc) {
  
  def authenticate = Action { implicit request =>
    val oauthProvider = config.get[Configuration]("myoauthprovider")
    val consumerKey = ConsumerKey(oauthProvider.get[String]("clientId"), oauthProvider.get[String]("clientSecret"))
    val serviceInfo = ServiceInfo(
      request.getQueryString("authorizationUrl").getOrElse(""), 
      request.getQueryString("tokenUrl").getOrElse(""), 
      None
    )
    val callbackUrl = routes.OAuthController.callback().absoluteURL()
    val oauth = OAuth(ServiceInfo, false)
    
    oauth.retrieveRequestToken(callbackUrl) match {
      case Right(requestToken) => {
        Redirect(oauth.redirectUrl(requestToken)).withSession("requestToken" -> requestToken.token, "requestSecret" -> requestToken.secret)
      }
      case Left(error) => throw new Exception("Error retrieving request token: " + error.getMessage())
    }
  }
  
  def callback = Action { implicit request =>
    val oauthProvider = config.get[Configuration]("myoauthprovider")
    val consumerKey = ConsumerKey(oauthProvider.get[String]("clientId"), oauthProvider.get[String]("clientSecret"))
    val serviceInfo = ServiceInfo(
      request.getQueryString("authorizationUrl").getOrElse(""), 
      request.getQueryString("tokenUrl").getOrElse(""), 
      None
    )
    val oauth = OAuth(ServiceInfo, false)
    
    val requestToken = RequestToken(Controller.request.session.get("requestToken").getOrElse(""),
                                   Controller.request.session.get("requestSecret").getOrElse(""))
    
    oauth.retrieveAccessToken(requestToken, request.queryString.get("oauth_verifier").head) match {
      case Right(accessToken) => {
        // 인증 성공 후 수행할 작업을 추가하세요.
        // accessToken을 사용하여 OAuth 제공자의 API를 호출할 수 있습니다.
        Ok("OAuth 인증이 완료되었습니다.")
      }
      case Left(error) => throw new Exception("Error retrieving access token: " + error.getMessage())
    }
  }
}
```

5. 라우팅 설정
Play Framework 애플리케이션의 `conf/routes` 파일에 다음과 같이 라우팅을 설정하세요.

```conf
GET     /oauth/authenticate         controllers.OAuthController.authenticate
GET     /oauth/callback             controllers.OAuthController.callback
```

이제 OAuth 인증을 위한 설정이 완료되었습니다. `/oauth/authenticate` 경로로 접근하면 OAuth 인증 절차가 시작되고, 인증이 완료되면 `/oauth/callback` 경로로 리디렉션됩니다.

추가적인 설정 및 OAuth 제공자의 API를 호출하는 방법은 해당 OAuth 제공자의 문서를 참조해주세요.