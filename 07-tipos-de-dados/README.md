# Modulo 07 - Tipos de dados

Tipos de dados determinam como o Python organiza e manipula informacoes. Escolher a estrutura correta facilita leitura, manutencao e modelagem do problema.

## Visao conceitual

Cada tipo serve melhor a um contexto:

- `str` para texto
- `list` para colecoes mutaveis e ordenadas
- `tuple` para dados fixos
- `dict` para registros nomeados

## Por que isso e importante

Sistemas reais raramente trabalham com um unico formato de dado. Um cadastro, por exemplo, mistura texto, listas de interesses e registros com campos nomeados.

## Vantagens

- melhor representacao do dominio
- codigo mais expressivo
- estruturas adequadas para diferentes operacoes

## Desvantagens e limites

- usar tipo errado gera codigo confuso
- estruturas mutaveis exigem mais cuidado
- iniciantes podem misturar responsabilidades entre lista e dicionario

## Como escolher o tipo certo

- use `str` quando o foco for texto, exibicao, busca ou padronizacao
- use `list` quando a ordem importa e os itens podem mudar
- use `tuple` quando os valores forem fixos e posicionais
- use `dict` quando cada dado precisar de um nome claro

## Truques e sugestoes praticas

### Strings

- use `strip()` para limpar espacos extras vindos de `input()`
- use `lower()` ou `upper()` para comparar textos sem depender de maiusculas
- use `title()` apenas para exibicao, nao para validacao interna
- prefira `f-string` para montar mensagens mais legiveis

Exemplo:

```python
email = input("Email: ").strip().lower()
print(f"Email normalizado: {email}")
```

### Listas

- use `append()` para adicionar um item ao final
- use `len(lista)` para saber quantos itens existem
- percorra listas com `for` em vez de acessar indice por indice manualmente
- evite alterar a lista enquanto a percorre sem necessidade

Exemplo:

```python
tarefas = []
tarefas.append("estudar Python")
tarefas.append("fazer exercicios")
print("Total de tarefas:", len(tarefas))
```

### Tuplas

- use tuplas para coordenadas, dimensoes, configuracoes fixas e retornos simples
- uma tupla comunica melhor a ideia de "nao alterar este conjunto"
- se voce precisa mudar os valores com frequencia, provavelmente uma lista faz mais sentido

Exemplo:

```python
resolucao = (1920, 1080)
print("Largura:", resolucao[0])
```

### Dicionarios

- use dicionarios para representar entidades como aluno, produto ou usuario
- prefira chaves descritivas como `nome`, `idade`, `preco`
- `dict.get("chave")` e util quando a chave pode nao existir
- dicionarios sao otimos para integrar com JSON e APIs

Exemplo:

```python
produto = {"nome": "Mouse", "preco": 99.9}
print(produto.get("estoque", "nao informado"))
```

## Armadilhas comuns

- `input()` sempre retorna texto; converta com `int()` ou `float()` quando necessario
- listas e dicionarios podem ser alterados depois de criados; isso e util, mas exige cuidado
- acessar uma chave inexistente com `dicionario["chave"]` gera erro
- comparar texto sem padronizar maiusculas e minusculas costuma causar falhas sutis

## Sugestoes de estudo

1. Pegue um mesmo problema e tente modela-lo com lista e com dicionario para comparar clareza.
2. Teste strings com espacos extras para ver o efeito de `strip()`.
3. Crie pequenos cadastros com `dict` e depois exiba com `f-string`.
4. Transforme listas simples em relatorios usando `for`.
5. Observe quando uma tupla expressa melhor "dado fixo" do que uma lista.

## Arquivos da secao

### 1. `01-strings.py`

Conceito:
- manipular texto

Entrada:
- nenhuma

Saida:
- transformacoes de uma frase

### 2. `02-listas.py`

Conceito:
- colecao ordenada com alteracao de itens

Entrada:
- nenhuma

Saida:
- lista original e atualizada

### 3. `03-tuplas_dicionarios.py`

Conceito:
- tupla como dado fixo
- dicionario como registro nomeado

Entrada:
- nenhuma

Saida:
- exibicao dos dados estruturados

### 4. `04-input_perfil_usuario.py`

Conceito:
- combinar entrada textual, lista e dicionario

Entrada:
- nome
- cargo
- hobbies separados por virgula

Saida esperada:

```text
Nome do usuario: Bianca
Cargo: Analista
Informe tres hobbies separados por virgula: leitura, cinema, viagem

Perfil gerado
{'nome': 'Bianca', 'cargo': 'Analista', 'hobbies': ['leitura', 'cinema', 'viagem']}
```

### 5. `05-projeto_final_catalogo.py`

Objetivo do projeto:
- modelar um produto com varios tipos de dados
- consolidar string, lista, tupla e dicionario

Caso real:
- cadastro de catalogo
- vitrine de e-commerce
- simulador de inventario

Entrada:
- nome do produto
- categoria
- preco

Saida esperada:

```text
Nome do produto: Mouse Gamer
Categoria: Perifericos
Preco: 149.9

Catalogo do produto
Nome: Mouse Gamer
Categoria: Perifericos
Preco: R$ 149.90
Dimensoes padrao: (10, 20, 30)
Tags: ['novo', 'destaque', 'perifericos']
```

### 6. `06-strings_avancadas.py`

Conceito:
- limpeza com `strip()`
- padronizacao com `title()`
- substituicao com `replace()`
- verificacao com `startswith()`
- quebra com `split()`
- interpolacao com transformacao embutida

Entrada:
- nenhuma

Saida:
- exemplos de tratamento mais profissional de texto

### 7. `07-projeto_final_boletim_formatado.py`

Objetivo do projeto:
- montar um boletim textual com alinhamento e formatacao
- combinar strings, calculo, condicoes e exibicao profissional

Caso real:
- relatorio academico
- resumo de desempenho
- emissao de comprovante simples em terminal

Entrada:
- nome do aluno
- disciplina
- nota 1
- nota 2
- frequencia

Saida esperada:

```text
Nome do aluno: bruno silva
Disciplina: algoritmos
Nota 1: 8
Nota 2: 7
Frequencia em percentual: 90

----------------------------------------------
              BOLETIM DO ALUNO
----------------------------------------------
Aluno         : Bruno Silva
Disciplina    : Algoritmos
Nota 1        :      8.0
Nota 2        :      7.0
Media         :      7.5
Frequencia    :    90.0%
Situacao      : Aprovado
----------------------------------------------
```

## Aprendizado profissional

Dominar tipos de dados e essencial para construir APIs, modelar entidades, integrar sistemas e organizar informacoes com mais precisao. Quando isso se junta a strings avancadas e boa formatacao, a qualidade da saida melhora muito em relatorios, dashboards textuais e automacoes.

## Erros comuns e sintaxe correta

- erro comum: esquecer aspas em strings, como `nome = Ana`
- sintaxe correta: `nome = "Ana"`
- erro comum: acessar indice inexistente em lista
- boa pratica: valide o tamanho com `len(lista)` quando necessario
- erro comum: acessar chave ausente com `dicionario["estoque"]`
- boa pratica: prefira `dicionario.get("estoque")` quando a chave for opcional
- erro comum: esquecer virgulas entre itens de lista, tupla ou dicionario
