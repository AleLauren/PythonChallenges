# DESAFIO 046
# FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA 
# PARA O ESTOURO DE FOGOS DE ARTIFÍCIO, INDO DE 10 ATÉ 0, 
# COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES. 

from pygame import mixer
from time import sleep
print('====== DESAFIO 46 ======')

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print("""                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ """)

# Inicia o mixer
mixer.init()
# Carrega a música
mixer.music.load("desafio46.mp3")
# Define o volume
mixer.music.set_volume(0.7)
# Play na música
mixer.music.play()

# LOOP INFINITO
while True:
	print("Pressione 'X' para encerrar os fogos")
	comando = input(" ").upper()
	if comando == 'X':
		# Para o mixer
		mixer.music.stop()
		break