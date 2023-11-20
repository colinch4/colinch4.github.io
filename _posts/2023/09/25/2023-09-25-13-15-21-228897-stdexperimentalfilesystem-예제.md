---
layout: post
title: "std::experimental::filesystem 예제"
description: " "
date: 2023-09-25
tags: [c++]
comments: true
share: true
---

먼저, `std::experimental::filesystem` 네임스페이스를 사용하기 위해 다음과 같이 헤더를 추가합니다:

```cpp
#include <iostream>
#include <experimental/filesystem>

namespace fs = std::experimental::filesystem;
```

이제 예제를 통해 `std::experimental::filesystem`의 기본 기능을 확인해보겠습니다. 아래 예제는 현재 작업 디렉토리에서 디렉토리를 생성하고, 해당 디렉토리에 파일을 생성한 후, 생성한 파일의 크기를 출력하는 코드입니다.

```cpp
int main() {
    fs::path directoryPath = fs::current_path() / "example_directory";

    // 디렉토리 생성
    fs::create_directory(directoryPath);

    // 파일 경로 생성
    fs::path filePath = directoryPath / "example_file.txt";

    // 파일 생성 및 쓰기
    std::ofstream outfile(filePath);
    outfile << "Hello, World!\n";
    outfile.close();

    // 파일 크기 출력
    std::cout << "File Size: " << fs::file_size(filePath) << " bytes" << std::endl;

    // 디렉토리와 파일 삭제
    fs::remove_all(directoryPath);

    return 0;
}
```

위의 예제에서 `fs::current_path()` 함수를 사용하여 현재 작업 디렉토리를 얻고, `/` 연산자를 사용하여 경로를 조합합니다. `fs::create_directory()` 함수로 디렉토리를 생성하고, `fs::path` 클래스를 사용하여 파일 경로를 생성합니다. 파일을 생성하고 쓴 후, `fs::file_size()` 함수로 파일의 크기를 얻어 출력합니다. 마지막으로, `fs::remove_all()` 함수로 생성한 디렉토리와 파일을 삭제합니다.

`std::experimental::filesystem` 라이브러리를 사용하면 파일 및 디렉토리 관리 작업을 쉽게 처리할 수 있습니다. 위 예제를 참고하여 필요한 파일 시스템 작업을 수행할 수 있습니다.