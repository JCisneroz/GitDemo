#Any pytest must start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#Method name must have sense
#-k stands for method names execution, -s logs in output, -v stands for more info metadata
#you can run specific file with py.test <filename>
#You can mark(tag) test @pytest.mark.name of tag and then run with -m
#YOu can skip test with @pytest.mark.skip
#Fixtures are used as setup and tear down methods for test cases-
# conftest file to generalize fixture and make it available to all test cases

import pytest

@pytest.mark.smoke

def test_fristProgram():
    print("hello")

def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == 8, "addition do not match"