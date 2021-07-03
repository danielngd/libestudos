from libestudos.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Daniel', email='daniel.ngd@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Daniel', email='daniel.ngd@gmail.com'),
        Usuario(nome='Lima', email='daniel_xp_@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
