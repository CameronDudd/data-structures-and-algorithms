"""Test the recursion module"""

from unittest import TestCase
from utils.recursion import (
    depth_of_bst,
    build_bst,
    flatten_list,
    sum_digits,
    find_min,
    is_palindrome,
    multiplication,
    move_to_end,
    wrap_string,
)


class TestRecursion(TestCase):
    """recursion module unit tests"""

    def test_bst(self) -> None:
        """test binary search tree build and depth"""

        bst = build_bst([0, 1, 2])
        self.assertEqual(
            {
                "data": 1,
                "left_child": {
                    "data": 0,
                    "left_child": None,
                    "right_child": None,
                },
                "right_child": {
                    "data": 2,
                    "left_child": None,
                    "right_child": None,
                },
            },
            bst,
        )
        self.assertEqual(2, depth_of_bst(bst))

        bst = build_bst(["ll", "l", "m", "r", "rr"])
        self.assertEqual(
            {
                "data": "m",
                "left_child": {
                    "data": "l",
                    "left_child": {
                        "data": "ll",
                        "left_child": None,
                        "right_child": None,
                    },
                    "right_child": None,
                },
                "right_child": {
                    "data": "rr",
                    "left_child": {
                        "data": "r",
                        "left_child": None,
                        "right_child": None,
                    },
                    "right_child": None,
                },
            },
            bst,
        )
        self.assertEqual(3, depth_of_bst(bst))

    def test_flatten_list(self) -> None:
        """test flatten_list function"""
        planets = ["mercury", "venus", ["earth"], "mars", [["jupiter", "saturn"]], "uranus", ["neptune", "pluto"]]
        flat_result = flatten_list(planets)
        self.assertEqual(["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"], flat_result)

    def test_sum_digits(self) -> None:
        """test sum_digits"""
        self.assertEqual(0, sum_digits(0))
        self.assertEqual(1, sum_digits(1))
        self.assertEqual(1, sum_digits(10))
        self.assertEqual(2, sum_digits(11))
        self.assertEqual(1, sum_digits(100))
        self.assertEqual(2, sum_digits(101))
        self.assertEqual(2, sum_digits(110))
        self.assertEqual(3, sum_digits(111))
        self.assertEqual(1, sum_digits(1000))
        self.assertEqual(2, sum_digits(1001))
        self.assertEqual(2, sum_digits(1010))
        self.assertEqual(3, sum_digits(1011))
        self.assertEqual(2, sum_digits(1100))
        self.assertEqual(3, sum_digits(1101))
        self.assertEqual(3, sum_digits(1110))
        self.assertEqual(4, sum_digits(1111))
        self.assertEqual(45, sum_digits(123456789))

    def test_find_min(self) -> None:
        """test find_min"""
        self.assertEqual(0, find_min([0, 1, 2, 3, 4, 5, 6]))
        self.assertEqual(0, find_min([9, 10, 11, 12, 0, 13, 14, 15]))
        self.assertEqual(-3, find_min([-3, -2, -1, 0, 1, 2, 3]))

    def test_is_palindrome(self) -> None:
        """test is_palindrome"""
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aba"))
        self.assertFalse(is_palindrome("ab"))
        self.assertFalse(is_palindrome("abc"))

    def test_multiplication(self) -> None:
        """test multiplication"""
        self.assertEqual(0, multiplication(0, 0))
        self.assertEqual(0, multiplication(0, 99999999))
        self.assertEqual(1, multiplication(1, 1))
        self.assertEqual(4, multiplication(1, 4))
        self.assertEqual(16, multiplication(4, 4))
        self.assertEqual(20, multiplication(4, 5))
        self.assertEqual(20, multiplication(5, 4))

    def test_move_to_end(self) -> None:
        """test move_to_end"""
        self.assertEqual([], move_to_end([], None))
        self.assertEqual(["b", "c", "a", "a"], move_to_end(["a", "b", "a", "c"], "a"))
        self.assertEqual([1, 2, 3, 4, 5, 0, 0, 0, 0, 0], move_to_end([0, 1, 0, 2, 0, 3, 0, 4, 0, 5], 0))

    def test_wrap_string(self) -> None:
        """test wrap_string"""
        self.assertEqual("", wrap_string("", 0))
        self.assertEqual("<>", wrap_string("", 1))
        self.assertEqual("test", wrap_string("test", 0))
        self.assertEqual("<test>", wrap_string("test", 1))
        self.assertEqual("<<test>>", wrap_string("test", 2))
        self.assertEqual("<<<test>>>", wrap_string("test", 3))
