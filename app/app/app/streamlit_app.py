# streamlit_app.py
import streamlit_app as st
from nlp_to_cpc import nl_to_cpc
from cpc_to_nlp import cpc_to_nl
from utils import looks_like_cpc

st.set_page_config(page_title="Agente NL↔CPC", layout="centered")
st.title("Agente IA: NL ↔ CPC — Conversão em tempo real")

st.markdown("Digite uma frase em português ou uma fórmula proposicional abaixo. O sistema detecta automaticamente o tipo e converte.")

inp = st.text_area("Entrada (frase ou fórmula):", value="João foi ao mercado e comprou leite", height=120)

if inp.strip() == "":
    st.info("Digite algo para ver a conversão.")
else:
    if looks_like_cpc(inp):
        st.subheader("Interpretação: Fórmula CPC detectada")
        nl = cpc_to_nl(inp)
        st.write("Frase gerada:")
        st.success(nl)
        st.write("Fórmula original:")
        st.code(inp)
    else:
        st.subheader("Interpretação: Frase em Português detectada")
        cpc = nl_to_cpc(inp)
        st.write("Fórmula gerada:")
        st.code(cpc)
        st.write("Frase original:")
        st.success(inp)

st.markdown("---")
st.markdown("**Dica:** para melhores resultados, use frases curtas e bem definidas que correspondam ao mapeamento. Você pode editar app/mapping.py para adicionar novas correspondências.")