import pytest

from libhttprequests.spam.email_sender import EmailSender, InvalidEmail


def test_email_sender():
    sender = EmailSender()
    assert sender is not None


@pytest.mark.parametrize(
    'email_to',
    ['test@gmail.com', 'test@outlook.com']
)
def test_email_to(email_to):
    sender = EmailSender()
    result = sender.send(
        email_to,
        'mauricio.doerr@gmail.com',
        'Testing Email Subject',
        'Testing Email Body'
    )
    assert email_to in result


@pytest.mark.parametrize(
    'email_to',
    ['', 'gmail.com']
)
def test_email_to_invalid(email_to):
    sender = EmailSender()
    with pytest.raises(InvalidEmail):
        sender.send(
            email_to,
            'mauricio.doerr@gmail.com',
            'Testing Email Subject',
            'Testing Email Body'
        )
