from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.json() == {'msg': 'Olá, mundo!!!'}


def test_root_code_deve_retornar_200():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_helloword_deve_retornar_html():
    client = TestClient(app)
    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK


def test_helloword_deve_retornar_200():
    client = TestClient(app)
    response = client.get('/hello')

    assert (
        response.text
        == """
        <html>
            <head>
            <title>Olá, mundo!!  </title>
            </head>
            <body>
                <h1>HELLO, WORLD!!!<h1/>
            </body>
        </html>
    """
    )
