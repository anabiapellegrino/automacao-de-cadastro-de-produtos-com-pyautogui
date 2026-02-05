import time
import pyautogui
import pandas as pd
import webbrowser

# Configuração de segurança
pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.5

# Carregar base de dados
tabela = pd.read_csv("produtos.csv", dtype=str)

def abrir_sistema():
    print("Iniciando automação...")
    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    
    webbrowser.open(link)
    
    time.sleep(5)

def fazer_login():
    print("iniciando o login...")

    pyautogui.press("tab")
    pyautogui.write("emailtop@gmail.com")
    pyautogui.press("tab")
    pyautogui.write("senhatop")
    pyautogui.press("tab") 
    pyautogui.press("enter")

    time.sleep(3)

def cadastrar_produtos():
    print(f"Iniciando cadastro de {len(tabela)} produtos...")

    for linha in tabela.index:
        pyautogui.press("f5")
        time.sleep(2)

        pyautogui.press("tab")
        
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        pyautogui.press("tab")

        obs = (str(tabela.loc[linha, "obs"]))
        if obs != "nan" and obs != "": 
            pyautogui.write(obs)

        pyautogui.press("tab")
        pyautogui.press("enter")

        time.sleep(1.5)

if __name__ == "__main__":
    abrir_sistema()

    fazer_login()
    cadastrar_produtos()
    print("Automação finalizada com sucesso!")