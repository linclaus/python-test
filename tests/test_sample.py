import pytest

testdata = [
    (2, 1, 1),
    (1, 2, 0)
]


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'm' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')

    @pytest.mark.parametrize("a,b,expected", testdata)
    def test_timedistance_v0(self, a, b, expected):
        diff = a - b
        assert diff == expected


if __name__ == '__main__':
    pytest.main()
