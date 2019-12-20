# Projeto Curva ABC (análise de Paretto)

Esse é um projeto feito para um teste, para analisar o seguinte tema proposto.

O foco desse problema é na classificação e organização das informações. Segue abaixo o descritivo e em anexo as "bases".

 

Você é um renomado analista no banco de Bravos e recebeu da alta diretoria a tarefa de criar a curva ABC dos atuais correntistas do banco. Infelizmente, não existe uma integração entre as duas bases de dados disponíveis (correntistas_banco_bravos.csv e correntistas_obito.csv). Dessa forma, todas as contas estão atualmente ativas, não levando em consideração os óbitos. Sabendo disso, crie a curva ABC seguindo as diretrizes do banco informadas abaixo:

 

- A: >= 50%;

- B: >= 20% e < 50%;

- C: <20%;

 

O propósito da análise é demonstrar para os acionistas em quais famílias/alianças há a necessidade de intensificar o investimento para o próximo ano, com base em seu patrimônio previsto para este ano.

## Getting Started

### Rodar Local
Projeto foi todo feito em python

Clone o repositório git e instale os requerimento (caso já não tenha)

```

git clone https://github.com/imartynetz/rpc_teste
cd rpc_teste
pip install -r requirements.txt

```

## Rodar a base de cálculo.
Os arquivos de cálculo e tratamento de dados estão contidos na pasta ETL, para rerodar basta fazer

```
cd ETL
python ETL.py

```
Isso salvará dois .csv na pasta dashboard/data.

O dashboard foi feito utilizando a biblioteca dash, todos seus arquivos estão dentro do diretório dashboard. 
Para vizualizar o dashboard basta fazer (estando na pasta principal do projeto) 
```
cd dashboard
python app.py
```

Isso gerará um servidor local provavelmente no endereço http://127.0.0.1:8050/, basta copiar o link gerado
em seu navegador e poderá visualizar o dashboard.