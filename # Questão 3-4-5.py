# Questão 3
# Valor da variável SOMA?
def variavel_soma():
    INDICE = 12
    SOMA = 0
    K = 1

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(f"O valor da variável SOMA é: {SOMA}")
# A variável SOMA é igual a: 77

# Questão 4 - Descubra a lógica e complete o próximo elemento:
#        a) 1, 3, 5, 7, (9).--------------------Adicionar 2 ao número anterior.
#        b) 2, 4, 8, 16, 32, 64, (128).---------Multiplicar por 2 o número anterior.
#        c) 0, 1, 4, 9, 16, 25, 36, (49).-------Adicionar o próximo número ímpar ao número anterior.
#        d) 4, 16, 36, 64, (100).---------------Elevar o próximo número par ao quadrado, iniciando do 2.
#        e) 1, 1, 2, 3, 5, 8, (13).-------------Somar os dois números anteriores.
#        f) 2, 10, 12, 16, 17, 18, 19, (200).---O próximo número, escrito, deve começar com a letra "D".


# Questão 5 - Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. 
# Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
# Seu objetivo é descobrir qual interruptor controla qual lâmpada. 
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

# resposta: nesta questão as variáveis que tenho controle são: luz, interruptores, e o calor.
# desta forma, o interruptor 1 eu deixaria ligado por vários minutos. O interruptor 2 deixaria desligado.
# E o interruptor 3 eu ligaria antes de desligar o interruptor 1.
# Porque no mesmo instante que eu desligar a número 1 e ligar a número 3, iria utilizar as 2 viagens para ir em qualquer sala.
# A primeira sala pode estar com luz quente e desligada - sendo do interruptor 1. 
# A segunda sala pode estar com a luz acesa - sendo do interruptor 3.
# E a terceira sala pode estar com a luz fria, pois nunca foi ligada - sendo do interruptor 2.