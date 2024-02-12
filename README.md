# Construção de gráficos em papel milimetrado

*(repositório em construção)*


## Introdução

Neste trabalho, mostramos como plotar um gráfico perfeito em papel milimetrado e como converter os dados para um plot mais simples e rápido. As seções abaixo ensinam o passo-a-passo desde o cálculo da melhor escala até o plot dos dados e barras de erros.

Desenvolvemos também uma aplicação para gerar um papel com a quantidade de divisões desejada e plotar os gráficos. A aplicação é bastante auto-explicativa mas, no fim do texto, escrevemos uma breve seção de como utilizar.

## Objetivos

O objetivo principal é aprender a plotar um gráfico para professor nenhum botar defeito! Como etapas intermediárias do processo, podemos citar:

- calcular a melhor escala para que os dados ocupem uma boa área do papel;
- construir a melhor escala de leitura para os dados;
- converter os dados a serem plotados para unidades de divisões;

## Dados

O primeiro conjunto de dados a ser considerado são as medidas do papel escolhido. Quanto mais divisões tiver o papel (desde que visualmente distinguíveis), maior a resolução do gráfico. 
O segundo conjunto de dados são os dados a serem plotados que devem conter abcissas, ordenadas e, opcionalmente, incertezas.

## Cálculo da escala

A escala ideal para um gráfico é aquela em que o gráfico fica bem visível no papel, o plot é fácil de fazer e a leitura dos dados é simples mesmo em pontos interpolados.

O primeiro passo para calcular a escala ideal para o gráfico é conhecer os limites dos dados que queremos plotar. Vamos usar um exemplo para tornar a explicação mais clara e interativa. Pensando no conjunto de dados x =  \[10, 20, 30, 40, 50\], os limites de x são 10 e 50. Ou seja, o x varia entre 10 e 50, tendo um &#916;x = 50-10 = 40. A escala natural para o gráfico seria dividir esse &#916;x pelo número de divisões no papel. Como exemplo, vamos usar um papel com 180 divisões na horizontal. Assim, a escala natural seria 40/180 = 0.2777... . Mas uma escala dízima não parece uma boa ideia, certo? 

Para o cálculo da escala ideal vamos usar o padrão recomendável de que a escala deve ter a mantissa 1, 2 ou 5. Ou seja, deve ser sempre 1, 2, ou 5 vezes uma potência de 10 (10<sup>-1</sup>, 10<sup>0</sup>, 10&sup1;, 10&sup2;...). Com isso, a escala fica de fácil leitura e interpolação. No exemplo, temos uma escala natural de 2.777 &middot; 10<sup>-1</sup>; com mantissa 2.777... . Para manter o padrão recomendado, precisamos arredondar o valor da mantissa para 1, 2 ou 5, respeitando a condição de que o valor seja imediatamente maior que a mantissa da escala natural (ou os dados não vão caber no gráfico). Nesse caso, a escala ideal terá mantissa 5 e será dada por 5 &middot;10<sup>-1</sup>, ou seja, a escala ideal do exemplo é 0.5. Com isso, garantimos que os dados ocupem o maior espaço possível do  do papel.

Alguns exemplos:

Calculando a escala para um papel de 180 divisões na horizontal:
***
x<sub>1</sub> = \[0.0, 0.7, 1.5, 2.2, 2.7\]

&#916;x<sub>1</sub> = 2.7

escala natural = &#916;x<sub>1</sub>/180 = 0.015

escala ideal = 0.02
***
x<sub>2</sub> = \[1, 2, 3, 4, 5\]

&#916;x<sub>2</sub> = 4

escala natural = &#916;x<sub>2</sub>/180 = 0.222...

escala ideal = 0.5
***
x<sub>3</sub> = \[17.2, 609.4 ,902.1 , 1246.7, 1599.4\]

&#916;x<sub>3</sub> = 1582.2

escala natural = &#916;x<sub>3</sub>/180 = 8.79

escala ideal = 10
***

Para os dados que contém incerteza, é imprescindível calcular os limites e o respectivo &#916; considerando as barras de erro. Como exemplos:

Calculando a escala para um papel de 280 divisões na vertical:
***
y<sub>1</sub> = \[120.0, 141.0, 165.0, 186.0, 201.0\]

yerry<sub>1</sub> = \[0.1, 0.2, 0.1, 0.3, 0.7\]

O menor valor dos dados é 120.0-0.1=119.9 e o maior é 201.0+0.7=201.7.

&#916;y<sub>1</sub> = 201.7-119.9 = 81.8

escala natural = &#916;x<sub>1</sub>/280 = 0.2921528571

escala ideal = 0.5.
***
y<sub>2</sub> = \[100, 120, 140, 160, 180\]

yerry<sub>2</sub> = \[5, 5, 5, 5, 5\]

O menor valor dos dados é $100.0-5=95$ e o maior é 180+5=185.

&#916;y<sub>2</sub> = 90

escala natural = &#916;x<sub>2</sub>/280 = 0.3214285714

escala ideal = 0.5.
***
y<sub>3</sub> = \[75.8, 2444.6, 3615.4, 4993.8, 6404.6\]

