import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
   "value, parts, expected_sum",
   [
       (8, 1, 8),
       (6, 2, 6),
       (32, 6, 32)
   ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        parts: int,
        expected_sum: int
) -> None:
    result = split_integer(value, parts)

    assert  len(result) == parts
    assert sum(result) == expected_sum


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(16, 2) == [8, 8]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(16, 1) == [16]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)

    assert len(result) == 4
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert max(result) != min(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(4, 6)

    assert len(result) == 6
    assert sum(result) == 4
    assert result == sorted(result)
    assert result.count(0) == 2 and result.count(1) == 4
