import datetime
import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui

audio = sr.Recognizer()
maquina = pyttsx3.init()


# Função para fechar a aba pelo título


def executa_comando():
    comando = ''

    with sr.Microphone() as mic:
        print('ouvindo...')
        voz = audio.listen(mic)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()

    return comando



def comando_voz_usuario(comando_inicial=None):
    comando = comando_inicial
    
    while True :  # Loop contínuo
        comando = executa_comando()
        if 'horas' in comando :
            hora = datetime.datetime.now().strftime('%H:%M')  # Use '%H:%M' para horas no formato 24h
            maquina.say("Agora são " + hora)
            maquina.runAndWait()

        elif 'toque' in comando :
            print('procurando')
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Tocando')
            maquina.runAndWait()

        elif ('google') in comando :
            maquina.say("O que você quer buscar no Google?")
            maquina.runAndWait()
            try :
                with sr.Microphone() as mic :
                    print('Ouvindo...')
                    voice = audio.listen(mic)
                    query = audio.recognize_google(voice, language='pt-BR' )
                    maquina.say(f"Aqui estão os resultados da pesquisa para {query}.")
                    maquina.runAndWait()
                    url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(url)

            except :
                maquina.say("Desculpe, não entendi o que você disse.")
                maquina.runAndWait()



        elif 'fechar aba' in comando :
            maquina.say("Fechando a aba.")
            maquina.runAndWait()
            pyautogui.hotkey('ctrl', 'w')# Use a função de atalho para fechar a aba (Ctrl + w)

        elif 'trocar aba' in comando :
            maquina.say("trocando.",)
            maquina.runAndWait()

            pyautogui.hotkey('ctrl', 'tab')

        elif 'no cu' in comando:
            maquina.say('Tomar no cu você')
            maquina.runAndWait()

        elif 'dormir' in comando :  # Comando para finalizar o loop
            maquina.say("Até logo!")
            maquina.runAndWait()
            break


comando_voz_usuario()
