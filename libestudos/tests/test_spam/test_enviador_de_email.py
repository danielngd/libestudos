from libestudos.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'daniel.ngd@gmail.com',
        'daniel_xp_@hotmail.com',
        'Curso PyTools',
        'Primeiro curso com testes no Pytools.'
    )
    assert 'daniel.ngd@gmail.com'in resultado
