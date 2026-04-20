# Função `return` no Python

Neste material, o objetivo é entender como a palavra-chave `return` funciona dentro de funções em Python.

O `return` é usado para devolver um valor para quem chamou a função. Isso significa que a função pode processar alguma informação e entregar um resultado para ser usado depois em uma variável, em outro cálculo, em uma condição ou até em outra função.

## O que é `return`

Quando criamos uma função, podemos fazer com que ela:

- apenas execute alguma ação, como mostrar algo na tela com `print()`
- ou devolva um valor com `return`

Exemplo:

```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print(resultado)
```

Nesse caso:

- a função recebe `5` e `3`
- calcula a soma
- devolve `8` com `return`
- esse valor é guardado na variável `resultado`

## Diferença entre `print()` e `return`

Essa é uma das partes mais importantes:

### `print()`

O `print()` serve para exibir informações na tela.

```python
def exemplo_print():
    print("Olá")
```

Aqui, a função mostra `"Olá"` no terminal, mas não devolve esse valor.

### `return`

O `return` devolve um valor para fora da função.

```python
def exemplo_return():
    return "Olá"
```

Aqui, a função não está apenas exibindo a mensagem: ela está entregando esse valor para ser reutilizado.

Exemplo:

```python
mensagem = exemplo_return()
print(mensagem)
```

## O que acontece quando a função não tem `return`

Se uma função não tiver `return`, o Python retorna `None` automaticamente.

Exemplo:

```python
def sem_retorno():
    print("Executando algo")

valor = sem_retorno()
print(valor)
```

Saída:

```python
Executando algo
None
```

O `None` significa que nenhum valor foi devolvido.

## Quando o `return` é executado

Assim que o Python encontra um `return`, a função termina imediatamente.

Exemplo:

```python
def teste(numero):
    if numero > 0:
        return "Positivo"
    print("Esta linha só aparece se a condição for falsa")
    return "Zero ou negativo"
```

Se `numero` for maior que zero, a função devolve `"Positivo"` e encerra naquele momento.

## Exemplos abordados em `funcaoReturn.py`

O arquivo [funcaoReturn.py](./funcaoReturn.py) foi organizado com exemplos progressivos para mostrar o uso de `return` na prática.

### 1. Retorno simples

Uma função pode retornar um valor fixo:

```python
def saudacao():
    return "Olá, mundo!"
```

### 2. Retorno de cálculo

Uma função pode receber parâmetros e devolver o resultado:

```python
def somar(a, b):
    return a + b
```

### 3. Comparação entre `print()` e `return`

O arquivo mostra claramente que:

- `print()` apenas exibe
- `return` devolve um valor

### 4. Retorno com condição

Também é possível retornar valores diferentes dependendo de uma condição:

```python
def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"
```

### 5. Retorno antecipado

O `return` pode encerrar a função antes do restante do código ser executado.

### 6. Retornando mais de um valor

No Python, podemos retornar vários valores separados por vírgula:

```python
def operacoes_basicas(a, b):
    return a + b, a - b, a * b
```

Na prática, o Python agrupa esses valores em uma tupla.

### 7. Retorno booleano

Funções também podem devolver `True` ou `False`:

```python
def eh_positivo(numero):
    return numero > 0
```

### 8. Função sem `return`

O arquivo também mostra que funções sem `return` devolvem `None`.

### 9. Uso do retorno em outro cálculo

O valor retornado pode ser usado em novas operações:

```python
def calcular_quadrado(numero):
    return numero ** 2
```

### 10. Validação com `return`

O `return` pode ser usado para impedir erros ou tratar casos inválidos:

```python
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b
```

### 11. Retorno explícito de `None`

Às vezes faz sentido retornar `None` de propósito, por exemplo quando um valor não é encontrado.

### 12. Uso entre funções

Uma função pode usar o retorno de outra:

```python
def calcular_media(n1, n2):
    return (n1 + n2) / 2
```

Depois, outra função pode aproveitar esse resultado para tomar decisões.

## Resumo final

Os pontos mais importantes sobre `return` são:

- `return` devolve um valor para fora da função
- quando o `return` é executado, a função termina
- uma função pode retornar números, textos, listas, booleanos e vários valores ao mesmo tempo
- se não houver `return`, o Python devolve `None`
- `print()` mostra algo na tela, enquanto `return` entrega algo para ser reutilizado

## Como estudar este arquivo

Uma boa forma de aprender é:

1. ler cada exemplo no arquivo `funcaoReturn.py`
2. executar o arquivo
3. observar o que aparece na tela
4. alterar os valores dos exemplos para testar novos resultados
5. tentar criar suas próprias funções usando `return`

## Arquivos relacionados

- [funcaoReturn.py](/home/avlis/python-uni-basic/funcoes/funcaoReturn.py)
- [funcaoPrint.py](/home/avlis/python-uni-basic/funcoes/funcaoPrint.py)
