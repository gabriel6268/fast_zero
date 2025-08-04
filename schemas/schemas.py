from pydantic import BaseModel


class Mensagem(BaseModel):
    msg: str


class HelloWorld(BaseModel):
    msg: str
