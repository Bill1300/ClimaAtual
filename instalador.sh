#!/bin/bash

mkdir ~/.ClimaAtual
mv executar.py apresentar.py ./pagina/ ~/.ClimaAtual/
sudo mv climaatual.sh /bin
sudo chmod 755 /bin/climaatual.sh
sudo mv /bin/climaatual.sh /bin/climaatual #Renomear
rm README.md
echo Instalado com sucesso!
