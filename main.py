from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import csv
import time

# Configurar o caminho do ChromeDriver
driver_path = r"C:\Users\Public\Chromedriver\chromedriver-win64\chromedriver.exe"  # Atualize para o caminho correto
service = Service(driver_path)

# URL do site de previsão do tempo
url = "https://www.climatempo.com.br/"

# Nome do arquivo CSV para salvar os dados
arquivo_csv = "dados_temperatura.csv"

# Função para criar o arquivo CSV (caso não exista)
def criar_arquivo_csv():
    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Data e Hora", "Temperatura", "Umidade"])

# Função para salvar dados no arquivo CSV
def salvar_dados_csv(data_hora, temperatura, umidade):
    with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([data_hora, temperatura, umidade])

# Criar o arquivo CSV se for a primeira execução
criar_arquivo_csv()

# Inicializar o navegador
driver = webdriver.Chrome(service=service)

try:
    # Acessar o site de previsão do tempo
    driver.get(url)
    time.sleep(5)  # Aguarde o carregamento do site

    # Capturar os elementos de temperatura e umidade
    temperatura_element = driver.find_element(By.ID, "current-weather-temperature")
    umidade_element = driver.find_element(By.XPATH, '//*[@id="current-weather-humidity"]')

    # Extrair os dados
    temperatura = temperatura_element.text
    umidade = umidade_element.text

    # Registrar data e hora
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Salvar no CSV
    salvar_dados_csv(data_hora, temperatura, umidade)
    print(f"Dados salvos: {data_hora}, {temperatura}, {umidade}")

finally:
    # Fechar o navegador
    driver.quit()
