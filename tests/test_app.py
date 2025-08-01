from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'message': 'Olá, mundo!!!'}


def test_root_code_deve_retornar_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
