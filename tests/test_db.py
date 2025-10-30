from dataclasses import asdict

from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            user_name='evelin', user_password='secret', user_email='evelin@email'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.user_name == 'evelin'))

    assert asdict(user) == {
        'id': 1,
        'user_name': 'evelin',
        'user_password': 'secret',
        'user_email': 'evelin@email',
        'created_at': time,
        'updated_at': time,
    }
