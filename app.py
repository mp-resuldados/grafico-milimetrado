from decimal import Decimal

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

def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1

def fman(number):
    return float(Decimal(number).scaleb(-fexp(number)).normalize())

def escala_boa(num):
    exp = fexp(num)
    if fman(num) / 5 == 1 or fman(num) / 2 == 1 or fman(num) == 1:
        return num
    if fman(num) / 5 > 1:
        return 10*10**exp
    if fman(num) / 2 > 1:
        return 5*10**exp
    if fman(num) > 1:
        return 2*10**exp
    return 10**exp


def limite_bom(esc, num):
    esc_cm = 10*esc
    return round(num / esc_cm) * esc_cm


def calcular_escala(h, v, dados):
    if type(dados) is pd.DataFrame:
    ##################################################
        delta_x = dados['x'].max()-dados['x'].min()
        delta_y = (dados['y']+dados['erro']).max()-(dados['y']-dados['erro']).min()
        escala_natural_x = delta_x/h
        escala_natural_y = delta_y/v
        escala_x = escala_boa(escala_natural_x)
        escala_y = escala_boa(escala_natural_y)
        delta_bom_x = h*escala_x
        delta_bom_y = v*escala_y
        sobra_x = delta_bom_x-delta_x
        sobra_y = delta_bom_y-delta_y
        lim_x = [dados['x'].min()-sobra_x/2, dados['x'].max()+sobra_x/2]
        lim_y = [(dados['y']-dados['erro']).min()-sobra_y/2, (dados['y']+dados['erro']).max()+sobra_y/2]
        limite_bom_x = limite_bom(escala_x, lim_x[1])
        limite_bom_y = limite_bom(escala_y, lim_y[1])
        div_h = np.array([limite_bom_x-escala_x*h+escala_x*10*i for i in range(0,int(h/10+1))])
        div_v = np.array([limite_bom_y-escala_y*v+escala_y*10*i for i in range(0,int(v/10+1))])

        # Conversão da escala para milímetro.
        x_mm = (dados['x'] - div_h[0]) / escala_x
        y_mm = (dados['y']+dados['erro'] - div_v[0]) / escala_y

    else:
        div_h = np.arange(0, h+1, 10)
        div_v = np.arange(0, v+1, 10)
    
    div_v_intervalo = div_v.max() - div_v.min()
    div_h_intervalo = div_h.max() - div_h.min()

    aspect_ratio = (v/div_v_intervalo) / (h/div_h_intervalo)

    return div_h, div_v, aspect_ratio


@st.cache_data
def gerar_papel(div_h, div_v, aspect_ratio):
    
    fig, ax = plt.subplots(figsize=(8.3, 11.7))

    ax.set_aspect(aspect_ratio)

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


div_h, div_v, aspect_ratio = calcular_escala(h, v, dados)

fig, ax = gerar_papel(div_h, div_v, aspect_ratio)

if isinstance(dados, pd.DataFrame):
    ax.errorbar(
        dados['x'],
        dados['y'],
        yerr = dados['erro'],
        marker='o',
        linestyle='none',
        color='green',
        label='dados experimentais',
    )


df = pd.DataFrame(columns=['x','y','erro'], dtype='float')

#def plotar

col1, col2 = st.columns([2,2])
with col1:
    dados = st.data_editor(df, num_rows='dynamic')
    st.button('plotar', on_click=gravar_dados, args=(dados,))

with col2:
    st.pyplot(fig)


#############################################################
# PLOTAR OS DADOS