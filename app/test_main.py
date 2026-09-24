import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        pytest.param(0, 0, [0, 0], id="zero ages"),
        pytest.param(14, 14, [0, 0], id="before first year"),
        pytest.param(15, 15, [1, 1], id="first human year"),
        pytest.param(23, 23, [1, 1], id="before second year"),
        pytest.param(24, 24, [2, 2], id="second human year"),
        pytest.param(27, 27, [2, 2], id="incomplete extra period"),
        pytest.param(28, 28, [3, 2], id="cat third year"),
        pytest.param(28, 29, [3, 3], id="dog third year"),
        pytest.param(15, 14, [1, 0], id="different ages"),
        pytest.param(100, 100, [21, 17], id="large ages"),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == expected
