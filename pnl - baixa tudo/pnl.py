from pytube import YouTube
import tkinter
import customtkinter
import os


def IniciarDownloadMusica():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        musica = ytObject.streams.filter(only_audio=True).first()
        file_path = f"{ytObject.title}.mp3"
        musica.download(output_path='.', filename=file_path)
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except Exception as e:
        ultimalabel.configure(text=f'Erro: {str(e)}', text_color='red')


def IniciarDownloadVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        file_path = f"{ytObject.title}.mp4"
        video.download(output_path='.', filename=file_path)
        titulo.configure(text=ytObject.title, text_color='white')
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except Exception as e:
        ultimalabel.configure(text=f'Erro: {str(e)}', text_color='red')

def on_progress(stream, chunk, bytes_remaining):
    tamanho_total = stream.filesize
    bytes = tamanho_total - bytes_remaining
    porcentagem = bytes / tamanho_total * 100
    por = str(int(porcentagem))
    barra_progresso2.configure(text=por + '%')
    barra_progresso2.update() 
    barra_progresso.set(float(porcentagem) / 100)

# < ==========Configs Initials ========== >
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Paneleiros Downloader')


# < ========== TITULO DO APP ========== >
titulo = customtkinter.CTkLabel(app, text='Coloque o link da sua música/vídeo que deseja baixar')
titulo.pack(padx=10, pady=10)

var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=var)
link.pack()

ultimalabel = customtkinter.CTkLabel(app, text='')
ultimalabel.pack()


# < ========== BARRA DE PROGRESSO ========== >
barra_progresso = customtkinter.CTkLabel(app, text='0%')
barra_progresso.pack()

barra_progresso2 = customtkinter.CTkProgressBar(app, width=400)
barra_progresso2.set(0)
barra_progresso2.pack(padx=10, pady=10)



# < ==========Botão de Download em Formato MP3 ========== >
downloadmusica = customtkinter.CTkButton(app, text='Iniciar Download em MP3', command=IniciarDownloadMusica)
downloadmusica.pack(padx=10, pady=10)

# < ==========Botão de Download em Formato MP4 ========== >
downloadvideo = customtkinter.CTkButton(app, text='Iniciar Download em MP4', command=IniciarDownloadVideo)
downloadvideo.pack(padx=10, pady=10)

app.mainloop()
