velocidade = 62
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 # distância de alcance do radar

velocidade_veiculo_acima_radar_1 = velocidade > RADAR_1

veiculo_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

multado_radar_1 = velocidade_veiculo_acima_radar_1 and veiculo_passou_radar_1

if veiculo_passou_radar_1 and velocidade <= RADAR_1:
    print('Veiculo dentro da velocidade permitida.')
 
if velocidade_veiculo_acima_radar_1:
    print('Velocidade do veiculo acima do permitido no radar 1.')

if  multado_radar_1 and \
    velocidade_veiculo_acima_radar_1:
    print('Multa aplicada.')