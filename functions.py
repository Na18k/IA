from time import sleep
import os

import gtts
from playsound import playsound

# from index import *

def delay(tempo_de_delay):
	sleep(tempo_de_delay)

def carrega_arquivo(arquivo, modo):

	if os.path.isfile('dados.txt') == True: 

		if modo == "r":
			arquivo = open(arquivo, "r")
			linhas = []

			for linha in arquivo:
				linha = linha.strip()
				linhas.append(linha)

			arquivo.close()
			return linhas

	else:
		print('Criando "dados.txt"...')
		arquivo = open("dados.txt", "w")
		arquivo.write("0;quem é seu criador?;Kainan H.")
		arquivo.close()
		print("Arquivo criado, tente novamente!")

def le_msg_audio(msg, nome_arquivo):

	if os.path.exists(f"audio/{nome_arquivo}.mp3"):

		playsound(f"audio/{nome_arquivo}.mp3")

	else:
		ser_falado = gtts.gTTS(msg, lang="pt-br")
		ser_falado.save(f"audio/{nome_arquivo}.mp3")

		playsound(f"audio/{nome_arquivo}.mp3")