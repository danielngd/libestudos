import pytest
from unittest.mock import Mock

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
def test_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daniel.ngd@mail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Daniel', email='daniel.ngd@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'daniel_xp_@hotmail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
    enviador.enviar.assert_called_once_with(
        'daniel_xp_@hotmail.com',
        'daniel.ngd@gmail.com',
        'Curso PyTools',
        'Excelente curso para operar com ferramentas Python'
    )
