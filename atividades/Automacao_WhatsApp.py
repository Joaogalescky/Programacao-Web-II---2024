# Importações
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import urllib.parse

# Carregar o arquivo Excel
# Atualize com o caminho correto
jadlog_contato_df = pd.read_excel(
    "C:\\Users\\Skyfall_jack\\Desktop\\JogLog_Teste.xlsx")

# Configuração das opções do Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Especificar o caminho para o binário do Chrome (certifique-se de incluir 'chrome.exe')
chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Instalar e utilizar o ChromeDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

# Abrir o WhatsApp Web
navegador.get("https://web.whatsapp.com/")

# Esperar o WhatsApp Web carregar
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)

# Enviar mensagens
for i, mensagem in enumerate(jadlog_contato_df['Mensagem']):
    aluno = jadlog_contato_df.loc[i, "Aluno"]
    contato = jadlog_contato_df.loc[i, "Contato"]
    texto = urllib.parse.quote(f"Olá {aluno}! {mensagem}")

    # Construir o link do WhatsApp
    link = f"https://web.whatsapp.com/send?phone={contato}&text={texto}"
    navegador.get(link)

    # Esperar o chat carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)

    # Enviar a mensagem
    navegador.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
    time.sleep(10)  # Dar tempo para a mensagem ser enviada
