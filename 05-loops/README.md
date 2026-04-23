# Modulo 05 - Loops

Loops existem para repetir instrucoes com controle. Eles evitam copia e cola de codigo e tornam possivel processar muitos dados em sequencia.

## Visao conceitual

No mundo real, e comum repetir tarefas:

- listar produtos
- percorrer alunos
- tentar uma operacao varias vezes
- somar diversos itens

Em Python, isso acontece principalmente com `for` e `while`.

## Por que isso e importante

Sem loops, programas ficam limitados a poucos passos fixos. Com loops, o software escala melhor para entradas variaveis.

## Vantagens

- reduzem repeticao manual
- permitem automacao de rotinas
- funcionam bem com colecoes e contagens

## Desvantagens e limites

- `while` mal definido pode virar loop infinito
- excesso de condicoes internas dificulta depuracao
- uso desnecessario de `break` e `continue` pode confundir

## Arquivos da secao

### 1. `01-for.py`

Conceito:
- repetir com uma faixa conhecida

Entrada:
- nenhuma

Saida:
- contagem sequencial

### 2. `02-while.py`

Conceito:
- repetir enquanto uma condicao for verdadeira

Entrada:
- nenhuma

Saida:
- atualizacao progressiva de contador

### 3. `03-break_continue.py`

Conceito:
- interromper ou pular iteracoes

Entrada:
- nenhuma

Saida:
- demonstracao de alteracao no fluxo do laco

### 4. `04-input_tabuada.py`

Conceito:
- gerar repeticao baseada em valor digitado

Entrada:
- numero para tabuada

Saida esperada:

```text
Digite um numero para ver a tabuada: 4

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
```

### 5. `05-projeto_final_caixa_mercado.py`

Objetivo do projeto:
- registrar varios itens ate o usuario encerrar
- consolidar `while`, `break` e `continue`

Caso real:
- caixa simples
- lancamento de despesas
- somatorio de entradas em terminal

Entrada:
- varios valores de itens
- `0` para finalizar

Saida esperada:

```text
Digite o valor do item ou 0 para finalizar: 12.5
Item registrado. Total parcial: R$ 12.50
Digite o valor do item ou 0 para finalizar: 8
Item registrado. Total parcial: R$ 20.50
Digite o valor do item ou 0 para finalizar: 0

Resumo do caixa
Itens registrados: 2
Total da compra: R$ 20.50
```

## Aprendizado profissional

Loops sao uma das ferramentas mais usadas em automacao, leitura de dados, ETL, scripts administrativos e processamentos em lote.

## Erros comuns e sintaxe correta

- erro comum: criar `while` sem atualizar a condicao e gerar loop infinito
- boa pratica: altere a variavel de controle dentro do laco
- erro comum: usar `break` e `continue` sem entender o efeito no fluxo
- boa pratica: use comentarios curtos nos trechos mais sensiveis
- sintaxe correta:

```python
for numero in range(1, 6):
    print(numero)
```
