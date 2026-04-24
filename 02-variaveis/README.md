# Modulo 02 - Variaveis

Variaveis representam dados com nomes significativos. Em vez de espalhar valores soltos pelo codigo, o programa passa a registrar informacoes com contexto.

## Visao conceitual

Uma variavel liga um nome a um valor. Essa ideia permite modelar o dominio do problema: aluno, saldo, estoque, media, produto, cidade e assim por diante.

## Por que isso e importante

Sem variaveis, o codigo fica preso a valores fixos. Com variaveis, o programa:

- adapta dados em tempo de execucao
- reaproveita valores
- fica mais legivel
- reduz repeticao

## Vantagens

- deixam o codigo mais claro
- facilitam manutencao
- ajudam a descrever o problema

## Desvantagens e limites

- nomes ruins confundem quem le
- excesso de reatribuicoes pode dificultar rastrear o estado
- variaveis genericas diminuem o valor didatico do codigo

## Arquivos da secao

### 1. `01-variaveis_basicas.py`

Conceito:
- armazenar texto, numero decimal, inteiro e booleano

Entrada:
- nenhuma

Saida:
- exibicao dos valores armazenados

### 2. `02-nomes_de_variaveis.py`

Conceito:
- escolha de nomes claros
- uso de `snake_case`

Entrada:
- nenhuma

Saida:
- exibicao de dados com nomes mais profissionais

### 3. `03-atualizando_variaveis.py`

Conceito:
- reatribuicao
- mudanca de estado

Entrada:
- nenhuma

Saida:
- demonstracao da evolucao de um valor

### 4. `04-input_cadastro.py`

Conceito:
- armazenar dados informados pelo usuario

Entrada:
- nome do aluno
- curso
- semestre

Saida esperada:

```text
Nome do aluno: Pedro
Curso: Analise de Dados
Semestre atual: 2

Dados cadastrados
Aluno: Pedro
Curso: Analise de Dados
Semestre: 2
```

### 5. `05-projeto_final_cadastro_aluno.py`

Objetivo do projeto:
- montar uma ficha academica simples
- consolidar nomeacao, armazenamento e reaproveitamento de dados

Caso real:
- pre-cadastro de estudantes
- triagem de atendimento academico
- automacoes de secretaria

Entrada:
- nome do aluno
- matricula
- curso
- media geral

Saida esperada:

```text
Nome do aluno: Julia Costa
Numero de matricula: 202401
Curso: Sistemas
Media geral: 8.4

Ficha academica
Nome: Julia Costa
Matricula: 202401
Curso: Sistemas
Media geral: 8.4
Situacao: aprovado
```

## Aprendizado profissional

Modelar bem variaveis e um passo essencial para escrever codigo que outras pessoas consigam manter, revisar e expandir.

## Erros comuns e sintaxe correta

- erro comum: usar nome com espaco, como `nome aluno = "Ana"`
- sintaxe correta: `nome_aluno = "Ana"`
- erro comum: tentar converter texto invalido com `float()`
- boa pratica: usar `try/except ValueError` quando a entrada vier do usuario
- erro comum: usar variaveis antes de atribuir valor
- boa pratica: inicialize sempre a variavel antes do uso
