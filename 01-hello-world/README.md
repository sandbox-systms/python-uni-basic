# Modulo 01 - Hello World e entrada/saida

Este modulo apresenta a comunicacao mais basica entre programa e usuario: escrever no terminal com `print()` e ler dados com `input()`.

## Visao conceitual

Todo programa precisa, em algum momento, exibir resultados. Em Python, `print()` e a forma mais simples de produzir saida. Quando combinado com `input()`, o codigo deixa de ser apenas demonstrativo e passa a reagir ao que o usuario digita.

## Por que isso e importante

Antes de trabalhar com banco de dados, APIs ou interfaces visuais, o iniciante precisa entender o fluxo minimo de interacao:

1. o programa pergunta algo
2. o usuario informa dados
3. o programa processa
4. o programa devolve uma resposta

Esse ciclo aparece em praticamente todo software.

## Vantagens

- curva de aprendizado baixa
- feedback imediato no terminal
- excelente para depuracao e ensino
- permite prototipos rapidos

## Desvantagens e limites

- interfaces de terminal nao sao ideais para todos os usuarios
- `print()` nao substitui logging estruturado
- `input()` retorna texto, exigindo conversoes em varios cenarios

## Arquivos da secao

### 1. `01-hello_world.py`

Conceito:
- primeira saida em Python
- entendimento da sintaxe basica

Entrada:
- nenhuma

Saida:
- mensagens fixas no terminal

### 2. `02-print_variados.py`

Conceito:
- variacoes de `print()`
- uso de `sep`, `end`, `f-string`, `\n` e `\t`

Entrada:
- nenhuma

Saida:
- exemplos de formatacao textual

### 3. `03-input_output.py`

Conceito:
- leitura com `input()`
- montagem de saida a partir de dados informados

Entrada:
- nome
- cidade

Saida esperada:

```text
Digite seu nome: Ana
Digite sua cidade: Recife

Resumo do cadastro
Nome: Ana
Cidade: Recife
Seja bem-vindo, Ana!
```

### 4. `04-projeto_final_cartao_boas_vindas.py`

Objetivo do projeto:
- criar um cartao textual de boas-vindas
- consolidar entrada e saida de dados

Caso real:
- onboarding de curso
- confirmacao de inscricao
- scripts de recepcao em terminal

Entrada:
- nome do participante
- curso
- turno

Saida esperada:

```text
Nome do participante: Larissa
Nome do curso: Python Basico
Turno: Noite

===================================
      CARTAO DE BOAS-VINDAS
===================================
Participante: Larissa
Curso: Python Basico
Turno: Noite
Mensagem: sua jornada em Python comecou.
===================================
```

### 5. `05-formatacao_strings.py`

Conceito:
- interpolacao com `f-string`
- formatacao de moeda, percentual e inteiros
- alinhamento de colunas e preenchimento

Quando usar:
- relatorios no terminal
- comprovantes simples
- tabelas textuais
- exibicao mais profissional de dados

Saida esperada:

```text
Interpolacao basica com f-string
Cliente: Marina

Formatacao numerica
Saldo atual: R$ 1534.50
Taxa de ocupacao: 87.5%
```

### 6. `06-projeto_final_relatorio_textual.py`

Objetivo do projeto:
- gerar um relatorio financeiro legivel
- consolidar interpolacao, alinhamento e formatacao numerica

Caso real:
- demonstrativo simples de faturamento
- resumo administrativo
- relatorio de fechamento mensal

Entrada:
- nome da empresa
- faturamento
- despesas

Saida esperada:

```text
Nome da empresa: Alpha Tech
Faturamento do mes: 12000
Despesas do mes: 7800

==========================================
             RELATORIO MENSAL
==========================================
Empresa           : Alpha Tech
Faturamento       : R$     12000.00
Despesas          : R$      7800.00
Lucro             : R$      4200.00
Margem de lucro   :        35.0%
==========================================
```

## Aprendizado profissional

Embora simples, este modulo ja introduz um padrao muito usado: capturar informacoes, formatar apresentacao e entregar retorno claro ao usuario. A partir dos arquivos 5 e 6, o aluno tambem passa a ver como formatacao textual melhora a leitura e a percepcao de qualidade do software.
