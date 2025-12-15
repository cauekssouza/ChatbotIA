from app.tools import consultar_pokemon

def test_consultar_pokemon():
    result = consultar_pokemon("pikachu")
    assert "nome" in result
    assert "altura" in result
    assert "peso" in result

from app.tools import consultar_cep

def test_consultar_cep():
    result = consultar_cep("01001-000")
    assert "cep" in result
    assert result["cep"] == "01001-000"
    assert "localidade" in result