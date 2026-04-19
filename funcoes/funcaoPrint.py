# Neste tópico vamos aprender a usar a função print() para exibir mensagens na tela, logo abaixo temos um exemplo de como usar a função print() para exibir uma mensagem simples:

print("Olá, mundo!")

# A função print() é usada para exibir mensagens na tela, ela pode receber uma ou mais mensagens como argumento, e cada mensagem será exibida em uma nova linha. Por exemplo:
print("Olá, mundo!")
print("Bem-vindo ao Python!")

# Também podemos usar a função print() para exibir o valor de variáveis, por exemplo:
nome = "Alice"
print(f"Olá, {nome}!")

# A função print() também pode ser usada para exibir o resultado de expressões, por exemplo:
a = 5
b = 10
print(f"A soma de a e b é: {a + b}") 

# Além disso, a função print() tem alguns parâmetros opcionais que podem ser usados para personalizar a saída, como o parâmetro end, que define o que será exibido no final da mensagem. Por exemplo:
print("Olá, ", end="")
print("mundo!")
# Neste exemplo, a primeira chamada da função print() exibe "Olá, " e o parâmetro end="" faz com que a próxima mensagem seja exibida na mesma linha, resultando em "Olá, mundo!" na tela.

# Outro parâmetro útil é o sep, que define o separador entre as mensagens. Por exemplo:
print("Python", "é", "incrível!", sep="-")
# Neste exemplo, as mensagens "Python", "é" e "incrível!" serão exibidas com um hífen como separador, resultando em "Python-é-incrível!"

# Em resumo, a função print() é uma ferramenta essencial para exibir mensagens, variáveis e resultados de expressões na tela, e pode ser personalizada usando os parâmetros end e sep para controlar a formatação da saída. 

# Agora vammso avançar com parametros mais avançados da função print(), como o parâmetro file, que permite direcionar a saída para um arquivo em vez de exibi-la na tela. Por exemplo:
with open("saida.txt", "w") as arquivo:
    print("Esta mensagem será escrita no arquivo saida.txt", file=arquivo)
# Neste exemplo, a mensagem "Esta mensagem será escrita no arquivo saida.txt" será escrita no arquivo "saida.txt" em vez de ser exibida na tela. O parâmetro file é útil para salvar resultados ou mensagens em arquivos para posterior análise ou registro.

# Outro parâmetro avançado é o flush, que controla se a saída deve ser imediatamente enviada para a tela ou para o arquivo. Por exemplo:
import time
print("Processando...", end="", flush=True)
time.sleep(2)
print(" Concluído!")
# Neste exemplo, a mensagem "Processando..." será exibida imediatamente na tela, mesmo que haja um atraso de 2 segundos antes de exibir " Concluído!". O parâmetro flush=True garante que a saída seja enviada imediatamente, o que é útil para mostrar mensagens de progresso ou status em tempo real.