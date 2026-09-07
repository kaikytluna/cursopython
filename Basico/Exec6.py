velocidade_carro=65
local_carro=150

# velocidade_carro=float(input("Insira a velocidade do carro:"))
# local_carro=float(input("Em que km da via o carro está? "))

TOLERANCIA_RADAR=7
RADAR_1=60
MULTA_RADAR_1=60+TOLERANCIA_RADAR
LOCAL_RADAR_1=100
RADAR_RANGE_1= 3
INICIO_RANGE= LOCAL_RADAR_1-RADAR_RANGE_1
FIM_RANGE= LOCAL_RADAR_1+RADAR_RANGE_1


# range_multa=local_carro>=(LOCAL_RADAR_1-(RADAR_RANGE_1)) \
#     and local_carro<=(LOCAL_RADAR_1+RADAR_RANGE_1)
range_multa=INICIO_RANGE<=local_carro<=FIM_RANGE
multa_carro= range_multa and velocidade_carro>MULTA_RADAR_1

if range_multa and multa_carro:
    print("O carro está no radar e vai tomar multa.")
if range_multa and not multa_carro:
    print("O carro está no radar e não vai tomar multa.")

if multa_carro and local_carro>range_multa:
    print(f"O carro passou a {velocidade_carro} km/h em um radar de {RADAR_1} km/h no KM {LOCAL_RADAR_1}, assim sendo multado.")
if local_carro<LOCAL_RADAR_1:
    print("O carro ainda não passou no radar")
if local_carro>FIM_RANGE and not multa_carro:
    print("O carro passou no radar e não foi multado.")
# elif local_carro>FIM_RANGE and multa_carro:
#     print(f"O carro passou a {velocidade_carro} km/h em um radar de {RADAR_1} km/h, assim sendo multado.")