yerr<sub>3</sub>= \[0.3, 0.2 ,0.1 , 0.4, 0.5\]

O menor valor dos dados é $75.8-0.3=75.5$ e o maior é 6404.6+0.5=6405.1.

&#916;y<sub>3</sub> =  6329.6 

escala natural = &#916;x<sub>3</sub>/280 = 22.6057142857

escala ideal = 50.
***

## Cálculo da da escala de leitura

A escala de leitura são os números que colocamos ao lado dos eixos para fazer a leitura dos dados. Não devemos escrever o valor dos dados plotados na escala de leitura. Ao invés disso, escrevemos valores igulamente espaçados que facilitem a leitura de qualquer ponto do gráfico.

O cálculo dos limites da escala de leitura é importante para definir os números que vão ser escritos nos eixos. No papel milimetrado, é comum escrever a escala de leitura a cada divisão maior. 

Para que o gráfico fique bem centralizado, devemos entender o espaço que os dados ocupam na região do plot. Os dados vão ocupar o espaço do &#916; que aprendemos a calcular na seção anterior. O espaço do plot depende da escala que vamos utilizar. Por exemplo: se a escala usada vai ser de 1 unidade por divisão e o número de divisões é 180, a região do plot será de 180 unidades. Se o número de divisões for 280, então a região do plot será 280 unidades. Se a escala do plot for 0.5 e o número de divisões for 180, então a região do plot será de 90 undidades. Se o número de divisões for 280, então a região do plot será de 140. Acompanhouu até aqui? Já consegue perceber a regra? Vamos definir a região do plot como &#916;'. A regra é: &#916;' = escala\*número de divisões. Vamos calcular a região do plot dos exemplos que estamos trabalhando. Vamos considerar que o eixo x terá 180 divisões e o eixo y, 280 divisões:
***
&#916;'x<sub>1</sub> = 3.6
&#916;'x<sub>2</sub> = 9
&#916;'x<sub>3</sub> = 1800
&#916;'y<sub>1</sub> = 140
&#916;'y<sub>2</sub> = 140
&#916;'y<sub>3</sub> = 14000
***

Podemos notar que a região do plot é sempre maior que a região dos dados (se não for, algum cálculo está errado). Devido a isso, sempre haverá uma região do gráfico sem dados. Idealmente, essa região ficará distribuída igualmente ao redor do gráfico. Para isso, vamos definir uma variável cahamada "sobra". Essa sobra nada mais é que a diferença entre a região dos dados e a região do plot, ou seja, a sobra é &#916;'-&#916;. Continuando com os exemplos, temos:
***
sobra_x<sub>1<\sub> = 0.9
sobra_x<sub>2<\sub> = 5
sobra_x<sub>3<\sub> = 217.8
sobra_y<sub>1<\sub> = 58.2
sobra_y<sub>2<\sub> = 50
sobra_y<sub>3<\sub> = 7670.4

Os limites da escala do plot deverão se tais que a "sobra" fique metade acima e metade abaixo dos dados, para garantir que os dados fiquem bem no meio. Para isso, dividimos a sobra por 2 e somamos ao menor valor dos dados. Conseguimos assim, obter um limite inferior para o plot. Seguindo os exemplos:
***    
x<sub>1 min<\sub> = 0 + sobra_x<sub>1<\sub>/2 = 
***
Como padrão recomendado, vamos escrever as escalas de leitura arredondando o limite calculado para 1, 2 ou 5 mais próximo, dependendo se a mantissa da escala for respectivamente 1, 2 ou 5. Assim, evitamos uma escala de leitura que varia de 10 em 10 como \[11, 21, 31,...\]. Nada elegante, certo? Se vai caminhar de 2 em 2, use número pares. Se vai caminhar de 5 em 5, privilegie os múltilos de 5. Se vai de 10 em 10, use múltiplos de 10. Isso não é uma regra, mas é uma boa prática. Reparem que os programas de plotar gráficos seguem estritamente essa prática. Para os exemplos em questão:
***
***
Nesse ponto, é sempre bom conferir se os dados estão dentro da região definida pelos limites calculados. Se não estiver, confira seus cálculos.

A partir do valor do limite inferior, podemos calcular a escala de leitura. Como vamos escrever nas diviões maiores, vamos calcular a escala de leitura a cada 10 divisões, ou seja, escrevemos o limite inferior e, depois de 10 divisões, escrevemos o próximo valor que será 10 vezes a escala mais o número anterior. Repetimos o processo até o final do eixo, para os dois eixos. Seguindo com os exemplos:
***
***

## Conversão dos dados para unidades de divisão

Neste ponto, já temos uma escala de leitura que permite um plot mais fácil dos dados. Mesmo assim, pode ser conveniente converter os dados para unidades de divisão para plotar só "contando quadradinhos". Para converter os dados, basta, para cada ponto, fazer a diferença entre o valor do dado e o início da escala de leitura e dividir pela escala que calculamos. Reparem que a unidade que resulta do cálculo é divisão! 

Com a tabela de dados convertidos, só resta contar os quadradinhos...

Seguindo os exemplos
***
***
    
    
    
    
    
    
    
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
