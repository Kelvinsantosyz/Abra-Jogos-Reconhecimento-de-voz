import speech_recognition as sr
import os
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

with sr.Microphone() as source: 
    engine.say("Olá, qual jogo você gostaria de jogar?")
    engine.say("1 -resident evil, 2- counter strinke, 3- valorant ")
    engine.runAndWait()
    
    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='pt-BR')
            print("Você disse: {}".format(text))
            if '1' in text.lower():
                jogo_path2 = r"C:/Users/Kelvin/Desktop/jogos/Resident Evil 2.url"
                os.startfile(jogo_path2)
                engine.say('Jogo aberto, divirta-se!')
                engine.runAndWait()
                
            elif '2' in text.lower():
                jogo_path = r"C:/Users/Kelvin/Desktop/jogos/CsGo.url"
                os.startfile(jogo_path)
                print("Jogo aberto!")
                engine.say("Jogo aberto!")
                engine.runAndWait()

            elif '3' in text.lower():
                jogo_path3 = r"C:/Users/Kelvin/Desktop/jogos/VALORANT.lnk"
                os.startfile(jogo_path3)
                engine.say('Jogo aberto, divirta-se!')
                engine.runAndWait()

            elif 'fechar' in text.lower():
                print("Encerrando o programa...")
                engine.say("Encerrando o programa...")
                engine.runAndWait()
                break

        
            engine.say("Algo mais ?")
            engine.runAndWait()

        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            engine.say("Não foi possível entender o áudio, por favor repita novamente")
            engine.runAndWait()

        except sr.RequestError as e:
            print("Erro ao solicitar reconhecimento de fala: {}".format(e))
            engine.say("Erro ao solicitar reconhecimento de fala")
            engine.runAndWait()
