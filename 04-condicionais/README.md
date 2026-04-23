# Modulo 04 - Condicionais

Condicionais permitem que o programa tome decisoes. Em vez de executar sempre o mesmo fluxo, o sistema escolhe um caminho de acordo com regras.

## Visao conceitual

Com `if`, `elif` e `else`, o desenvolvedor traduz politicas do mundo real em codigo. Isso vale para acesso, aprovacao, descontos, riscos e classificacoes.

## Por que isso e importante

Programas profissionais nao apenas calculam; eles decidem. Exemplos:

- liberar ou bloquear um acesso
- definir a faixa de um aluno
- encaminhar um usuario para o fluxo correto

## Vantagens

- representam regras de negocio de forma direta
- permitem respostas diferentes para situacoes diferentes
- sao base para automacao inteligente

## Desvantagens e limites

- muitos niveis de aninhamento complicam leitura
- condicoes duplicadas aumentam manutencao
- regras mal priorizadas geram comportamentos incorretos

## Arquivos da secao

### 1. `01-if.py`

Conceito:
- executar um bloco quando uma condicao for verdadeira

Entrada:
- nenhuma

Saida:
- uma mensagem condicionada

### 2. `02-if_else.py`

Conceito:
- escolher entre dois caminhos

Entrada:
- nenhuma

Saida:
- decisao binaria

### 3. `03-elif.py`

Conceito:
- tratar faixas intermediarias

Entrada:
- nenhuma

Saida:
- classificacao por faixa

### 4. `04-input_avaliacao.py`

Conceito:
- receber uma nota e decidir a situacao do aluno

Entrada:
- nota final

Saida esperada:

```text
Digite a nota final: 6.2
Situacao: recuperacao
```

### 5. `05-projeto_final_triagem_acesso.py`

Objetivo do projeto:
- validar se uma pessoa pode entrar em um evento
- consolidar condicoes simples e combinadas

Caso real:
- portarias
- check-in
- validacao de elegibilidade

Entrada:
- idade
- documento
- ingresso

Saida esperada:

```text
Idade do participante: 21
Possui documento com foto? (s/n): s
Possui ingresso valido? (s/n): s
Entrada liberada. Bom evento!
```

## Aprendizado profissional

Quem domina condicionais consegue modelar grande parte das regras que sustentam sistemas administrativos, academicos e comerciais.

## Erros comuns e sintaxe correta

- erro comum: esquecer os dois pontos no final do `if`
- sintaxe correta:

```python
if idade >= 18:
    print("Maior de idade")
```

- erro comum: identacao incorreta dentro do bloco
- boa pratica: mantenha 4 espacos por nivel
- erro comum: comparar texto sem padronizar maiusculas e minusculas
- boa pratica: use `.strip().lower()` antes de comparar respostas como `s` e `n`
