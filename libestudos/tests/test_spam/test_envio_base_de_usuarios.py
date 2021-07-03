import pytest

from libestudos.spam.enviador_de_email import Enviador
from libestudos.spam.main import EnviadorDeSpam
from libestudos.spam.models import Usuario


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
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daniel.ngd@mail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados
