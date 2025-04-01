import random
import string

print("**********************************")
print("** Gerador de Senhas Aleatorias **")
print("**********************************")

# Define os tipos de caracteres disponíveis
letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

# Junta todos os caracteres possíveis
conjunto_de_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

# Solicita o tamanho da senha ao usuário
tamanho_senha = int(input("Digite o tamanho da senha: "))

# Gera uma lista de caracteres aleatórios com o tamanho especificado
lista_de_caracteres = random.choices(conjunto_de_caracteres, k=tamanho_senha)

# Converte a lista de caracteres em uma string
senha_gerada = "".join(lista_de_caracteres)

# Exibe a senha gerada
print("Sua senha segura é:", senha_gerada)