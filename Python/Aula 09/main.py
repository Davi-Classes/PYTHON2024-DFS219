import streamlit as st


'''
# Meu titulo

## Lista não ordenada

- Tomate
- Maçã
         
## Lista ordenada
         
1. Item 1
2. Item 2    
'''

st.write('## Imagens')

col1, col2 = st.columns(2)

with col1:
    st.image('https://www.nutrire.ind.br/images/f69cb32b09206b60746c751f7d6f7b96.png')

with col2:
    st.image('./cachorrinho.jpg')