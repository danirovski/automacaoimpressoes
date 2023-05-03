#Importação das bibliotecas que serão utilizadas
import os
import win32api
import win32print

#verificação do index das impressoras listadas em nosso sistema
# for impressora in lista_impressoras:
# print(impressora)

lista_impressoras = win32print.EnumPrinters(2) 
impressora = lista_impressoras[1]
win32print.SetDefaultPrinter(impressora[2]) # Como exemplo, escolhemos a impressora de índice (2)
# Enviar todos os arquivos da pasta definida para impressão

caminho = r"path" #Escolha o caminho da pasta em seu computador
lista_arquivos = os.listdir(caminho)
for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0) #parâmetros fixos
