from libestudos.spam.enviador_de_email import Enviador
from libestudos.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'daniel.ngd@mail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
