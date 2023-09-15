from selenium import webdriver
from termcolor import colored
import os

def tratarVento(vento_vel, vento_dir):
    vento_vel = round((vento_vel * 3.6), 2)

    if 0 <= vento_dir < 22.5:
        vento_dir = "Norte"
        vento_ico = 0
    elif 22.5 <= vento_dir < 45:
        vento_dir = "Nor-nordeste"
        vento_ico = 22.5
    elif 45 <= vento_dir < 67:
        vento_dir = "Nordeste"
        vento_ico = 45
    elif 67.5 <= vento_dir < 90:
        vento_dir = "Lés-nordeste"
        vento_ico = 67.5
    elif 90 <= vento_dir < 112.5:
        vento_dir = "Leste"
        vento_ico = 90
    elif 112.5 <= vento_dir < 135:
        vento_dir = "Lés-sudeste"
        vento_ico = 112.5
    elif 135 <= vento_dir < 157.5:
        vento_dir = "Sudeste"
        vento_ico = 135
    elif 157.5 <= vento_dir < 180:
        vento_dir = "Sul-sudeste"
        vento_ico = 157.5
    elif 180 <= vento_dir < 202.5:
        vento_dir = "Sul"
        vento_ico = 180
    elif 202.5 <= vento_dir < 225:
        vento_dir = "Sul-sudoeste"
        vento_ico = 202.5
    elif 225 <= vento_dir < 247.5:
        vento_dir = "Sudoeste"
        vento_ico = 225
    elif 247.5 <= vento_dir < 270:
        vento_dir = "Oés-sudoeste"
        vento_ico = 247.5
    elif 270 <= vento_dir < 292.5:
        vento_dir = "Oeste"
        vento_ico = 270
    elif 292.5 <= vento_dir < 315:
        vento_dir = "Oés-noroeste"
        vento_ico = 292.5
    elif 315 <= vento_dir < 337.5:
        vento_dir = "Noroeste"
        vento_ico = 315
    elif 337.5 <= vento_dir <= 360:
        vento_dir = "Nor-noroeste"
        vento_ico = 337.5
    else:
        vento_dir = "Sem informação"

    return vento_vel, vento_dir, vento_ico


def apresentarDados(dados, cidade, auto):
    index = os.path.expanduser("~/.ClimaAtual/pagina/index.html")

    vento_vel, vento_dir, vento_ico = tratarVento(dados["wind"]["speed"],dados["wind"]["deg"])

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
    conteudo = conteudo.replace('[vento_vel]', str(vento_vel))
    conteudo = conteudo.replace('[vento_dir]', str(vento_dir))
    conteudo = conteudo.replace('[vento_ico]', str(vento_ico))
    conteudo = conteudo.replace('[condicao]', dados["weather"][0]["description"].capitalize()+".")

    with open(index, 'w') as arquivo_saida:
        arquivo_saida.write(conteudo)


def apresentarDadosSimples(dados, cidade, auto):
    if auto:
        titulo = ("Clima em "+ colored(cidade, attrs=["bold"]) + " (\U0001F6DC  Detecção automática) ➜")
    else:
        titulo = "Clima em " + colored(cidade, attrs=["bold"]) + " ➜"
    
    vento_velocidade, vento_direcao, _ = tratarVento(dados["wind"]["speed"],dados["wind"]["deg"])
    
    print(titulo)
    print("Temperatura ➜ {} °C   (\U0001F53C Máx. {} °C   \U0001F53D Min. {} °C)".format(dados["main"]["temp"], dados["main"]["temp_min"], dados["main"]["temp_max"]))
    print("Sensação térmica ➜ {} °C".format(dados["main"]["feels_like"]))
    print(f'Umidade ➜ {dados["main"]["humidity"]} %')
    print(f'Vento ➜ {vento_velocidade} Km/h ({vento_direcao})')
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
