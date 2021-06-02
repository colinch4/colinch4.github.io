# Binary Search (이진 탐색)

이진 탐색(Binary Search) 알고리즘은 반씩 나누어 반은 보고 반은 보지않는 탐색법인데요 이진탐색은 반씩 보기때문에 데이터가 이미 정렬되어 있다는 가정하에 탐색을 합니다.

## 이진 탐색 구현

주어진 정렬된 리스트안에서 특정한 요소를 찾는 경우에 인덱스를 반환하여야 될 때

<br>

```python
def binary_search(element, some_list):
    # 코드를 작성하세요
    sta_idx = 0
    end_idx = len(some_list) - 1

    while end_idx >= sta_idx:
        mid_idx = sta_idx + end_idx // 2

        if some_list[mid_idx] == element:
            return mid_idx

        if some_list[mid_idx] > element:
            end_idx = mid_idx - 1
        else:
            sta_idx = mid_idx + 1

    return None



print(binary_search(2, [2, 3, 5, 7, 11]))       # 0
print(binary_search(0, [2, 3, 5, 7, 11]))       # None
print(binary_search(5, [2, 3, 5, 7, 11]))       # 2
print(binary_search(3, [2, 3, 5, 7, 11]))       # 1
print(binary_search(11, [2, 3, 5, 7, 11]))      # 4
```
