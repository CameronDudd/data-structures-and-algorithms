"""recursion"""

from typing import Any, Dict, List, Optional


def depth_of_bst(tree: Optional[Dict[Any, Any]]) -> int:
    """find the depth of a tree built by build_bst"""
    if tree is None:
        return 0
    l = depth_of_bst(tree.get("left_child", None))
    r = depth_of_bst(tree.get("right_child", None))
    if l > r:
        return l + 1
    return r + 1


def build_bst(input_arr: List[Any]) -> Dict[str, Any]:
    """build binary search tree"""
    if len(input_arr) == 0:
        return None
    middle_idx = len(input_arr) // 2
    middle_value = input_arr[middle_idx]
    return {
        "data": middle_value,
        "left_child": build_bst(input_arr[:middle_idx]),
        "right_child": build_bst(input_arr[middle_idx + 1 :]),
    }


def flatten_list(input_arr: List[Any]) -> List[Any]:
    """flatten multidimensional input_arr into 1D output arr"""
    result: List[Any] = []
    for i in input_arr:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result


def sum_digits(n: int) -> int:
    """sum all of the digits in n (base 10)"""
    if n <= 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


def find_min(input_arr: List[int]) -> Optional[int]:
    """find the minimum value in input_arr"""
    if len(input_arr) == 0:
        return None
    _ = find_min(input_arr[1:])
    return input_arr[0] if _ is None or _ > input_arr[0] else _


def is_palindrome(input_str: str) -> bool:
    """return input_str is palindrome"""
    if len(input_str) == 0:
        return True
    return input_str[0] == input_str[-1] and is_palindrome(input_str[1:-1])


def multiplication(num_1: int, num_2: int) -> int:
    """return multiplication of two numbers"""
    if num_1 == 0 or num_2 == 0:
        return 0
    return num_1 + multiplication(num_1, num_2 - 1)


def move_to_end(input_arr: List[Any], val: Any) -> List[Any]:
    """move all instances of val to end of input_arr"""
    if len(input_arr) == 0:
        return []
    _: List[Any] = [input_arr[0]]
    if _[0] == val:
        return move_to_end(input_arr[1:], val) + _
    return _ + move_to_end(input_arr[1:], val)


def wrap_string(string: str, n: int) -> str:
    """wrap the input_str with n number of surrounding '<' and '>'"""
    if n == 0:
        return string
    return wrap_string(f"<{string}>", n - 1)
