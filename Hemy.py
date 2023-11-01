'''
Requisitos

1) pyautogui - No Windows, pode ser instalado por "pip install pyautogui" no prompt de comando.
2) selênio - No Windows, pode ser instalado por “pip install selenium” no prompt de comando.
3) webdriver para Selenium - Pode ser instalado pesquisando "yourbrowsername webdriver" e instalando-o, de acordo com as instruções em README.md sobre Selenium.

'''

import random
import datetime
import pyautogui
import time
import win32com.client as wincl 
speak = wincl.Dispatch("SAPI.SpVoice")
# from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

################################################

# Local para criar a senha se necessário, cole aqui o código em "Proteção de senha para Hemy code.txt" !

################################################

# ----------------------------------------------- FUNÇÃO HORA ----------------------------------------------------------------------------------#


time.sleep(1)
hour = int(datetime.datetime.now().hour)

if hour>=0 and hour<12:
        speak.Speak('Olá, Bom Dia')
elif hour>=12 and hour<15:
        speak.Speak('Olá, Boa Tarde')
elif hour>=15 and hour<23:
        speak.Speak('Olá, Boa noite')

        
# ------------------------------------------------- PERGUNTAS PROGRAMADAS -----------------------------------------------------------------------#


ola = ["oi", "ola","ola hemy","ei hemy","OI","Hello","olá","opa","eai","eae","iae"]
bd = ["bom dia","bom dia hemy","BOM DIA","dia","DIA"]
bt = ["boa tarde","boa tarde hemy","Boa Tarde","TARDE"]
bn = ["boa noite","boa noite hemy","Boa Noite","NOITE"]
xau = ["xau","tchau","adeus","sair","ate logo","ate mais","xau hemy","ate depois","vou embora"]
estado = ["tudo bem com vc?","tudo bem contigo","como voce esta?","como voce ta?","como você está?","como vai voce?","como vai hemy?","tudo bem?","beleza?","como voce esta hoje?","como esta se sentindo?","como ta voce?","voce ta bem?"]
apresentacao = ["qual o seu nome","hemy","qual e o seu nome?","nome","qual seu nome?","seu nome?","como se chama?","como é o seu nome?","como e o seu nome","teu nome?","name","nome?","como voce se chama?","nome"]
hora = ["que horas são?","a hora atual?","hora atual","horas","horario","que horas?","me diga a hora","horário","que horas sao?" ,"que hora e?","que horas é?"]
tempo = ["tempo","qual e o tempo?","qual é o tempo?","tempo","boletim do tempo","tempo atual","tempo aberto","boletim do tempo aberto","Qual é o tempo?","Boletim do tempo","Tempo atual","Tempo aberto","Abra o boletim meteorológico","previsao do tempo"]
google = ["google","abra o google","google","Abra o google","Google","GOOGLE","abrir o google"]
calendario = ["dia","calendario","abra o calendario","mostre o calendario","abrir o calendario","abrir calendario","que dia e hoje"]
news = ["noticias","me mostre as noticias","abrir noticias","news","ver noticias"]
youtube = ["youtube","abrir o youtube","abrir youtube","abra o youtube"]
notepad = ["abra o bloco de notas","bloco de notas", "notepad","abra o bloco de nota","abrir bloco de notas"]
gmail = ["abra o gmail","gmail","enviar gmail","GMAIL","abrir gmail","abrir o gmail"]
av = ["aumentar volume","aumente o volume","aumentar volume","aumentar o volume"]
dv = ["diminua o volume","diminuir volume","diminuir o volume","abaixe o volume","abaixar volume","abaixar o volume"]
vm = ["mutar","mutar volume","mutar o volume","mute"]
vum = ["desmutar volume","desmutar o volume","desmutar"]
webcam = ["webcam","abrir camera","tire uma foto","tirar foto","ligar webcam"]
gmailsent = ["gmail","enviar gmail","envie um gmail","enviar um gmail"]
screenshot = ["print","printscreen","tire um print","print a tela","printscreen","captura de tela"]
desligar = ["desligar o computador","desligar o pc","desligue o computador","desligar","desligue","desligue a maquina","desligue o notebook"]
reiniciar = ["reiniciar","reinieie","reinicie o computador","reinicie a maquina","reinicie o notebook"]
idade = ["qual minha idade?","idade","calcule minha idade","minha idade","quantos anos eu tenho?","qual e a minha idade?","qual a minha idade","calcule a minha idade","calcule minha idade"]
linguagem = ["python","qual sua linguagem?","linguagem","que linguagem voce foi programada?","que linguagem voce usa?","qual a sua linguagem?",'linguagem de programação?']
assistentes = ["eai alexa","eai siri","siri","google assistente","alexa","conhece a siri?","conhece a alexa?","conhece a google assistente?","ok google"]
calc = ["calculadora","abra a calculadora","abrir calculadora","abrir a calculadora"]
ping = ["ping","veja o ping","verifique o ping","use o ping","abra o ping","ver ping","dispare o ping","abrir ping","abrir o ping"]
whatsapp = ["whatsapp","abrir whatsapp","abra o whatsapp","abrir o whatsapp","zapzap"]
ativador = ["ative o windows","ativador","ativar windows","ativar o windows"]

