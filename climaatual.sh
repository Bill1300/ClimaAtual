#!/bin/bash

function desinstalar() {
    rm -r ~/.ClimaAtual
    sudo rm /bin/climaatual
    echo "🟧 Desinstalado com sucesso."
}

if [ -z "$1" ]; then
    python3 ~/.ClimaAtual/executar.py
else
    if [[ $1 == "-s" ]]; then #apresentarDadosSimples
        python3 ~/.ClimaAtual/executar.py -s
    elif [[ $1 == "-e" ]]; then #editarParametros
        python3 ~/.ClimaAtual/executar.py -e
    elif [[ $1 == "-d" ]]; then #desinstalar
        echo "🟧 Você deseja confirmar a desinstalação? (S/N)" 
        read des
        if [[ $des == "s" || $des == "S" ]]; then
            desinstalar
        fi
        if [[ $des == "n" || $des == "N" ]]; then
            echo "🟥 Operação cancelada."
        fi
    elif [[ $1 == "-D" ]]; then #desinstalarSemConfirmacao
        desinstalar
    else #parametroDesconhecido
        echo "🟥 Parâmetro desconhecido."
    fi
fi
