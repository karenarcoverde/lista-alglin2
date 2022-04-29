# lista-alglin2
Um código do processo de Gram-Schmidt e a resolução da lista em LaTeX.

Questão 1. A decomposição QR de uma matriz A quadrada pode ser usada para que possamos descobrir seus autovalores. O algoritmo funciona bem para várias classes de matrizes e se baseia no fato de que A=QR e B=RQ são matrizes similares, ou seja, compartilham os mesmos autovalores.

(a) Mostre que as matrizes A=QR e B=RQ são matrizes similares.

(b) Calcule os autovalores da matriz A dada a seguir (com precisão de quatro casas decimais) usando o algoritmo QR abaixo:
A=[0.7140299 0.6918437 0.6748934 0.7884872
0.6918437 1.2492256 1.0307285 0.6275049
0.6748934 1.0307285 1.0893471 0.5567456
0.7884872 0.6275049 0.5567456 0.9550583]

Algoritmo QR:
-------------
Passo 1: Calcule a decomposição QR da matriz A
Passo 2: Faça A=R*Q;
Passo 3: Se a condição de parada foi atingida,
então forneça os autovalores revelados pela diagonal principal de A;
caso contrário, retorne ao passo 1.
-------------

Em cada iteração do algoritmo acima, a matriz A=RQ resultante se tornará cada vez mais próxima de uma triangular superior, portanto seus autovalores aos poucos estarão revelados na diagonal principal. Como ela é similar à matriz A original do problema, após algumas iterações teremos calculado os autovalores de A.

O critério de parada no passo 3 pode ser a convergência dos valores ao longo da diagonal principal: quando os valores na diagonal principal da matriz A=RQ calculada no passo 2 se mantiverem constantes até a quarta casa decimal, o algoritmo poderá ser interrompido.

Para obter a decomposição QR da matriz A, necessária no passo 1 do algoritmo, escolha entre os métodos de Gram-Schmidt, rotações de Givens, ou reflexões de Householder. Indique qual método foi escolhido em sua resposta.
