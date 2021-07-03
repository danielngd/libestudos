from libestudos.spam.enviador_de_email import EmailInvalido, Enviador
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['daniel_xp_@hotmail.com', 'daniel.ngd@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'daniel_xp_@hotmail.com',
        'Curso PyTools',
        'Primeiro curso com testes no Pytools.'
    )

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'daniel']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'daniel_xp_@hotmail.com',
            'Curso PyTools',
            'Primeiro curso com testes no Pytools.'
        )
