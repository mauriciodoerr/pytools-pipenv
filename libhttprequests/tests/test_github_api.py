from unittest.mock import Mock

import pytest
from libhttprequests.github_api import get_github_avatar


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'mocked url'
    resp_mock.json.return_value = {
        'login': 'mauricio',
        'id': 28199933,
        'avatar_url': url
    }
    get_mock = mocker.patch('libhttprequests.github_api.requests.get')
    get_mock.return_value = resp_mock
    yield url


def test_github_avatar(avatar_url):
    result = get_github_avatar('mauriciodoerr')
    assert 'mocked url' in result


def test_github_avatar_integrated():
    result = get_github_avatar('mauriciodoerr')
    assert 'https://avatars.githubusercontent.com/u/28199933?v=4' in result
