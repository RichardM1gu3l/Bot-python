import pyautogui
import  time

pyautogui.PAUSE =  1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#tempo de click
time.sleep(3)

#localização do mouse
pyautogui.click(x=1051, y=175)
pyautogui.click(x=528, y=397)

pyautogui.write("teste@gmail.com")

pyautogui.click(x=482, y=497)

pyautogui.write("12345")
#ou podemos utilizar a tecla tab.
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#importar base de dados
import pandas

tabela  =   pandas.read_csv("/home/rim1gu3l/Documentos/pythonpowerup/produtos.csv")

print(tabela)

#Cadastrar um produto
for linha   in  tabela.index:

    pyautogui.click(x=481, y=288)

    codigo  =   tabela.loc[linha,   "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca   =   tabela.loc[linha,   "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo    =   tabela.loc[linha,   "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria   =   str(tabela.loc[linha,   "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario  =   str(tabela.loc[linha,   "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo   =   str(tabela.loc[linha,   "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs =   str(tabela.loc[linha,   "obs"])

    if  obs !=  "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)