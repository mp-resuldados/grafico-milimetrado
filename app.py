import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, FixedLocator


################################################################################
# ESTADO DA SESSÃO

if 'dados' not in st.session_state:
    st.session_state['dados'] = None

dados = st.session_state['dados']


#############################################################
# PARÂMETROS DE ENTRADA

with st.sidebar:
    st.subheader('Número de divisões:')
    col1, col2 = st.columns(2)
    with col1:
        h = st.number_input('horizontal',
                    value=180,
                    min_value=100,
                    max_value=300,
                    step=10
                   )
    with col2:
        v = st.number_input('vertical',
                    value=280,
                    min_value=100,
                    max_value=300,
                    step=10
                   )


#############################################################
# GERAR O PAPEL

def gravar_dados(dados):
    st.session_state['dados'] = dados


def calcular_escala(h, v, dados):
    if type(dados) is pd.DataFrame:
        div_h = range(0, 100, 10)
        div_v = range(0, 100, 10)

    else:
        div_h = range(0, h+1, 10)
        div_v = range(0, v+1, 10)

    return div_h, div_v


def gerar_papel(div_h, div_v):
    
    fig, ax = plt.subplots(figsize=(8.3, 11.7))

    ax.set_aspect(1)

    ax.set_title('Papel milimetrado')
    ax.set_xlabel('eixo horizontal')
    ax.set_ylabel('eixo vertical')

    ax.set_xlim(div_h[0],div_h[-1])
    ax.set_ylim(div_v[0],div_v[-1])

    # grid lines
    ax.grid(which = "major")
    ax.grid(which = "minor", alpha = 0.2)
    ax.set_axisbelow(True)

    ax.tick_params(which = "minor", bottom = False, left = False)

    #  major grid do eixo horizontal
    ax.xaxis.set_major_locator(FixedLocator(div_h))

    #  major grid do eixo vertical
    ax.yaxis.set_major_locator(FixedLocator(div_v))

    # Minor grid dividindo o major grid em 10
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    
    return fig, ax


div_h, div_v = calcular_escala(h, v, dados)

fig, ax = gerar_papel(div_h, div_v)

df = pd.DataFrame(columns=['x','y','erro'])

#def plotar

col1, col2 = st.columns([2,2])
with col1:
    dados = st.data_editor(df, num_rows='dynamic')
    st.button('plotar', on_click=gravar_dados, args=(dados,))

with col2:
    st.pyplot(fig)


#############################################################
# PLOTAR OS DADOS