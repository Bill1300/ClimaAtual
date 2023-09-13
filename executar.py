import requests, os, json, sys
from datetime import datetime
from requests import get

import apresentar
parametro_entrada = None
valor_chave = None
cidade = None
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
LOCAL_CHAVE = os.path.expanduser("~/.ClimaAtual/climaA.chave")
LOCAL_DADO = os.path.expanduser("~/.ClimaAtual/climaA.dado")

def apresentarDados(dados, cidade, auto, parametro_entrada):
    modo_simples = False
    if parametro_entrada == "-s":
        modo_simples = True

    if modo_simples:
        apresentar.apresentarDadosSimples(dados, cidade, auto)
    else:
        apresentar.apresentarDados(dados, cidade, auto)
        apresentar.abrirNavegador()


def requisicaoDados(valor_chave, cidade, auto, parametro_entrada):
    params = {"q": cidade, "appid": valor_chave, "lang": "pt_br", "units": "metric"}
    try:
        requisicao = requests.get(BASE_URL, params=params)
        if requisicao.status_code == 200:
            dados = requisicao.json()
            with open(LOCAL_DADO, "w") as arq_dados:
                json.dump(dados, arq_dados)
            apresentarDados(dados, cidade, auto, parametro_entrada)
        else:
            print("Erro na solicitação.")

    except (requests.ConnectionError, requests.Timeout) as exception: 
        print("Erro de conexão.") 


def gravarInfo():
    chave = ""
    while len(chave) != 32:
        print(
            "Para a requisição de informações é necessário o cadastro na plataforma OpenWeather (https://home.openweathermap.org/api_keys) para ter uma chave de acesso."
        )
        chave = str(input("Insira a chave de API ➜ "))

    cidade = str(
        input("Insira o nome da cidade ( vazio para detecção automática ) ➜ ")
    ).capitalize()
    if cidade == "":
        cidade = autoLocal()
        auto_localizacao = True
    else:
        auto_localizacao = False

    hora_atual = datetime.now().strftime("%H")
    dados = {
        "chave": chave,
        "cidade": cidade,
        "hora_atual": hora_atual,
        "auto": auto_localizacao,
    }
    with open(LOCAL_CHAVE, "w") as arquivo_json:
        json.dump(dados, arquivo_json)


def lerMeta():
    if os.path.exists(LOCAL_CHAVE):
        with open(LOCAL_CHAVE, "r") as arquivo_json:
            dados = json.load(arquivo_json)

        valor_chave = dados.get("chave", "")
        cidade = dados.get("cidade", "")
        auto = dados.get("auto", "")
        hora_salva = dados.get("hora_atual", "")
        return valor_chave, cidade, auto, hora_salva
    else:
        return None, None, None, None


def autoLocal():
    ip = get("https://api.ipify.org").content.decode("utf8")
    cidade = get(f"https://ipapi.co/{ip}/city/").text
    return cidade


def main():
    parametro_entrada = None
    if len(sys.argv) > 1:
        parametro_entrada = sys.argv[1]
    else:
        parametro_entrada = None
    
    if parametro_entrada == "-e":
        gravarInfo()

    valor_chave, cidade, auto, hora_salva = lerMeta()
    
    if valor_chave is None or cidade is None:
        gravarInfo()
        valor_chave, cidade, auto, hora_salva = lerMeta()

    hora_atual = datetime.now().strftime("%H")
    if int(hora_salva) == int(hora_atual):
        if os.path.exists(LOCAL_DADO):
            with open(LOCAL_DADO, "r") as arq_dados:
                dados_local = json.load(arq_dados)
            apresentarDados(dados_local, cidade, auto, parametro_entrada)
        else:
            requisicaoDados(valor_chave, cidade, auto, parametro_entrada)
    else:
        with open(LOCAL_CHAVE, "r") as arq_meta:
            dados = json.load(arq_meta)
            dados["hora_atual"] = datetime.now().strftime("%H")
            with open(LOCAL_CHAVE, "w") as arq_meta:
                json.dump(dados, arq_meta)

        requisicaoDados(valor_chave, cidade, auto, parametro_entrada)

main()
