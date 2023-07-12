"""
CONSTANTE == 'Variáveis' que não vão mudar
Muitas condições no mesmo if (prática ruim)
    <- Contagem de complexidade (prática ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 99 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

local_carro_range = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
velocidade_maior_radar_1 = velocidade > RADAR_1

if local_carro_range:
    if velocidade_maior_radar_1:
        print('Multa! Carro passou da velocidade do radar 1')
    else: 
        print('Carro não ultrapassou a velocidade no radar 1')
else: 
    print('Carro não passou no range do radar 1')
