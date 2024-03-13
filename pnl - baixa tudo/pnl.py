from pytube import YouTube
import tkinter
import customtkinter




def IniciarDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        musica = ytObject.streams.get_audio_only()
        titulo.configure(text=ytObject.title, text_color='white')
        titulo.configure(text='')
        musica.download()
        ultimalabel.configure(text='Download Concluído com sucesso!', text_color='green')
    except:
        ultimalabel.configure(text='Url não reconhecida, Download não concluído. Tente novamente.', text_color='red')

def on_progress(stream, chunk, bytes_remaining):
    tamanho_total = stream.filesize
    bytes = tamanho_total - bytes_remaining
    porcentagem = bytes / tamanho_total * 100
    por = str(int(porcentagem))
    barra_progresso2.configure(text=por + '%')
    barra_progresso2.update()

    barra_progresso.set(float(porcentagem) / 100)
    

# Configurações Iniciais TKINTER
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')


app = customtkinter.CTk()
app.geometry('720x480')
app.title('Paneleiros Downloader')


titulo = customtkinter.CTkLabel(app, text='Coloque o link da sua música que deseja baixar')
titulo.pack(padx=10, pady=10)

var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=var)
link.pack()

ultimalabel = customtkinter.CTkLabel(app, text='')
ultimalabel.pack()

barra_progresso = customtkinter.CTkLabel(app, text='0%')
barra_progresso.pack()

barra_progresso2 = customtkinter.CTkProgressBar(app, width=400)
barra_progresso2.set(0)
barra_progresso2.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text='Iniciar Download', command=IniciarDownload)
download.pack(padx=10, pady=10)

                                                                                    
app.mainloop()