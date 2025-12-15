import streamlit as st

from llm import ask_gemini
from vector_store import add_to_vector_store, query_vector_store
from feedback import (
    save_feedback,
    update_prompt,
    load_prompt,
    load_feedbacks,
    load_all_prompts,
    clear_feedbacks,   
    clear_prompts,     
    reset_prompt      
)
from tools import consultar_cep, consultar_pokemon
from guarda import validate_response



st.set_page_config(
    page_title="Chatbot IA",
    page_icon="",
    layout="wide",
)


if "page" not in st.session_state:
    st.session_state.page = "chat"

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Chatbot IA com Feedback Inteligente")

col_menu1, col_menu2 = st.columns(2)
with col_menu1:
    if st.button("Chat do Agente", use_container_width=True):
        st.session_state.page = "chat"
with col_menu2:
    if st.button("Feedback & Ferramentas", use_container_width=True):
        st.session_state.page = "feedback"

st.divider()


if st.session_state.page == "chat":
    st.subheader("Chat do Agente")

    user_input = st.chat_input("Digite sua pergunta")

    if user_input:
        prompt = load_prompt()
        context = query_vector_store(user_input)

        response = ask_gemini(f"{prompt}\nUsuário: {user_input}", context)
        response = validate_response(response)

        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})

        add_to_vector_store(user_input + " " + response, {"type": "chat"})

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Limpar Chat", key="limpar_chat"):
            st.session_state.messages = []
            st.success("Histórico do chat limpo!")
    

    st.divider()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


elif st.session_state.page == "feedback":
    st.subheader("Feedback e Melhoria Contínua")

    feedback = st.selectbox("Qualidade da resposta", ["Boa", "Regular", "Ruim"])
    suggestion = st.text_area("Sugestão de melhoria do agente")

    if st.button("Enviar Feedback", key="enviar_feedback"):
        save_feedback(feedback, suggestion)
        if suggestion:
            update_prompt(suggestion, feedback)
        st.success("Feedback processado e prompt atualizado!")

    
    colf1, colf2, colf3 = st.columns(3)
    with colf1:
        if st.button("Limpar Feedbacks", key="limpar_feedbacks"):
            clear_feedbacks()
            st.success("Histórico de feedbacks apagado!")
    with colf2:
        if st.button("Limpar Prompts", key="limpar_prompts"):
            clear_prompts()
            st.success("Histórico de prompts apagado!")
    with colf3:
        if st.button("Resetar Prompt", key="reset_prompt_feedback"):
            reset_prompt()
            st.success("Prompt resetado para padrão!")

    st.subheader("Prompt Atual")
    st.code(load_prompt())

    st.divider()

    with st.expander("Histórico de Feedbacks"):
        feedbacks = load_feedbacks()
        if feedbacks:
            for f in reversed(feedbacks):
                st.markdown(
                    f"""
                    **Qualidade:** {f['feedback']}  
                    **Sugestão:** {f['suggestion']}  
                    {f['date']}
                    ---
                    """
                )
        else:
            st.info("Nenhum feedback registrado.")

    with st.expander("Histórico de Prompts"):
        prompts = load_all_prompts()
        if prompts:
            for p in reversed(prompts):
                st.markdown(
                    f"""
                    `{p['prompt']}`  
                    {p['date']}
                    ---
                    """
                )

    st.divider()
    st.subheader("Ferramentas")

    tab1, tab2 = st.tabs(["CEP", "Pokédex"])

    with tab1:
        cep = st.text_input("Digite o CEP")
        if st.button("Buscar CEP", key="buscar_cep"):
            if cep:
                st.json(consultar_cep(cep))
            else:
                st.warning("Digite um CEP válido.")

    with tab2:
        pokemon = st.text_input("Digite o Pokémon")
        if st.button("Buscar Pokémon", key="buscar_pokemon"):
            if pokemon:
                st.json(consultar_pokemon(pokemon))
            else:
                st.warning("Digite o nome de um Pokémon.")
