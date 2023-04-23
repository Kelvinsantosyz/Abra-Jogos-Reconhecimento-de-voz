import speech_recognition as sr
import os
import pyttsx3

class Action :
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.action  = {
            '1': r'C:/Users/Kelvin/Desktop/jogos/Resident Evil 2.url',
            '2': r'C:/Users/Kelvin/Desktop/jogos/CsGo.url',
            '3': r'C:/Users/Kelvin/Desktop/jogos/VALORANT.lnk'
        }

    def run(self):
        with sr.Microphone() as source: 
            self.engine.say("Olá, qual jogo você gostaria de jogar?")
            self.engine.say("1- resident evil, 2- counter strinke, 3- valorant")
            self.engine.say("Ou se quiser sair do programa fale fechar")
            self.engine.runAndWait()
            
            while True:
                audio = self.r.listen(source)
                try:
                    text = self.r.recognize_google(audio, language='pt-BR')
                    print("Você disse: {}".format(text))
                    if '1' in text.lower():
                        os.startfile(self.action['1'])
                        self.engine.say('Jogo aberto, divirta-se!')
                        self.engine.runAndWait()
                        
                    elif '2' in text.lower():
                        os.startfile(self.action['2'])
                        print("Jogo aberto!")
                        self.engine.say("Jogo aberto!")
                        self.engine.runAndWait()
    
                    elif '3' in text.lower():
                        os.startfile(self.action['3'])
                        self.engine.say('Jogo aberto, divirta-se!')
                        self.engine.runAndWait()
    
                    elif 'fechar' in text.lower():
                        print("Encerrando o programa...")
                        self.engine.say("Encerrando o programa...")
                        self.engine.runAndWait()
                        break
    
                
                    self.engine.say("Algo mais ?")
                    self.engine.runAndWait()
    
                except sr.UnknownValueError:
                    print("Não foi possível entender o áudio")
                    self.engine.say("Não foi possível entender o áudio, por favor repita novamente")
                    self.engine.runAndWait()
    
                except sr.RequestError as e:
                    print("Erro ao solicitar reconhecimento de fala: {}".format(e))
                    self.engine.say("Erro ao solicitar reconhecimento de fala")
                    self.engine.runAndWait()

game_launcher = Action()
game_launcher.run()