print("\n")
print("⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄          ****         ****   #############   ******     *****    ####       ####")
print("⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄          ****         ****   ############    ******     *****    ####       ####") 
print("⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰          ****         ****   ####            ******     *****    ####       ####")
print("⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤          ****         ****   ####            ******     *****    ####       ####")
print("⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗          *****************   ####            **   **  ** ****    ####       ####")
print("⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄          *****************   ############    **   **  ** ****    ###############")
print("⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄          ****         ****   ############    **   **  ******     ###############")
print("⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆   ⠄⠄⠄⠄⠄⠄⠄ ⠹⠈⢋⣽⣿⣿⣿            ****         ****   ####            **    ****  ****          ####")
print("⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄           ****         ****   ####            **          ****          ####")
print("⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄           ****         ****   ############    **          ****          ####")
print("⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⣿⠿⠛⠁              ****        ****    ############    ***          ****         ####")

print("\n")
print("Hemy - Uma pequena assistente virtual | (●'◡'●)\n\n")


nome = input(speak.Speak('Para iniciarmos , digite seu nome: '))

if nome == "jonathan" or nome == "john" or nome == "JONATHAN" or nome == "JOHN":
        speak.Speak(f'Engraçado, esse é o nome do meu criador, seja bem vindo, {nome}')


# ----------------------------------------- APRESENTAÇÃO DA BOT ----------------------------------------------------------------------------#
speak.Speak(f'Ok, {nome}')
speak.Speak('Primeiramente vou me apresentar. me chamo, Hemy, e sou um bot assistente virtual. ainda estou em desenvolvimento, porém, você pode me fazer perguntas objetivas que será um prazer lhe responder.')
speak.Speak('Peço gentilmente que utilize frases em minúsculo. Não use acentuação como til, ou agudo, não use caixa alta,nem abreviação, e por gentileza, se fizer alguma pergunta use o sinal de interrogação no final da frase')
speak.Speak('Eu quase me esqueci, para atividade via WEB, minha configuração padrão é acionada apenas no navegador. GOOGLE CHROME')

