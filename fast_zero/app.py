from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from schemas.schemas import Mensagem

app = FastAPI(title='Minha API')


@app.get('/', status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'msg': 'Olá, mundo!!!'}


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_world():
    return """
        <html>
            <head>
            <title>Olá, mundo!!  </title>
            </head>
            <body>
                <h1>HELLO, WORLD!!!<h1/>
            </body>
        </html>
    """
