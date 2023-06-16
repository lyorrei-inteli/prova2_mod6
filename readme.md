# Documentação da parte prática da Prova 2

## Informações gerais

O projeto contido nesse repositório utiliza da biblioteca "opencv" para a leitura do vídeo da webcam do usuário para identificar faces utilizando um modelo já treinado. Ao identificar uma face, o script cria um quadrado preto ao redor dela. Além disso, ele armazena o vídeo gerado em um arquivo "out.avi" na root do repositório.

## Instalação

Para fazer o script funcionar, é preciso instalar todas as bibliotecas que estão no arquivo "requirements.txt". Para isso, execute os seguintes comandos:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

## Como rodar o projeto?

Para rodar o script, apenas execute o seguinte comando:

```
python3 app.py
```
