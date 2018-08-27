


'''
você deve criar uma classe carro que vai possuir dois atributos compostos por outras classes:

1) Motor
2) Direção --

O motor controlará a velocidade. Terá os seguintes atributos:
1) atributo de dado velocidade
2) método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em  2 unidades

A direção terá a responsabilidade de controlar a direção. Ela oferecerá os atributos:
1- valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2 - Método girar à direita
3 - Método girar à esquerda

 N
O  L
 S

Exemplo:
#Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade()
2
>>> motor.acelerar()
>>> motor.velocidade()
3
>>> motor.frear()
>>> motor.velocidade()
1
>>> motor.frear()
>>> motor.velocidade()
0
>>> #Testando direção
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.frear()
>>> carro.calcular_velocidade()
0
>>> carro.calcular_direcao()
>>> 'Norte'

>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Leste'

>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Norte'

>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Oeste  '

'''

