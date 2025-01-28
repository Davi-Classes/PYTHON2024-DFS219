import streamlit as st
from tinydb import TinyDB

# Titulo e Icone da ABA
st.set_page_config(
    page_title='Meus Produtos',
    page_icon=':shark:'
)

db = TinyDB('./produtos.json', indent=4)
produtos = db.table('produtos').all()

# Conteúdo do Site
with st.sidebar:
    st.title('Novo Produto')

    with st.form('form-produto') as form:
        nome_produto = st.text_input('Produto')
        preco_produto = st.number_input('Preço', step=0.01)
        descricao_produto = st.text_area('Descrição')

        salvar_produto = st.form_submit_button('Salvar')

        if salvar_produto:
            produto = {
                'Nome': nome_produto,
                'Preço': preco_produto,
                'Descricao': descricao_produto
            }

            db.table('produtos').insert(produto)
            produtos = db.table('produtos').all()

        
st.title('Produtos')
st.text_input('Pesquisar')

st.table(produtos)
