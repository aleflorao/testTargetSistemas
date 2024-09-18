# Questão 2
# Contar a ocorrência da letra 'a' em uma string

def contar_letra_a():
    texto = input("Digite uma string: ")
    quantidade_a = texto.lower().count('a')

    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")
