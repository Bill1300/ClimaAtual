<div align="center">
    <img  width="200"  src="./pagina/imgs/icon.png">
</div>

# ClimaAtual
Script para apresentação de dados relacionados ao clima-tempo.

<span>Este obra está licenciado com uma <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
Licença Creative Commons Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional</a>.</span>

### Instalação ➜

Para instalar o programa execute o comando:

>$ **bash instalador&#46;sh**

(É necessário a inserir a senha de super-usuário)

### Execução ➜

Na primeira execução é necessário definir o local e a chave de requisição disponibilizada em <a href="https://openweathermap.org/api">openweathermap.org/api</a>.

#### Modo Simples

Para utilizar o programa execute o comando **climaatual** seguido do parâmetro `-s`:

> $ **climaatual -s**

#### Modo Comum

Para utilizar o programa execute o comando **climaatual**:

> $ **climaatual**

### Desinstalar ➜

Para desinstalar execute o comando **climaatual** seguido do parâmetro `-d` (use `-D` para desinstalar sem a confirmação):

> $ **climaatual -d**

### Editar ➜

Para editar as informações salvas execute o comando **climaatual** seguido do parâmetro `-e`:

> $ **climaatual -e**

- - -
Estrutura utilizada:

```markdown
├── home/
│	└── .ClimaAtual/
│	    ├── pagina/
│	    │   ├── index.html
│	    │   ├── raw.html
│	    │   ├── style.css
│	    │   ├── raw.html
│	    │   └── imgs/
│	    │       └── icon.png
│	    ├── executar.py
│	    ├── apresentar.py
│	    ├── climaA.dado
│	    └── climaA.chave
└── bin/
    └── climaatual
```
