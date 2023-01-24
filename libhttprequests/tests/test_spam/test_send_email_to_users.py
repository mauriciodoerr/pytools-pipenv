from unittest.mock import Mock

import pytest

from libhttprequests.spam.main import SpamSender
from libhttprequests.spam.models import User


@pytest.mark.parametrize(
    'user_list',
    [
        [
            User(name='User One', email='user_one@gmail.com'),
            User(name='User Two', email='user_two@gmail.com')
        ],
        [
            User(name='User One', email='user_one@gmail.com')
        ]
    ]
)
def test_quantity_spam_sent(session, user_list):
    for user in user_list:
        session.save(user)
    email_sender = Mock()
    spam_sender = SpamSender(session, email_sender)
    spam_sender.send_email(
        'mauricio.doerr@gmail.com',
        'Email Subject',
        'Email Body'
    )
    assert len(user_list) == email_sender.send.call_count


def test_spam_parameters(session):
    user = User(name='User One', email='user_one@gmail.com')
    session.save(user)
    email_sender = Mock()
    spam_sender = SpamSender(session, email_sender)
    spam_sender.send_email(
        'mauricio.doerr@gmail.com',
        'Email Subject',
        'Email Body'
    )
    email_sender.send.assert_called_once_with(
        'mauricio.doerr@gmail.com',
        'user_one@gmail.com',
        'Email Subject',
        'Email Body'
    )
