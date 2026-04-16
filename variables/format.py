# Nesta seção, vamos aprender a formatar strings usando o método `format()` e outros recursos de formatação em Python. A formatação de strings é uma maneira poderosa de criar mensagens dinâmicas e personalizadas. O método `format()` permite inserir valores em uma string de forma fácil e legível.
# Exemplo básico de formatação usando `format()`

nome = "Alice"
idade = 30
# Desta forma podemos criar uma mensagem formatada usando o método `format()`, onde os valores de `nome` e `idade` são inseridos nos lugares correspondentes na string.
# Curly braces `{}` são usadas como marcadores de posição para os valores que serão inseridos. O método `format()` substitui esses marcadores pelos valores fornecidos como argumentos.
# A ordem dos argumentos no método `format()` corresponde à ordem dos marcadores de posição na string. Você também pode usar índices para especificar a posição dos argumentos, como `{0}` para o primeiro argumento, `{1}` para o segundo, e assim por diante.
# Assim ao inves de alterar a string toda vez que quisermos mudar o nome ou a idade, podemos simplesmente alterar os valores das variáveis `nome` e `idade`, e a mensagem formatada será atualizada automaticamente.
# O método `format()` é muito flexível e pode ser usado para formatar números, datas, e outros tipos de dados, além de strings. Ele também suporta formatação avançada, como alinhamento, preenchimento, e formatação de casas decimais.
# Exemplo executando a redeclaração das variáveis e a formatação da mensagem:
nome = "Maycon"
idade = 23
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem) # Saída: Meu nome é Maycon e eu tenho 23 anos.

# Além do método `format()`, Python também oferece outras formas de formatar strings, como f-strings (disponíveis a partir do Python 3.6) e o operador `%`. As f-strings são uma maneira mais concisa e legível de formatar strings, usando a sintaxe `f"..."` e expressões dentro de chaves `{}`.
# Exemplo usando f-strings:
nome = "Maycon"
idade = 23
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem) # Saída: Meu nome é Maycon e eu tenho 23 anos
# Em resumo, a formatação de strings em Python é uma habilidade essencial para criar mensagens dinâmicas e personalizadas. O método `format()` e as f-strings são ferramentas poderosas que permitem inserir valores em strings de maneira fácil e legível, tornando seu código mais flexível e eficiente.
# O melhor método de formatação depende do contexto e da preferência pessoal, mas as f-strings são geralmente recomendadas por sua simplicidade e clareza.