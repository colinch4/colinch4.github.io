# Dynamic Programming

중복을 피하여 효율적인 알고리즘 짜는 법

<br>

## Dynamic Programming의 조건

- **최적 부분 구조(Optimal Substructure)** : 최적 부분 구조가 있다는 것은 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것!

- 중복되는 부분 문제(Overlapping Subproblems)

<br>

## Memorization

- 중복되는 계산은 한번만 계산 해두어 저장
- 비효율성을 해결하는 알고리즘
- Top-down Approach(하향식 접근)
- 위에서부터 내려오기 때문에 필요한 값만 계산하여 불필요한 계산을 하지 않는다.
- 콜스택이 쌓여 성능에 부하가 걸릴 위험이 있다.

<br>

## Tabulation

- Bottom-up Approach(상향식 접근)
- Table 방식으로 정리
- Memorization이 재귀라면 Tabulation은 반복문
- 처음부터 값을 계산하기 때문에 불 필요한 계산도 함
- 반복문으로 돌려서 성능에 부하는 없음

<br>

## 문제

### 피보나치 수열을 Memorization 방식으로 알고리즘 구현하는 문제입니다.

```python
def fib_memo(n, cache):
    # Base Case
    if n < 3:
        return 1

    # cache에 n이 저장되어 있으면 저장되어있는 값을 바로 리턴
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
'''
Out Put
55
12586269025
354224848179261915075
'''
```

<br>

### 피보나치 수열을 Tabulation 방식으로 알고리즘 구현하는 문제입니다.

```python
def fib_optimized(n):
    # Tabulation을 위한 변수설정
    cur = 1
    pre = 0

    # Tabulation 방식으로 메모리가 cur과 pre만 계속 update 함으로써 공간복잡도 O(1)
    for i in range(1, n):
        cur, pre = pre+cur, cur
    return cur

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))

# 987
# 53316291173
# 146178119651438213260386312206974243796773058
```

모든 값을 계산하고 저장하면 공간을 많이 차지하여 메모리를 많이 차지함 그래서 previous 와 current를 활용하여 공간복잡도 O(1)으로 풀이

<br>

### 새꼼달꼼 장사 Memoization 방식으로 풀기

#### code

```python
def max_profit_memo(price_list, count, cache):

    if count < 2:
        cache[count] = price_list[count]
        return price_list[count]

    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익 저장하는 변수
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총개수에 대한 가격 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    # 중복해서 계산하는 것을 막기 위해 (count // 2) + 1
    for i in range(1, (count // 2) + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                     + max_profit_memo(price_list, count - i, cache))
        print('profit: ', profit)
    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit

    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
# print(max_profit([0, 100, 400, 800, 900, 1000], 10))
# print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
```

- 다이나믹프로그래밍의 Memoization 방식으로 푼 코드이다.

- max profit을 비교하는 것이 아직 이해되지 않는다.

<br>

### 새꼼달꼼 장사 Tabulation 방식으로 풀기

#### Code

```python
def max_profit(price_list, count):
    # 개수별로 가능한 최대 수익을 저장하는 리스트
    # 새꼼달꼼 0개면 0원
    profit_table = [0]

    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
        # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
        # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
        if i < len(price_list):
            profit = price_list[i]
        else:
            profit = 0

        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 찾는다
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])

        profit_table.append(profit)

    return profit_table[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
```
