# Modulo 03 - Operadores

Operadores transformam valores em resultados. Eles sao a base dos calculos, comparacoes e regras logicas que aparecem em sistemas reais.

## Visao conceitual

Sempre que um programa precisa somar, comparar, verificar ou combinar condicoes, ele usa operadores. Em Python, isso inclui:

- operadores aritmeticos
- operadores relacionais
- operadores logicos

## Por que isso e importante

Negocios reais dependem de regras objetivas. Exemplos:

- calcular total de compra
- verificar idade minima
- decidir se um usuario atende varios criterios ao mesmo tempo

## Vantagens

- permitem expressoes curtas e poderosas
- reduzem trabalho manual
- aproximam o codigo das regras do negocio

## Desvantagens e limites

- expressoes densas ficam dificeis de ler
- divisao e comparacoes exigem atencao
- logica mal agrupada produz bugs silenciosos

## Arquivos da secao

### 1. `01-operadores_aritmeticos.py`

Conceito:
- soma, subtracao, multiplicacao, divisao, modulo e potencia

Entrada:
- nenhuma

Saida:
- resultados numericos fixos

### 2. `02-operadores_relacionais.py`

Conceito:
- comparar valores e obter `True` ou `False`

Entrada:
- nenhuma

Saida:
- avaliacoes booleanas

### 3. `03-operadores_logicos.py`

Conceito:
- combinar varias condicoes

Entrada:
- nenhuma

Saida:
- decisoes booleanas compostas

### 4. `04-input_calculadora.py`

Conceito:
- aplicar operadores a valores digitados pelo usuario

Entrada:
- primeiro numero
- segundo numero

Saida esperada:

```text
Primeiro numero: 10
Segundo numero: 5

Resultados
Soma: 15.0
Subtracao: 5.0
Multiplicacao: 50.0
Divisao: 2.0
```

### 5. `05-projeto_final_simulador_compra.py`

Objetivo do projeto:
- simular subtotal, desconto e total final
- aplicar operadores aritmeticos, relacionais e logicos em conjunto

Caso real:
- fechamento de carrinho
- simulador comercial
- conferencia de desconto

Entrada:
- valor unitario
- quantidade
- percentual de desconto

Saida esperada:

```text
Valor unitario do produto: 50
Quantidade: 3
Percentual de desconto: 10

Resumo da compra
Subtotal: R$ 150.00
Desconto: R$ 15.00
Total final: R$ 135.00
Desconto aplicado? True
Compra acima de R$ 100? True
```

## Aprendizado profissional

Este modulo aproxima bastante o estudo de cenarios de loja, financeiro, planilhas automatizadas e validacoes de negocio.

## Erros comuns e sintaxe correta

- erro comum: dividir por zero em expressoes como `a / b`
- boa pratica: valide `b != 0` antes da divisao
- erro comum: confundir `=` com `==`
- sintaxe correta: `=` atribui valor e `==` compara valores
- erro comum: escrever expressoes longas sem parenteses
- boa pratica: use parenteses para deixar a intencao mais clara
