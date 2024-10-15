import pyautogui
import pyperclip
from time import sleep

class Robo():
    """
    Robô para extrair um link de um site qualquer

    Atributos:
        tempo (int): Tempo de esperar após acessar um site. 
            Obs.: Pode ser usado como sleep() entre uma ação ou outra durante a construção do programa
    """
    def __init__(self, tempo):
        self.tempo = tempo
        pyautogui.PAUSE = 1

    def abrir_programa(self, programa:str):
        pyautogui.press('win')
        pyautogui.write(programa)
        pyautogui.press('enter')

    def acessar_site(self, link:str):
        self.escrever(link)
        self.aguardar()

    def escrever(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')

    def aguardar(self):
        sleep(self.tempo)

    def pesquisar_campo(self, texto):
        self.escrever(texto)
        self.aguardar()

    def clicar(self, x:int, y:int, botao:str ='left'):
        pyautogui.click(x=x, y=y, button=botao)

    def extrair_link(self,x,y,botao:str):
        self.clicar(x,y,botao)
        pyautogui.press('up',4)
        pyautogui.press('enter')

        texto = pyperclip.paste()
        print(texto)


if __name__ == "__main__":
  
    robos = Robo(3)
    robos.abrir_programa('microsoft Edge')
    robos.acessar_site('https://sjcelulares.com/')
    robos.clicar(x=1415,y=201)
    robos.aguardar()
    robos.extrair_link(x=816,y=645,botao='right')
