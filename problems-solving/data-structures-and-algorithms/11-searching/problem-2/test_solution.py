# I'll create unit tests for the given problem using pytest and loguru for logging.

import pytest
from loguru import logger
from solution import solution_2


def test_empty_array():
    logger.info("Testing with an empty array")
    assert solution_2([], 5) == -1


def test_single_element_array():
    logger.info("Testing with a single-element array")
    assert solution_2([5], 5) == 0
    assert solution_2([6], 5) == -1


def test_multiple_elements_array():
    logger.info("Testing with a multiple-elements array")
    assert solution_2([1, 2, 3, 4, 5], 3) == 2
    assert solution_2([1, 2, 3, 4, 5], 6) == -1


def test_duplicate_elements_array():
    logger.info("Testing with an array having duplicate elements")
    assert solution_2([1, 2, 2, 2, 3, 4, 5], 2) == 1
    assert solution_2([1, 1, 1, 1, 1], 1) == 0


def test_negative_elements_array():
    logger.info("Testing with an array having negative elements")
    assert solution_2([-5, -4, -3, -2, -1], -3) == 2
    assert solution_2([-5, -4, -3, -2, -1], 0) == -1
