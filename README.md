# Exercício de redução de dimensionalidade de imagens para tons de cinza e preto e branco
Este exercício foi desenvolvido como entregável durante o bootcamp BairesDev - Machine Learning Practitioner disponibilizado pela DIO.

## Objetivo
O objetivo do exercício é reduzir a dimensão da imagem a ser processada cortando as camadas RGB para tons de cinza e reduzir novamente dos tons de cinza para preto e branco usando o conceito de binarização da imagem.

Desta forma é possível reduzir em até 500x a carga computacional necessaria para o processamento da imagem de acordo com o que foi discutido no curso.

## Codígo
    . versão Python: 3.13.1
    . versão Pillow: 11.0.0

Foi utilizada a biblioteca Pillow para trabalhar com imagens, caso queira executar este código na sua máquina e não tenha pillow instalada, use o comando `pip install Pillow`
    
* A instalação de bibliotecas e frameworks diretamente no seu ambiente pode causar problemas de dependências se você já usa python, sugiro que use um environment próprio para fazer a instalação e testar o código, o visual studio code tem esta opção, mas você pode optar por usar [ANACONDA](https://www.anaconda.com/download) e fazer a gestão dos ambientes instalados na sua máquina.