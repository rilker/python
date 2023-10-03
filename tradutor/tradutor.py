import tkinter as tk
from translate import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os

# Dicionário de idiomas comuns
idiomas = {
    "Inglês": "en",
    "Espanhol": "es",
    "Francês": "fr",
    "Alemão": "de",
    "Italiano": "it",
    "Holandês": "nl",
    "Russo": "ru",
    "Chinês": "zh",
    "Japonês": "ja",
    "Coreano": "ko",
    "Árabe": "ar",
    "Português": "pt",
    "Grego": "el",
    "Turco": "tr",
    "Sueco": "sv",
    "Dinamarquês": "da",
    "Norueguês": "não",
    "Finlandês": "fi",
    "Polonês": "pl",
    "Tcheco": "cs",
    "Húngaro": "hu",
    "Hebraico": "ele",
    "Hindi": "oi",
    "Tailandês": "th",
    "Indonésia": "id",
    "Vietnamita": "vi",
    "Malaio": "senhora",
    "Filipino": "tl",
    "Ucraniano": "reino unido",
    # Adicione mais idiomas conforme necessário
}

# Função para traduzir o texto e reproduzir a resposta em voz
def traduzir_e_falar():
    texto_origem = entrada_texto.get()
    idioma_destino = idiomas[lista_idiomas_destino.get()]
    tradutor = Translator(from_lang="pt-br", to_lang=idioma_destino)
    texto_traduzido = tradutor.translate(texto_origem)
    label_resultado.config(text=texto_traduzido)

    # Criar um arquivo temporário para a resposta em áudio
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio_file:
        tts = gTTS(text=texto_traduzido, lang=idioma_destino)
        tts.save(tmp_audio_file.name)

    # Carregar e reproduzir o arquivo de áudio
    resposta_audio = AudioSegment.from_mp3(tmp_audio_file.name)
    play(resposta_audio)

    # Excluir o arquivo temporário após a reprodução
    os.remove(tmp_audio_file.name)

# Configurar a janela
janela = tk.Tk()
janela.title("Tradutor com Voz")
janela.geometry("400x300")

# Configurar as cores da janela
janela.configure(bg="#333333")  # Cor de fundo da janela (cinza escuro)

# Criar um rótulo para a entrada
label_entrada = tk.Label(janela, text="Digite o texto em português:", bg="#333333", fg="white")  # Cor de fundo do rótulo (cinza escuro) e cor do texto (branco)
label_entrada.pack()

# Criar uma caixa de entrada de texto
entrada_texto = tk.Entry(janela, width=40)
entrada_texto.pack()

# Criar uma lista de opções para selecionar o idioma de destino
label_idioma_destino = tk.Label(janela, text="Selecione o idioma de destino:", bg="#333333", fg="white")  # Cor de fundo do rótulo (cinza escuro) e cor do texto (branco)
label_idioma_destino.pack()

# Lista de idiomas de destino
idiomas_destino = list(idiomas.keys())
lista_idiomas_destino = tk.StringVar(janela)
lista_idiomas_destino.set(idiomas_destino[0])  # Definir o primeiro idioma como padrão

menu_idiomas_destino = tk.OptionMenu(janela, lista_idiomas_destino, *idiomas_destino)
menu_idiomas_destino.pack()

# Criar um botão para iniciar a tradução e a voz
botao_traduzir = tk.Button(janela, text="Traduzir e Falar", command=traduzir_e_falar, bg="#007ACC", fg="white")  # Cor de fundo do botão (azul) e cor do texto (branco)
botao_traduzir.pack()

# Criar um rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="", bg="#333333", fg="white")  # Cor de fundo do rótulo (cinza escuro) e cor do texto (branco)
label_resultado.pack()

# Iniciar a janela
janela.mainloop()
