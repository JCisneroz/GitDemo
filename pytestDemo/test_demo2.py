#Any pytest must start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_thirdProgram():
    msg = "Hello"
    assert msg == "Hello", "test failes 'cause strings do not match"

