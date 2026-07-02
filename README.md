# Python Playwright Challenge

Projeto de automação desenvolvido em **Python** utilizando **Playwright** para resolver um desafio de sincronização de elementos em uma interface web. O projeto também utiliza **MongoDB** para persistência de dados, **python-dotenv** para gerenciamento de variáveis de ambiente e **logging** para registro das execuções.

---

## 📋 Desafio

Automatizar o seguinte fluxo:

1. Abrir a página.
2. Clicar no botão **Add**.
3. Verificar se o campo de entrada da **Row 2** é exibido.

O principal desafio é que a **Row 2** não é renderizada imediatamente após o clique. Sem uma estratégia adequada de sincronização, a automação pode tentar localizar o elemento antes que ele esteja disponível.

Neste projeto, essa situação é tratada utilizando os mecanismos de **Auto Waiting** do Playwright, tornando a automação mais confiável e estável.

---

## 🚀 Tecnologias

- Python 3.14
- Playwright
- MongoDB
- python-dotenv
- uv
- Logging

---

## 📁 Estrutura do projeto

```text
.
├── config/
│   └── log.py
├── db/
│   └── mongo.py
├── logs/
│   ├── app.log
│   └── error.log
├── pages/
│   ├── click_test.py
│   ├── initial_page.py
│   ├── patrice_page.py
│   └── test_exceptions.py
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## ⚙️ Configuração

### Clone o repositório

```bash
git clone https://github.com/Zavan7/desafio_rpa_quatro
cd desafio_rpa_quatro
```

### Instale o uv

Caso ainda não tenha o **uv** instalado:

```bash
pip install uv
```

ou

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Instale as dependências

```bash
uv sync
```

### Instale os navegadores do Playwright

```bash
uv run playwright install
```

---

## 🔐 Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Exemplo:

```env
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=playwright_db
```

As configurações são carregadas automaticamente utilizando **python-dotenv**.

---

## 🍃 MongoDB

O projeto utiliza o MongoDB para armazenar dados utilizados durante a execução da automação.

Certifique-se de que o banco esteja em execução antes de iniciar a aplicação.

---

## ▶️ Executando o projeto

```bash
uv run main.py
```

---

## 📝 Logs

Durante a execução, os registros são armazenados na pasta `logs/`.

- `app.log` — informações gerais da aplicação.
- `error.log` — erros encontrados durante a execução.

---

## 🎯 Objetivos do projeto

- Automatizar uma interface web utilizando Playwright.
- Demonstrar o uso de sincronização automática para elementos dinâmicos.
- Aplicar uma arquitetura organizada utilizando o padrão **Page Object Model (POM)**.
- Utilizar variáveis de ambiente para configurações sensíveis.
- Integrar a aplicação ao MongoDB.
- Centralizar o registro de eventos por meio de logs.

---

## 📚 Conceitos utilizados

- Playwright Auto Waiting
- Page Object Model (POM)
- Python
- MongoDB
- python-dotenv
- Logging
- Modularização

---

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e demonstração de conhecimentos em automação com Python e Playwright.
