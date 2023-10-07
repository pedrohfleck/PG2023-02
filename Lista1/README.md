## Lista de Exercícios 1 – Processamento Gráfico

<b>1. O que é a GLSL? Quais os dois tipos de shaders são obrigatórios no pipeline programável da versão atual que trabalhamos em aula e o que eles processam?</b>

OpenGL Shading Language (GLSL) é uma linguagem de programação de alto nível com uma sintaxe baseada em C. No contexto da versão que trabalhamos em aula, existem dois tipos de shaders obrigatórios: o Vertex Shader, que define como processar um vértice, e o Fragment Shader, que define como processar uma área (fragmento).

<b>2. O que são primitivas gráficas? Como fazemos o armazenamento dos vértices na OpenGL?</b>

As primitivas gráficas são os elementos mais simples que podem ser criados.

- GL_POINTS: pontos
- GL_LINES: linha a cada 2 pontos do array
- GL_LINE_STRIP: linha entre todos os pontos do array do primeiro ao ultimo
- GL_LINE_LOOP: linha entre todos os pontos do array
- GL_TRIANGULOS: triangulo a cada 3 pontos do array
- GL_TRIANGLE_STRIP: triangulos grudados
- GL_TRIANGLE_FAN: triangulo a cada 2 pontos do array sendo que o terceiro ponto é sempre o primeiro do array

Para armazenar vértices na OpenGL, geralmente se utiliza Buffers de Vértices (Vertex Buffers) e Vertex Arrays.

<b>3. Explique o que é VBO, VAO e EBO, e como se relacionam (se achar mais fácil, pode fazer um gráfico representando a relação entre eles).</b>

VBO: é uma região de memória na placa de vídeo (GPU) que armazena os dados dos vértices. Isso inclui informações como coordenadas 3D, cores, texturas, normais e quaisquer outros atributos associados a cada vértice.
VAO: é um objeto que gerencia o estado e a configuração dos VBOs. Ele mantém informações sobre como os dados nos VBOs estão organizados e quais atributos estão associados a cada vértice.
EBO: é outro tipo de buffer que armazena índices que referenciam vértices nos VBOs. Os índices são usados para definir a ordem em que os vértices são renderizados, permitindo a reutilização de vértices e economizando memória.

Usar VBOs, VAOs e EBOs juntos ajuda a organizar e otimizar o fluxo de dados entre a CPU e a GPU, melhorando o desempenho e simplificando a renderização de objetos 3D complexos.

<b> 5. Faça o desenho de 2 triângulos na tela. Desenhe eles: </b>

a. Apenas com o polígono preenchido

<img src="./Exercício 5/Imagens/5.a.png" width="500">

b. Apenas com contorno

<img src="./Exercício 5/Imagens/5.b.png" width="500">

c. Apenas como pontos

<img src="./Exercício 5/Imagens/5.c.png" width="500">

d. Com as 3 formas de desenho juntas

<img src="./Exercício 5/Imagens/5.d.png" width="500">

<b> 6. Faça o desenho de um círculo na tela, utilizando a equação paramétrica do círculo para gerar os vértices. Depois disso: </b>

<img src="./Exercício 6/Imagens/6.png" width="500">

a. Desenhe um octágono

<img src="./Exercício 6/Imagens/6.a.png" width="500">

b. Desenhe um pentágono

<img src="./Exercício 6/Imagens/6.b.png" width="500">

c. Desenhe um pac-man!

<img src="./Exercício 6/Imagens/6.c.png" width="500">

d. Desenhe uma fatia de pizza

<img src="./Exercício 6/Imagens/6.d.png" width="500">

<b>7. Desenhe uma espiral, assim:</b>

<img src="./Exercício 7/Imagens/7.png" width="500">

<b>8. Considerando o seguinte triângulo abaixo, formado pelos vértices P1, P2 e P3, respectivamente com as cores vermelho, verde e azul.</b>

a. Descreva uma possível configuração dos buffers (VBO, VAO e EBO) para representá-lo.

b. Como estes atributos seriam identificados no vertex shader?

Agora implemente!

<img src="./Exercício 8/Imagens/8.png" width="500">

<b>9. Faça um desenho em um papel quadriculado (pode ser no computador mesmo) e reproduza-o utilizando primitivas em OpenGL. Neste exercício você poderá criar mais de um VAO e fazer mais de uma chamada de desenho para poder utilizar primitivas diferentes, se necessário.</b>

<img src="./Exercício 9/Imagens/9.png" width="500">