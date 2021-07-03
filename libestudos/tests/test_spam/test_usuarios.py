from libestudos.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Daniel')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Daniel'), Usuario(nome='Lima')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
