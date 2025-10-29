from http import HTTPStatus


def test_root(client):  # arrange
    """
    Teste AAA
    Arrange: Configurar o cenário do teste
    Act: Executar a ação a ser testada
    Assert: Verificar se o resultado é o esperado
    """
    # act
    response = client.get('/')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello World'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'user_name': 'evelin',
            'user_email': 'evelin@email.com',
            'user_password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'user_name': 'evelin',
        'user_email': 'evelin@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'user_name': 'evelin',
                'user_email': 'evelin@email.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'user_name': 'bob',
            'user_email': 'bob@example.com',
            'user_password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'user_name': 'bob',
        'user_email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
