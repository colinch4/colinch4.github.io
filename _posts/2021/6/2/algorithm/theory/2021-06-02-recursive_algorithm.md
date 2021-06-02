# Recursive Algorithm

## 재귀 함수란

하나의 함수에서 자신을 다시 호출하여 작업을 수행 하는 함수

- Recursive case : 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우

- Base case : 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우

<br>

## 예제

### 피보나치 수열 재귀함수로 구현해보기

```python
# n번째 피보나치 수를 리턴
def fib(n):
    # Base Case
    if n < 3:
        return 1
    # Recursive Case
    else:
        return fib(n - 2) + fib(n - 1)

# Test
for i in range(1, 11):
    print(fib(i))
```

<br>

### 1부터 n까지의 합인 n번째 삼각수(triangle number)를 구현

```python
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # Base Case
    if n < 2:
        return n

    # Recursive Case
    else:
        return triangle_number(n - 1) + n


# Test
for i in range(1, 11):
    print(triangle_number(i))
```

<br>

### n의 각 자릿수의 합을 리턴해주는 재귀함수를 구현

```python
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # Base Case
    if n < 10:
        return n

    # Recursive Case
    else:
        return (n % 10) + sum_digits(n // 10)

# 코드를 작성하세요.


# 테스트
print(sum_digits(22541))    # 14
print(sum_digits(92130))    # 15
print(sum_digits(12634))    # 16
print(sum_digits(704))      # 11
print(sum_digits(3755))     # 20
```

<br>

### 입력받은 리스트를 뒤집힌 리스트로 리턴 하는 것을 재귀함수로 구현

```python
# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    # Base Case
    if len(some_list) < 2:
        return some_list

    # Recursive Case
    else:
        return [some_list[-1]] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
```

<br>

### 이진탐색 재귀함수로 구현

```python
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # Base Case 1
    if start_index > end_index:
        return None

    mid_idx = (start_index + end_index) // 2

    # Base Case 2
    if some_list[mid_idx] == element:
        return mid_idx

    # Recursive Case
    elif some_list[mid_idx] > element:
        return binary_search(element, some_list, start_index=start_index, end_index=mid_idx - 1)
    elif some_list[mid_idx] < element:
        return binary_search(element, some_list, start_index=mid_idx + 1, end_index=end_index)

    return None



print(binary_search(2, [2, 3, 5, 7, 11]))   # 0
print(binary_search(0, [2, 3, 5, 7, 11]))   # None
print(binary_search(5, [2, 3, 5, 7, 11]))   # 2
print(binary_search(3, [2, 3, 5, 7, 11]))   # 1
print(binary_search(11, [2, 3, 5, 7, 11]))  # 4
```

<br>

### 하노이의 탑 재귀로 구현

```python
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # Base Case
    if num_disks == 0:
        return

    # Recursive Case
    else:
        # 경유하는 기둥
        pass_peg = 6 - (start_peg + end_peg)

        # 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 pass_peg로 이동
        hanoi(num_disks - 1, start_peg, pass_peg)

        # 가장 큰 원판을 start_peg에서 end_peg로 이동
        move_disk(num_disks, start_peg, end_peg)

        # 나머지 원판들을 pass_peg에서 end_peg로 이동
        hanoi(num_disks - 1, pass_peg, end_peg)

# 테스트 코드
hanoi(4, 1, 3)
```
