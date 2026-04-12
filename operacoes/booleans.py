# Nesta seção vamos falar sobre os tipos de dados booleanos em Python. 
# Os booleanos são usados para representar valores de verdade, ou seja, verdadeiro (True) e falso (False). 
# Eles são fundamentais para a lógica de programação e controle de fluxo.

# Em Python, os booleanos são representados pelas palavras-chave True e False, que são sensíveis a maiúsculas.

# Exemplo de uso de booleanos:
esta_chovendo = True
esta_ensolarado = False

# Podemos usar os booleanos em estruturas de controle, como if, while, etc.
if esta_chovendo:
    print("Está chovendo, pegue um guarda-chuva!")
else:
    print("Não está chovendo, aproveite o dia!")

# Os booleanos também podem ser usados em expressões lógicas e comparações.
idade = 18
pode_dirigir = idade >= 18  # Isso retorna True, pois a idade é maior ou igual a 18
print(pode_dirigir)  # Saída: True  

# Além disso, em Python, outros valores também podem ser considerados como verdadeiros ou falsos.
# Por exemplo, os seguintes valores são considerados falsos:
# - False
# - None
# - 0 (zero de qualquer tipo numérico)
# - 0.0 (zero de ponto flutuante)
# - "" (string vazia)
# - [] (lista vazia)
# - () (tupla vazia)
# - {} (dicionário vazio)
# Todos os outros valores são considerados verdadeiros.
# Exemplo:
if not esta_ensolarado:
    print("Não está ensolarado, talvez chova mais tarde.")  
# Em resumo, os booleanos são essenciais para a lógica de programação e controle de fluxo em Python, permitindo que você tome decisões com base em condições verdadeiras ou falsas.
