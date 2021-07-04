from unittest.mock import Mock
from libestudos import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'danielngd', 'id': 62218061,
        'avatar_url': 'https://avatars.githubusercontent.com/u/62218061?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('danielngd')
    assert 'https://avatars.githubusercontent.com/u/62218061?v=4' == url
