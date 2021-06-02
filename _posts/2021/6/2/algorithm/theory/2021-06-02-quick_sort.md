# Quick Sort

## 단계

- Partition : 리스트를 나누는 과정

  1. 기준점을 정하는 단계

  2. 피봇을 기준으로 값들을 새롭게 배치

<br>

## Partition 구현

<img src="https://user-images.githubusercontent.com/58774316/112801288-acedb900-90ab-11eb-983f-643de72dbf9e.png" width=700px>

### Code

```python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    return my_list

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i, b = start, start
    p = end

    # 범위안의 모든 값들을 볼 때까지 반복문을 돌린다.
    while i < p:
        # i 인덱스의 값이 기준점보다 작으면 i인덱스와 b인덱스에 있는 값들을 바꾸고 b를 1 증가 시킨다.
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    # b와 기준점인 p 인덱스에 있는 값들을 바꿔준다.
    swap_elements(my_list, b, p)

    # pivot의 최종 인덱스를 리턴
    return b


# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)

```

<br>

## 최종 Quick Sort 구현

### code

```python
# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    i, b = start, start
    p = end

    while i < p:
        if my_list[i] < my_list[p]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1

    swap_elements(my_list, b, p)
    return b


# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1

    # Base case :
    if end - start < 1:
        # merge_sort와 달리 quicksort 함수는 새로운 리스트를 리턴하지 않는다.
        return  # return None과 같은 효과

    # -- Recursive case --

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다.
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)





# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
```