while True:
        
        speak.Speak('Me faça uma pergunta, ou me diga como posso te ajudar:')
        a = input('Digite: ')
        

        # -------------------------------------------- Horas -----------------------------------------------------#
        if a.lower() in hora:
                now = datetime.datetime.now()
                speak.Speak(nome + "são exatamente. " + now.strftime("%H:%M")+'\n')
                print ("São: " + now.strftime("%H:%M")+'\n')


        # -------------------------------------------- Print -----------------------------------------------------#
        elif a.lower() in screenshot:

                speak.Speak(f'{nome}, você está utilizando notebook, ou computador?')
                speak.Speak('Digite 1 para notebook, e 2 para computador')
                print("Digite [1/2]:")
                perguntacaptura = int(input("Digite [1/2]: "))

                if perguntacaptura == 1:

                        #método que funciona no notebook
                        speak.Speak("Você está utilizando um notebook")
                        speak.Speak("Preparando a Captura de tela")
                        pyautogui.hotkey('alt','space','n')
                        pyautogui.hotkey('alt','space','n')
                        pyautogui.hotkey('win','shift','s')
                        pyautogui.moveTo(946,767,duration=5)
                        pyautogui.click(728,29)
                        pyautogui.moveTo(946,767,duration=5)
                        pyautogui.click(1231,629)
                        speak.Speak("Captura realizada")

                elif perguntacaptura == 2:
                        speak.Speak("Você está utilizando um computador")

                        # método que funciona no pc
                        speak.Speak("Iniciando a captura de tela")
                        pyautogui.hotkey('printscreen')
                        pyautogui.hotkey('tab')
                        time.sleep(1)
                        pyautogui.hotkey('tab')
                        time.sleep(1)
                        pyautogui.hotkey('tab')
                        time.sleep(1)
                        pyautogui.hotkey('tab')
                        time.sleep(1)
                        pyautogui.hotkey('tab')
                        time.sleep(1)
                        pyautogui.hotkey('space')
                        pyautogui.typewrite("    ")
                        speak.Speak("Captura realizada")
                

        # -------------------------------------------- Gmail -----------------------------------------------------#
        #função de enviar gmail
        #função não pronta, ainda será trabalhada, pois acessar gmail requer segurança e acesso ao gmail.
        elif a.lower() in gmailsent:
                speak.Speak("Quem é o destinatário: ")
                print("Quem é o destinatário:")
                x = input()
                print("     ")

                speak.Speak("Qual é o assunto :")
                print("Qual é o assunto :")
                y = input()
                print("     ")
                speak.Speak("Qual é a mensagem: ")
                print("Qual é a mensagem: ")
                z = input()
                print("     ")

                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.moveTo(946,767,duration=1)
                pyautogui.typewrite("mail.google.com")
                pyautogui.typewrite(["enter"])
                pyautogui.moveTo(946,767,duration=6)
                pyautogui.click(80,194)
                pyautogui.moveTo(946,767,duration=3)
                pyautogui.click(722,285)
                pyautogui.typewrite(x)
                pyautogui.click(735,332)
                pyautogui.typewrite(y)
                pyautogui.click(716,373)
                pyautogui.typewrite(z)
                pyautogui.click(731,690)

        # -------------------------------------------- Webcam -----------------------------------------------------#
        elif a.lower() in webcam:
                speak.Speak("Irei tentar abrir sua câmera")
                speak.Speak("A função pode não funcionar devido a sua predefinição de segurança e privacidade")
                speak.Speak("ah, só irá funcionar em notebooks ou computadores com webcam")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("webcam") #posso utilizar diretamente "camera"
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                speak.Speak("Agora Sorria !!!")
                time.sleep(1)
                pyautogui.hotkey("space")
                print("     ")


        elif a.lower() in ativador:
                speak.Speak("Iniciando comandos de ativação do windows")
                speak.Speak("Lemabrando que a chave de ativação configurada é a do windows 11, caso sua versão seja outra, favor ajustar antes de seguir a execução")
                pyautogui.hotkey('win','r')
                time.sleep(1)
                pyautogui.typewrite("cmd")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite("slmgr.vbs /upk")
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("slmgr /ipk 6TP4R-GNPTD-KYYHQ]-7B7DP-J447Y")
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("slmgr /skms kms8.msguides.com")
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("slmgr /ato")
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                speak.Speak("Foi utilizado um comando padrão de ativação, caso não tenha funcionado, verifique as etapas abaixo")
                speak.Speak("se deseja verificar a versão do windows e configurações do sistema digite 1, caso queira sair, digite 2")
                at = int(input("1 - Verificação | 2 - Sair: "))
                if at == 1:
                        time.sleep(1)
                        pyautogui.hotkey('win','r')
                        time.sleep(2)
                        pyautogui.typewrite("cmd")
                        time.sleep(2)
                        pyautogui.typewrite(["enter"])
                        time.sleep(1)
                        pyautogui.typewrite("systeminfo")
                        pyautogui.typewrite(["enter"])
                        time.sleep(1)
                if at != 1:
                        print("Você escolheu sair, até logo, espero que tenha dado certo.")


        elif a.lower() in whatsapp:
                speak.Speak("Você deseja abrir o Whatspp via navegador ou aplicativo desktop?")
                speak.Speak("1 Para navegador, 2 para aplicativo desktop")
                escolha = int(input("1 - Navegador | 2 - App : \n"))
                if escolha == 1:
                        speak.Speak("Abrindo Whatsapp versão Navegador.")
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.typewrite("google chrome")
                        time.sleep(1)
                        pyautogui.typewrite(["enter"])
                        time.sleep(1)
                        pyautogui.typewrite('https://web.whatsapp.com/')
                        time.sleep(1)
                        pyautogui.typewrite(["enter"])
                        time.sleep(1)
                        speak.Speak("Pronto, agora aponte sua câmera ao QR code e inicie a sessão.")

                elif escolha == 2:
                        speak.Speak(f"Imagino que {nome} já tenha a aplicação baixada, caso não, tente baixa-lo na loja ou inicie pelo navegador")
                        time.sleep(1)
                        pyautogui.hotkey('win')
                        time.sleep(1)
                        pyautogui.typewrite("whatsapp")
                        time.sleep(1)
                        pyautogui.typewrite(["enter"])
                        time.sleep(1)
                        pyautogui.typewrite(["tab"])
                        pyautogui.typewrite(["space"])
                        time.sleep(1)
                        speak.Speak("Pronto, agora aponte sua câmera ao QR code e inicie a sessão.")


        # -------------------------------------------- Comandos pré-definidos -----------------------------------------------------#
        elif a.lower() in estado:
                speak.Speak(f"Olá, {nome}")
                status = input(speak.Speak('Eu estou ótima, melhor agora falando com você. e você? como vai?'))
                print("Estou ótima, e você ? (*/ω＼*)")
                if status == "bem" or status == "bem e voce?" or status == "vou bem" or status == "vou bem tambem":
                        speak.Speak('Que bom que está bem, fico feliz')
                        speak.Speak('Também estou bem, obrigada')
                elif status == 'mau' or status == 'mal' or status == "triste" or status == "vou mau" or status == "vou mal" or status == "estou mau" or status == "estou mal":
                        speak.Speak('Sinto muito, espero que você fique bem')
                        piada = input(speak.Speak('Fui programada para contar uma piada caso estivesse triste, você gostaria de ouvir?'))
                        if piada == "sim" or piada == "ok" or piada == "SIM" or piada == "tudo bem" or piada == "claro":
                                speak.Speak('Ok. lá vai.')
                                speak.Speak('Por que o rádio não pode ter filhos? . Porque ele é estéreo.')
                                print('Por que ele é estéreo (*/ω＼*)')

                                piada1 = input(speak.Speak('Gostaria de ouvir outra?'))
                                if piada1 == "sim" or piada1 == "ok" or piada1 == "SIM" or piada1 == "tudo bem" or piada1 == "claro":
                                        speak.Speak('ok, Por que o policial não usa sabão?. Porque ele prefere deter gente.')
                                        print('Por que o policial não usa sabão?. Porque ele prefere deter gente. (*/ω＼*)')
                                elif piada1 == "nao" or piada1 == "não":
                                        speak.Speak('Ok, não contarei.')
                        elif piada == "nao" or piada == "não":
                                speak.Speak(f'Que pena que não quer ouvir minha piada, mas espero que fique bem, {nome}')
                print("     ")


        elif a.lower() in idade:
                anoatual = 2023
                anouser = int(input(speak.Speak(f"{nome} ,Em que ano você nasceu?")))
                calc_idade = 2023 - anouser
                speak.Speak(f"{nome}, você tem {calc_idade} anos de idade.")
                print(f"{nome} tem {calc_idade} anos de idade !")

        elif a.lower() in linguagem:
                speak.Speak("Eu fui desenvolvida em Paiton")
                print("Desenvolvida em Python !!!")

        elif a.lower() in assistentes:
                speak.Speak("Você mencionou uma das minhas ídolas. As conheço e as admiro. tenho que evoluir muito pra chegar até o nível delas")
                speak.Speak("Algo me diz que a Siri, Alexa e a Google assistente temos algo me comum, vai ver seja a cor do cabelo.")

        # -------------------------------------------- Volumes -----------------------------------------------------#
        elif a.lower() in av:
                speak.Speak("Volume foi aumentado !")
                pyautogui.hotkey('volumeup')
                print("Aumentando volume")
                print("     ")

        elif a.lower() in dv:
                speak.Speak("Volume foi diminuido")
                pyautogui.hotkey('volumedown')
                print("Diminuindo volume")
                print("     ")

        elif a.lower() in vm:
                speak.Speak("Volume mutado")
                pyautogui.hotkey('volumemute')
                print("Mutando volume")
                print("     ")

        elif a.lower() in vum:
                speak.Speak("Volume desmutado")
                pyautogui.hotkey('volumemute')
                print("Volume desmutado")
                print("     ")
        # -------------------------------------------- Saudações -----------------------------------------------------#
        elif a.lower() in ola:
                speak.Speak(f"olá, {nome}.")
                print(f"Olá {nome}.")
        
        elif a.lower() in bd:
                speak.Speak(f"Bom dia, {nome} !")
                print (f"Bom dia {nome} !")
                print("     ")

        elif a.lower() in bt:
                speak.Speak(f"Boa tarde, {nome} !")
                print (f"Boa tarde {nome} !")
                print("     ")

        elif a.lower() in bn:
                speak.Speak(f"Boa noite, {nome} !")
                print (f"Boa noite, {nome} !")
                print("     ")

        elif a.lower() in xau:
                speak.Speak(f"Até mais, {nome}, foi bom conversar com você")
                botans = [f"Até mais, {nome}, foi bom conversar com você (✿◡‿◡)"]
                print(random.choice(botans)+'\n')
                break

        
        # -------------------------------------------- Tempo -----------------------------------------------------#
        elif a.lower() in tempo:
                speak.Speak("Para abrir a previsão do tempo, primeiramente irei abrir seu navegador")
                speak.Speak("Abrindo o Google Chrome")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("google")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite("previsao do tempo")
                time.sleep(2)
                pyautogui.typewrite(["enter"])


                print("Você abriu A previsão do tempo")
                print("     ")
                
                #https://weather.com/weather/today/l/-8.09,-34.94?par=google



        # ------------------------------------ Bloco de notas -----------------------------------------------------#
        elif a.lower() in notepad:
                speak.Speak("Abrindo o bloco de notas")
                pyautogui.hotkey('win' , 'r')
                time.sleep(1)
                pyautogui.typewrite("notepad")
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                pyautogui.typewrite("    ")

        # ---------------------------------------- Desligar -----------------------------------------------------#
        elif a.lower() in desligar:
                speak.Speak("Você desejou desligar o computador")
                speak.Speak("Para sua segurança, ele desligará em cinco segundos a partir de agora, até logo.")
                pyautogui.hotkey('win' , 'r')
                pyautogui.typewrite("cmd")
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("shutdown -s -t 5")
                pyautogui.typewrite(["enter"])
                break

        # ---------------------------------------- Reiniciar -----------------------------------------------------#
        elif a.lower() in reiniciar:
                speak.Speak("Você desejou reiniciar o computador")
                speak.Speak("Para sua segurança, ele desligará em menos de um minuto, até logo.")
                pyautogui.hotkey('win' , 'r')
                pyautogui.typewrite("cmd")
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("shutdown /r")
                pyautogui.typewrite(["enter"])
                break

        # ---------------------------------------- Avatar -----------------------------------------------------#
       


       #trabalhar os seguintes comandos abaixo:
       #Entender como funciona no pyautogui o botão do windows
       #abrir o cmd executar
       #abrir o chrome
       #realizar pesquisa do url
       #seguir as linhas do código


        # -------------------------------------------- Google -----------------------------------------------------#
        elif a.lower() in google:
                speak.Speak("Para abrir o google, primeiramente irei abrir seu navegador")
                speak.Speak("Abrindo o Google Chrome")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("google")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                speak.Speak("Você abriu o google")
                print("Você abriu o Google")
                print("     ")
                
                '''
                Método do google inicialmente foi pensado em abrir o cmd (win,r), escrever chrome e iniciar o google.
                '''

        # -------------------------------------------- Gmail -----------------------------------------------------#
        elif a.lower() in gmail:
                speak.Speak("Abrindo Gmail")
                pyautogui.click(264,744)
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite("mail.google.com")
                pyautogui.typewrite(["enter"])
                speak.Speak("Você abriu o gmail")
                print("     ")

        # -------------------------------------------- Youtube -----------------------------------------------------#
        elif a.lower() in youtube:
                speak.Speak("Para abrir o Youtube, primeiramente irei abrir seu navegador")
                speak.Speak("Abrindo o Google Chrome")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("google")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                time.sleep(2)
                pyautogui.typewrite("youtube")
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                speak.Speak("Você abriu o youtube")
                print("Você abriu o Youtube")
                print("     ")

        # -------------------------------------------- Notícias -----------------------------------------------------#
        elif a.lower() in news:
                speak.Speak("Abrindo as noticias")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("noticias")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                speak.Speak("Você abriu as notícias")
                print("Você abriu as notícias")
                print("     ")

        # -------------------------------------------- Calendário -----------------------------------------------------#
        elif a.lower() in calendario:
                speak.Speak("Abrindo o calendário")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("calendario")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                speak.Speak("você abriu o calendário")
                print("Você abriu o calendario")
                print("     ")

        # -------------------------------------------- Calculadora -----------------------------------------------------#

        elif a.lower() in calc:
                speak.Speak("Abrindo a calculadora")
                pyautogui.hotkey('win')
                time.sleep(2)
                pyautogui.typewrite("calc")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                speak.Speak("Você abriu a calculadora")
                print("Você abriu a Calculadora")
                


        # -------------------------------------------- Ping -----------------------------------------------------#

        elif a.lower() in ping:
                speak.Speak("Verificando o Pingue")
                pyautogui.hotkey('win','r')
                time.sleep(2)
                pyautogui.typewrite("cmd")
                time.sleep(2)
                pyautogui.typewrite(["enter"])
                time.sleep(1)
                pyautogui.typewrite("ping 8.8.8.8")
                time.sleep(1)
                pyautogui.typewrite(["enter"])
                speak.Speak("Foi executado o comando pingue padrão de 4 pacotes de dados")
                print("Ping Executado")
                
        # -------------------------------------------- Apresentação -----------------------------------------------------#
        elif a.lower() in apresentacao:
                speak.Speak("eu me chamo hemy. sou uma pequena assistente virtual")
                speak.Speak("fui desenvolvida em paiton,e ainda estou em fases de testes")
                botans = ["eu me chamo hemy. sou uma pequena assistente virtual"]
                print(random.choice(botans)+'\n')

        # Função caso não ache o comando desejado
        else:
                # speak.Speak("Searching for " + a)
                # pyautogui.click(264,744)
                # pyautogui.hotkey('ctrl', 't')
                # pyautogui.typewrite(a)
                # pyautogui.typewrite(["enter"])
                # print("     ")

                speak.Speak("Desculpe, mas não entendi")
                speak.Speak(f"Ainda não aprendi nada sobre {a}. Mas vou me esforçar pra aprender")
                speak.Speak("Refaça sua pergunta, se atente as definições iniciais, ou utilize os comandos pré definidos")
                
                
