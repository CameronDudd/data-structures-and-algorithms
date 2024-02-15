"""sorting algorithms"""

from typing import Any, List, Callable, TypeVar
from random import randrange

T = TypeVar("T")


def swap(arr: List[Any], idx1: int, idx2: int) -> None:
    """swap two values within an array based on index"""
    tmp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = tmp


def bubble_sort(arr: List[Any], inplace: bool = False) -> List[Any]:
    """
    sort input arr using bubble sort alg
    O(N^2)
    """
    arr = arr if inplace else arr.copy()
    for _ in range(len(arr)):
        for idx, i in enumerate(arr[:-1]):
            if i > arr[idx + 1]:
                swap(arr, idx, idx + 1)
    return arr


def bubble_sort_custom_comp_func(arr: List[T], comp_func: Callable[[T, T], bool], inplace: bool = False) -> List[T]:
    """sort input arr using bubble sort alg with custom object comparison function"""
    arr = arr if inplace else arr.copy()
    for _ in range(len(arr)):
        for idx, i in enumerate(arr[:-1]):
            if comp_func(i, arr[idx + 1]):
                swap(arr, idx, idx + 1)
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    sort input arr using merge sort alg
    Θ(N*log(N))
    """

    def merge(left: List[Any], right: List[Any]) -> List[Any]:
        """
        merge two array in ascending order
        """
        result = []
        while len(left) > 0 and len(right) > 0:
            val = left.pop(0) if left[0] < right[0] else right.pop(0)
            result.append(val)
        result += left
        result += right
        return result

    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2
    left_split = arr[:mid_idx]
    right_split = arr[mid_idx:]

    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def quick_sort_inplace(arr: List[Any], start: int, end: int) -> None:
    """
    sort input arr using quick_sort sort alg
    O(N^2)
    Θ(N * log N) - Most common case
    """
    # this portion of the list has been sorted
    if start >= end:
        return

    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = arr[pivot_idx]

    # swap random element with last element in sub-lists
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]

    # tracks all elements which should be to the left (lesser than) pivot
    lt_ptr = start

    for idx in range(start, end):
        # we found an element out of place
        if arr[idx] < pivot_element:
            # swap element to the right-most portion of lesser elements
            arr[idx], arr[lt_ptr] = arr[lt_ptr], arr[idx]
            # tally that we have one more lesser element
            lt_ptr += 1
    # move pivot element to the right-most portion of lesser elements
    arr[end], arr[lt_ptr] = arr[lt_ptr], arr[end]
    quick_sort_inplace(arr, start, lt_ptr - 1)
    quick_sort_inplace(arr, lt_ptr + 1, end)


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    sort input arr using quick_sort sort alg
    O(N^2)
    Θ(N * log N) - Most common case
    """
    # this portion of the list has been sorted
    if len(arr) <= 1:
        return arr

    lt_arr = []
    gt_arr = []
    pvt = 0
    pvt_ele = arr[pvt]

    for idx in range(1, len(arr)):
        if arr[idx] < pvt_ele:
            lt_arr.append(arr[idx])
        else:
            gt_arr.append(arr[idx])

    sorted_lt_arr = quick_sort(lt_arr)
    sorted_gt_arr = quick_sort(gt_arr)

    return sorted_lt_arr + [pvt_ele] + sorted_gt_arr


def quick_sort_custom_comp_func(arr: List[T], comp_func: Callable[[T, T], bool]) -> List[T]:
    """sort input arr using quick_sort sort alg with a custom comparison function"""
    # this portion of the list has been sorted
    if len(arr) <= 1:
        return arr

    lt_arr = []
    gt_arr = []
    pvt = 0
    pvt_ele = arr[pvt]

    for idx in range(1, len(arr)):
        if comp_func(pvt_ele, arr[idx]):
            lt_arr.append(arr[idx])
        else:
            gt_arr.append(arr[idx])

    sorted_lt_arr = quick_sort_custom_comp_func(lt_arr, comp_func)
    sorted_gt_arr = quick_sort_custom_comp_func(gt_arr, comp_func)

    return sorted_lt_arr + [pvt_ele] + sorted_gt_arr
