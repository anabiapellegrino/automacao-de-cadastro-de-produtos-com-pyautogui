# Automação de Cadastro de Produtos (RPA)

Este repositório contém uma solução desenvolvida em Python para automatizar o fluxo de entrada de dados de um inventário industrial/comercial. O script construído lê informações de uma base de dados estruturada e consegue realizar o preenchimento automático em um site.


## Objetivo do Projeto
Eliminar possíveis erros humanos e diminuir o tempo em tarefas repetitivas. Essa simples automação é capaz processar uma lista de produtos via CSV além de interagir interage com o navegador.

---

## Tomadas de Decisão

Durante o desenvolvimento, identifiquei alguns desafios de interface que me influenciaram a moldar um pouco a estrutura do código:

### 1. Encontrando uma forma de prosseguir com os cadastros:
* **Desafio:** Após cada cadastro, o uso contínuo da tecla `TAB` tornava-se impreciso, pois o "ponto de partida" mudava a cada item.
* **Solução:** Implementei um comando de **Refresh (F5)** no início de cada iteração. Isso consegue forçar o navegador a recarregar a página, garantindo que o formulário esteja sempre vazio e que o primeiro `TAB` foque no primeiro campo de cadastro.

### 2. Preenchimento de Campo Opcional:
* **Desafio:** O Pandas preenche células vazias com o valor técnico `NaN`. Sem tratamento de dados, a automação escreveria literalmente "nan" no campo de observações.
* **Solução:** Adicionei uma estrutura condicional para validar o conteúdo da célula antes da execução do comando `pyautogui.write()`.

---

## Tecnologias

O projeto foi construído utilizando módulos nativos e bibliotecas externas especializadas:

* **Python**: Linguagem base.
* **Pandas**: Processamento e manipulação de dados.
* **PyAutoGUI**: Automação de interface.
* **Webbrowser**: Módulo nativo para gestão de instâncias do navegador.

### Como instalar as dependências
Abra um novo terminal na pasta do projeto e execute:
```bash
pip install pandas pyautogui openpyxl