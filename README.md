# Python Uni Basic

Material introdutorio de Python organizado por secoes progressivas, com exemplos executaveis, explicacoes conceituais, arquivos com entrada e saida de dados e mini projetos finais por modulo.

## Proposta do projeto

Este repositorio foi estruturado para servir como trilha de aprendizado. Cada modulo aborda um fundamento da linguagem e apresenta:

- objetivo tecnico
- justificativa de uso do conceito
- vantagens e limitacoes
- exemplos simples para estudo
- exemplos de aplicacao em problemas do mundo real
- arquivos com `input()` e `output`
- um projeto final para consolidacao
- exemplos de formatacao de strings e interpolacao profissional

## Estrutura da trilha

### 01. Hello World

Diretorio: `01-hello-world`

Aprendizados principais:
- como exibir saida no terminal
- como usar `print()`
- como formatar mensagens simples

Aplicacoes reais:
- mensagens de status
- logs iniciais de programas pequenos
- feedback visual para usuarios em scripts de terminal
- relatorios textuais com alinhamento e moeda

### 02. Variaveis

Diretorio: `02-variaveis`

Aprendizados principais:
- armazenar dados em memoria
- reaproveitar valores ao longo do programa
- nomear informacoes de forma clara

Aplicacoes reais:
- cadastro de usuarios
- calculo de totais
- configuracoes e preferencias

### 03. Operadores

Diretorio: `03-operadores`

Aprendizados principais:
- calcular valores
- comparar informacoes
- combinar regras logicas

Aplicacoes reais:
- calculo de desconto
- verificacao de idade minima
- validacao de regras de negocio

### 04. Condicionais

Diretorio: `04-condicionais`

Aprendizados principais:
- tomar decisoes no codigo
- executar caminhos diferentes conforme uma regra

Aplicacoes reais:
- aprovacao ou reprovacao de alunos
- liberacao de acesso
- classificacao por faixas

### 05. Loops

Diretorio: `05-loops`

Aprendizados principais:
- repetir tarefas automaticamente
- percorrer conjuntos de dados
- interromper ou pular iteracoes

Aplicacoes reais:
- processar listas de produtos
- validar entradas ate obter valor correto
- gerar relatorios repetitivos

### 06. Funcoes

Diretorio: `06-funcoes`

Aprendizados principais:
- encapsular logica
- reutilizar codigo
- tornar programas mais organizados

Aplicacoes reais:
- calculo de frete
- validacao de formulario
- geracao de relatorios e mensagens

### 07. Tipos de dados

Diretorio: `07-tipos-de-dados`

Aprendizados principais:
- trabalhar com texto
- manipular colecoes
- organizar dados compostos

Aplicacoes reais:
- listas de tarefas
- dados de alunos
- catalogos de produtos
- boletins e saidas formatadas com strings avancadas

### 08. Projeto integrador

Diretorio: `08-projeto-integrador`

Aprendizados principais:
- integracao entre modulos
- reutilizacao de funcoes utilitarias
- validacao centralizada
- estrutura mais proxima de um programa real

Aplicacoes reais:
- sistema academico simples
- formulario validado
- relatorio final com regras de negocio

## Estrutura interna de cada modulo

Cada secao foi padronizada com cinco niveis de estudo:

1. exemplo conceitual inicial
2. exemplo complementar
3. explicacao de variacao importante
4. arquivo com entrada e saida no terminal
5. mini projeto final aplicado

## Como estudar

1. Leia o `README.md` da secao antes de executar os arquivos.
2. Rode os exemplos na ordem numerada.
3. Altere valores e observe o novo comportamento.
4. Compare os exemplos basicos com os exemplos de caso real descritos na documentacao.
5. Reescreva cada solucao com seus proprios dados para consolidar o aprendizado.
6. Execute os arquivos com `input()` digitando valores diferentes para perceber como o comportamento muda.
7. Termine cada modulo rodando o projeto final da pasta.

## Como executar

Use `python3`:

```bash
python3 01-hello-world/01-hello_world.py
python3 02-variaveis/01-variaveis_basicas.py
python3 03-operadores/01-operadores_aritmeticos.py
python3 04-condicionais/05-projeto_final_triagem_acesso.py
```

## Padrao adotado no projeto

- cada secao possui arquivos enumerados
- os nomes dos arquivos descrevem o topico estudado
- os exemplos foram mantidos pequenos para destacar um conceito por vez
- a documentacao explica quando usar cada recurso e quais trocas ele envolve
- os arquivos interativos passam a incluir validacoes basicas e `try/except`

## Confiabilidade e sintaxe correta

Ao longo dos modulos, o projeto agora destaca:

- erros comuns de sintaxe, como esquecer `:` em `if`, `for`, `while` e `def`
- erros de conversao com `int()` e `float()`
- validacao de faixas, como notas entre 0 e 10 e percentual entre 0 e 100
- uso de `try/except` para evitar que uma entrada invalida derrube o programa
- exemplos de escrita correta com identacao consistente e nomes claros

## Padrao tecnico adicional

O projeto agora tambem inclui:

- utilitarios compartilhados em `shared/`
- testes automatizados com `unittest` em `tests/`
- projeto integrador final em `08-projeto-integrador/`

## Evolucao recomendada

Depois de estudar esta base, o proximo passo ideal e adicionar:

- `input()` para interacao com usuario
- tratamento de erros com `try` e `except`
- leitura e escrita de arquivos
- modulos e pacotes
- testes automatizados
