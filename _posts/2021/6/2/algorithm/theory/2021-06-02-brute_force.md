# Brute Force

- 완벽탐색 알고리즘

- 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건에 충족되는 결과만을 가져온다.

<br>

## 예제

### 가까운 매장 찾기

```python
# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    # for문을 이용하여 모두 검사
    pair = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            # pair의 거리와 coordinates의 i인덱스와 j인덱스의 거리를 비교 후 pair 업데이트
            if distance(pair[0], pair[1]) > distance(coordinates[i], coordinates[j]):
                pair[0], pair[1] = coordinates[i], coordinates[j]
    return pair

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))   # [(2, 3), (3, 4)]
```

<br>

### 비가 내렸을 때 담기는 물의 총량을 계산하기

```python
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스를 돌면서 해당 칸에 담기는 빗물의 양을 구한다.
    # 0번 인덱스와 마지막 인덱스는 볼필요가 없다.
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 높이를 구한다.
        left_max = max(buildings[:i])
        right_max = max(buildings[i+1:])

        # 현재 인덱스에 빗물이 담길 수 있느 높이
        upper_bound = min(left_max, right_max)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))        # 10
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))      # 6
```
