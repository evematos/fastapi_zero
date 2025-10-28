from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root():
    """
    Teste AAA
    Arrange: Configurar o cenário do teste
    Act: Executar a ação a ser testada  
    Assert: Verificar se o resultado é o esperado
    """

    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello World'}
