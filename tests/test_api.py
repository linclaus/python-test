from pip._vendor import requests


class TestAPI():
    def test_api(self):
        url = 'https://www.v2ex.com/api/nodes/show.json?name=python'
        res = requests.get(url).json()
        assert res['id'] == 90
        assert res['name'] == 'python'
