from selenium import webdriver
from termcolor import colored
import os

def apresentarDados(dados, cidade, auto):
    index = os.path.expanduser("~/.ClimaAtual/pagina/index.html")

    vento = round((dados["wind"]["speed"] * 3.6), 2)

    with open(index, 'r') as arquivo_entrada:
        conteudo = arquivo_entrada.read()
    if auto:
        conteudo = conteudo.replace('[icone_local]', 'location_searching')
        conteudo = conteudo.replace('[mensagem_icone]', '🟩 Detecção automática ativada')
    else:
        conteudo = conteudo.replace('[icone_local]', 'location_disabled')
        conteudo = conteudo.replace('[mensagem_icone]', '🟥 Detecção automática desativada')
    conteudo = conteudo.replace('[cidade]', cidade)
    conteudo = conteudo.replace('[temperatura_atual]', str(dados["main"]["temp"]))
    conteudo = conteudo.replace('[sensacao_termica]', str(dados["main"]["feels_like"]))
    conteudo = conteudo.replace('[temperatura_min]', str(dados["main"]["temp_min"]))
    conteudo = conteudo.replace('[temperatura_max]', str(dados["main"]["temp_max"]))
    conteudo = conteudo.replace('[umidade]', str(dados["main"]["humidity"]))
    conteudo = conteudo.replace('[vento]', str(vento))
    conteudo = conteudo.replace('[condicao]', dados["weather"][0]["description"].capitalize()+".")

    with open(index, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo)


def apresentarDadosSimples(dados, cidade, auto):
    if auto:
        titulo = ("Clima em "+ colored(cidade, attrs=["bold"]) + " (\U0001F6DC  Detecção automática) ➜")
    else:
        titulo = "Clima em " + colored(cidade, attrs=["bold"]) + " ➜"
    
    print(titulo)
    print("Temperatura ➜ {} °C   (\U0001F53C Máx. {} °C   \U0001F53D Min. {} °C)".format(dados["main"]["temp"], dados["main"]["temp_min"], dados["main"]["temp_max"]))
    print("Sensação térmica ➜ {} °C".format(dados["main"]["feels_like"]))
    print(f'Umidade ➜ {dados["main"]["humidity"]} %')
    vento = round((dados["wind"]["speed"] * 3.6), 2)
    print(f'Vento ➜ {vento} Km/h')
    print(f'Condição ➜ {dados["weather"][0]["description"].capitalize()}.')


def abrirNavegador():
    params = {
        'scrollbars': 'no',
        'resizable': 'no',
        'status': 'no',
        'location': 'no',
        'toolbar': 'no',
        'menubar': 'no',
        'width': 750,
        'height': 900,
        'left': 0,
        'top': 0
    }
    param_string = ','.join([f'{key}={value}' for key, value in params.items()])

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--window-position={params["left"]},{params["top"]}')
    chrome_options.add_argument(f'--window-size={params["width"]},{params["height"]}')
    chrome_options.add_argument(f'--window-features={param_string}')

    driver = webdriver.Chrome(options=chrome_options)

    arquivo = os.path.expanduser('~/.ClimaAtual/pagina/index.html')
    driver.get(f'file://{arquivo}')
    input("🟧 Pressione Enter para fechar o visualizador ➜")
    driver.quit()
    os.system("cp ~/.ClimaAtual/pagina/raw.html ~/.ClimaAtual/pagina/index.html")

