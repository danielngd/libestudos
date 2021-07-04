import pytest
from unittest.mock import Mock
from libestudos import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/62218061?v=4'
    resp_mock.json.return_value = {
        'login': 'danielngd', 'id': 62218061,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libestudos.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('danielngd')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('danielngd')
    assert 'https://avatars.githubusercontent.com/u/62218061?v=4' == url
