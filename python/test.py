# Contributors
# ---------------------------
# En-Ho Shen <enhoshen@gmail.com>, 2023

# import header
import pytest

# test class
class TestSuite():
    # auto use fixture
    @pytest.fixture(autouse=True)
    def test_fixture(self):
        pass

    # fixture with parameters
    @pytest.fixture(params=[i for i in cases])
    def cases(self, request):
        return request.param

    # pytest marks
    @pytest.mark.xfail(reason="expected to fail reason")
    def expected_to_fail(self):
        assert 0
