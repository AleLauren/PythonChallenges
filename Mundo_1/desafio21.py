# DESAFIO 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA 
# O ÁUDIO DE UM ARQUIVO MP3.

from pygame import mixer
print('====== DESAFIO 21 ======')

# Inicia o mixer
mixer.init()
# Carrega a música
mixer.music.load("desafio21.mp3")
# Define o volume
mixer.music.set_volume(0.7)
# Play na música
mixer.music.play()

# LOOP INFINITO
while True:
	print("Pressione 'P' para pausar, 'V' para voltar")
	print("Pressione 'X' para fechar o programa")
	comando = input(" ")
	if comando in 'Pp':
		# Pausa a música
		mixer.music.pause()	
	elif comando in 'Vv':
		# Volta a música
		mixer.music.unpause()
	elif comando in 'Xx':
		# Para o mixer
		mixer.music.stop()
		break

