from tkinter import Tk, Frame, Label, PhotoImage, Button, Frame, Entry, mainloop
from functions import *

from threading import Thread

version = "0.3.0"

# Config
nome_IA = "Programa"
altura_janela = 700
largura_janela = 500

texto_inicial = f'Bem-Vindo\n\nPrograma criado por:\nKainan H. C. dos Santos\n\nParticipantes: Alice Cristina, Gustavo Schmitt\n\nCriado para a atividade de apresentação de Filosofia, sobre tecnologia.\nTema: "Inteligência Artificial"\n\nEXEMPLO DE INTELIGÊNCIA ARTIFICIAL PROCEDURAL!\n Version: {version}'

# Interface Gráfica
def sistema():
	dados = carrega_arquivo("dados.txt", "r")
	num_erros = 0
	limite_erros = 3

	entrada.lower()

	if entrada.get() == "/...":
		pass

	else:
		index = 0
		while index < len(dados):
			dados_perguntas = dados[index].split(";")

			if entrada.get() == dados_perguntas[1]:
				muda_aparencia(0)
				msg_resposta(f"{nome_IA}: {dados_perguntas[2]}")

				mensagem_ler_audio = dados_perguntas[2]
				arquivo_ler_audio = str(index).strip()

				sound_thread = Thread(target=le_msg_audio(mensagem_ler_audio, arquivo_ler_audio))
				sound_thread.start()

				# le_msg_audio(mensagem_ler_audio, arquivo_ler_audio)
				break
			else:
				index += 1
		if index == len(dados):
			msg_resposta(f"{nome_IA}: Hum parece que isso não está em meu banco de dados :)", "erro")
			muda_aparencia(1)


			le_msg_audio("Hum parece que isso não está em meu banco de dados.", "erro_nao_encontrado")

def programa():
	msg_resposta("Carregando...")
	sistema()

def msg_resposta(msg, tipo="normal"):
	
	if tipo == "erro":
		resposta["foreground"] = "#ff0000"
	else:
		resposta["foreground"] = "white"
	resposta["text"] = msg
	resposta.update()

def muda_aparencia(aparencia):
	if aparencia == 0:
		ia_aparencia_img["file"] = "img/iaFeliz.png"
	elif aparencia == 1:
		ia_aparencia_img["file"] = "img/iaTriste.png"



# ========================================================
# 
# 					INTERFACE GRÁFICA
# 
# ========================================================


janela_app = Tk()
janela_app.title("IA | Inteligência Artificial")
janela_app["bg"] = "black"
# janela_app.iconbitmap(r'img/ia.ico')
janela_app.geometry(f"{largura_janela}x{altura_janela}")

janela = Frame(
	janela_app,
	bg="black",
	padx=1,
	pady=1
	)
janela.pack()


versao = Label(janela, text=f"V: {version}", bg="black", foreground="green")
versao.grid(column=0, row=0)

# --------------
# 
# Aparência IA
# 
# --------------

ia_aparencia_img = PhotoImage(file="img/iaFeliz.png")
ia_aparencia = Label(
	janela,
	image=ia_aparencia_img,
	bg="black"
	)
ia_aparencia.grid(column=2, row=1, padx=2, pady=2)

# --------------
# 
# --------------

container_resposta = Frame(janela)

resposta = Label(
	container_resposta,
	text=f"{texto_inicial}",
	bg="black",
	foreground="white",
	font="System",
	bd=1,
	padx=2,
	pady=2,
	wraplength=(400),
	height=(20),
	width=(50),
	relief="solid",
	justify="left"
	)
resposta.grid(column=1, row=2, padx=2, pady=2)
container_resposta.grid(column=2, row=2 , padx=2, pady=2)

container_entrada = Frame(janela)
entrada = Entry(
	container_entrada,
	bg="black",
	foreground="white",
	font="System",
	width=40
	)
entrada.grid(column=1, row=3, padx=2, pady=2)
container_entrada.grid(column=2, row=3 , padx=2, pady=2)

botao_enviar = Button(
	container_entrada,
	text="==>",
	command=programa,
	bg="black",
	foreground="white",
	font="System",
	)
botao_enviar.grid(column=2, row=3 , padx=2, pady=2)

janela.mainloop()
exit()