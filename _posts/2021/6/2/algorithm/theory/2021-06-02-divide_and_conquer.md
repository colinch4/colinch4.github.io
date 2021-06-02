# Divide And Conquer (분할 정복)

한 문제에대해서 너무 풀기에 크다고 생각되어질 때 나눠서 문제를 푸는 것

<br>

## 단계

1. Divide : 문제를 부분 문제로 나눈다.

2. Conquer : 각 부분 문제를 정복한다.

3. Combine : 부분 문제들의 솔루션을 합쳐서 기존 문제를 해결한다.

<br>

## 예제

### Divide and Conquer로 1부터 N까지 더하기

```python
def consecutive_sum(start, end):
    # Base Case
    if start == end:
        return start

    # 문제를 나누기 위해 중앙 값을 정함 (Divide)
    mid = (start + end) // 2

    # 각 부문 문제를 재귀적으로 풀고(Conquer), 부문문제의 답을 더한다C(Combine).
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))
```
