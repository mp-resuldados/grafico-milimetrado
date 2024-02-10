# Construção de gráficos em papel milimetrado

*(repositório em construção)*


## Introdução

Neste trabalho, mostramos como plotar um gráfico perfeito em papel milimetrado e como converter os dados para um plot mais simples e rápido. As seções abaixo ensinam o passo-a-passo desde o cálculo da melhor escala até o plot dos dados e barras de erros. Para dados lineares, há uma seção sobre o método do paraleogramo para o cálculo de coeficientes e incertezas.

Desenvolvemos também uma aplicação para gerar um papel com a quantidade de divisões desejada e plotar os gráficos. Para os dados com comportamento linear, a aplicação dá a opção de gerar uma reta e calcular os coeficientes e incertezas através de uma regressão linear ou do método do paralelogramo. Todas as etapas têm a opção de salvar para impressão.

A aplicação é bastante auto-explicativa mas, no fim do texto, escrevemos uma breve seção de como utilizar.

## Objetivos

O objetivo principal é aprender a plotar um gráfico para professor nenhum botar defeito! Como etapas intermediárias do processo, podemos citar:
- calcular a melhor escala para que os dados ocupem pelo menos metade do papel;
- construir a melhor escala de leitura para os dados;
- converter os dados a serem plotados para unidades de divisões;

Para dados lineares, vamos aprender a:
- traçar a melhor reta pelo método visual;
- construir o paralelogramo para o cálculo dos coeficientes;
- calcular os coeficientes e suas respectivas incertezas.

## Dados

O primeiro conjunto de dados a ser considerado são as medidas do papel escolhido. Quanto mais divisões tiver o papel (desde que visualmente distinguíveis), maior a resolução do gráfico. 
O segundo conjunto de dados são os dados a serem plotados que devem conter abcissas, ordenadas e, opcionalmente, incertezas.

## Cálculo da escala

O primeiro passo para calcular a escala é conhecer os limites dos dados que queremos plotar. Vamos usar um exemplo para tornar a explicação mais clara e interativa. Pensando no conjunto de dados x: \[10, 20, 30, 40, 5\], os limites de x são 10 e 50. Ou seja, o x varia entre 10 e 50, tendo um $\Delta$x = 50-10 = 40. A escala natural para o gráfico seria dividir esse \Delta x pelo número de divisões no papel. Como exemplo, vamos usar um papel com 180 divisões na horizontal. Assim, a escala natural seria (40/180 = 0.2777...). Uma escala dízima não parece uma boa ideia, certo? 

Para o cálculo da escala ideal vamos usar o padrão recomendável de que a escala deve ter a mantissa 1, 2 ou 5. Ou seja, deve ser sempre 1, 2, ou 5 vezes uma potência de 10 ($10^{-1}, 10^0, 10^1, 10^2$...). Com isso, a escala fica de fácil leitura e interpolação. No exemplo, temos uma escala natural de $2.777 \cdot 10^{-1}$ com mantissa (2.777...). Para manter o padrão recomendado, precisamos arredondar o valor da mantissa para 1, 2 ou 5, respeitando a condição de que seja maior que a mantissa da escala natural (ou os dados não vão caber no gráfico). Nesse caso, a escala ideal terá mantissa 5 e será dada por 5 $\cdot 10^{-1}$, ou seja, a escala ideal do exemplo é 0.5.

Alguns exemplos:
Calculando a escala para um papel de 180 divisões:

x_1 = \[0.0, 0.7, 1.5, 2.2, 2.7\]
$\Delta$x_1 = 2.7
escala natural = 0.015
escala ideal = 0.02

x_2 = \[1, 2, 3, 4, 5\]
$/Delta$ x_1 = 4
$escala natural = 0.222...$
$escala ideal = 0.5$

$x_3 = [17.2, 609.4 ,902.1 , 1246.7, 1599.4]$
$/Delta x_1 = 1582.2$
$escala natural = 8.79$
$escala ideal = 10$

Para os dados que contém incerteza, é imprescindível calcular os limites e o respectivo $/Delta$ considerando as barras de erro. Como exemplos:
Calculando a escala para um papel de 180 divisões:

$y_1 = [120.0, 141.0, 165.0, 186.0, 201.0]$
$yerr_1 = [0.1, 0.2, 0.1, 0.3, 0.7]$
O menor valor dos dados é $120.0-0.1=119.9$ e o maior valor dos dados é $201.0+0.7=201.7$
$/Delta x_1 = 201.7-119.9 = 81.8$
$A escala natural é 0.4555... e a escala ideal é 0.5.$

$y_2 = [100, 120, 140, 160, 180]$
$yerr_2 = [5, 5, 5, 5, 5]$
O menor valor dos dados é $100.0-5=95$ e o maior valor dos dados é $180+5=185$
/Delta x_1 = 2.7
A escala natural é 0.4555... e a escala ideal é 0.5.


$y_2 = [75.8, 2444.6, 3615.4, 4993.8, 6404.6])$
$yerr_3 = [0.3, 0.2 ,0.1 , 0.4, 0.5]$

## Cálculo dos limites superior e inferior

O cálculo dos limites é importante para definir as escalas de leitura que vão ser escritas nos eixos. No papel milimetrado, é comum escrever a escala de leitura a cada divisão maior. Como padrão recomendado, vamos escrever as escalas de leitura arredondando o limite calculado para 1, 2 ou 5 mais próximo, dependendo se a mantissa da escala for respectivamente 1,2 ou 5.

## Como usar a aplicação

O objetivo da aplicação é:

- gerar um papel com o número de divisões escolhido;
- contruir a visualização dos dados no papel;
- em caso de dados lineares, calcular coeficientes e incertezas através de uma regressão linear ou do método do paralelogramo;
- salvar o trabalho para posterior impressão.

Na aplicação, o papel gerado não é necessariamente milimetrado, a dimensão da menor divisão pode variar segundo o número de divisões escolhido para o papel. O número de divisões a ser escolhido se refere às divisões menores. As divisões maiores em destaque contém 10 divisões menores.

As abcissas estão representadas no eixo horizontal e ordenadas no eixo vertical. As barras de erro são definidas considerando que o dado possui o valor mais ou menos a incerteza. Com isso, o tamanho da barra de erro é de duas vezes a incerteza.

Para os dados lineares, a opção "melhor reta" calcula os coeficientes angular e linear e suas respectivas incertezas usando o método dos mínimos quadrados. A opção "paralelogramo" usa a representação gráfica e o coeficiente angular da reta feita pelos mínimos quadrados para construir um paraleogramo. Os coeficientes gerados são calculados pela média dos coeficientes máximos e mínimos, obtidos pelas retas de maior e menor inclinação (diagonais do paralelogramo). A incerteza dos coeficientes é dada pela metade da discrepância.



## Referências bibliográficas

vou colocar as fotos das capas do Vuolo e do caderno didático do Barthem (melhores referências et al!)


-----------------------------------------------------------------------------
MP-resuldados
Dos dados aos resultados. Um pouco de física, matemática, negócios e finanças.
