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
    st.session_state['dados'] = pd.DataFrame()

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

    xlabel = st.text_input(
        label='nome do eixo horizontal',
        value='eixo horizontal',
    )

    ylabel = st.text_input(
        label='nome do eixo vertical',
        value='eixo vertical',
    )


#############################################################
# GERAR O PAPEL

def gravar_dados(dados):
    dados.fillna(0,inplace=True)    
    st.session_state['dados'] = dados

def escala(h, v, dados):
    
    if not dados.empty:
        # cálculo do delta    
        delta_x = dados['x'].max()-dados['x'].min()
        dados_y_max  = (dados['y']+dados['erro']).max()
        dados_y_min = (dados['y']-dados['erro']).min()
        delta_y = dados_y_max - dados_y_min
        
        #cálculo da escala natural
        escala_nat_x = delta_x / h 
        escala_nat_y = delta_y / v 
        
        # função auxiliar para o cálculo da escala boa
        def fexp(number):
            (sign, digits, exponent) = Decimal(number).as_tuple()
            return len(digits) + exponent - 1

        def fman(number):
            return float(Decimal(number).scaleb(-fexp(number)).normalize())
        
        # cálculo da escala boa
        def escala_boa(num):
            exp = 10**fexp(num)
            man = fman(num)
            if man == 5 or man == 2 or man == 1:
                return num
            if man > 5:
                return 10*exp
            if man > 2:
                return 5*exp
            if man > 1:
                return 2*exp
            return exp
        
        escala_boa_x = escala_boa(escala_nat_x)
        escala_boa_y = escala_boa(escala_nat_y)
        
        delta_bom_x = escala_boa_x*h
        delta_bom_y = escala_boa_y*v
        
        # cálculo dos limites
        limite_x = [ round(dados['x'].min()-(delta_bom_x-delta_x)/2, 10),
        round(dados['x'].max()+(delta_bom_x-delta_x)/2, 10) ]
        limite_y = [ round(dados_y_min -(delta_bom_y-delta_y)/2, 10),
        round(dados_y_max +(delta_bom_y-delta_y)/2, 10) ]
        
        # cálculo dos limites bons
        def limite_bom(esc, num):
            esc_cm = 10*esc
            return round(num / esc_cm) * esc_cm
        v_limite_bom = np.vectorize(limite_bom)
        
        limite_bom_x = [ round(limite_bom(escala_boa_x, limite_x[1])-h*escala_boa_x, 10),
                        round(limite_bom(escala_boa_x, limite_x[1]), 10) ]
                    
        limite_bom_y = [ round(limite_bom(escala_boa_y, limite_y[1])-v*escala_boa_y, 10),
                        round(limite_bom(escala_boa_y, limite_y[1]), 10) ]
        
        # cálculo das divisões
        div_x = [ round(limite_bom_x[0] + escala_boa_x*10*i,10) for i in range(0,int(h/10+1)) ]
        div_y = [ round(limite_bom_y[0] + escala_boa_y*10*i,10) for i in range(0,int(v/10+1)) ]
        
        # conversão para mm
        dados_mm = pd.DataFrame()
        dados_mm['x_mm'] = v_limite_bom(0.05, (dados['x'] - div_x[0]) / escala_boa_x)
        dados_mm['y_mm'] = v_limite_bom(0.05, (dados['y'] - div_y[0]) / escala_boa_y)
        dados_mm['erro_mm']  = v_limite_bom(0.05, dados['erro'] / escala_boa_y) # tamanho da incerteza

    else:
        delta_x = None
        delta_y = None
        escala_nat_x = None
        escala_nat_y = None
        escala_boa_x = None
        escala_boa_y = None
        delta_bom_x = None
        delta_bom_y = None
        limite_x = None
        limite_y = None
        limite_bom_x = None
        limite_bom_y = None
        div_x = np.arange(0, h+1, 10)
        div_y = np.arange(0, v+1, 10)
        dados_mm = None
    
    return (delta_x, delta_y,
            escala_nat_x, escala_nat_y,
            escala_boa_x, escala_boa_y,
            delta_bom_x, delta_bom_y,
            limite_x, limite_y,
            limite_bom_x, limite_bom_y,
            div_x, div_y,
            dados_mm
           )
    

def plot(h, v, dados, xlabel, ylabel):
    # cálculo da escala
    (delta_x, delta_y,
     escala_nat_x, escala_nat_y,
     escala_boa_x, escala_boa_y,
     delta_bom_x, delta_bom_y,
     limite_x, limite_y,
     limite_bom_x, limite_bom_y,
     div_x, div_y,
     dados_mm) = escala(h, v, dados)
    
    # proporcionalização
    ratio =(v/(np.array(div_y).max()-np.array(div_y).min()))/(h/(np.array(div_x).max()-np.array(div_x).min()))

    fig, ax = plt.subplots(figsize=(8.3, 11.7)) # tamanho A4

    ax.set_aspect(ratio)

    ax.set_title('Papel milimetrado')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    ax.set_xlim(div_x[0],div_x[-1])
    ax.set_ylim(div_y[0],div_y[-1])

    # grid lines
    ax.grid(which = "major")
    ax.grid(which = "minor", alpha = 0.2)
    ax.set_axisbelow(True)

    ax.tick_params(which = "minor", bottom = False, left = False)

    #  major grid do eixo horizontal
    ax.xaxis.set_major_locator(FixedLocator(div_x))

    #  major grid do eixo vertical
    ax.yaxis.set_major_locator(FixedLocator(div_y))

    #  minor grid dividindo o major grid em 10
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))

    # plot
    if not dados.empty:
        ax.errorbar(
            dados['x'],
            dados['y'],
            yerr = dados['erro'],
            marker='.',
            linestyle='none',
            color='green',
            label='dados experimentais',
            )

    return fig

fig = plot(h, v, dados, xlabel, ylabel)

df = pd.DataFrame(columns=['x','y','erro'], dtype='float')


col1, col2 = st.columns([2,2])
with col1:
    dados = st.data_editor(df, num_rows='dynamic')
    st.button('plotar', on_click=gravar_dados, args=(dados,))

with col2:
    st.pyplot(fig)
