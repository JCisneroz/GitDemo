import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def editProfile(self, dataLoad):
        print(dataLoad)