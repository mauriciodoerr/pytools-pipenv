from libhttprequests.spam.models import User


def test_save_user(session):
    user = User(name='User One', email='user_one@gmail.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [
        User(name='User One', email='user_one@gmail.com'),
        User(name='User Two', email='user_two@gmail.com')
    ]
    for user in users:
        session.save(user)
    assert users == session.list()
