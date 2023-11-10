---
layout: post
title: "파이썬 환경 설정 패턴: Singleton, Factory, Dependency Injection"
description: " "
date: 2023-11-10
tags: [opensource, python]
comments: true
share: true
---

파이썬 애플리케이션을 개발하면서, 환경 설정은 중요한 부분입니다. 애플리케이션의 동작을 제어하기 위해 환경 설정을 유지하고 업데이트하는 것은 필수적입니다. 이를 위해 파이썬에서는 Singleton, Factory, Dependency Injection과 같은 패턴을 사용할 수 있습니다.

## Singleton 패턴

Singleton 패턴은 애플리케이션에서 특정 클래스의 인스턴스를 오직 하나만 생성하고, 이를 공유하는 패턴입니다. 이를 통해 여러 곳에서 동일한 인스턴스를 사용할 수 있습니다. Singleton 패턴을 사용하면, 애플리케이션 전체에서 환경 설정을 단 하나의 인스턴스로 관리할 수 있습니다.

예를 들어, 아래의 코드는 Singleton 패턴을 사용하여 환경 설정을 관리하는 클래스의 예시입니다.

```python
class Config:
    __instance = None

    @staticmethod
    def get():
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self):
        self.config_data = {}

    def set(self, key, value):
        self.config_data[key] = value

    def get(self, key):
        return self.config_data.get(key)
```

위의 코드에서 `Config` 클래스는 `get` 메소드를 통해 오직 하나의 인스턴스를 반환합니다. `set` 메소드를 통해 특정 키에 해당하는 값을 설정하고, `get` 메소드를 통해 해당 키의 값을 가져올 수 있습니다.

## Factory 패턴

Factory 패턴은 객체 생성을 캡슐화하여, 클라이언트가 구체적인 클래스를 직접 생성하는 것이 아니라 팩토리를 통해 객체를 생성하도록 하는 패턴입니다. 환경 설정을 위한 객체를 생성할 때, Factory 패턴을 사용하면 더 유연하고 확장 가능한 코드를 작성할 수 있습니다.

아래의 코드 예시는 Factory 패턴을 사용하여 환경 설정 객체를 생성하는 예시입니다.

```python
class Config:
    def __init__(self):
        self.config_data = {}

    def set(self, key, value):
        self.config_data[key] = value

    def get(self, key):
        return self.config_data.get(key)

class ConfigFactory:
    def create(self):
        # 환경 설정을 초기화하고 필요한 값들을 설정하는 로직
        config = Config()
        config.set('api_key', 'my_api_key')
        config.set('db_url', 'my_db_url')
        return config

config_factory = ConfigFactory()
config = config_factory.create()
```

위의 코드에서 `ConfigFactory` 클래스는 `create` 메소드를 통해 환경 설정 객체를 생성합니다. `create` 메소드 내에서 초기화 로직과 필요한 값들을 설정할 수 있습니다.

## Dependency Injection 패턴

Dependency Injection 패턴은 객체 간의 의존성을 명시적으로 주입하는 패턴입니다. 환경 설정 객체의 의존성을 주입함으로써, 애플리케이션의 다른 부분에서도 동일한 환경 설정을 사용할 수 있습니다. 이를 통해 유연하고 테스트 가능한 코드를 작성할 수 있습니다.

아래의 코드는 Dependency Injection 패턴을 사용하여 환경 설정 객체를 주입받는 예시입니다.

```python
class Config:
    def __init__(self):
        self.config_data = {}

    def set(self, key, value):
        self.config_data[key] = value

    def get(self, key):
        return self.config_data.get(key)

class SomeClass:
    def __init__(self, config):
        self.config = config

    def do_something(self):
        api_key = self.config.get('api_key')
        db_url = self.config.get('db_url')
        # 환경 설정을 사용하여 작업 수행

config = Config()
config.set('api_key', 'my_api_key')
config.set('db_url', 'my_db_url')

some_obj = SomeClass(config)
some_obj.do_something()
```

위의 코드에서 `SomeClass`는 `config` 인자를 받아 의존성을 주입받는 형태로 구현되어 있습니다. 이를 통해 `SomeClass` 내에서 `config` 객체를 사용하여 작업을 수행할 수 있습니다.

## 결론

파이썬 애플리케이션에서 환경 설정을 관리하는 방법으로 Singleton, Factory, Dependency Injection 패턴을 적용할 수 있습니다. 이러한 패턴을 사용하면 환경 설정을 효율적으로 유지하고 업데이트할 수 있으며, 유연하고 확장 가능한 코드를 작성할 수 있습니다.

#opensource #python