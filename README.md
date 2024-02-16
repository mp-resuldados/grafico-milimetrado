# Construção de gráficos em papel milimetrado


## Introdução

Neste trabalho, mostramos como plotar um gráfico perfeito em papel milimetrado e como converter os dados para um plot mais simples e rápido. As seções abaixo ensinam o passo-a-passo desde o cálculo da melhor escala até o plot dos dados e barras de erros.

Desenvolvemos também uma aplicação para gerar um papel com a quantidade de divisões desejada e plotar os gráficos. A aplicação é bastante auto-explicativa mas, no fim do texto, escrevemos uma breve seção de como utilizar. Segue o link para a aplicação em streamlit:

[grafico-milimetrado](https://grafico-milimetrado.streamlit.app/)




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

Para o cálculo da escala ideal vamos usar o padrão recomendável de que a escala deve ter a mantissa 1, 2 ou 5. Ou seja, deve ser sempre 1, 2, ou 5 vezes uma potência de 10 (10<sup>-1</sup>, 10<sup>0</sup>, 10&sup1;, 10&sup2;...). Com isso, a escala fica de fácil leitura e interpolação. No exemplo, temos uma escala natural de 2.777 &middot; 10<sup>-1</sup>; com mantissa 2.777... . Para manter o padrão recomendado, precisamos arredondar o valor da mantissa para 1, 2 ou 5, respeitando a condição de que o valor seja imediatamente maior que a mantissa da escala natural. Com isso, garantimos que os dados caibam no papel ocupando a maior área possível. No exemplo, a escala ideal terá mantissa 5 e será dada por 5 &middot;10<sup>-1</sup>, ou seja, a escala ideal é 0.5.

Para treinar os cálculos, vamos adotar 3 exemplos. São 3 conjuntos de dados de medidas reais realizadas no Laboratório de Física Esperimental 2 da UFRJ no ano de 2023. Vamos realizar os cálculos de escala passo a passo seguindo as seções do texto. Vamos calcular a escala para um papel de 180 divisões na horizontal e 280 na vertical. É um papel bem comum, encontrado para vender em qualquer papelaria.

O primeiro conjunto de dados é uma medida para obter a densidade da água. Utilizamos uma barra de metal que, pendurada em um tripé, pode ser deslocada para dentro de uma proveta com água que fica em cima de uma balança. Medimos, para cada porção de barra submersa, a massa em gramas na balança e o volume em mililitros na proveta graduada. O plot é feito com a massa no eixo horizontal e o volume com sua barra de erro no vertical.

M = \[260, 266, 272, 278, 284, 290, 296, 302, 308\] g

V = \[156, 162, 168, 174, 180, 186, 192, 198, 204\] ml

&#963;V = \[1, 1, 1, 1, 1, 1, 1, 1, 1\] ml


&#916;M = 48 g 

escala natural = 48 g / 180 divisões = 0.2666... g/divisão

escala ideal = 0.5 g/divisão

Para os dados que contém incerteza, é imprescindível calcular os limites e o respectivo &#916; considerando os limite das barras de erro.


&#916;V = 50 ml

escala natural = 50 ml / 280 divisões = 0.1785714296 ml/divisão

escala ideal = 0.2 ml/divisão


O segundo conjunto de dados se refere ao período de um pêndulo simples medido com um cronômetro. Cada medida abaixo é dada pelo valor médio de 25 períodos medidos para um dado comprimento do fio. O plot é feito com o comprimento do pêndulo na horizontal e o valor do período na vertical.

L = \[149.5, 137.5, 126.5, 113.5, 100.5\] cm

T = \[2427, 2330, 2251, 2106, 1993\] ms

&#963;T = \[4, 4, 6, 7, 5]\] ms


&#916;L = 49 cm

escala natural = 49 cm / 180 divisões = 0.27222... cm/divisão

escala ideal = 0.5 cm/divisão

Como os dados que contém incerteza, vamos calcular os limites e o respectivo &#916; considerando as barras de erro.

&#916;T = 443 ms

escala natural = 443 ms / 280 divisões = 1.5821428571 ms/divisão

escala ideal = 2 ml/divisão


O terceiro conjunto de dados se refere ao comprimento de onda em uma corda vibrante. A medida é feita com as extremidades da corda fixas. Variando a frequência a qual a corda é submetida, medimos o comprimento da onda com uma régua quando ela está oscilando em um harmônico. O plot é feito com o comprimento de onda na horizontal e a frequência na vertical.

&#955; = \[334, 167, 111, 84, 67, 56, 48\] cm

f = \[12, 24, 36, 48, 59, 72, 83\] Hz

&#963;f = \[2, 2, 2, 2, 2, 2, 2]\] Hz


&#916;&#955; = 286 cm

escala natural = 286 cm / 180 divisões = 1.5888... cm/divisão

escala ideal = 2 cm/divisão

Lembrando que precisamos calcular os limites e o respectivo &#916; considerando os limites das barras de erro.

&#916;&#955; = 75 Hz

escala natural = 75 ms / 280 divisões = 0.2678571429 ms/divisão

escala ideal = 0.5 ml/divisão

De posse da escala ideal para a construção do gráfico, vamos pensar na escala de leitura.


## Cálculo da da escala de leitura

A escala de leitura são os números que colocamos ao lado dos eixos para fazer a leitura dos dados. Não devemos escrever o valor dos dados plotados na escala de leitura. Ao invés disso, escrevemos valores igulamente espaçados que facilitem a leitura de qualquer ponto do gráfico.

O cálculo dos limites da escala de leitura é importante para definir os números que vão ser escritos nos eixos. No papel milimetrado, é comum escrever a escala de leitura a cada divisão maior. 

Para que o gráfico fique bem centralizado, devemos conhecer o espaço que os dados ocupam na região do plot. Os dados vão ocupar o espaço do &#916; que aprendemos a calcular na seção anterior. O espaço do plot depende da escala que vamos utilizar. Por exemplo: se a escala usada vai ser de 1 unidade por divisão e o número de divisões é 180, a região do plot será de 180 unidades. Se o número de divisões for 280, então a região do plot será 280 unidades. Se a escala do plot for 0.5 e o número de divisões for 180, então a região do plot será de 90 undidades. Se o número de divisões for 280, então a região do plot será de 140. Acompanhouu até aqui? Já consegue perceber a regra? Vamos definir a região do plot como &#916;'. A regra é: &#916;' = escala\*número de divisões. Vamos calcular a região do plot dos exemplos que estamos trabalhando. Lembrando que consideramos que o eixo x terá 180 divisões e o eixo y, 280 divisões:

&#916;'M = 90 g

&#916;'V = 56 ml

&#916;'L = 90 cm

&#916;'T = 560 ms

&#916;'&#955; = 360 cm

&#916;'f = 140 Hz

Podemos notar que a região do plot é sempre maior que a região dos dados (se não for, algum cálculo está errado). Devido a isso, sempre haverá uma região do gráfico sem dados. Idealmente, essa região ficará distribuída igualmente ao redor do gráfico. Para isso, vamos definir uma variável cahamada "sobra". Essa sobra nada mais é que a diferença entre a região dos dados e a região do plot, ou seja, a sobra é &#916;'-&#916;. Calculando a sobra dos exemplos que estamos trabalhando:

sobra de M = 42 g

sobra de V = 6 ml

sobra de L = 41 cm

sobra de T = 117 ms

sobra de &#955; = 74 cm

sobra de f = 65 Hz

Os limites da escala do plot deverão ser tais que a "sobra" fique metade acima e metade abaixo dos dados, para garantir que os dados fiquem bem no meio. Para isso, dividimos a sobra por 2 e diminuimos do menor valor dos dados (não esqueça de considerar os limites da barra de erro!). Conseguimos assim, obter um limite inferior para o plot. Seguindo os exemplos, calculamos o limite inferior:

para M = 260 - 42/2 = 239 g

para V = 155 - 6/2 = 152 ml

para L = 100.5 - 41/2 = 80 cm

para T = 1988 - 117/2 = 1929.5 ms

para &#955; = 48 - 74/2 = 11 cm

para f = 10 - 65/2 = -22.5 Hz
    
Como padrão recomendado, vamos escrever as escalas de leitura arredondando o limite inferior calculado para 1, 2 ou 5 mais próximo, dependendo se a mantissa do passo for respectivamente 1, 2 ou 5. O passo é definido pelo intervalo que os valores vão ser escritos na escala. Vamos adotar um passo de 10 vezes o valor da escala, ou seja, escrever os números nas divisões maiores do papel. Fazendo o arredondamento, evitamos uma escala de leitura que varia de 10 em 10 como \[11, 21, 31,...\]. Nada elegante, certo? A dica é simples, se vai caminhar de 2 em 2, use número pares. Se vai caminhar de 5 em 5, privilegie os múltilos de 5. Se vai de 10 em 10, use múltiplos de 10... Isso não é uma regra, mas é uma boa prática. Reparem que os programas de plotar gráficos seguem estritamente essa prática. Para os exemplos em questão, vamos arredondar o limite inferior calculado acima:

para M (escala de 0.5, passo de 5) = 240 g

para V (escala de 0.2, passo de 2)=  152 ml

para L (escala de 0.5, passo de 5)=  80 cm

para T (escala de 2, passo de 20)= 1920 ms

para &#955; (escala de 2, passo de 20)= 20 cm

para f (escala de 0.5, passo de 5)= -20 Hz

Tente arredondar para o número mais próximo possível e verifique se os dados ficaram dentro da região do plot.

A partir do valor do limite inferior, podemos calcular a escala de leitura. Como vamos escrever nas diviões maiores, vamos calcular a escala de leitura a cada 10 divisões, ou seja, escrevemos o limite inferior e, depois de 10 divisões, escrevemos o próximo valor que será 10 vezes a escala mais o número anterior. Repetimos o processo até o final do eixo, para os dois eixos. Seguindo com os exemplos:

para M = \[240, 245, 250 ... 320, 325, 330\]

para V = \[152, 154, 156 ... 204, 206, 208\]

para L = \[80, 85, 90 ... 160, 165, 170\]

para T = \[1920, 1940, 1960 ... 2440, 2460, 2480\]

para &#955; = \[20, 40, 60 ... 340, 360, 380\]

para f = \[-20, -15, -10 ... 110, 115, 120\]

Com isso, já temos o "esqueleto" do gráfico. Na maioria dos caso, isso já é suficiente para fazer o plot com facilidade. Caso os dados sejam mais complicados, vale a pena converte-los para unidades de divisões antes de plotar.


## Conversão dos dados para unidades de divisão

Neste ponto, já temos uma escala de leitura que permite um plot mais fácil dos dados. Mesmo assim, pode ser conveniente converter os dados para unidades de divisão para plotar só "contando quadradinhos". Para converter os dados, basta, para cada ponto, fazer a diferença entre o valor do dado e o início da escala de leitura e dividir pela escala que calculamos. Reparem que a unidade que resulta do cálculo é divisão! Seguindo os exemplos:

Calculando a conversão para o primeiro ponto das tabelas dos exemplos:
M = (260 - 240)g / (0.5 g/divisão) = 40 divisões

V = (156 - 152)g / (0.2 ml/divisão) = 20 divisões

L = (149.5 - 80)g / (0.5 cm/divisão) = 139 divisões

T = (2427 - 1920)g / (2 ms/divisão) = 253.5 divisões

&#955; = (334 - 20)g / (2 cm/divisão) = 157 divisões

f = (12 - (-20))g / (0.5 Hz/divisão) = 64 divisões

A resolução da escala do papel é metade da divisão. Com isso, ao converter os dado em unidades de divisão, lembrem-se de arredondar para 0 ou 0.5 divisão. Não temos resolução visual (nem da caneta!) para dividir um quadradinho minúsculo em 3 ou 4 partes, certo? Dito isto e com a tabela de dados convertidos, só resta contar os quadradinhos... 

Depois do plot de todos os pontos, só resta desenhar as barras de erro. A conversão do tamanho da incerteza para divisões, se faz apenas dividindo o valor do dado pela escala que escolhemos. Seguindo com os exemplos:

para V = \[5, 5, 5 ... \]

para T = \[2, 2, 3, 3.5, 2.5\]

para f = \[4, 4, 4, ...\]

Atentem para o fato da barra de erro ser duas vezes o valor da incerteza padrão. Então, a barra de erro vai ter o tamanho de uma incerteza para cima e uma para baixo. 

Espero que, nesse ponto, já consigam plotar um bom gráfico! Se tiverem dúvidas ou dificuldade em algum dos pontos, não hesitem em pedir ajuda. Perguntem ao seu professor ou mandem um e-mail para mp.resuldados@gmail.com.


## Como usar a aplicação

O objetivo da aplicação é:

- gerar um papel com o número de divisões escolhido;
- contruir a visualização dos dados no papel;
- calcular tudo o que foi explicado nas seções anteriores e gerar um arquivo de resultados;
- salvar o arquivo e o gráfico.

Na aplicação, o papel gerado não é necessariamente milimetrado, a dimensão da menor divisão pode variar segundo o número de divisões escolhido para o papel. O número de divisões a ser escolhido se refere às divisões menores. As divisões maiores em destaque contém 10 divisões menores.

As abcissas estão representadas no eixo horizontal e ordenadas no eixo vertical. As barras de erro são definidas considerando que o dado possui o valor mais ou menos a incerteza. Com isso, o tamanho da barra de erro é de duas vezes a incerteza padrão.

## Resultados dos exemplos gerados com a aplicação:

![gráfico dos dados de volume em função da massa](./imagens/V(ml)_x_M(g).png)

![gráfico dos dados de período em função do comprimento do pêndulo](./imagens/T(ms)_x_L(cm).png)

![gráfico dos dados de  frequência em função do comprimento de onda](./imagens/f(Hz)_x_λ(cm).png)


## Referências bibliográficas

<img src="https://github.com/mp-resuldados/grafico-milimetrado/blob/master/imagens/Capa_Barthem.png" height="250">
<img src="https://github.com/mp-resuldados/grafico-milimetrado/blob/master/imagens/Capa_Vuolo.png" height="250">

-----------------------------------------------------------------------------
MP-resuldados
Dos dados aos resultados. Um pouco de física, matemática, negócios e finanças.
