# Modulo 06 - Funcoes

Funcoes organizam o codigo em blocos reutilizaveis. Elas transformam sequencias soltas de instrucoes em unidades com nome, entrada e retorno.

## Visao conceitual

Uma funcao recebe dados, executa uma responsabilidade e pode devolver um resultado. Esse modelo favorece:

- reaproveitamento
- testes
- legibilidade
- separacao de responsabilidades

## Por que isso e importante

Projetos maiores ficam rapidamente desorganizados sem funcoes. Ao dividir o programa em pequenas partes nomeadas, fica mais facil evoluir o sistema com seguranca.

## Vantagens

- reduzem duplicacao
- melhoram manutencao
- facilitam revisao e testes
- deixam o codigo mais modular

## Desvantagens e limites

- funcoes grandes demais perdem clareza
- nomes vagos escondem intencao
- excesso de responsabilidades em uma unica funcao piora design

## Arquivos da secao

### 1. `01-criando_funcoes.py`

Conceito:
- definicao e chamada de funcao

Entrada:
- nenhuma

Saida:
- mensagem padrao

### 2. `02-parametros.py`

Conceito:
- receber argumentos externos

Entrada:
- nenhuma no terminal

Saida:
- exibicao de dados passados para a funcao

### 3. `03-retorno.py`

Conceito:
- devolver valor para reutilizacao

Entrada:
- nenhuma no terminal

Saida:
- resultado de soma retornado por funcao

### 4. `04-input_funcoes.py`

Conceito:
- receber dados com `input()`
- processar com funcao
- exibir o retorno

Entrada:
- duas notas

Saida esperada:

```text
Primeira nota: 7
Segunda nota: 9
Media final: 8.0
```

### 5. `05-projeto_final_folha_pagamento.py`

Objetivo do projeto:
- dividir o calculo de folha em funcoes pequenas
- consolidar parametros e retorno

Caso real:
- calculo simplificado de pagamento
- simulador financeiro
- rotinas de RH

Entrada:
- valor da hora
- horas trabalhadas

Saida esperada:

```text
Valor da hora trabalhada: 25
Horas trabalhadas no mes: 160

Resumo da folha
Salario bruto: R$ 4000.00
Desconto INSS: R$ 320.00
Salario liquido: R$ 3680.00
```

## Aprendizado profissional

Funcoes sao uma transicao natural entre scripts iniciantes e software com arquitetura mais limpa.

## Erros comuns e sintaxe correta

- erro comum: esquecer parenteses ao chamar a funcao
- sintaxe correta: `resultado = calcular_total(10, 2)`
- erro comum: declarar a funcao sem identar o corpo
- erro comum: nao retornar valor quando o fluxo depende do resultado
- boa pratica: use `return` para devolver dados e `print()` apenas para exibir
