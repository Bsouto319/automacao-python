# Passo a passo do projeto

#1. Abrir o sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#para instalar o pyautogui 
#import pyautogui
import pyautogui

# pyauto.click ->clicar o mause
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
#pyauto.hotkey -> apertar um conjunto de teclas (Ctrl C , Ctrl V , Alt Tab)
 
 
# Abrir o navegador (Crome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 

# Entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#2. Fazer login
#3. Abrir/impotar a base de dados de produtos para cadastrar
#4. Cadastrar um produto
#Repetir isso ate acabar a lista de produtos

