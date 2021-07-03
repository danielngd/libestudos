import pytest

from libestudos.spam.enviador_de_email import Enviador
from libestudos.spam.main import EnviadorDeSpam
from libestudos.spam.models import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Daniel', email='daniel.ngd@gmail.com'),
            Usuario(nome='Lima', email='daniel_xp_@hotmail.com')
        ],
        [
            Usuario(nome='Daniel', email='daniel.ngd@gmail.com'),
        ]
    ]
)
def test_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daniel.ngd@mail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Daniel', email='daniel.ngd@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daniel_xp_@hotmail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
    assert enviador.parametros_de_envio == (
        'daniel_xp_@hotmail.com',
        'daniel.ngd@gmail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
