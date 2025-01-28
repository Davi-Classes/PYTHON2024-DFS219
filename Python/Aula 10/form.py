import streamlit as st


st.title('Soma de Numeros')

with st.form('soma_numeros') as form:
    n1 = st.number_input('1º Numero', step=0.1)
    n2 = st.number_input('2º Numero', step=0.1)

    sum_numbers = st.form_submit_button('Somar')
    multiply_numbers = st.form_submit_button('Multiplicar')

if sum_numbers:
    st.write(f'### Resultado: {n1 + n2}')
elif multiply_numbers:
    st.write(f'### Resultado: {n1 * n2}')
