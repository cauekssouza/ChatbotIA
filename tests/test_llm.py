from app.llm import ask_gemini

def test_ask_gemini_retorna_texto():
    resposta = ask_gemini("Olá", "")
    assert isinstance(resposta, str)
    assert len(resposta) > 0
