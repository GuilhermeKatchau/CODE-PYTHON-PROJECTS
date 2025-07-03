import tkinter as tk
import pygame 
import os
pygame.mixer.init()

def play_sound(sound_file):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

window = tk.Tk()
window.title("Soundboard")
window.geometry("300x200")

sons ={
    "son1": "son1.mp3",
    "son2": "son2.mp3",
    "son3": "son3.mp3.mp3",
    "son4": "son4.mp3",
}
for nome, caminho in sons.items():
    button = tk.Button(window, text=nome, command=lambda caminho=caminho: play_sound(caminho))
    button.pack(pady=10)

def add_sound():
   caminho = tk.askopenfilename(
       title="Selecione um arquivo de som",
       filetypes=(("Arquivos MP3", "*.mp3"), ("Todos os arquivos", "*.*"))
   )
   if caminho:
        nomeFicheiro = os.path.basename(caminho)
        criar_btn (nomeFicheiro, caminho)

def criar_btn(nome, caminho):
    button = tk.Button(window, text=nome, command=lambda caminho=caminho: play_sound(caminho))
    button.pack(pady=10)

# Configurações de janela
window.configure(bg='lightblue')

for nome, caminho in sons.items():
    if os.path.exists(caminho):
        criar_btn(nome, caminho)

# Botão para adicionar sons
btn_adicionar = tk.Button(window, text="Adicionar Som +", bg="lightgreen", command=add_sound)
btn_adicionar.pack(pady=10)
    
window.mainloop()